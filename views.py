from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from scipy import stats
import rasterio
import pysheds
from pysheds.grid import Grid
def acercaDe(request):
        return HttpResponse("Bienvenidos a Decodexs")
def cursos(request):
        return HttpResponse("Acerca del curso")
def paralelo(request,idparalelo):
        return HttpResponse(idparalelo)
def pagina(request):
        return render(request,"index.html")
def paginaweb1(request):
        data={
                 'titulo':'Nueva Pagina Web',
                 'bdatos':'Bienvenido a Obras Hidraulicas',
                 'clista':['PHP','Java','Django','Csharp'],
                 'detalle':[
                         {'nombre':'luis','celular':71568993},
                         {'nombre':'andres','celular':7214677},
                         {'nombre':'israel','celular':79102753}
                 ]
        }
        return render(request,"pagina1.html",data)
def paginaweb2(request):
        resultado=0
        try:
                n1=int(request.GET['num1'])
                n2=int(request.GET['num2'])
                print(n1+n2)
                resultado=n1+n2    
        except:
                passfrom django.http import HttpResponse
        return render(request,"pagina2.html",{'salida':resultado})
def paginaweb3(request):
        pendiente=0
        tconcen=0
        intensdis=0
        caudal=0
        try:
                dac=float(request.GET['ac'])
                dlc=float(request.GET['lc'])
                dcmac=float(request.GET['cmac'])
                dcmic=float(request.GET['cmic'])
                dce=float(request.GET['ce'])
                dpr=float(request.GET['pr'])
                print(dcmac-dcmic)
                pendiente=((dcmac-dcmic)/dlc)
                print((dcmac-dcmic)/dlc)
                tconcen=0.000323*60*((pow(dlc,0.77))/(pow(pendiente,0.385)))
                print(tconcen)
                intensdis=((615*(pow(dpr,0.18)))/(pow((tconcen+5),0.685)))
                print(intensdis)
                caudal=(dce*intensdis*dac)/360
                print(caudal)
        except:
                pass
        return render(request,"pagina3.html",{'ope':pendiente,'otc':tconcen,'oid':intensdis,'oca':caudal})
def paginaweb4(request):
        from pysheds.grid import Grid
        return render(request,"pagina4.html")

def paginaweb5(request):
        datos=pd.read_csv('/home/felro775/Dataton/prueba1/static/docs/pcp_elalto.csv',index_col=0, parse_dates=True)
        datosa=datos.shape      
        promedio = datos[datos>0].mean()
        promedios = promedio[0]
        desviacion = datos[datos>0].std()
        desviaciones = desviacion[0]
        ay=datos.plot()
        ay.get_figure().savefig('/home/felro775/Dataton/prueba1/static/img/grafica1.jpg')
        ay.get_figure().savefig('/home/felro775/Dataton/prueba1/static/docs/grafica1.pdf')
        ax=datos.plot.hist()
        ax.get_figure().savefig('/home/felro775/Dataton/prueba1/static/img/grafica2.jpg')
        ax.get_figure().savefig('/home/felro775/Dataton/prueba1/static/docs/grafica2.pdf')
        print(datos.head)
        print(promedio)
        print(desviacion)
        tabulaciones=np.arange(-40,51,0.1)
        distnormal = stats.norm.pdf(tabulaciones, loc=promedio, scale=desviacion)
        #distlognormal = stats.pearson3.pdf(tabulaciones,skew=1,loc=promedio, scale=desviacion)        
        return render(request,"pagina5.html",{'salidadat':datosa,'salidaprom':promedios,'salidades':desviaciones})
def paginaweb6(request):
        
        grid1 = Grid.from_raster('/home/felro775/Dataton/prueba1/static/img/DEM.tif')
        dem1 = grid1.read_raster('/home/felro775/Dataton/prueba1/static/img/DEM.tif')
        dr1 = plt.imshow(grid1.view(dem1))        
        dr1.get_figure().savefig('/home/felro775/Dataton/prueba1/static/img/demima1.jpg')        
        return render(request,"pagina6.html")
