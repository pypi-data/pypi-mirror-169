"""
Libreria per fare grafici di fit e tabelle LaTeX a partire da dati raccolti in un file Excel
TODO: graph log con p value
TODO: rivedere esempi documentazione
"""
__docformat__="numpy"

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from scipy.odr import *
from scipy import stats
import pandas as pd
from pint import UnitRegistry
import re

def _tex_escape(text):
    """
        :param text: a plain text message
        :return: the message escaped to appear correctly in LaTeX
    """
    conv = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
        '\\': r'\textbackslash{}',
        '<': r'\textless{}',
        '>': r'\textgreater{}',
    }
    regex = re.compile('|'.join(re.escape(str(key)) for key in sorted(conv.keys(), key = lambda item: - len(item))))
    return regex.sub(lambda match: conv[match.group()], text)

def _converti_latex(text):
    ureg = UnitRegistry()
    um=re.search(r"\[(.+)\]",text).group(1) #ricerca unità di misura
    u=ureg.Unit(um)
    um_tex=f"{u:Lx}"
    new_text=text.replace("["+um+"]","[]") #cancellazione unità di misure
    new_text=_tex_escape(new_text) 
    new_text=new_text.replace("[]",r"\(\left["+um_tex+r"\right]\)") #inserimento siunix dopo aver fatto l'escape dei caratteri speciali per latex
    return new_text

def _deriva(funzione, x0, parametri, precisione=0.00000001):
    derivata_x0=[]
    for element in x0:
        old=0
        derivata=1
        #TODO: secondo me funziona strano ci sono sicuramente errori numerici e non so se trascurabili
        #limite numericamente calcolato
        while np.abs(old-derivata)>precisione:
            old=derivata
            n=-10
            epsilon=np.power(10.0, n)
            derivata=(funzione(element+epsilon, *parametri) - funzione(element, *parametri))/epsilon
            n-=10
        derivata_x0.append(derivata)

    return derivata_x0


