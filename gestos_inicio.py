from PIL import Image
from threading import Thread
from claseReconocerGestos import *
from claseGraficos import *
from claseMenu import *

import cv2
import sys
import time


captura = cv2.VideoCapture(0)
nuevo_frame = captura.read()[1]
hilo_corte = 0
identificador_textura = 0


#-------------
menuActivo1=1
menuActivo2=0
menuActivo3=0
seleccionFigura=0
seleccionOperacion=0



etapasCubo=1
pinturaCuadrado1=0  
pinturaCuadrado2=0  
pinturaCuadrado3=0  
pinturaCuadrado4=0  
pinturaCuadrado5=0  
pinturaCuadrado6=0  
temporaly=0 
pyf=0  
direccionPlano=0  
anguloRotacion=0 
anguloRot=0 
contador=-0.5 
velocidadAngular=5 


contadorCubo=0
contadorCubo1=-1 
contadorCubo2=1
contadorPrismaVolumen=-1

pinturaPrisma1a=0  
pinturaPrisma1b=0  
pinturaPrisma2a=0  
pinturaPrisma2b=0  
pinturaPrisma3a=0  
pinturaPrisma3b=0 
contadorPrisma=-1 

anguloMovimiento=90
anguloMovimiento1=-90
pintarCirculo=0
pintarCirculo2=0
pintarRectangulo=0
anguloRot1=90
anguloRot2=180
condicion=1

contadorCilindro=0 
contadorCilindro2=2

contadorCuadradoArea=-0.5
contadorCuadradoVolumen=-1
contadorCuboLado2=0
contadorCuboLado3=0
dedoLado=0
contadorPrismaVolumenDedo=0
inicioPrismaVolumen=1
llavePaso=0

visualizacionVolumen=0

dedoRadio=0

colorBlanco=(1,1,1,1)

class interaccion():
      def __init__(self):
        pass      

def cambio():
    global nuevo_frame
    while(True):
        nuevo_frame = captura.read()[1]
        if hilo_corte == 1:
           break
    captura.release()
    cv2.destroyAllWindows()

def init():        
        video_hilo = Thread(target=cambio, args=())
        video_hilo.start()
                 
    
