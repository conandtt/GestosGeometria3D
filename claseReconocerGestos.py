import math
import mediapipe as mp
from numpy import arctan

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

class reconocerMano():
 
 def __init__(self,modo=False,manos=2,certidumbre=0.75):
      self.modo=modo
      self.manos=manos
      self.certidumbre=certidumbre
      self.dibujo= mp_drawing
      self.mpmanos=mp.solutions.hands
      self.mismanos=self.mpmanos.Hands( self.modo,self.manos,self.certidumbre)
 
 def laMano(self):
     return self.mismanos

 def coordenadasReferencia(self,frame,width,height,indice):
     x=0
     y=0
     results=self.mismanos.process(frame)
     if results.multi_hand_landmarks is not None: 
          for hand_landmarks in (results.multi_hand_landmarks):
               for i, punto in enumerate(hand_landmarks.landmark):
                    if (i==indice):
                         x = int(punto.x * width)
                         y = int(punto.y * height)
                     
     return x,y
 
      
 
 def distanciaDedos(self,dedoAx,dedoAy,dedoBx,dedoBy):
       return math.sqrt(pow((dedoBx-dedoAx),2)+pow((dedoBy-dedoAy),2))
 
 def distanciaPuntosXY(self,dedoAx,dedoAy,dedoBx,dedoBy):
       return dedoBx-dedoAx,dedoBy-dedoAy     


 def queMano(self,frame):
     results=self.mismanos.process(frame)
     if  results.multi_handedness is not None:
          for x,y in  enumerate(results.multi_handedness):
             return y.classification[0].label
          

        
 def contarDedos(self,frame,ancho,alto):
       dedoIndice=self.distanciaDedosPunto(frame,ancho,alto,8,5)
       dedoMedio=self.distanciaDedosPunto(frame,ancho,alto,12,9)
       dedoAnular=self.distanciaDedosPunto(frame,ancho,alto,16,13)
       dedoMenique=self.distanciaDedosPunto(frame,ancho,alto,20,17)
      
       contandoDedoIndice=0
       contandoDedoMedio=0
       contandoDedoAnular=0
       contandoDedoMenique=0
       contandoDedoPulgar=0
       
       if dedoIndice<-20:
            contandoDedoIndice=1
       if dedoMedio<-20:
            contandoDedoMedio=1
       if dedoAnular<-20:
            contandoDedoAnular=1
       if dedoMenique<-20:
            contandoDedoMenique=1
                

       return  contandoDedoIndice+contandoDedoMedio+contandoDedoAnular+contandoDedoMenique#+contandoDedoPulgar     


 def definirPuntoEspejo2(self,x,y,unFrame):      
      alto,ancho,_ = unFrame.shape
      puntoMedioX= ancho/2
      puntoMedioY= alto/2
      x2=int(-x+puntoMedioX)
      y2=int(-y+puntoMedioY)
      return x2,y2


 def distanciaPuntos(self,unFrame,ancho,alto,pf,pi):
        
        puntoFinalX,puntoFinalY=self.coordenadasReferencia(unFrame,ancho,alto,pf)           
        puntoFinalX,puntoFinalY=self.definirPuntoEspejo2(puntoFinalX,puntoFinalY,unFrame)   
        
        puntoInicialX,puntoInicialY=self.coordenadasReferencia(unFrame,ancho,alto,pi)
        puntoInicialX,puntoInicialY=self.definirPuntoEspejo2(puntoInicialX,puntoInicialY,unFrame)

        
        return puntoFinalX-puntoInicialX,puntoFinalY-puntoInicialY
         
 def distanciaDedosPunto(self,unFrame,ancho,alto,puntoSuperior,puntoInferior):
        
        puntoSuperior_x,puntoSuperior_y=self.coordenadasReferencia(unFrame,ancho,alto,puntoSuperior)
        puntoInferior_x,puntoInferior_y=self.coordenadasReferencia(unFrame,ancho,alto,puntoInferior)
        return puntoSuperior_y-puntoInferior_y

 def anguloPuntosDedo(self,frame_rgb,width,height,puntoSuperior,puntoInferior):
        distanciay=0.01
        distanciax=0.01
        puntoSuperiorx,puntoSuperiory=self.coordenadasReferencia(frame_rgb,width,height,puntoSuperior)
        puntoInferiorx,puntoInferiory=self.coordenadasReferencia(frame_rgb,width,height,puntoInferior)
        distanciay,distanciax=self.distanciaPuntosXY(puntoInferiorx,puntoInferiory,puntoSuperiorx,puntoSuperiory)
        if ((distanciay is not None) and (distanciax is not None)):
            if distanciax!=0: 
               return arctan(distanciay/distanciax)  
        else:
          return 0.1
        
 def seleccionarMenu(self,frame,ancho,alto):
             
        width=ancho
        height=alto
        dindice_x,dindice_y=self.coordenadasReferencia(frame,width,height,8)
        return dindice_x,dindice_y


 def selmenuActivo1(self,frameActual,coordX,coordY,menuNivel1,menuNivel2,menuNivel3,selFigura): 
     ancho=640
     alto=480
     coordX,coordY=self.seleccionarMenu(frameActual,ancho,alto)   
     
     if((coordX>470 and coordX<510)and(coordY>230 and coordY<270)):  
                 menuNivel1=0
                 menuNivel2=1
                 menuNivel3=0 
                 selFigura=1
              
             # menu l2 prisma
     if((coordX>290 and coordX<340)and(coordY>230  and coordY<270)):               
                 menuNivel1=0
                 menuNivel2=1
                 menuNivel3=0
                 selFigura=2
              
                 
             # menu l2 cilindro
     if((coordX>120 and coordX<170 )and(coordY>230 and coordY<270)):  
                  menuNivel1=0
                  menuNivel2=1
                  menuNivel3=0 
                  selFigura=3                
             
             # menu inicio        
     if ((coordX>130 and coordX<160)and(coordY>40 and coordY<70)):
                 menuNivel1=1
                 menuNivel2=0
                 menuNivel3=0       
        
     return   menuNivel1,menuNivel2,menuNivel3,selFigura  
 
 def selmenuActivo2(self,frameActual,coordX,coordY,menuNivel1,menuNivel2,menuNivel3,selOperacion): 
     ancho=640
     alto=480
     coordX,coordY=self.seleccionarMenu(frameActual,ancho,alto)   
     
     # volumen        
     if((coordX>170 and coordX< 210)and(coordY>130 and coordY<180)):
          menuNivel1=0
          menuNivel2=0
          menuNivel3=1 
          selOperacion=1 
     # area
     if((coordX>400 and coordX<450)and(coordY>130 and coordY<180)):
          menuNivel1=0
          menuNivel2=0
          menuNivel3=1 
          selOperacion=2
     # inicio      
     if ((coordX>130 and coordX<160)and(coordY>40 and coordY<70)):
          menuNivel1=1
          menuNivel2=0
          menuNivel3=0      
        
     return   menuNivel1,menuNivel2,menuNivel3,selOperacion      
           
 def selmenuActivo3(self,frameActual,coordX,coordY,menuNivel1,menuNivel2,menuNivel3): 
      ancho=640
      alto=480
      coordX,coordY=self.seleccionarMenu(frameActual,ancho,alto)   
      if ((coordX>130 and coordX<160)and(coordY>40 and coordY<70)):
                    menuNivel1=1
                    menuNivel2=0
                    menuNivel3=0  
      else:
                if ((coordX>170 and coordX<200)and(coordY>40 and coordY<70)):
                    menuNivel1=0
                    menuNivel2=1
                    menuNivel3=0
                   # selOperacion=2
                else:
                    
                    menuNivel1=0
                    menuNivel2=0
                    menuNivel3=1 
                          
      return   menuNivel1,menuNivel2,menuNivel3        


     

 def transicionEtapa(self, etapa,llavePaso,etapaFinal,frame_rgb):
     dpulgar_x,dpulgar_y=self.coordenadasReferencia(frame_rgb,640,480,4)
     dindice_x,dindice_y=self.coordenadasReferencia(frame_rgb,640,480,8)
     distanciaDedotes= self.distanciaDedos( dpulgar_x,dpulgar_y, dindice_x,dindice_y)
     mano=self.queMano(frame_rgb)
    
                             
     if (mano != None):    

        if mano=='Left':
            if distanciaDedotes<20:
                    llavePaso=1
                    
            if ((distanciaDedotes>50) and (llavePaso==1)):
                    if etapa==etapaFinal:
                         etapa=etapaFinal
                    else:
                         etapa=etapa+1   
                    llavePaso=0
                    
           
        else:
            if mano=='Right':
                if distanciaDedotes<20:
                    llavePaso=1
                if ((distanciaDedotes>50) and (llavePaso==1)):
                    if etapa==1:
                        etapa=1
                    else:
                        etapa=etapa-1    
                    llavePaso=0 
     return etapa,llavePaso     