def fit(excel_name,file_result,f_fit,popt_names_latex,variabile_x,variabile_y,sigma_y,
    sigma_x=None,
    use_ODR=False,
    numero_iterazioni=10,
    split_graphs=False,
    titoli=["",""],
    xlabel=None,
    ylabel=None,
    chi=True,
    ridotto=True,
    x_chi=0,
    y_chi=0,
    post_decimal_chi=0,
    log_to_file=False,
    nolatex=False,
    path=".",
    xscale="linear",
    yscale="linear",
    lim_inf=None,
    lim_sup=None,
    griglia_fit={
        "which" : "both",
        "ls" : "dashed",
        "color" : "powderblue"
    },
    griglia_residui={
        "which" : "both",
        "ls" : "dashed",
        "color" : "powderblue"
    },
    style_fit={"fmt" : "."},
    fit_line_color="darkorange",
    style_residui={"fmt" : "."},
    res_line_color="navy",
    pad_percent=0.10,
    precisione_curvatura=1001,
    foglio="Foglio1",
    funzioni_modifica=[None, None],
    residui_ratio=[4, 1],
    fig_dimension=(6.24136,4.4),
    estensione_grafico=".pdf"
):
    """
    funzione che genera:

        - un pdf:

            - contenente il grafico di fit e quello dei residui

        - un file LaTeX:
        
            - contenete i parametri ottimali del fit
    
    Parameters
    -------------------------
    excel_name : str
        nome file excel da elaborare

    file_result : str
        nome da dare ai pdf generati

    f_fit : func
        funzione che rappresenta la curva g(x) utilizzata nel fit.
        il primo parametro di f è x, gli altri sono tutti i parametri che definiscono g(x)
    
    popt_names_latex : list
        elenco dei nomi dei parametri ottimali che vengono ricavati dal fit
        verranno usati come contenuto della cella del titolo di una tabella latex contenente i valori numerici dei parametri
        devono essere scritti in Latex

    variable_x, variable_y, sigma_y : str
        ogni parametro contine il valore dell'header della colonna del foglio excel da cui prendere i dati
        (deve contenere l'unità di misura nel formato: "[unità di misura]")
    
    sigma_x: str, optional
        contine il valore dell'header della colonna del foglio excel da cui prendere i dati
        (deve contenere l'unità di misura nel formato: "[unità di misura]") (default: None)
        se un valore diverso d "None" viene specificato, viene usato un metodo di fit iterato con sigma efficaci, altrimenti si usa scypi.curvefit()

    use_ODR: bool, optional
        se True viene eseguito il fit con Orthogonal Distance Regression invece che iterando un fit del minimo chi^2 con sigma efficaci

    split_graphs: bool, optional
        se True la funzione genera due file separati per il grafico dei residui e il grafico di fit (default: False)

    titoli : list, optional
        lista di due elementi con i due titoli per i due grafici, il primo è il grafico di fit e il secondo è il grafico dei 
        residui (default: ["",""])
    
    xlabel, ylabel : str, optional
        stringa da utilizzare per la generazione dei label degli assi del grafico, usare notazione LaTeX. Se None allora i nomi delle colonne
        del file excel verranno utilizzati, convertendoli automaticamente in LaTeX ed interpretando um tra parentesi quadre (default: None)

    chi : bool, optional
        se True allora sul grafico viene mostrato il valore del chi quadro (default: True)

    ridotto : bool, optional
        se True allora sul grafico viene mostrato il valore del chi quadro ridotto,
        se False viene mostrato il chi quadro e i gradi di linertà (default: True)


    x_chi, y_chi : int, optional
        coordinate del punto in cui scrivere il valore del chi quadro e il numero di gradi di libertà (default: 0, 0 --> primo punto del plot)

    post_decimal_chi : int, optional
        numero di cifre dopo la virgola con cui scrivere il valore del chi quadro (default: 0)

    log_to_file : bool, optional
        if True le informazioni sulla bontà del grafico sono messe in un file di testo. If False le informazioni possono essere lette in console. (default: False)

    nolatex : bool, optional
        if True il grafico è disegnato senza compilare in latex

    path : str, optional
        path directory di partenza (default: ".")

    xscale, yscale : str, optional
        tipo di scala da utilizzare per l'asse corrispondente del grafico (default: 'linear')

    lim_inf, lim_sup : float, optional
        valori minimo e massimo rappresentati sull'asse delle x nella creaione del grafico. Se il valore è None il grafico si adatta al set di dati (default: None)

    griglia_fit, griglia_residui : dict, optional
        dizionario contenente i parametri opzionali da passare a pyplot.grid() (default: {"which" : "both", "ls" : "dashed", "color" : "powderblue"})

    style_fit, style_residui : dict, optional
        dizionario contenente i parametri opzionali da passare a pyplot.errorbar() (default: {"fmt" : "."})

    fit_line_color, res_line_color : str, optional
        colori da applicare alla curva di fit e alla linea dello zero nel grafico dei residui (default: "darkorange", "navy")

    pad_pecent : float, optional
        dimensione percentuale dello spazio del grafico in più rispetto al minimo necessario a contenere i dati (default: 0.10)

    precisione_curvatura : int, optional
        numero di punti utilizzato per il disegno della curva (default: 1001)

    foglio : str, optional
        nome del foglio da cui prendere i dati (default: "Foglio1")

    funzioni_modifica : list, optional
        lista contenete due funzioni (default: [None, None]). Entrambe devono avere 6 parametri: (fig, asse, x, y, params, data). La prima funzione verrà applicata al
        grafico di fit, la seconda al grafico dei residui, i parametri che vengono passati sono:

        - fig, asse: oggetti restituiti da pyplot.subplots() relativi al grafico che si vuole modificare
            
        - x, y: vettori contenenti il set di dati di cui si sta creando il grafico
            
        - params: vettore dei parametri ottimali di fit
            
        - data: panda dataframe rappresentante il foglio Excel

    residui_ratio : [int, int], optional
        rapporto dimensione (altezza), tra grafico e grafico dei residui (default: [4,1])

    fig_dimensions : (float, float), optional
        tupla contenete le dimensioni (x,y) dell'immagine creata in inches (default: (6.24136,4.5))

    estensione_grafico : str, optional
        estensione in cui viene salvato il grafico (default: ".pdf")

    Examples
    ----------------------------
    >>> def retta(x,m,q):
            return m*x+q
        result="nome grafico"
        file="moto_rettilineo.xlsx"
        var_x="tempi [s]"
        var_y="posizioni [cm]"
        sigma_y="incertezza posizione [cm]"
        titoli=["\\hat{m} [\\si{\\centi\\metre\\per\\second}]", "\\hat{q} [\\si{\\centi\\metre}]"]
        result=fit(file,result,var_x,var_y,sigma_y,retta,titoli)
        if result:
            print(result)
    
    oppure usando la funzione del pendolo fisico che utilizza un solo parametro:
    >>> def pendolo(d, l):
            return 2.0 * np.pi * np.sqrt((l**2.0 / 12.0 + d**2.0) / (9.81 * d))
        result="nome grafico"
        file="pendolo.xlsx"
        var_x="lunghezze [m]"
        var_y="tempi_medi [s]"
        sigma_y="sigma_t [s]"
        titoli_pendolo=["\\hat{l} [\\si{\\metre}]"]
        result=fit(file,result,var_x,var_y,sigma_y,pendolo,titoli_pendolo)
        if result:
            print(result)

    oppure passando parametri opzionali:
    >>> def retta(x,m,q):
            return m*x+q
        my_path="C:\\Users\\cremo\\Documents\\Università\\Relazioni"
        res="nome grafico"
        file="moto_rettilineo.xlsx"
        x="tempi [s]"
        y="posizioni [cm]"
        s_y="incertezza posizione [cm]"
        titoli=["\\hat{m} [\\si{\\centi\\metre\\per\\second}]", "\\hat{q} [\\si{\\centi\\metre}]"]
        asse_y="log"
        style={"ls" : "dotted", "color" : "green"}
        result=fit(file,res,x,y,s_y,retta,titoli,yscale=asse_y,griglia_fit=style, path=my_path)
        if result:
            print(result)
    """
 
    #definizione di una funzione della forma utile all'utilizzo di ODR
    def f_fit_odr (Beta, variabile):
        return f_fit(variabile, *Beta)



    #verifica parametri
    if "[" not in variabile_x or "]" not in variabile_x: 
        return "Manca unità di misura in x"
    if "[" not in variabile_y or "]" not in variabile_y:
        return "Manca unità di misura in y"
    if "[" not in sigma_y or "]" not in sigma_y:
        return "Manca unità di misura in dy"
    if sigma_x:
        if "[" not in sigma_x or "]" not in sigma_x:
            return "Manca unità di misura in dx"    
    if not excel_name:
        return "specificare nome file excel"
    if not file_result:
        return "specificare nome file pdf risultato (senza .pdf)"
    if not popt_names_latex:
        return "specificare i nomi dei parametri ottimmali di fit (scritti in latex)"

    #lettura file
    excel = pd.read_excel(path+'\\'+excel_name, sheet_name=foglio)

    t=[e for e in excel[variabile_x].tolist() if e == e] #t perché x non si poteva usare per  ambiguità
    y=[e for e in excel[variabile_y].tolist() if e == e] #NaN != NaN quindi il test impedisce di scrivere i valori nulli
    dy=[e for e in excel[sigma_y].tolist() if e == e]
    if sigma_x:
        dx=[e for e in excel[sigma_x].tolist() if e == e]

    #fit

    #fit iniziale
    popt, pcov = curve_fit(f_fit,t,y,sigma=dy,absolute_sigma=True)
    #sigma efficace
    if dx:
        sigma_eff=np.sqrt(np.power(dy,2)+np.power(_deriva(f_fit, t, popt)*dx,2)) #potrebbe non funzionare
    else:
        sigma_eff=dy
        dx=np.zeros(len(t))
    
    #fit iterato
    for i in range(numero_iterazioni):
        sigma_eff=np.sqrt(np.power(dy,2)+np.power(_deriva(f_fit, t, popt)*dx,2)) #potrebbe non funzionare
        popt, pcov = curve_fit(f_fit,t,y,sigma=sigma_eff,absolute_sigma=True)

    #ODR
    if use_ODR:
        linear_model = Model(f_fit_odr)
        data = RealData(t,y,dx,dy)
        odr = ODR(data,linear_model,beta0=popt)
        output = odr.run()
        popt = output.beta
        pcov = output.cov_beta



    #chi^2
    
    if not use_ODR:
        chisq=sum(np.power((y-f_fit(np.array(t),*popt)), 2)/np.power(sigma_eff,2))
    else:
        chisq=output.sum_square
    gradi_di_liberta=len(t)-len(popt)
    chi_rid=chisq/gradi_di_liberta    
 
    #valutazione grafico
    sopra_fit=0
    sotto_fit=0
    lontano_fit=0
    for element_y, element_t, element_dy in zip(y, t, sigma_eff):
        if element_y-f_fit(element_t,*popt)>0:
            sopra_fit+=1
        if element_y-f_fit(element_t,*popt)<0:
            sotto_fit+=1
        if np.absolute(element_y-f_fit(element_t,*popt))>element_dy:
            lontano_fit+=1
    p_value=stats.distributions.chi2.sf(chi_rid, 1)

    frase_log=[]
    frase_log.append("Numero di punti sopra alla funzione di best fit: "+str(sopra_fit)+"\n"+"Numero di punti sotto alla funzione di best fit: "+str(sotto_fit))
    frase_log.append("(expected: " + str(len(t)/2)+")")
    frase_log.append("Numero di punti che distano dal grafico n>1 barre di errore: "+str(lontano_fit)+" (expected-ipotesi  errori gaussiani: "+str(0.32 *len(t))+")")
    frase_log.append("la probabilità di ottenere un valore più estremo è di: "+p_value)
    if log_to_file:
        with open(path+"\\"+file_result+"_fit_log.txt", 'w') as fit_log:
            fit_log.write("\n".join(frase_log))
            fit_log.close()
    else:
        for e in frase_log:
            print(e)


    #scrittura file: *_tabella.tex con i risultati di fit (longtable)

    colonne="c"*len(popt) # colonne centrate in numero pari al numero di parametri
    line_begin=r"\begin{longtable}{"+colonne+r"}"
    table_header="&".join(popt_names_latex)+r"\\"
    longtable_header=[r"\toprule",table_header ,r"\midrule", r"\endfirsthead", r"\toprule",table_header ,r"\midrule",r"\endhead", r"midrule", r"\multicolumn{3}{r}{{continua a pagina seguente}} \\", r"\midrule", r"\endfoot", r"\bottomrule", r"\endlastfoot"]
    string_popt=[str(i_opt) for i_opt in popt] #numeri convertiti in stringa
    data_table=r" & ".join(string_popt)+r" \\"
    line_end=r"\end{longtable}"

    tabella=[] #creazione tabella completa
    tabella.append(line_begin)
    tabella.extend(longtable_header)
    tabella.append(data_table)
    tabella.append(line_end)
    
    with open(path+"\\"+file_result+"_tabella.tex", 'w') as tabella_tex: #scrittura file .tex
        tabella_tex.write("\n".join(tabella))
        tabella_tex.close()

    #disegno grafico 
    plt.rcParams["figure.figsize"] = fig_dimension #dimensioni impostate come richiesto (utile per corretta dimensione dei caratteri)

    #aggiunta di spazio prima e dopo il range di dati rappresentato
    pad=(max(t)-min(t))*pad_percent
    if not lim_inf:
        if min(t)-pad>0 or min(t)<0:
            lim_inf=min(t)-pad
        else: 
            lim_inf=0
    if not lim_sup:
        if max(t)+pad<0 or max(t)>0:
            lim_sup=max(t)+pad
        else: 
            lim_sup= 0


    #categorizzazione punti reali e punti previsti dal modello con tratteggio e linea continua
    a1 = np.linspace(lim_inf, min(t), precisione_curvatura) #tratteggio prima
    a2 = np.linspace(min(t), max(t), precisione_curvatura) #continua
    a3 = np.linspace(max(t), lim_sup, precisione_curvatura) #tratteggio poi

    #TODO: nolatex mode for faster debug
    #Latex parameters
    plt.rcParams.update({"text.usetex" : True,   #utilizza latex nella compilazione del grafico
        "font.family": "computer modern",
        "text.latex.preamble": "\n".join([ # plots will use this preamble
        r"\usepackage[utf8]{inputenc}",
        r"\usepackage[T1]{fontenc}",
        r"\usepackage{siunitx}",
        r"\usepackage{amsmath}",
        ])})

    #default label impostati a nome della ccolonna di excel usata per estrarre i dati   
    if not xlabel:
        xlabel=_converti_latex(variabile_x)

    if not ylabel:
        ylabel=_converti_latex(variabile_y)

    #creazione oggetti plt usando sempre metodi subplot
    if split_graphs:
        fig1, ax1 = plt.subplots(1, 1)
        fig2, ax2 = plt.subplots(1, 1)
    else:
        fig1, (ax1, ax2) = plt.subplots(2, 1, gridspec_kw={'height_ratios': residui_ratio}, sharex=True)

    #grafico di fit
    ##aspetto
    ax1.set_title(titoli[0])
    ax1.set_xscale(xscale)
    ax1.set_yscale(yscale)
    ax1.grid(**griglia_fit)
    ##plot TODO: verificare che funzioni con dx=0
    ax1.errorbar(t, y, dy, dx, **style_fit)
    ax1.plot(a1, f_fit(a1, *popt), linestyle="dashed", color=fit_line_color)
    ax1.plot(a2, f_fit(a2, *popt), color=fit_line_color)
    ax1.plot(a3, f_fit(a3, *popt), linestyle="dashed", color=fit_line_color)
    ##adjust limits
    ax1.set_xlim(min(a1),max(a3))

    #residui
    ##aspetto
    ax2.set_title(titoli[1])
    ax2.margins(0, 0.2) #TODO: controllare perché ho fatto questa cosa
    ax2.set_xscale(xscale)
    ax2.set_yscale(yscale)
    ax2.grid(**griglia_residui)
    ##plot
    y_res=y-f_fit(np.array(t), *popt)
    ax2.errorbar(t, y_res, dy, **style_residui)
    ax2.plot(a1, a1-a1, color=res_line_color) #evidenzia la linea dello zero
    ax2.plot(a2, a2-a2, color=res_line_color)
    ax2.plot(a3, a3-a3, color=res_line_color)
    ##adjust ylim for x axis symmetry
    low, high = ax2.get_ylim() 
    bound = max(abs(low), abs(high)) # find the new limits
    ax2.set_ylim(-bound, bound) # set new limits
    ax2.set_xlim(min(a1),max(a3))  # manual share x (così funziona anche per split_graph=True )

    #chi^2
    #TODO: posizionamento del chi^2
    if x_chi==0:
        x_chi=t[0]
    if y_chi==0:
        y_chi=y[0]+0.1*(max(y)-min(y))

    if chi:
        if ridotto:
            ax1.text(x_chi,y_chi,r"$$\frac{\chi^2}{\nu}="+str(round(chi_rid,post_decimal_chi))+r"$$")
        else:
            ax1.text(x_chi,y_chi,r"$$\chi^2 / \nu}="+str(round(chi,post_decimal_chi))+r" / "+gradi_di_liberta+r"$$")
            

    fig1.supxlabel(xlabel, y=0.05)
    fig1.supylabel(ylabel, x=0.03)

    #possibilità di modificare un po' tutto con una funzione arbitraria per disegnare cose extra
    if funzioni_modifica[0]:
        funzioni_modifica[0](fig1, ax1,t,y,popt, excel)  

    if split_graphs:
        
        fig2.supxlabel(xlabel, y=0.05)
        fig2.supylabel(ylabel, x=0.03)

        if funzioni_modifica[1]:
            funzioni_modifica[1](fig2, ax2,t,y,popt, excel)   
        
        fig2.tight_layout()
        fig2.canvas.manager.set_window_title("Residui") 

        fig2.savefig(path+'\\'+file_result+'_residui'+estensione_grafico)
    else:
        if funzioni_modifica[1]:
            funzioni_modifica[1](fig1, ax2,t,y,popt, excel)     

    fig1.tight_layout()
    fig1.canvas.manager.set_window_title("Grafico") 
    fig1.savefig(path+'\\'+file_result+estensione_grafico)
    plt.show()

