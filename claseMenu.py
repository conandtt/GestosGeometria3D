import numpy as np
import cv2
from PIL import Image,ImageOps

class menu():
 def __init__(self,frame):
       self.frame=frame

 def menuPrincipal(self,frame):
    icono = cv2.imread('mpt2.png', cv2.IMREAD_UNCHANGED)
    return self.menuMadre(icono,frame)  

 def seleccionFiguraNivel2(self,frame,selFigura):
      
     if (selFigura==1):
                return self.menuCubo(frame)
     if (selFigura==2):
                return self.menuPrisma(frame)
     if (selFigura==3):
               return self.menuCilindro(frame)   
     
     
 def seleccionFiguraNivel3(self,frame,selFigura,selOperacion):
      
     if ((selFigura==1)and(selOperacion==2)):
          return self.menuAreaCubo(frame)
     if ((selFigura==1)and(selOperacion==1)):
          return self.menuVolumenCubo(frame)
     if ((selFigura==2)and(selOperacion==2)):
          return self.menuAreaPrisma(frame)
     if ((selFigura==2)and(selOperacion==1)):
          return self.menuVolumenPrisma(frame)
     if ((selFigura==3)and(selOperacion==2)):
          return self.menuAreaCilindro(frame)
     if ((selFigura==3)and(selOperacion==1)):
          return self.menuVolumenCilindro(frame) 
 
 def menuAreaCilindro(self,frame):
    icono = cv2.imread('aCilindro.png', cv2.IMREAD_UNCHANGED)
    return self.menuMadre(icono,frame)
  
 def menuVolumenCilindro(self,frame):
    icono = cv2.imread('vCilindro.png', cv2.IMREAD_UNCHANGED)
    return self.menuMadre(icono,frame)

 def menuAreaPrisma(self,frame):
    icono = cv2.imread('aPrisma.png', cv2.IMREAD_UNCHANGED)
    return self.menuMadre(icono,frame)
  
 def menuVolumenPrisma(self,frame):
    icono = cv2.imread('vPrisma.png', cv2.IMREAD_UNCHANGED)
    return self.menuMadre(icono,frame)
 
 def menuAreaCubo(self,frame):
    icono = cv2.imread('aCubo.png', cv2.IMREAD_UNCHANGED)
    return self.menuMadre(icono,frame)
  
 def menuVolumenCubo(self,frame):
    icono = cv2.imread('vCubo.png', cv2.IMREAD_UNCHANGED)
    return self.menuMadre(icono,frame)
 
 def menuCubo(self,frame):
    icono = cv2.imread('menuCubo.png', cv2.IMREAD_UNCHANGED)
    return self.menuMadre(icono,frame)   
   
 def menuCilindro(self,frame):
    icono = cv2.imread('menuCilindro.png', cv2.IMREAD_UNCHANGED)
    return self.menuMadre(icono,frame)
 
 def menuPrisma(self,frame):
    icono = cv2.imread('menuPrisma.png', cv2.IMREAD_UNCHANGED)
    return self.menuMadre(icono,frame)
    
 def menuMadre(self,imagen, frame):
    icono = Image.fromarray(imagen)
    icono=ImageOps.mirror(icono)
    icono=np.array(icono)
    mascara=icono[:,:,3] 
    mascara_invertida = cv2.bitwise_not(mascara)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
    n_frame=frame[10:310,70:570,:]
    bg_black = cv2.bitwise_and(icono, icono, mask=mascara)
    bg_frame = cv2.bitwise_and(n_frame, n_frame, mask=mascara_invertida)
    result = cv2.add(bg_black, bg_frame)
    frame[10:310,70:570]=result
    frame=cv2.cvtColor(frame,cv2.COLOR_BGRA2BGR)
    img1 = Image.fromarray(frame)
    return img1     
  
      
      
      
      
      
      
      


     







 
 
    
    









     

      


  




           