import Logica
import Experimento01 as exp1
import Experimento02 as exp2
import Experimento03 as exp3
import Experimento04 as exp4
import TemperaturasAmb as amb
#import GraficoWiki38 as wiki38
#import GraficoWiki70 as wiki70
import GraficoWiki as wiki
#import HipoteticoExp

i = 0
p = 5

if(p==1):
    Logica.logica(exp1.data, exp1.dados(),i)
if(p==2):
    Logica.logica(exp2.data, exp2.dados(),i)
if(p==3):
    listaDados = []
    listaDados.append(exp3.dados()[0])  #30°C
    listaDados.append(exp3.dados()[1])  #35°C
    listaDados.append(exp3.dados()[2])  #40°C
    listaDados.append(exp3.dados()[3])  #45°C
    #listaDados.append(exp1.dados()[1])  #28°C exp1
    listaDados.append(exp2.dados()[1])  #28°C exp2
    #listaDados.append(amb.dados()[0])   #25°C exp01
    #listaDados.append(amb.dados()[1])   #25°C exp02
    
    Logica.logica(exp3.data,listaDados,i)
if(p==4):
    listaDados = []
    #Logica.logica(exp4.data,listaDados,i)
if(p==0):
    #Logica.logica(wiki38.data,wiki38.dados(),i)
    #Logica.logica(wiki70.data,wiki70.dados(),i)
    Logica.logica(wiki.data, wiki.dados(), i)
if(p==5):
    Logica.logica(exp4.data,exp4.dados(),i)