def VisualizacionCubo():        
        
        # menu
        global menuActivo1   # primer nivel de menu 
        global menuActivo2   # segundo nivel de menu 
        global menuActivo3   # tercer nivel de menu
        global seleccionFigura # selccion figura de menu, cubo, prisma o cilindro
        global seleccionOperacion # selccion operacion, area o volumen 
        global llavePaso  # llave para abir adelante y atras en una determinada etapa
       
        # cubo area
        global contadorCuadradoArea # para la simulacion de area de un cuadrado en area
        global anguloRotacion # para abrir y cerrar el cubo
        global temporaly # para abir y cerrar  cubo
        global pyf # para abir y cerrar  cubo
        global direccionPlano # direccion de plano para abrir y cerrar    
        global anguloRot # para que el cubo de vueltas
        global velocidadAngular # velocidad angular para abrir y cerrar cubo
        global etapasCubo # etapas para visualizar la formacion del area del cubo
        
        global pinturaCuadrado1  # activar pintura de cuadrado 1
        global pinturaCuadrado2  # activar pintura de cuadrado 2
        global pinturaCuadrado3  # activar pintura de cuadrado 3
        global pinturaCuadrado4  # activar pintura de cuadrado 4
        global pinturaCuadrado5  # activar pintura de cuadrado 5
        global pinturaCuadrado6  # activar pintura de cuadrado 6        

         # cubo volumen  
        global contadorCuadradoVolumen # para la simulacion de area de un cuadrado en volumen
        global contadorCubo  #  cubo de volumen
        global contadorCubo1  #  cubo de volumen
        global contadorCubo2 # decrecer cubo de volumen
        global contadorCuboLado2 # para dibujar cubo lado 2
        global contadorCuboLado3 # para dibujar cubo lado 3
        global dedoLado # para seleccionar longitud lado cubo
        global visualizacionVolumen # visualizacion de volumen en pantalla
        
        # prism area 
        global pinturaPrisma1a  # activar pintura de prisma 1
        global pinturaPrisma1b  # activar pintura de prisma 1
        global pinturaPrisma2a  # activar pintura de prisma 2
        global pinturaPrisma2b  # activar pintura de prisma 2
        global pinturaPrisma3a  # activar pintura de prisma 3
        global pinturaPrisma3b  # activar pintura de prisma 3
        global contadorPrisma  # para la simulacion de area de un cuadrilatero

        
        # prism volumen
        global contadorPrismaVolumen # para volumen de prisma
        global contadorPrismaVolumenDedo # para construir volumen prisma
        global inicioPrismaVolumen # iniciar contador prisma volumen
      

        # cilindro area
        global anguloMovimiento # para abrir  el circulo 
        global anguloMovimiento1 # para cerrar el circulo 
        global pintarCirculo  # pintar area de circulo superior
        global pintarCirculo2 # pintar area de circulo inferior 
        global pintarRectangulo # pintar rectangulo
        global anguloRot1 # para abrir tapa
        global anguloRot2 # para cerrar tapa
        global anguloRotacion # para girar cilindro
        global condicion # abierto o cerrado
       

         # cilindro volumen
        global contadorCilindro # para aumentar altura cilindro
        global contadorCilindro2 # para disminuir altura cilindro
        global  dedoRadio # radio de volumen

        #colores
        global colorBlanco
     
        glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)        
 
        frame_rgb =cv2.cvtColor(nuevo_frame, cv2.COLOR_BGR2RGB)
      
        height,width,_ = nuevo_frame.shape
        tx_image = Image.fromarray(nuevo_frame)
        
        ix = tx_image.size[0]
        iy = tx_image.size[1]       
    

        elmenux,elmenuy=miMano.seleccionarMenu(frame_rgb,width,height)
        
        
        if (menuActivo1==1):
             etapasCubo=1
             
             #cubo 
             pinturaCuadrado1=0
             pinturaCuadrado2=0
             pinturaCuadrado3=0 
             pinturaCuadrado4=0 
             pinturaCuadrado5=0
             pinturaCuadrado6=0

             anguloRotacion=0 
             contadorCubo=0
             
             #cubo volumen 
             anguloRot=0
             contadorCubo=0
             
             #prisma
             contadorCuadradoArea=-0.5
             contadorCuadradoVolumen=-1
             contadorPrisma=-1
             pinturaPrisma1a=0
             pinturaPrisma1b=0
             pinturaPrisma2a=0 
             pinturaPrisma2b=0 
             pinturaPrisma3a=0
             pinturaPrisma3b=0

             pintarCirculo=0
             pintarCirculo2=0
             pintarRectangulo=0
             anguloMovimiento=90
             anguloMovimiento1=-90
            
            
             tx_image= miMenu.menuPrincipal(nuevo_frame)
             menuActivo1,menuActivo2,menuActivo3,seleccionFigura=miMano.selmenuActivo1(nuevo_frame,elmenux,elmenuy,menuActivo1,menuActivo2,menuActivo3,seleccionFigura) 
                                     

        if (menuActivo2==1):

             etapasCubo=1
                #cubo 
             pinturaCuadrado1=0
             pinturaCuadrado2=0
             pinturaCuadrado3=0 
             pinturaCuadrado4=0 
             pinturaCuadrado5=0
             pinturaCuadrado6=0

             anguloRotacion=0 
             contadorCubo=0
             
             #cubo volumen 
             anguloRot=0
             contadorCubo=0
             
             #prisma
             contadorCuadradoArea=-0.5
             contadorCuadradoVolumen=-1
             contadorPrisma=-1
             pinturaPrisma1a=0
             pinturaPrisma1b=0
             pinturaPrisma2a=0 
             pinturaPrisma2b=0 
             pinturaPrisma3a=0
             pinturaPrisma3b=0

             pintarCirculo=0
             pintarCirculo2=0
             pintarRectangulo=0
             anguloMovimiento=90
             anguloMovimiento1=-90
             tx_image= miMenu.seleccionFiguraNivel2(nuevo_frame,seleccionFigura)
             menuActivo1,menuActivo2,menuActivo3,seleccionOperacion=miMano.selmenuActivo2(nuevo_frame,elmenux,elmenuy,menuActivo1,menuActivo2,menuActivo3,seleccionOperacion) 
                                            
        
        if (menuActivo3==1):
              
                tx_image= miMenu.seleccionFiguraNivel3(nuevo_frame,seleccionFigura,seleccionOperacion)   
                menuActivo1,menuActivo2,menuActivo3=miMano.selmenuActivo3(nuevo_frame,elmenux,elmenuy,menuActivo1,menuActivo2,menuActivo3)   
                                   
                if ( seleccionFigura==1)and(seleccionOperacion==2):                   
                  
                    colorCuadrado1=0.7,0.5,0.8,1.0
                    colorCuadrado2=0.7,0.2,0.2,1.0
                    colorCuadrado3=0.9, 0.4, 0.3,1.0
                    colorCuadrado4=0.5,0.7,0.9,1.0
                    colorCuadrado5=0.5,0.8,0.6,1.0
                    colorCuadrado6=0.9,0.8,0.4,1.0

        
                    if pinturaCuadrado1==1:
                                    miGrafico.pintarCuadradoT(-0.5,-0.5,-0.5,0.5,-1.5,0.5,-1.5,-0.5,colorCuadrado1)     

                    if pinturaCuadrado2==1:
                                    miGrafico.pintarCuadradoT(0.5,0.5,0.5,1.5,-0.5,1.5,-0.5,0.5,colorCuadrado2)  
 
                    if pinturaCuadrado3==1:
                                     miGrafico.pintarCuadradoT(0.5,-0.5,0.5,0.5,-0.5,0.5,-0.5,-0.5,colorCuadrado3) 

                    if pinturaCuadrado4==1:
                                     miGrafico.pintarCuadradoT(0.5,0.5,1.5,0.5,1.5,-0.5,0.5,-0.5,colorCuadrado4) 
 
                    if pinturaCuadrado5==1:
                                     miGrafico.pintarCuadradoT(1.5,0.5,2.5,0.5,2.5,-0.5,1.5,-0.5,colorCuadrado5)             


                    if pinturaCuadrado6==1:

                                     miGrafico.pintarCuadradoT(0.5,-0.5,0.5,-1.5,-0.5,-1.5,-0.5,-0.5,colorCuadrado6)     
                    
                    if (etapasCubo==1):

                        
                        miGrafico.graficoLineaColorU(-0.5,-0.5,0,-0.5,0.5,0,colorBlanco)   
                        etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,5,frame_rgb)  
                        miGrafico.dibujoTexto18("L",1.0, 0.2)
                        area=str(pinturaCuadrado1+pinturaCuadrado2+pinturaCuadrado3+pinturaCuadrado4+pinturaCuadrado5+pinturaCuadrado6)                                                 
                      

                    if (etapasCubo==2):
                        miGrafico.graficoLineaColorU(-0.5,-0.5,0,-0.5,0.5,0,colorBlanco) 
                        miGrafico.graficoLineaColorU(-0.5,-0.5,0,0.5,-0.5,0,colorBlanco)
                        miGrafico.dibujoTexto18("L",1.0, 0.2)
                        miGrafico.dibujoTexto18("L",0, 1)
                        etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,5,frame_rgb)
                                           
                    if (etapasCubo==3):

                        miGrafico.dibujoTexto18("L",1.0, 0.2)
                        miGrafico.dibujoTexto18("L",0, 1)                          
                        miGrafico.graficoLineaColorU(-0.5,-0.5,0,-0.5,0.5,0,colorBlanco) 
                        miGrafico.graficoLineaColorU(-0.5,-0.5,0,0.5,-0.5,0,colorBlanco) 

                        if  contadorCuadradoArea<=0.5:   
                            
                            miGrafico.graficoCuadrilateroSimulacion(-0.5,0.5,0,contadorCuadradoArea,0.5,0,contadorCuadradoArea,-0.5,0,-0.5,-0.5,0)
                            contadorCuadradoArea=contadorCuadradoArea+0.05
                            time.sleep(1/10)   
                        if contadorCuadradoArea >0.5 :       
                                miGrafico.graficoCuadrilateroSimulacion(-0.5,0.5,0,contadorCuadradoArea,0.5,0,contadorCuadradoArea,-0.5,0,-0.5,-0.5,0)
                                miGrafico.dibujoTexto18("Area Cuadrado = L x L ", 2, 2.5) 

                        etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,5,frame_rgb)
                        if (etapasCubo==2 or etapasCubo==4):
                               contadorCuadradoArea=-0.5           
                        
                    
                    if (etapasCubo==4):
                       
                        colorCubo1=(0.7,0.2,0.2,0.5)
                        miGrafico.graficoCuadrilatero(0.5,0.5,0.5,1.5,-0.5,1.5,-0.5,0.5,colorCubo1)
                        colorCubo2=(0.9, 0.4, 0.3,0.5)
                        miGrafico.graficoCuadrilatero(0.5,-0.5,0.5,0.5,-0.5,0.5,-0.5,-0.5,colorCubo2)
                        colorCubo3=(0.9,0.8,0.4,0.5)
                        miGrafico.graficoCuadrilatero(0.5,-0.5,0.5,-1.5,-0.5,-1.5,-0.5,-0.5,colorCubo3)
                        colorCubo4=(0.7,0.5,0.8,0.5)
                        miGrafico.graficoCuadrilatero(-0.5,-0.5,-0.5,0.5,-1.5,0.5,-1.5,-0.5,colorCubo4)
                        colorCubo5=(0.5,0.7,0.9,0.5)
                        miGrafico.graficoCuadrilatero(0.5,0.5,1.5,0.5,1.5,-0.5,0.5,-0.5,colorCubo5)
                        colorCubo6= (0.5,0.8,0.6,0.5)
                        miGrafico.graficoCuadrilatero(1.5,0.5,2.5,0.5,2.5,-0.5,1.5,-0.5,colorCubo6)

                        if (((elmenux>360)and(elmenux<380))and((elmenuy>230)and(elmenuy<250))):    
                                pinturaCuadrado1=1
                        if (((elmenux>310)and(elmenux<330))and((elmenuy>180)and(elmenuy<210))):    
                                pinturaCuadrado2=1                                  
                        if (((elmenux>310)and(elmenux<330))and((elmenuy>230)and(elmenuy<260))):    
                                pinturaCuadrado3=1 
                        if (((elmenux>260)and(elmenux<280))and((elmenuy>230)and(elmenuy<260))):    
                                pinturaCuadrado4=1 
                        if (((elmenux>200)and(elmenux<230))and((elmenuy>230)and(elmenuy<260))):    
                                pinturaCuadrado5=1
                        if (((elmenux>310)and(elmenux<330))and((elmenuy>270)and(elmenuy<300))):  
                                pinturaCuadrado6=1
                      
                        area=str(pinturaCuadrado1+pinturaCuadrado2+pinturaCuadrado3+pinturaCuadrado4+pinturaCuadrado5+pinturaCuadrado6)
                        miGrafico.dibujoTexto18(area+" Area Cuadrado", 2, 3) 
                        etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,5,frame_rgb)
                        if (etapasCubo==3 or etapasCubo==5) :
                                pinturaCuadrado1=0
                                pinturaCuadrado2=0
                                pinturaCuadrado3=0 
                                pinturaCuadrado4=0 
                                pinturaCuadrado5=0
                                pinturaCuadrado6=0 


                    if (etapasCubo==5):
                        miGrafico.dibujoTexto18("Area Cubo = 6(Area Cuadrado)", 3, 3)
                        anguloRot=anguloRot%360+5
                        distanciax12,distanciay12 = miMano.distanciaPuntos(frame_rgb,width,height,12,0)
                        temporaly=pyf
                        pyf=distanciay12                       

                        if (distanciay12==0):                  
                            if(anguloRotacion==0):
                                direccionPlano=-1 
                            else:
                                if (anguloRotacion==90):
                                            direccionPlano=1
                        else:                  

                            if (abs(pyf)- abs(temporaly))>10:
                                direccionPlano=-1
                            else:
                                if (abs(temporaly)-abs(pyf))>10:
                                    direccionPlano=1
                         

                        punto11=(0.5,0.5,0)
                        punto12=(-0.5,0.5,0)
                        punto13=(-0.5,-0.5,0)
                        punto14=(0.5,-0.5,0)
                        color=(0.9, 0.4, 0.3,0.5)  

                        anguloRot=anguloRot+5
                        glRotate(anguloRot,0,1,0)
                        glTranslate(0,0,-0.5)

                        ejeGiro=(1,0,0)
                        cx=0
                        cy=0
                        cz=0
                        dx=0
                        dy=0
                        dz=0
                    
                        miGrafico.graficandoPlanoDelPrisma(punto11,punto12,punto13,punto14,dx,dy,dz,cx,cy,cz,ejeGiro,0,color)       

                        dx2=-0.5 
                        cx2=-0.5
                        ejeGiro2=(0,1,0)
                   
                        color2=(0.7,0.5,0.8,0.5)
                        
                        dx4=0.5
                        cx4=0.5
                        ejeGiro4=(0,1,0)
                   
                        color4=(0.5,0.7,0.9)

                        dx5=1.5
                        cx5=0.5
                    
                        ejeGiro5=(0,1,0)
                        color5=(0.5,0.8,0.6)
                        color5=(0.5,0.8,0.6)

                        dy6=-0.5
                        cy6=-0.5      
                        ejeGiro6=(1,0,0)
                        color6=(0.9,0.8,0.4)

                        dy3=0.5
                        cy3=0.50
                        ejeGiro3=(1,0,0)
                        color3=(0.7,0.2,0.2)
                        
                        if ((anguloRotacion>=90)and(direccionPlano==-1)):
                            anguloRotacion-=velocidadAngular
                        if ((anguloRotacion<=0)and(direccionPlano==1)):
                            anguloRotacion+=velocidadAngular
                        if ((anguloRotacion>=0)and(direccionPlano==1)):
                            anguloRotacion+=velocidadAngular
                        if ((anguloRotacion<=90)and(direccionPlano==-1)):
                            anguloRotacion-=velocidadAngular  
                        if ((anguloRotacion<=0)and(direccionPlano==-1)):
                            anguloRotacion=0  
                        if ((anguloRotacion>=90)and(direccionPlano==1)):
                            anguloRotacion=90  
                        miGrafico.graficandoPlanoDelPrisma(punto11,punto12,punto13,punto14,dx2,dy,dz,cx2,cy,cz,ejeGiro2,-anguloRotacion,color2)
                        miGrafico.graficandoPlanoDelPrisma(punto11,punto12,punto13,punto14,dx4,dy,dz,cx4,cy,cz,ejeGiro4,anguloRotacion,color4)      
                        if ((anguloRotacion>=90)and(direccionPlano==1)):
                            
                            dx5=0.5
                            cx5=0.5
                            cz5=1
                            miGrafico.graficandoPlanoDelPrisma(punto11,punto12,punto13,punto14,dx5,dy,dz,cx5,cy,cz5,ejeGiro5,180,color5)   
                        else:
                            miGrafico.graficandoPlanoDelPrisma(punto11,punto12,punto13,punto14,dx5,dy,dz,cx5,cy,cz,ejeGiro5,anguloRotacion,color5)
                        miGrafico.graficandoPlanoDelPrisma(punto11,punto12,punto13,punto14,dx,dy6,dz,cx,cy6,cz,ejeGiro6,anguloRotacion,color6)
                        miGrafico.graficandoPlanoDelPrisma(punto11,punto12,punto13,punto14,dx,dy3,dz,cx,cy3,cz,ejeGiro3,-anguloRotacion,color3)
                        
                        etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,5,frame_rgb)

                       
                        if (etapasCubo==4 or etapasCubo==6):
                              anguloRotacion=0                  
                       
                      
                if ( seleccionFigura==1)and(seleccionOperacion==1):                
                       
                        if (etapasCubo==1):
   
                            miGrafico.graficoLineaColorU(-1,-1,0,-1,1,0,colorBlanco) 
   
                            miGrafico.graficoLineaColorU(-1,-1,0,1,-1,0,colorBlanco)
   
                            miGrafico.graficoLineaColorU(-1,-1,0,-1,-1,0,colorBlanco)
                            
                            miGrafico.dibujoTexto18(" L", 0, 1.8)
                            miGrafico.dibujoTexto18(" L", 2, 0.2) 

                           
                            glPushMatrix() 
                            glTranslate(0,0,-3)
                            miGrafico.dibujoTexto18(" L", 0.5, 0.4)

                            glPopMatrix()
                            etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,5,frame_rgb)
                        if (etapasCubo==2):
                                
                       
                            miGrafico.graficoLineaColorU(-1,-1,0,-1,1,0,colorBlanco) 
                        
                            miGrafico.graficoLineaColorU(-1,-1,0,1,-1,0,colorBlanco)
                      
                            miGrafico.graficoLineaColorU(-1,-1,0,-1,-1,0,colorBlanco)
                            
                            miGrafico.dibujoTexto18(" L", 2, 0.2)
                            miGrafico.dibujoTexto18(" L", 0, 1.8)                            
                     
                            glPushMatrix() 
                            glTranslate(0,0,-3)
                            miGrafico.dibujoTexto18(" L", 0.5, 0.4) 
                            glPopMatrix()
                            
                            
                            
                            if  contadorCuadradoVolumen<=1:   
                                 
                                    miGrafico.graficoCuadrilateroSimulacion(-1,-1,0,1,-1,0,1,contadorCuadradoVolumen,0,-1,contadorCuadradoVolumen,0)             


                                    contadorCuadradoVolumen=contadorCuadradoVolumen+0.05
                                    time.sleep(1/20)   
                            else:
                                    if contadorCuadradoVolumen >1 :
                                 
                                      miGrafico.graficoCuadrilateroSimulacion(-1,-1,0,1,-1,0,1,1,0,-1,1,0) 

                            etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,5,frame_rgb)
                            if (etapasCubo==1 or etapasCubo==3):
                                  contadorCuadradoVolumen=-1          
                         

                        
                        if (etapasCubo==3):
                                anguloRot=anguloRot+5
                                if anguloRot<=90:
                                                            
                                    glRotate(-anguloRot,1,0,0) 
                                    miGrafico.graficandoCoordenadas(1)
                                 
                                    miGrafico.graficoCuadrilateroSimulacion(-1,-1,0,1,-1,0,1,1,0,-1,1,0) 
                                    
                                else:
                                    
                                    glRotate(-90,1,0,0) 
                                    
                                    if contadorCubo<=1:
                                        contadorCubo=contadorCubo+0.01
                                        glTranslate(0,0, contadorCubo)
                                        miGrafico.graficandoCoordenadas(1)                      
                                  
                                        miGrafico.graficoCuadrilateroSimulacion(-1,-1,0,1,-1,0,1,1,0,-1,1,0) 

                                    else:
                                        if contadorCubo>1:    
                                                glTranslate(0,0, 1)  
                                                miGrafico.graficandoCoordenadas(1)                                  
                                                miGrafico.graficoCuadrilateroSimulacion(-1,-1,0,1,-1,0,1,1,0,-1,1,0)            

                                miGrafico.dibujoTexto18(" L", 2, 0.2)
                                miGrafico.dibujoTexto18(" L", 0, 1.8)
                             
                                glPushMatrix() 
                                glTranslate(0,0,-1)
                                miGrafico.dibujoTexto18(" L", 0.5, 0.4) 
                                glPopMatrix()
                                etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,5,frame_rgb)
                                if (etapasCubo==2 or etapasCubo==4):
                                      anguloRot=0
                                      contadorCubo=0
                                  
                              
                        
                        if (etapasCubo==4):

                           
                            
                            distanciax12,distanciay12 = miMano.distanciaPuntos(frame_rgb,width,height,12,0)
                                            
                            if (distanciay12>=100):
                                condicion=1
                            else:
                                if (distanciay12>=20)and(distanciay12<100):
                                    condicion=-1   

                            glRotate(-90,1,0,0) 
                            glTranslate(0,0,1)
                            miGrafico.dibujoTexto18(" L", 2, 0.2)
                            miGrafico.dibujoTexto18(" L", 0, 1.8)  
                            glPushMatrix() 
                            glTranslate(0,0,-1)
                            miGrafico.dibujoTexto18(" L", 0.5, 0.4) 
                            glPopMatrix()
                            miGrafico.graficoLineaColorU(-1,-1,0,-1,1,0,colorBlanco) 
                            miGrafico.graficoLineaColorU(-1,-1,0,1,-1,0,colorBlanco)
                            miGrafico.graficoLineaColorU(-1,-1,0,-1,-1,0,colorBlanco)
                      
                            anguloRot=anguloRot+5
                            glRotate(anguloRot,0,0,1)
                            glTranslate(0,0,-1)
                            
                            if  condicion==1 :
                                 
                                 if  contadorCuadradoVolumen <1 :

                                     miGrafico.graficoPlanoSimulacion(-1,-1,contadorCuadradoVolumen,1)
                                     miGrafico.graficoCuboEsqueleticoVariableVolumen(-1,-1,1,1,1,contadorCuadradoVolumen)
                                     contadorCuadradoVolumen=contadorCuadradoVolumen+0.05
                                 else:
                                        if  contadorCuadradoVolumen >1 :
                                            miGrafico.graficoPlanoSimulacion(-1,-1,1,1) 
                                            miGrafico.graficoCuboEsqueleticoVariableVolumen(-1,-1,1,1,1,1)
                                           
                            else:
                                 if  condicion==-1:
                                        if  contadorCuadradoVolumen >-1 :
                                            miGrafico.graficoPlanoSimulacion(-1,-1,contadorCuadradoVolumen,1)
                                            miGrafico.graficoCuboEsqueleticoVariableVolumen(-1,-1,1,1,1,contadorCuadradoVolumen)
                                            
                                            contadorCuadradoVolumen=contadorCuadradoVolumen-0.05
                                        else:
                                             if  contadorCuadradoVolumen <=-1.0 :                                
                                                 miGrafico.graficoPlanoSimulacion(-1,-1,-1,1)  
                                                 miGrafico.graficoCuboEsqueleticoVariableVolumen(-1,-1,1,1,1,-1)


                            etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,5,frame_rgb)
                            if (etapasCubo==3 or etapasCubo==5):
                                      anguloRot=0   
                                      contadorCubo2=1      
                                      contadorCubo1=-1                 
                           

                        if (etapasCubo==5):                                            
                                                            
                            longitudCubo=miMano.contarDedos(nuevo_frame,width,height)
                            rango=10
 
                            glPushMatrix()                                                             
                          
                            
                            anguloRot=anguloRot%360+5
                            anguloRot=anguloRot+10                                     
                            glRotate(anguloRot,1,1,0)
                          
                           
                            if longitudCubo==1:
                                  dedoLado=1
                                  
                            else:
                                  if longitudCubo==2:
                                        dedoLado=2   
                                  else:
                                        if longitudCubo==3:
                                              dedoLado=3          
                           
                            color1=(0.18,0.52,0.75,1.0)
                            color2=(1,0.906,0,1.0)                          
                            
                           
                            if dedoLado==1:
                                  
                                  miGrafico.graficoCuboSecuencial8Cubos(color2,1,0,0,0,0,0,0,0) 
                                  visualizacionVolumen=1
                                  contadorCuboLado2=0
                                  contadorCuboLado3=0
                              
                                  
                            else:
                                
                                if dedoLado==2:        
                                        contadorCuboLado3=0
                                        contadorCuboLado2=contadorCuboLado2+1
                                         

                                        if contadorCuboLado2>0 and contadorCuboLado2<=rango:
                                           
                                            miGrafico.graficoCuboSecuencial8Cubos(color1,1,0,0,0,0,0,0,0)
                                            visualizacionVolumen=1
                                        
                                        if contadorCuboLado2>rango and contadorCuboLado2<=2*rango:    
                                           
                                            miGrafico.graficoCuboSecuencial8Cubos(color1,1,1,0,0,0,0,0,0)
                                            visualizacionVolumen=2 
                                        
                                        if contadorCuboLado2>2*rango and contadorCuboLado2<=3*rango:
                                           
                                            miGrafico.graficoCuboSecuencial8Cubos(color1,1,1,1,0,0,0,0,0)
                                            visualizacionVolumen=3
                                        
                                        if contadorCuboLado2>3*rango and contadorCuboLado2<=4*rango:
                                           
                                            miGrafico.graficoCuboSecuencial8Cubos(color1,1,1,1,1,0,0,0,0)
                                            visualizacionVolumen=4  
                                        
                                        if contadorCuboLado2>4*rango and contadorCuboLado2<=5*rango:
                                            miGrafico.graficoCuboSecuencial8Cubos(color1,1,1,1,1,1,0,0,0)
                                            visualizacionVolumen=5 
                                        
                                        if contadorCuboLado2>5*rango and contadorCuboLado2<=6*rango:
                                           
                                            miGrafico.graficoCuboSecuencial8Cubos(color1,1,1,1,1,1,1,0,0)
                                            visualizacionVolumen=6
                                       
                                        if contadorCuboLado2>6*rango and contadorCuboLado2<=7*rango:
                                           
                                            miGrafico.graficoCuboSecuencial8Cubos(color1,1,1,1,1,1,1,1,0)
                                            visualizacionVolumen=7
                                        
                                        if contadorCuboLado2>7*rango and contadorCuboLado2<=8*rango:
                                           
                                            miGrafico.graficoCuboSecuencial8Cubos(color1,1,1,1,1,1,1,1,1)

                                            visualizacionVolumen=8
                                        
                                        if contadorCuboLado2>8*rango:
                                           
                                            miGrafico.graficoCuboSecuencial8Cubos(color2,1,1,1,1,1,1,1,1)
                                            visualizacionVolumen=8                   
    
                                else:                                        
                                        
                                        if dedoLado==3:   
                                                         
                                             contadorCuboLado3=contadorCuboLado3+1                        
                                             contadorCuboLado2=0
                                             rango=5
                                             if contadorCuboLado3>0 and contadorCuboLado3<=rango:
                                                  
                                               
                                                  miGrafico.graficoCuboSecuencial27Cubos(color1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                                                  visualizacionVolumen=1
                                                
                                            
                                             if contadorCuboLado3>rango and contadorCuboLado3<=2*rango:
                                                  
                                               
                                                  miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                                                 
                                                  visualizacionVolumen=2
                                            
                                             if contadorCuboLado3>2*rango and contadorCuboLado3<=3*rango:
                                               
                                                  miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                                                  visualizacionVolumen=3
                                             if contadorCuboLado3>3*rango and contadorCuboLado3<=4*rango:
                                               
                                                  miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                                                  visualizacionVolumen=4
                                             
                                             if contadorCuboLado3>4*rango and contadorCuboLado3<=5*rango:
                                               
                                                 miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                                                 visualizacionVolumen=5
                                            
                                             if contadorCuboLado3>5*rango and contadorCuboLado3<=6*rango:
                                                
                                                 miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                                                 visualizacionVolumen=6
                                                 

                                             if contadorCuboLado3>6*rango and contadorCuboLado3<=7*rango:
                                                
                                               
                                                 miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                                                 visualizacionVolumen=7
                                                
                                             if contadorCuboLado3>7*rango and contadorCuboLado3<=8*rango:
                                                   
                                                    miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                                                    visualizacionVolumen=8
                                                
                                             if contadorCuboLado3>8*rango and contadorCuboLado3<=9*rango:
                                                 
                                                    miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                                                    visualizacionVolumen=9
                                             
                                             
                                             if contadorCuboLado3>9*rango and contadorCuboLado3<=10*rango:
                                                   
                                                    miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                                                    visualizacionVolumen=10
                                                 
                                             if contadorCuboLado3>10*rango and contadorCuboLado3<=11*rango:
                                                  
                                                   
                                                    miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                                                    visualizacionVolumen=11                                             
                                            
                                             if contadorCuboLado3>11*rango and contadorCuboLado3<=12*rango:
   
                                                    miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                                                    visualizacionVolumen=12
                                                        
                                             if contadorCuboLado3>12*rango and contadorCuboLado3<=13*rango:
                                                  
                                                    miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0)                                             
                                                    visualizacionVolumen=13
                                            
                                             
                                             if contadorCuboLado3>13*rango and contadorCuboLado3<=14*rango:
                                                  
                                                    miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0)
                                                    visualizacionVolumen=14

                                             if contadorCuboLado3>14*rango and contadorCuboLado3<=15*rango:
                                                  
                                                    miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0)
                                                    visualizacionVolumen=15

                                             if contadorCuboLado3>15*rango and contadorCuboLado3<=16*rango:

                                                    miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0)

                                                    visualizacionVolumen=16
                                             
                                             if contadorCuboLado3>16*rango and contadorCuboLado3<=17*rango:

                                                   
                                                    miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0)
                                                    visualizacionVolumen=17                                                    

                                             if contadorCuboLado3>17*rango and contadorCuboLado3<=18*rango:
                                                     
                                                  
                                                    miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0)
                                                    visualizacionVolumen=18

                                             if contadorCuboLado3>18*rango and contadorCuboLado3<=19*rango:
                                                  
                                                   
                                                    miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0)
                                                    visualizacionVolumen=19

                                             if contadorCuboLado3>19*rango and contadorCuboLado3<=20*rango:
                                                  

                                                    miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0)
                                                    
                                                    visualizacionVolumen=20


                                             if contadorCuboLado3>20*rango and contadorCuboLado3<=21*rango:

                                                    miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0)

                                                    visualizacionVolumen=21

                                             if contadorCuboLado3>21*rango and contadorCuboLado3<=22*rango:

                                                    miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0)

                                                    visualizacionVolumen=22
                                                 

                                             if contadorCuboLado3>22*rango and contadorCuboLado3<=23*rango:

                                                    miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0)

                                                    visualizacionVolumen=23
                                             
                                             if contadorCuboLado3>23*rango and contadorCuboLado3<=24*rango:

                                                    miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0)

                                                    visualizacionVolumen=24

                                             if contadorCuboLado3>24*rango and contadorCuboLado3<=25*rango:

                                                    miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0)
                                                 
                                                    
                                                    visualizacionVolumen=25

                                            
                                             if contadorCuboLado3>25*rango and contadorCuboLado3<=26*rango:

                                                    miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0)
                                                    visualizacionVolumen=26     


                                             if contadorCuboLado3>26*rango and contadorCuboLado3<=27*rango:

                                                    miGrafico.graficoCuboSecuencial27Cubos(color1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
                                                    visualizacionVolumen=27     
                                             
                                             if contadorCuboLado3>27*rango:
                                                    miGrafico.graficoCuboSecuencial27Cubos(color2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
                                                   
                                                    visualizacionVolumen=27  
                            glPopMatrix()
                              
                            if dedoLado==1:

                                 miGrafico.dibujoTexto18("L = 1 u",2, 3)
                                 miGrafico.dibujoTexto18("Volumen = 1 u", 2, 4)
                                 miGrafico.dibujoTexto10("3", -0.32, 3.8)
                                 
                                  
                            else:
                                  if (dedoLado==2):
                                         
                                       
                                         miGrafico.dibujoTexto18("L = 2 u",2, 3)
                                         if visualizacionVolumen<8:  
                                           miGrafico.dibujoTexto18("Volumen = "+str(visualizacionVolumen)+" u", 2, 4)
                                           miGrafico.dibujoTexto10("3", -0.33, 3.8)
                                         else:
                                            
                                           miGrafico.dibujoTexto18("Volumen = "+str(visualizacionVolumen)+" u", 2, 4)
                                           miGrafico.dibujoTexto10("3", -0.33, 3.8)
                                  else:
                                        if (dedoLado==3):
                                              miGrafico.dibujoTexto18("L = 3 u",2, 3)
                                              
                                              if visualizacionVolumen<27:  
                                                    if visualizacionVolumen<10:
                                                         miGrafico.dibujoTexto10("3", -0.33, 3.8)
                                                    else:
                                                          miGrafico.dibujoTexto10("3", -0.50, 3.8)    
                                                    miGrafico.dibujoTexto18("Volumen = "+str(visualizacionVolumen)+" u", 2, 4)
                                                
                                              else:
                                               
                                                miGrafico.dibujoTexto18("Volumen = "+str(visualizacionVolumen)+" u", 2, 4)
                                                miGrafico.dibujoTexto10("3", -0.50, 3.8)
                            
                                               
                            etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,5,frame_rgb)                            

                          

                if ( seleccionFigura==2)and(seleccionOperacion==2):
                    
                
                    if pinturaPrisma1a==1:
                    
                                    color1ab=(0.7,0.5,0.8,0.5)
                                    miGrafico.graficoPrismaPintaT(-1,2,1,2,1,-2,-1,-2,color1ab) 
                                    miGrafico.graficoPrismaPintaT(2,2,4,2,4,-2,2,-2,color1ab) 
                                    glColor4f(0.7,0.5,0.8,0.5)
                                    miGrafico.dibujoTexto18("2A2",-1,4)
                                    glColor4f(1,1,1,1)  
                                   
                    if pinturaPrisma1b==1: 
                    
                                     miGrafico.graficoPrismaPintaT(2,2,4,2,4,-2,2,-2,color1ab) 
                                     miGrafico.graficoPrismaPintaT(-1,2,1,2,1,-2,-1,-2,color1ab)  
                                   

                    if pinturaPrisma2a==1:
                    
                                     color2ab=(0.9, 0.4, 0.3,0.5)
                                     miGrafico.graficoPrismaPintaT(-2,2,-1,2,-1,-2,-2,-2,color2ab) 
                                     miGrafico.graficoPrismaPintaT(1,2,2,2,2,-2,1,-2,color2ab)  

                                   
                    if pinturaPrisma2b==1:                  
                    
                                    miGrafico.graficoPrismaPintaT(1,2,2,2,2,-2,1,-2,color2ab)  
                                    miGrafico.graficoPrismaPintaT(-2,2,-1,2,-1,-2,-2,-2,color2ab)                                         
                                    glColor4f(0.9, 0.4, 0.3,0.5)
                                    miGrafico.dibujoTexto18("2A3",-2,4)
                                    glColor4f(1,1,1,1)

                    if pinturaPrisma3a==1:
                    
                                    color3ab=(0.9,0.8,0.4,0.5)
                                    miGrafico.graficoPrismaPintaT(-1,3,1,3,1,2,-1,2,color3ab)  
                                    miGrafico.graficoPrismaPintaT(-1,-3,1,-3,1,-2,-1,-2,color3ab)  
                                    glColor4f(0.9,0.8,0.4,0.5)
                                    miGrafico.dibujoTexto18("2A1",0,4)
                                    glColor4f(1,1,1,1) 
                                   
                    if pinturaPrisma3b==1:
                    
                                    miGrafico.graficoPrismaPintaT(-1,-3,1,-3,1,-2,-1,-2,color3ab)  
                                    miGrafico.graficoPrismaPintaT(-1,3,1,3,1,2,-1,2,color3ab)   
                    
                    if (etapasCubo==1):
                    
                       
                        miGrafico.graficoLineaColorU(-1,-2,0,-1,2,0,colorBlanco)
                        miGrafico.dibujoTexto18("L1",2,0)
                        
                        etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,6,frame_rgb)  
                       

                    if (etapasCubo==2):
                   
                        miGrafico.graficoLineaColorU(-1,-2,0,-1,2,0,colorBlanco)
                   
                        miGrafico.graficoLineaColorU(-1,-2,0,1,-2,0,colorBlanco)

                        miGrafico.dibujoTexto18("L1",2,0)
                        miGrafico.dibujoTexto18("L2",0,3)
                        etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,6,frame_rgb)  
                       
                     
                    
                    if (etapasCubo==3):
                    
                        miGrafico.graficoLineaColorU(-1,-2,0,-1,2,0,colorBlanco)                        
                        miGrafico.graficoLineaColorU(-1,-2,0,1,-2,0,colorBlanco) 

                        miGrafico.dibujoTexto18("L1",2,0)
                        miGrafico.dibujoTexto18("L2",0,3)
                        if  contadorPrisma<=2:   
                            miGrafico.graficoCuadrilateroSimulacion(-1,-2,0,1,-2,0,1,contadorPrisma,0,-1,contadorPrisma,0)
                            contadorPrisma=contadorPrisma+0.05
                            time.sleep(1/30)   
                        if contadorPrisma >2 :

                                  miGrafico.graficoCuadrilateroSimulacion(-1,-2,0,1,-2,0,1,2,0,-1,2,0)
                                
                        miGrafico.dibujoTexto18("Area Rectángulo = L1 x L2",2.5,4)

                        
                        etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,6,frame_rgb)  
                        if (etapasCubo==2 or etapasCubo==4):
                              contadorPrisma=-2                          
                    
                    if (etapasCubo==4):
                        glPushMatrix()
                        glTranslate(0,0,1)
                        miGrafico.dibujoTexto18("A1",0,-2.1)
                        miGrafico.dibujoTexto18("A1",0,2.3)

                        miGrafico.dibujoTexto18("A2",0,0)
                        miGrafico.dibujoTexto18("A2",-2.5,0)

                        miGrafico.dibujoTexto18("A3",1.5,0)
                        miGrafico.dibujoTexto18("A3",-1.2,0)
                        
                        glPopMatrix()


                        
                        color1=(0.7,0.5,0.8,0.5)

                        miGrafico.graficoCuadrilatero(-1,2,1,2,1,-2,-1,-2,color1)
 
                        miGrafico.graficoCuadrilatero(2,2,4,2,4,-2,2,-2,color1)                    
                        
                        color2=(0.9, 0.4, 0.3,0.5)

                        miGrafico.graficoCuadrilatero(-2,2,-1,2,-1,-2,-2,-2,color2)                       

                        miGrafico.graficoCuadrilatero(1,2,2,2,2,-2,1,-2,color2)
                        
                        color3=(0.9,0.8,0.4,0.5)

                        miGrafico.graficoCuadrilatero(-1,3,1,3,1,2,-1,2,color3)                    

                        miGrafico.graficoCuadrilatero(-1,-2,1,-2,1,-3,-1,-3,color3)  
                       

                        if ((elmenux>280)and(elmenux<350))and((elmenuy>160)and(elmenuy<300)):
                                pinturaPrisma1a=1
                                pinturaPrisma1b=1
                               

                        if ((elmenux>130)and(elmenux<190))and((elmenuy>160)and(elmenuy<300)):   
                                pinturaPrisma1b=1
                                pinturaPrisma1a=1

                        if (((elmenux>380)and(elmenux<400))and((elmenuy>160)and(elmenuy<300))):    
                                pinturaPrisma2a=1 
                                pinturaPrisma2b=1  
                               
                        
                        if (((elmenux>230)and(elmenux<250))and((elmenuy>160)and(elmenuy<300))):
                                    pinturaPrisma2b=1  
                                    pinturaPrisma2a=1  


                        if (((elmenux>280)and(elmenux<350))and((elmenuy>110)and(elmenuy<130))):  
                                pinturaPrisma3a=1
                                pinturaPrisma3b=1 
                               
                        
                        if (((elmenux>280)and(elmenux<350))and((elmenuy>350)and(elmenuy<380))):  
                                pinturaPrisma3b=1 
                                pinturaPrisma3a=1             

                        etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,5,frame_rgb)  
                        
                        if (etapasCubo==3):
                                    pinturaPrisma1a=0
                                    pinturaPrisma1b=0
                                    pinturaPrisma2a=0
                                    pinturaPrisma2b=0
                                    pinturaPrisma3a=0
                                    pinturaPrisma3b=0  
                      

                    if (etapasCubo==5):
                        
                      

                        pinturaPrisma1a=0
                        pinturaPrisma1b=0
                        pinturaPrisma2a=0 
                        pinturaPrisma2b=0 
                        pinturaPrisma3a=0
                        pinturaPrisma3b=0   


                        glColor4f(1,1,1,1)
                        miGrafico.dibujoTexto18("Area Prisma =",2.3,4)
                        glColor4f(1,1,1,1)

                        glColor4f(0.9,0.8,0.4,0.5)
                        miGrafico.dibujoTexto18("2A1+",0,4)
                        glColor4f(1,1,1,1)

                        glColor4f(0.7,0.5,0.8,0.5)
                        miGrafico.dibujoTexto18("2A2+",-1,4)
                        glColor4f(1,1,1,1)

                        glColor4f(0.9, 0.4, 0.3,0.5)
                        miGrafico.dibujoTexto18("2A3",-2,4)
                        glColor4f(1,1,1,1)

                  
                        
                        anguloRot=anguloRot%360+5
                        distanciax12,distanciay12 = miMano.distanciaPuntos(frame_rgb,width,height,12,0)
                        temporaly=pyf
                        pyf=distanciay12         


                        if (distanciay12==0):                  
                            if(anguloRotacion==0):
                                direccionPlano=-1 
                            else:
                                if (anguloRotacion==90):
                                            direccionPlano=1
                        else:                  

                            if (abs(pyf)- abs(temporaly))>10:
                                direccionPlano=-1
                            else:
                                if (abs(temporaly)-abs(pyf))>10:
                                    direccionPlano=1

                         
                        if ((anguloRotacion>=90)and(direccionPlano==-1)):
                            anguloRotacion-=velocidadAngular
                        if ((anguloRotacion<=0)and(direccionPlano==1)):
                            anguloRotacion+=velocidadAngular
                        if ((anguloRotacion>=0)and(direccionPlano==1)):
                            anguloRotacion+=velocidadAngular
                        if ((anguloRotacion<=90)and(direccionPlano==-1)):
                            anguloRotacion-=velocidadAngular  
                        if ((anguloRotacion<=0)and(direccionPlano==-1)):
                            anguloRotacion=0  
                        if ((anguloRotacion>=90)and(direccionPlano==1)):
                            anguloRotacion=90  
                    
         

                        punto11=(-1,2,0)
                        punto12=(1,2,0)
                        punto13=(1,-2,0)
                        punto14=(-1,-2,0)
                  
                        color=( 0.7,0.5,0.8,0.5)
                        anguloRot=anguloRot+5                       
                        glRotate(anguloRot,0,1,0)
                       

                        ejeGiro=(1,0,0)
                        cx=0
                        cy=0
                        cz=0
                        dx=0
                        dy=0
                        dz=0
                        
                        miGrafico.graficandoPlanoDelPrisma(punto11,punto12,punto13,punto14,dx,dy,dz,cx,cy,cz,ejeGiro,0,color)

                        
                        #plano 1b

                        punto11=(-1+3,2,0)
                        punto12=(1+3,2,0)
                        punto13=(1+3,-2,0)
                        punto14=(-1+3,-2,0)
                        ejeGiro=(0,1,0)
                    
                        if ((anguloRotacion>=90)and(direccionPlano==1)):
                            
                                cx1b=3
                                cz1b=1
                                miGrafico.graficandoPlanoDelPrisma(punto11,punto12,punto13,punto14,dx,dy,dz,cx1b,cy,cz1b,ejeGiro,180,color)
                        
                        else:
                                cx1b=1
                                dx1b=-1                   
                                miGrafico.graficandoPlanoDelPrisma(punto11,punto12,punto13,punto14,dx1b,dy,dz,cx1b,cy,cz,ejeGiro,anguloRotacion,color)   

                        #plano 2a
                        color=(0.9, 0.4, 0.3,0.5)
                        punto11=(-2,2,0)
                        punto12=(-1,2,0)
                        punto13=(-1,-2,0)
                        punto14=(-2,-2,0)
                        ejeGiro=(0,1,0)
                        
                        cx2a=-1
                        dx2a=1
                        miGrafico.graficandoPlanoDelPrisma(punto11,punto12,punto13,punto14,dx2a,dy,dz,cx2a,cy,cz,ejeGiro,-anguloRotacion,color)  
                        #dx2=3 

                        #plano 2b
                        color=(0.9, 0.4, 0.3,0.5)
                        punto11=(2,2,0)
                        punto12=(1,2,0)
                        punto13=(1,-2,0)
                        punto14=(2,-2,0)
                        ejeGiro=(0,1,0)
                        cx2b=1
                        dx2b=-1
                        miGrafico.graficandoPlanoDelPrisma(punto11,punto12,punto13,punto14,dx2b,dy,dz,cx2b,cy,cz,ejeGiro,anguloRotacion,color)  
                    
                        #plano 3a
                        color=(0.9,0.8,0.4,0.5)
                        punto11=(-1,3,0)
                        punto12=(1,3,0)
                        punto13=(1,2,0)
                        punto14=(-1,2,0)
                        ejeGiro=(1,0,0)
                    # cy2=3
                        cy2=2
                        dy2=-2
                        
                        miGrafico.graficandoPlanoDelPrisma(punto11,punto12,punto13,punto14,dx,dy2,dz,cx,cy2,cz,ejeGiro,-anguloRotacion,color)  
                        
                        #plano 3b
                        color=(0.9,0.8,0.4,0.5)
                        punto11=(-1,-3,0)
                        punto12=(1,-3,0)
                        punto13=(1,-2,0)
                        punto14=(-1,-2,0)
                        ejeGiro=(1,0,0)

                        dy2=2
                        cy2=-2
                        #dy2=0
                        miGrafico.graficandoPlanoDelPrisma(punto11,punto12,punto13,punto14,dx,dy2,dz,cx,cy2,cz,ejeGiro,anguloRotacion,color)  

                        etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,5,frame_rgb)
                        if (etapasCubo==4):
                              anguloRotacion=0                
                        

                if ( seleccionFigura==2)and(seleccionOperacion==1):
                    
                        if (etapasCubo==1):
                            miGrafico.graficoLineaColorU(-1,-1,0,-1,1,0,colorBlanco)
                            miGrafico.dibujoTexto18(" L1", 2, 0)
                            etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,6,frame_rgb)  

                        if (etapasCubo==2):
                            miGrafico.dibujoTexto18(" L1", 2, 0)
                            miGrafico.dibujoTexto18(" L2", 0, 1.8)                                                                    
                            glPushMatrix() 
                            glTranslate(0,0,-2)
                            miGrafico.dibujoTexto18(" L3", 0.5, 0.4) 
                            glPopMatrix() 
                            miGrafico.graficoLineaColorU(-1,-1,0,-1,1,0,colorBlanco)
                            miGrafico.graficoLineaColorU(-1,-1,0,1,-1,0,colorBlanco)
                            miGrafico.graficoLineaColorU(-1,-1,0,-1,-1,-1,colorBlanco)

                            etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,6,frame_rgb)

                          
                        
                        if (etapasCubo==3):
                                

                            miGrafico.graficoLineaColorU(-1,-1,0,-1,1,0,colorBlanco)

                            miGrafico.graficoLineaColorU(-1,-1,0,-1,1,0,colorBlanco)

                            miGrafico.graficoLineaColorU(-1,-1,0,-1,-1,-1,colorBlanco)


                            if  contadorPrisma<=1:   


                                miGrafico.graficoCuadrilateroSimulacion(-1,-1,0,1,-1,0,1,contadorPrisma,0,-1,contadorPrisma,0)
                                contadorPrisma=contadorPrisma+0.05
                                time.sleep(1/30)  
                                miGrafico.dibujoTexto18(" L1", 2, 0)
                                miGrafico.dibujoTexto18(" L2", 0, 1.8)                                                                    
                                glPushMatrix() 
                                glTranslate(0,0,-2)
                                miGrafico.dibujoTexto18(" L3", 0.5, 0.4) 
                                glPopMatrix() 
                            if contadorPrisma >1 :

                                  
                                    miGrafico.graficoCuadrilateroSimulacion(-1,-1,0,1,-1,0,1,1,0,-1,1,0)
                                    miGrafico.dibujoTexto18(" L1", 2, 0)
                                    miGrafico.dibujoTexto18(" L2", 0, 1.8)                                                                        
                                    glPushMatrix() 
                                    glTranslate(0,0,-2)
                                    miGrafico.dibujoTexto18(" L3", 0.5, 0.4) 
                                    glPopMatrix() 

                          

                            etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,6,frame_rgb)
                            if (etapasCubo==2 or etapasCubo==4):
                                   contadorPrisma=-1
                                  

                        if (etapasCubo==4):
                               
                                anguloRot=anguloRot+5
                                if anguloRot<=90:
                                                            
                                    glRotate(-anguloRot,1,0,0) 

                                    miGrafico.graficoLineaColorU(-1,-1,0,-1,1,0,colorBlanco)

                                    miGrafico.graficoLineaColorU(-1,-1,0,1,-1,0,colorBlanco)


                                    miGrafico.graficoLineaColorU(-1,-1,0,-1,-1,-3,colorBlanco) 

                                    miGrafico.graficoCuadrilateroSimulacion(-1,-1,0,1,-1,0,1,1,0,-1,1,0)
                                    miGrafico.dibujoTexto18(" L1", 2, 0)
                                    miGrafico.dibujoTexto18(" L2", 0, 1.8)
                                                                       
                                    glPushMatrix() 
                                    glTranslate(0,0,-2)
                                    miGrafico.dibujoTexto18(" L3", 0.5, 0.4)  
                                    glPopMatrix()
                                    
                                else:
                                    
                                    glRotate(-90,1,0,0) 
                                    
                                    if contadorCubo<=2:
                                            contadorCubo=contadorCubo+0.01
                                            glTranslate(0,0, contadorCubo)

                                            miGrafico.graficoLineaColorU(-1,-1,0,-1,1,0,colorBlanco)

                                            miGrafico.graficoLineaColorU(-1,-1,0,1,-1,0,colorBlanco)

                                            miGrafico.graficoLineaColorU(-1,-1,0,-1,-1,-3,colorBlanco)

                                            miGrafico.graficoCuadrilateroSimulacion(-1,-1,0,1,-1,0,1,1,0,-1,1,0) 
                                            miGrafico.dibujoTexto18(" L1", 2,0)
                                            miGrafico.dibujoTexto18(" L2", 0, 1.8)                                     
                                            glPushMatrix() 
                                            glTranslate(0,0,-2)
                                           
                                            miGrafico.dibujoTexto18(" L3", 0.5, 0.4) 
                                            glPopMatrix()
                                    else:
                                        if contadorCubo>2:    
                                                glTranslate(0,0, 2)  

                                                miGrafico.graficoLineaColorU(-1,-1,0,-1,1,0,colorBlanco)

                                                miGrafico.graficoLineaColorU(-1,-1,0,1,-1,0,colorBlanco)

                                                miGrafico.graficoLineaColorU(-1,-1,0,-1,-1,-3,colorBlanco)

                                                miGrafico.graficoCuadrilateroSimulacion(-1,-1,0,1,-1,0,1,1,0,-1,1,0)
                                                miGrafico.dibujoTexto18(" L1", 2, 0)
                                                miGrafico.dibujoTexto18(" L2", 0, 1.8)
                                                                                    
                                                glPushMatrix() 
                                                glTranslate(0,0,-2)
                                                miGrafico.dibujoTexto18(" L3", 0.5, 0.4) 
                                                glPopMatrix()


                                
                                etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,6,frame_rgb)
                                if (etapasCubo==3 or etapasCubo==5):
                                      anguloRot=0
                                      contadorCubo=0
                                
                               
                        
                        if (etapasCubo==5):
                           
                       
                            distanciax12,distanciay12 = miMano.distanciaPuntos(frame_rgb,width,height,12,0)                             
                                                                                     
                            if (distanciay12>=100):
                                condicion=1
                            else:
                                if (distanciay12>=20)and(distanciay12<100):
                                    condicion=-1   
                         
                            glRotate(-90,1,0,0) 
                            glPushMatrix() 
                            glTranslate(0,0,2)
                            miGrafico.dibujoTexto18(" L1", 2, 0)
                            miGrafico.dibujoTexto18(" L2", 0, 1.8)                                                                
                            glPushMatrix() 
                            glTranslate(0,0,-2)
                            miGrafico.dibujoTexto18(" L3", 0.5, 0.4) 
                            glPopMatrix()     
                            glPopMatrix()    
                            miGrafico.posicionCoordenadasPrisma()
                           

                            anguloRot=anguloRot+5
                            glRotate(anguloRot,0,0,1)
                  
                            if  condicion==1 :
                                 
                                 if  contadorPrismaVolumen <2 :

                                     miGrafico.graficoPlanoSimulacion(-1,-1,contadorPrismaVolumen,2)
                                     miGrafico.graficoCuboEsqueleticoVariableVolumen(-1,-1,2,1,1,contadorPrismaVolumen)
                                     contadorPrismaVolumen=contadorPrismaVolumen+0.05
                                 else:
                                        if  contadorPrismaVolumen >2 :
                                            miGrafico.graficoPlanoSimulacion(-1,-1,2,2) 
                                            miGrafico.graficoCuboEsqueleticoVariableVolumen(-1,-1,2,1,1,2)
                                           
                            else:
                                 if  condicion==-1:
                                        if  contadorPrismaVolumen >-2 :
                                            miGrafico.graficoPlanoSimulacion(-1,-1,contadorPrismaVolumen,2)
                                            miGrafico.graficoCuboEsqueleticoVariableVolumen(-1,-1,2,1,1,contadorPrismaVolumen)
                                            
                                            contadorPrismaVolumen=contadorPrismaVolumen-0.05
                                        else:
                                             if  contadorPrismaVolumen <=-2.0 :                                
                                                 miGrafico.graficoPlanoSimulacion(-1,-1,-2,2)  
                                                 miGrafico.graficoCuboEsqueleticoVariableVolumen(-1,-1,2,1,1,-2)                  
                                
                       
                        
                                    
                            etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,6,frame_rgb)
                            if (etapasCubo==4 or etapasCubo==6):
                                       contadorCubo2=1      
                                       contadorCubo1=-1

                        if (etapasCubo==6):                             
                             
                            glPushMatrix()
                            glTranslate(0,0,-3)
                           
                            miGrafico.dibujoTexto18("L1 = 2 u",3.5,5)
                          
                            miGrafico.dibujoTexto18("L2 = 3 u",1,5)
                            
                            miGrafico.dibujoTexto18("L3 = "+str(visualizacionVolumen)+" u",-1.5,5) 
                          
                        
                            miGrafico.dibujoTexto18("Volumen = 2 u x 3 u x "+str(visualizacionVolumen)+" u",3.7,6)                            
                            miGrafico.dibujoTexto18(" = "+str(2*3*visualizacionVolumen)+" u ",-1.7,6)
                         
                            if 2*3*visualizacionVolumen<10:
                                 miGrafico.dibujoTexto10("3", -3, 5.7) 
                            else:                                  
                                miGrafico.dibujoTexto10("3", -3.2, 5.7)                        
                            
                            glPopMatrix() 
                            
                            anguloRot=anguloRot%360+5
                            anguloRot=anguloRot+5        
                             
                            glRotate(anguloRot,1,1,1)
                       
                            longitudCubo=miMano.contarDedos(nuevo_frame,width,height)  

                            
                            if longitudCubo==1:
                                  dedoLado=1                                  
                            else:
                                  if longitudCubo==2:
                                        dedoLado=2   
                                  else:
                                        if longitudCubo==3:
                                              dedoLado=3          
                                        else:
                                            if  longitudCubo==4:
                                                  dedoLado=4
                                           
                             
                            color1=(0.18,0.52,0.75,1.0)
                            color2=(1,0.906,0,1.0) 
                            colorNaranja=(0.9,0.8,0.4,0.5)
                            colorMorado=(0.7,0.5,0.8,0.5)
                                                     
                            x1=-0.25
                            y1=0
                            z1=0
                            x2=0
                            y2=0.25
                            z2=0
                            x3=0.25
                            y3=0
                            z3=0
                          
                            if dedoLado==1:
                                 
                                 
                                 miGrafico.graficoPrismaSecuencial(color1,1,0,0,0) 
                            
                                 
                                 visualizacionVolumen=1

                                 miGrafico.dibujoTexto18("L1",3,0.5)                               
                                 miGrafico.graficoLineaColorU(-2.5,0,0,-2.5,-1.4,0,colorBlanco)
                                
                                 glPushMatrix()                                 
                                 glTranslate(2.5,0,0)
                                 glRotate(90,0,1,0)
                                 miGrafico.dibujandoTriangulo(x1,y1,z1,x2,y2,z2,x3,y3,z3) 
                                 glPopMatrix()
                            
                                 miGrafico.dibujoTexto18("L2",0,-1.5)
                            
                            
                                 glPushMatrix()                                 
                                 glTranslate(-1.2,-1,0)
                                 glRotate(-90,0,0,1)
                                 glRotate(90,0,1,0)
                                 miGrafico.dibujandoTriangulo(x1,y1,z1,x2,y2,z2,x3,y3,z3) 
                                 glPopMatrix()


                                 miGrafico.graficoLineaColorU(-1.5,1,0,1.3,1,0,colorBlanco) 
                                 
                                 
                                 miGrafico.dibujoTexto18("L3",1.5,2.5)
                        
                                 glPushMatrix()                                 
                                 glTranslate(1.5,2,0)
                                 glRotate(90,1,0,0)
                                 miGrafico.dibujandoTriangulo(x1,y1,z1,x2,y2,z2,x3,y3,z3) 
                                 glPopMatrix()

                                 miGrafico.graficoLineaColorU(-1.5,-2,-0.1,-1.5,-2,0.5,colorBlanco)

                  
                            else:

                                if dedoLado==2:
                                        

                                        miGrafico.graficoPrismaSecuencial(color1,1,1,0,0)
 
                                        visualizacionVolumen=2

                                        miGrafico.dibujoTexto18("L1",3,0.5)                               
                                        miGrafico.graficoLineaColorU(-2.5,0,0,-2.5,-1.4,0,colorBlanco)
                                        
                                        glPushMatrix()                                 
                                        glTranslate(2.5,0,0)
                                        glRotate(90,0,1,0)
                                        miGrafico.dibujandoTriangulo(x1,y1,z1,x2,y2,z2,x3,y3,z3) 
                                        glPopMatrix()

                                        miGrafico.dibujoTexto18("L2",0,-1.5)
                                    
                                    
                                        glPushMatrix()                                 
                                        glTranslate(-1.2,-1,0)
                                        glRotate(-90,0,0,1)
                                        glRotate(90,0,1,0)
                                        miGrafico.dibujandoTriangulo(x1,y1,z1,x2,y2,z2,x3,y3,z3) 
                                        glPopMatrix()


                                        miGrafico.graficoLineaColorU(-1.5,1,0,1.3,1,0,colorBlanco) 
                                        miGrafico.dibujoTexto18("L3",1.5,2.5)
                        
                                        glPushMatrix()                                 
                                        glTranslate(1.5,2,-1)
                                        glRotate(90,1,0,0)
                                        miGrafico.dibujandoTriangulo(x1,y1,z1,x2,y2,z2,x3,y3,z3) 
                                        glPopMatrix()

                                        miGrafico.graficoLineaColorU(-1.5,-2,-1,-1.5,-2,0.5,colorBlanco)


                                else:
                                        
                                    if dedoLado==3:

                                        miGrafico.graficoPrismaSecuencial(color1,1,1,1,0)
                                        

                                        miGrafico.dibujoTexto18("L1",3,0.5)                               
                                        miGrafico.graficoLineaColorU(-2.5,0,0,-2.5,-1.4,0,colorBlanco)
                                        
                                        glPushMatrix()                                 
                                        glTranslate(2.5,0,0)
                                        glRotate(90,0,1,0)
                                        miGrafico.dibujandoTriangulo(x1,y1,z1,x2,y2,z2,x3,y3,z3) 
                                        glPopMatrix()

                                        miGrafico.dibujoTexto18("L2",0,-1.5)
                                    
                                    
                                        glPushMatrix()                                 
                                        glTranslate(-1.2,-1,0)
                                        glRotate(-90,0,0,1)
                                        glRotate(90,0,1,0)
                                        miGrafico.dibujandoTriangulo(x1,y1,z1,x2,y2,z2,x3,y3,z3) 
                                        glPopMatrix()


                                        miGrafico.graficoLineaColorU(-1.5,1,0,1.3,1,0,colorBlanco) 
                                       
                                        visualizacionVolumen=3
                                        miGrafico.dibujoTexto18("L3",1.5,2.5)
                        
                                        glPushMatrix()                                 
                                        glTranslate(1.5,2,-2)
                                        glRotate(90,1,0,0)
                                        miGrafico.dibujandoTriangulo(x1,y1,z1,x2,y2,z2,x3,y3,z3) 
                                        glPopMatrix()

                                        miGrafico.graficoLineaColorU(-1.5,-2,-2,-1.5,-2,0.5,colorBlanco)
                                    
                                    else:
                                          if dedoLado==4:
                                                
                                                miGrafico.graficoPrismaSecuencial(color1,1,1,1,1)

                                              
                                                miGrafico.dibujoTexto18("L1",3,0.5)                               
                                                miGrafico.graficoLineaColorU(-2.5,0,1,-2.5,-1.4,1,colorBlanco)
                                                
                                                glPushMatrix()                                 
                                                glTranslate(2.5,0,1)
                                                glRotate(90,0,1,0)
                                                miGrafico.dibujandoTriangulo(x1,y1,z1,x2,y2,z2,x3,y3,z3) 
                                                glPopMatrix()
                                                
                                                miGrafico.dibujoTexto18("L2",0,-1.5)
                                            
                                            
                                                glPushMatrix()                                 
                                                glTranslate(-1.2,-1,1)
                                                glRotate(-90,0,0,1)
                                                glRotate(90,0,1,0)
                                                miGrafico.dibujandoTriangulo(x1,y1,z1,x2,y2,z2,x3,y3,z3) 
                                                glPopMatrix()


                                                miGrafico.graficoLineaColorU(-1.5,1,1,1.3,1,1,colorBlanco) 
                                                
                                                miGrafico.dibujoTexto18("L3",1.5,2.5)                        
                                                glPushMatrix()                                 
                                                glTranslate(1.5,2,-2)
                                                glRotate(90,1,0,0)
                                                miGrafico.dibujandoTriangulo(x1,y1,z1,x2,y2,z2,x3,y3,z3) 
                                                glPopMatrix()

                                                miGrafico.graficoLineaColorU(-1.5,-2,-2,-1.5,-2,1.5,colorBlanco)                         
                                                visualizacionVolumen=4
                                      

                            etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,6,frame_rgb)
                            if (etapasCubo==5): 
                                       contadorCubo2=1      
                                       contadorCubo1=-1                            
                              

                if ( seleccionFigura==3)and(seleccionOperacion==2):                     
                        
                        colorNaranja=(0.9,0.8,0.4,0.5)
                        colorMorado=(0.7,0.5,0.8,0.5)
                        
                        medianoAncho=1.5
                        plano1=-1
                        plano2=1

 
                        if (etapasCubo==1):
                            
                            radio=1
                            pi=round(3.1415,2)
                            miGrafico.dibujoTexto18("r",-0.5,-2)
                            miGrafico.graficoLineaColorU(0,2,0,1,2,0,colorBlanco)                   
                            
                            miGrafico.longitudArcoCirculoAvanceT(-90,90,1,-1,0,2,colorNaranja,1.5,1)

                            miGrafico.longitudArcoCirculoAvanceT(-90,90,1,1,0,2,colorNaranja,2,1)
                         
                          

                            anguloMovimiento=anguloMovimiento-5
                           

                            if (anguloMovimiento>=-90):

                        
                                miGrafico.longitudArcoCirculoAvanceT(-90,anguloMovimiento,1,-1,0,2,colorNaranja,1.5,plano1)
                                miGrafico.longitudArcoCirculoAvanceT(-90,anguloMovimiento,1,1,0,2,colorNaranja,1.5,plano1)
                                             
                                time.sleep(1/10)
                            else:
                                if (anguloMovimiento<-90) and (anguloMovimiento>-180) : 
                                    
                                     miGrafico.dibujandoLineaCilindroColorAncho(-radio*pi,1,0,radio*pi,1,0,colorNaranja,medianoAncho)
                                     miGrafico.grafico2rpi(0,0,colorBlanco)
                                else:
                                      if (anguloMovimiento<-180) and (anguloMovimiento>-270) : 
                                             
                                             miGrafico.dibujandoLineaCilindroColorAncho(-radio*pi,1,0,radio*pi,1,0,colorMorado,medianoAncho)   
                                             miGrafico.grafico2rpi(0,0,colorBlanco)  
                                      else:
                                            if (anguloMovimiento<-270) and (anguloMovimiento>-360):
                                                   miGrafico.grafico2rpi(0,0,colorBlanco)                                                   
                                                   miGrafico.dibujandoLineaCilindroColorAncho(-radio*pi,1,0,radio*pi,1,0,colorMorado,medianoAncho)  
                                                   miGrafico.dibujandoLineaCilindroColorAncho(-radio*pi,1,0,-radio*pi,-1,0,colorMorado,medianoAncho)
                                                   miGrafico.dibujandoLineaCilindroColorAncho(radio*pi,1,0,radio*pi,-1,0,colorMorado,medianoAncho)
                                                   miGrafico.dibujoTexto18("h",-3.5,0.4)
                                            
                                            else:
                                                if anguloMovimiento<-360:
                                                        miGrafico.dibujoTexto18("h",-3.5,0.4)
                                                        miGrafico.grafico2rpi(0,0,colorBlanco) 
                                                        miGrafico.dibujandoLineaCilindroColorAncho(-radio*pi,1,0,radio*pi,1,0,colorMorado,medianoAncho)  
                                                        miGrafico.dibujandoLineaCilindroColorAncho(-radio*pi,1,0,-radio*pi,-1,0,colorMorado,medianoAncho)
                                                        miGrafico.dibujandoLineaCilindroColorAncho(radio*pi,1,0,radio*pi,-1,0,colorMorado,medianoAncho)
                                                        miGrafico.dibujandoLineaCilindroColorAncho(-radio*pi,-1,0,radio*pi,-1,0,colorMorado,medianoAncho)
                                                        anguloMovimiento1=anguloMovimiento1+5 
                                                      
                                                        if (anguloMovimiento1<=90):

                                                                        miGrafico.longitudArcoCirculoAvanceT(-90,anguloMovimiento1,1,1,0,-2,colorNaranja,1.5,plano2)
                                                                        miGrafico.longitudArcoCirculoAvanceT(-90,anguloMovimiento1,1,-1,0,-2,colorNaranja,1.5,plano2)
                                                                                                   
                                                                        time.sleep(1/10)
                                                        else:
                                                                if (anguloMovimiento1>=90):

                                                                    miGrafico.longitudArcoCirculoAvanceT(-90,90,1,1,0,-2,colorNaranja,1.5,plano2)
                                                                    miGrafico.longitudArcoCirculoAvanceT(-90,90,1,-1,0,-2,colorNaranja,1.5,plano2)
                                                                    anguloMovimiento=90
                                                                    anguloMovimiento1=-90
                                                                    miGrafico.dibujoTexto18("r",-0.5,2)
                                                                    miGrafico.graficoLineaColorU(0,-2,0,1,-2,0,colorBlanco)
                                                                    etapasCubo=2
                                                       
                            etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,3,frame_rgb)
                            if (etapasCubo==2):
                                    anguloMovimiento=90
                                    anguloMovimiento1=-90                          
                                 

                        if (etapasCubo==2):
                                
                               
                                miGrafico.dibujoTexto18("r",-0.5,-2)
                                miGrafico.grafico2rpi(0,0,colorBlanco)                               
                                miGrafico.dibujoTexto18("h",-3.5,0.4)
                                miGrafico.dibujoTexto18("r",-0.5,2)
                                miGrafico.graficoLineaColorU(0,2,0,1,2,0,colorBlanco)
                                miGrafico.graficoLineaColorU(0,-2,0,1,-2,0,colorBlanco)

                                elmenux,elmenuy=miMano.seleccionarMenu(frame_rgb,width,height)
                                

                                if (pintarCirculo==1):
                                    miGrafico.dibujandoCirculoSuperficie(1,0,2)   
                                if (pintarCirculo2==1):
                                    miGrafico.dibujandoCirculoSuperficie(1,0,-2)   
                                if (pintarRectangulo==1):
                                    
                                    miGrafico.longitudArcoCilindroZ(-90,-90,1,1,0,0,-1)
                                    miGrafico.longitudArcoCilindroZ(-90,-90,1,-1,0,0,-1) 

                                radio=1
                                pi=round(3.1415,2)                               
                                

                                miGrafico.longitudArcoCirculoAvanceT(-90,90,1,-1,0,2,colorNaranja,1.5,plano1)
                                miGrafico.longitudArcoCirculoAvanceT(-90,90,1,1,0,2,colorNaranja,1.5,plano1)
                                miGrafico.dibujandoLineaCilindroColorAncho(-radio*pi,1,0,-radio*pi,-1,0,colorMorado,medianoAncho)
                                miGrafico.dibujandoLineaCilindroColorAncho(radio*pi,1,0,radio*pi,-1,0,colorMorado,medianoAncho)
                                miGrafico.dibujandoLineaCilindroColorAncho(-radio*pi,-1,0,radio*pi,-1,0,colorMorado,medianoAncho)
                                miGrafico.dibujandoLineaCilindroColorAncho(-radio*pi,1,0,radio*pi,1,0,colorMorado,medianoAncho)
                                miGrafico.longitudArcoCirculoAvanceT(-90,90,1,1,0,-2,colorNaranja,1.5,plano2)
                                miGrafico.longitudArcoCirculoAvanceT(-90,90,1,-1,0,-2,colorNaranja,1.5,plano2)

                                if ((elmenux>290)and(elmenux<340))and((elmenuy>120)and(elmenuy<160)):
                                    pintarCirculo=1
                                    

                                if ((elmenux>290)and(elmenux<340))and((elmenuy>320)and(elmenuy<370)):
                                    pintarCirculo2=1
                                    
                            
                                if ((elmenux>200)and(elmenux<400))and((elmenuy>200)and(elmenuy<260)):
                                    pintarRectangulo=1
                                    

                                if pintarCirculo==1:
                                     
                                        miGrafico.graficoPirCuadrado(1.31,4.45,colorBlanco)
                                     

                                if pintarCirculo2==1:
                                     
                                       
                                        miGrafico.graficoPirCuadrado(-0.9,4.45,colorBlanco)
                                                                          
                                     
                                if pintarRectangulo==1:
                                   

                                        miGrafico.grafico2rpi(0.2,4.45,colorBlanco) 
                                        miGrafico.dibujoTexto18("h",-0.3,3.95)                                 
                                    
 
                                etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,3,frame_rgb)
                                if (etapasCubo==1 or etapasCubo==3):
                                        pintarCirculo=0
                                        pintarCirculo2=0
                                        pintarRectangulo=0
                                        anguloRot1=90
                                        anguloRot2=180
                                        condicion=1                                         

                        
                        if (etapasCubo==3):    
                                     
                                miGrafico.dibujoTexto18("Area = ",2.5,3.95)
                                miGrafico.dibujoTexto18("+",0.7,3.95)
                                miGrafico.dibujoTexto18("+",-0.6,3.95)
                              

                                
                                miGrafico.graficoPirCuadrado(1.31,4.45,colorBlanco)
                                miGrafico.graficoPirCuadrado(-0.9,4.45,colorBlanco)
                                miGrafico.grafico2rpi(0.2,4.45,colorBlanco) 
                                miGrafico.dibujoTexto18("h",-0.3,3.95) 
                              
                                
                                anguloRotacion=anguloRotacion-5
                                glRotatef(anguloRotacion, 0, 1, 0) 
                                radio=1
                                pimedio=round(3.1415,2)/2
                                pi=round(3.1415,2)
                                
                                distanciax12,distanciay12 = miMano.distanciaPuntos(frame_rgb,width,height,12,0)
                                temporaly=pyf
                                pyf=distanciay12
                            
                                if (abs(pyf)- abs(temporaly))>10:
                                    direccion=-1
                                        
                                            
                                if (abs(temporaly)-abs(pyf))>10:
                                    direccion=1
                                    
                                if (distanciay12>=100):
                                    condicion=1
                                else:
                                    if (distanciay12>=20)and(distanciay12<100):
                                        condicion=-1   
                                    
                            
                                
                                if (condicion==1):     
                            
                                    time.sleep(1/20)
                                    anguloRot1=anguloRot1+5
                                    anguloMovimiento1=-90
                                    anguloRot2=180
                                    
                                    if (anguloRot1<=180):
                                            miGrafico.rotarTapaCilindro(anguloRot1,0,1,0,1)
                                            miGrafico.rotarTapaCilindro(-anguloRot1,0,-1,0,-1)
                                    else:
                                            if (anguloRot1>180):
                                                    miGrafico.rotarTapaCilindro(180,0,1,0,1)
                                                    miGrafico.rotarTapaCilindro(-180,0,-1,0,-1)

                                    if (anguloMovimiento>=-90):
                                        

                                            
                                            miGrafico.longitudArcoCilindroZ(-90,anguloMovimiento,1,1,0,0,-1)
                                            miGrafico.longitudArcoCilindroZ(-90,anguloMovimiento,1,-1,0,0,-1)
                                            anguloMovimiento=anguloMovimiento-10
                                            
                                            
                                    else:
                                                if (anguloMovimiento<-90):     

                                                    miGrafico.longitudArcoCilindroZ(-90,-90,1,1,0,0,-1)
                                                    miGrafico.longitudArcoCilindroZ(-90,-90,1,-1,0,0,-1)

                                if (condicion==-1):
                            
                                    time.sleep(1/20)
                                    anguloRot2=anguloRot2-5
                                    anguloRot1=90
                                    anguloMovimiento=90

                                    if (anguloRot2>=90):
                                            miGrafico.rotarTapaCilindro(anguloRot2,0,1,0,1)
                                            miGrafico.rotarTapaCilindro(-anguloRot2,0,-1,0,-1)
                                    else:
                                            if (anguloRot2<90):
                                                    miGrafico.rotarTapaCilindro(90,0,1,0,1)
                                                    miGrafico.rotarTapaCilindro(-90,0,-1,0,-1)

                                    if (anguloMovimiento1<=90):                 
                                        
                                        miGrafico.longitudArcoCilindroZ(-90,anguloMovimiento1,1,-1,0,1,-1)
                                        miGrafico.longitudArcoCilindroZ(-90,anguloMovimiento1,1,1,0,1,-1) 
                                        anguloMovimiento1=anguloMovimiento1+10
                                    
                                    else:
                                        if (anguloMovimiento1>90):                    
                                                    
                                                    miGrafico.longitudArcoCilindroZ(-90,90,1,-1,0,1,-1)
                                                    miGrafico.longitudArcoCilindroZ(-90,90,1,1,0,1,-1) 

                                
                                etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,3,frame_rgb)
                                if (etapasCubo==2 ): 
                                      anguloMovimiento=90
                                      anguloMovimiento1=-90

                if ( seleccionFigura==3)and(seleccionOperacion==1): 
                   

                     colorNaranja=(0.9,0.8,0.4,0.5)
                     colorMorado=(0.7,0.5,0.8,0.5)
                     colorBlanco=(1,1,1,1)
                     if (etapasCubo==1):
                            miGrafico.graficoLineaColorU(0,0,0,2,0,0,colorBlanco)
                            miGrafico.graficoLineaColorU(0,0,0,0,2,0,colorBlanco)
                            miGrafico.graficoLineaColorU(0,0,0,0,0,-2,colorBlanco)
                            etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,5,frame_rgb)
                            

                     if (etapasCubo==2):
                            miGrafico.dibujoTexto18("r",-2,-1.5)
                            miGrafico.graficoLineaColorU(1.5,1.5,0,2.5,1.5,0,colorBlanco)                           
                            miGrafico.graficoLineaColorU(0,0,0,2,0,0,colorBlanco)
                            miGrafico.graficoLineaColorU(0,0,0,0,2,0,colorBlanco)
                            miGrafico.graficoLineaColorU(0,0,0,0,0,-2,colorBlanco)
                            miGrafico.longitudArcoCirculoAvanceT(-90,90,1,-1,1.5,1.5,colorNaranja,1.5,1)
                            miGrafico.longitudArcoCirculoAvanceT(-90,90,1,1,1.5,1.5,colorNaranja,1.5,1)
                            
                            if ((elmenux>220)and(elmenux<270))and((elmenuy>140)and(elmenuy<190)):
                                    pintarCirculo=1

                            if  pintarCirculo==1:       
                                    miGrafico.dibujandoCirculoSuperficie(1,1.5,1.5)    
                                          
                            etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,5,frame_rgb)           

                        
                     if (etapasCubo==3):
                               
                                glRotate(30,0,1,0)
                                anguloRot=anguloRot+5
                                if anguloRot<=90:
                                                            
                                        glRotate(-anguloRot,1,0,0) 
                                        miGrafico.graficoLineaColorU(0,0,0,2,0,0,colorBlanco)
                                        miGrafico.graficoLineaColorU(0,0,0,0,2,0,colorBlanco)
                                        miGrafico.graficoLineaColorU(0,0,0,0,0,-2,colorBlanco)
                                        miGrafico.dibujandoCirculoSuperficie(1,1.5,1.5)
                                    
                                else:
                                    
                                    glRotate(-90,1,0,0) 
                                    
                                    if contadorCubo<=1:
                                            contadorCubo=contadorCubo+0.01
                                            glTranslate(0,0, contadorCubo)
                                            miGrafico.graficoLineaColorU(0,0,0,2,0,0,colorBlanco)
                                            miGrafico.graficoLineaColorU(0,0,0,0,2,0,colorBlanco)
                                            miGrafico.graficoLineaColorU(0,0,0,0,0,-2,colorBlanco)
                                            miGrafico.dibujandoCirculoSuperficie(1,1.5,1.5)
                                            
                                    else:
                                        if contadorCubo>1:    
                                                    glTranslate(0,0, 1)  
                                                    miGrafico.graficoLineaColorU(0,0,0,2,0,0,colorBlanco)
                                                    miGrafico.graficoLineaColorU(0,0,0,0,2,0,colorBlanco)
                                                    miGrafico.graficoLineaColorU(0,0,0,0,0,-2,colorBlanco)
                                                    miGrafico.dibujandoCirculoSuperficie(1,1.5,1.5) 
                                                       

                                
                                etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,5,frame_rgb)
                                if (etapasCubo==2 or etapasCubo==4):
                                      anguloRot=0
                                      contadorCubo=0
                               
                        
                     if (etapasCubo==4):
                              
                            miGrafico.dibujoTexto18("Volumen = ",3,3.0)
                            miGrafico.graficoPirCuadrado(1.25,3.45,colorBlanco)
                            miGrafico.dibujoTexto18("h",0.52,3.0) 
                            miGrafico.dibujoTexto18("Volumen = ",3,4.0)
                            miGrafico.graficoPi(1.25,4.45,colorBlanco)
                            miGrafico.dibujoTexto18("x1x",0.85,4.0) 
                          
                            alt=round(contadorCilindro,1)
                            if alt <=0.0:
                                 alt=0
                            altt=str(alt)
                            miGrafico.dibujoTexto18(altt,0.25,4.0) 
                            miGrafico.dibujoTexto18("=",-0.3,4.0) 
                            resultadoVolumen=round(3.1416*1*alt,1)
                            resultadoVolumenV=str(resultadoVolumen)                            
                            miGrafico.dibujoTexto18(resultadoVolumenV,-0.7,4.0) 
                            miGrafico.dibujoTexto18("u",-1.2,4.0) 
                            miGrafico.dibujoTexto10("3",-1.4,3.8)         
                            
                            glRotate(30,0,1,0)
                            anguloRot=anguloRot+5
                            glRotate(anguloRot,1,0,0)
                            glRotate(-90,1,0,0) 
                            glTranslate(0,0,1)
                            miGrafico.graficoLineaColorU(0,0,0,2,0,0,colorBlanco)
                            miGrafico.graficoLineaColorU(0,0,0,0,2,0,colorBlanco)
                            miGrafico.graficoLineaColorU(0,0,0,0,0,-2,colorBlanco)
                                    
                            distanciax12,distanciay12 = miMano.distanciaPuntos(frame_rgb,width,height,12,0)
                                                
                            if (distanciay12>=100):
                                condicion=1
                            else:
                                if (distanciay12>=20)and(distanciay12<100):
                                    condicion=-1

                            if (condicion==1):  
                                                           
                                if  contadorCilindro<=2:   
                                    miGrafico.dibujandoCilindro2(1,contadorCilindro,1.5,1.5,0)
                                    contadorCilindro=contadorCilindro+0.1
                                   
                                
                                else:
                                    if  contadorCilindro >2 :
                                        miGrafico.dibujandoCilindro2(1,2,1.5,1.5,0)   
                                                    

                            
                            if (condicion==-1):  
                                    
                                    if  contadorCilindro>=0:   
                                            miGrafico.dibujandoCilindro2(1,contadorCilindro,1.5,1.5,0)
                                            contadorCilindro=contadorCilindro-0.1
                                        
                                    else:
                                            if  contadorCilindro <=0 :
                                                miGrafico.dibujandoCilindro2(1,0,1.5,1.5,0)                             

                            etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,5,frame_rgb)
                            if (etapasCubo==3 or etapasCubo==5):
                                      contadorCilindro2=2
                                      contadorCilindro=0      

                     if (etapasCubo==5):
                            
                            miGrafico.dibujoTexto18("r = ",3,3.0)
                            miGrafico.dibujoTexto18(str(dedoRadio),2.5,3.0)

                            miGrafico.dibujoTexto18("Volumen = ",3,3.5)
                            miGrafico.graficoPirCuadrado(1.25,3.95,colorBlanco)
                            miGrafico.dibujoTexto18("h",0.52,3.5) 

                            miGrafico.dibujoTexto18("Volumen = ",3,4.0)
                            miGrafico.graficoPi(1.25,4.45,colorBlanco)
                            radioVolumenCuadrado=round(dedoRadio*dedoRadio,1)
                            radioVolumenCuadradoT=str(radioVolumenCuadrado)
                            miGrafico.dibujoTexto18("x",0.9,4.0) 
                            miGrafico.dibujoTexto18(radioVolumenCuadradoT,0.7,4.0) 
                            miGrafico.dibujoTexto18("x2",0.26,4.0) 
                         
                            miGrafico.dibujoTexto18("=",-0.3,4.0) 
                            resultadoVolumen=round(3.1416*radioVolumenCuadrado*2,1)
                            resultadoVolumenV=str(resultadoVolumen)                            
                            miGrafico.dibujoTexto18(resultadoVolumenV,-0.7,4.0) 
                            if resultadoVolumen<100:
                                  miGrafico.dibujoTexto18("u",-1.4,4.0) 
                                  miGrafico.dibujoTexto10("3",-1.6,3.8)
                            else:
                                  miGrafico.dibujoTexto18("u",-1.6,4.0) 
                                  miGrafico.dibujoTexto10("3",-1.8,3.8)
                                        
                           
                            glRotate(30,0,1,0)
                            anguloRot=anguloRot+5
                            glRotate(anguloRot,1,0,0)
                            glRotate(-90,1,0,0) 
                            glTranslate(0,0,1)                           
                          

                            longitudRadio=miMano.contarDedos(nuevo_frame,width,height)
                          
                            if longitudRadio==1:
                                  dedoRadio=1                                  
                            else:
                                  if longitudRadio==2:
                                        dedoRadio=2   
                                  else:
                                        if longitudRadio==3:
                                           dedoRadio=3    
                                        else:
                                              if longitudRadio==4:
                                                     dedoRadio=4                
                          
                            miGrafico.dibujandoCilindro2(dedoRadio*0.5,2,0,0,0)
                        
                            etapasCubo,llavePaso=miMano.transicionEtapa(etapasCubo,llavePaso,5,frame_rgb)
                           
        
       

        tx_image = tx_image.tobytes('raw', 'BGRX', -1, 1)        
        miGrafico.dibujoFondo(nuevo_frame,identificador_textura,tx_image,ix,iy)        
        glutSwapBuffers()

if __name__ == "__main__":  
       
    miMano=reconocerMano(False,2,0.75)
    miMenu=menu(nuevo_frame)    
    init()
    glutInit(sys.argv)
    angulo=30
    miGrafico=graficos()
    miGrafico.pre()
    glutDisplayFunc(VisualizacionCubo)
    glutIdleFunc(VisualizacionCubo) 
    miGrafico.inicio(640,480)   
    glutMainLoop() 
  