def tabella(excel_name,file_result,
    path=".",
    colonne=None,
    foglio="Foglio1",
    index_on=False,
    formatter=None,
    column_align=None,
    table_caption="Tabella di dati"
):
    """
    funzione che crea una tabella in LaTeX a partire da dati in un file Excel.

    le unità di misura devono essere riportaate per ogni colonna tra parentesi quadre.

    Parameters
    -------------------------
    excel_name : str
        nome file excel da elaborare

    file_result : str
        nome da dare alle tabelle generate

    path : str, optional
        path directory di partenza (default: ".")

    colonne : list, optional
        lista contenete i valori degli header delle colonne del foglio excel da cui prendere i dati
        (default: None, che corrisponde a selezionare tutte le colonne)

    foglio: str, optional
        indica il nome del foglio da cui prendere i dati (default: "Foglio1")

    index_on: bool, optional
        decide se mostrare l'indice di riga (default: False)

    formatter: dict, optional
        dizionario contenente laa funzione per formattare i valori della tabella. I valori del dizionario usano come chiave il nome
        della colonna e come volore la funzione che formatta(default: None)

    column_align: str, optional
        stringa contenete il formato delle colonne, il formato stringa deve essere stile LaTeX, ad esempio "||l|c|r||" (default: None)

    table_caption: str, optional
        label da posizionare sotto alla tabella generata (default: "Tabella di dati")

    Examples
    ----------------------------
    >>> my_path="C:\\Users\\cremo\\Documents\\Università\\Relazioni\\pendolo_json"
        file_result="nome_grafico"
        file_tabella="nome_tabella"
        excel_name="prova_json.xlsx"
        formati={
            "tempi_medi [s]": "{:.4f}".format,
            "sigma_t [s]": "{:.9f}".format,
            "lunghezze [m]": "{:.3f}".format
        }
        result=js.tabella(excel_name,file_tabella, formatter=formati, path=my_path)
        if result:
            print(result)
    """
    #lettura file
    excel = pd.read_excel(path+'\\'+excel_name, sheet_name=foglio, usecols=colonne)
    #scrittura file
    ##creazione header in stile LaTeX
    my_header=[]
    for col in excel.columns:
        new_col=_converti_latex(col)
        my_header.append(new_col)

    latex = excel.to_latex(
        buf=path+"\\"+file_result+".tex",
        index=index_on,
        formatters=formatter,
        column_format=column_align,
        decimal=",", #separatore decimale
        longtable=True, #tipo di tabella
        caption=table_caption,
        na_rep="", #carattere da mettere nei posti NaN
        header=my_header,
        escape=False #impedisce escape latex special char
    )


