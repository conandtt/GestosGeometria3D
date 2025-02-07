from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

class graficos():
    
    def __init__(self):
      pass
    
    def pre(self):     
      glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
      glutInitWindowSize(640, 480)
      glutInitWindowPosition(150, 150)
      glutCreateWindow('moverCubo') 
     
    def inicio(self,width, height):   
        glClearColor(0.0,0.0,0.0,0.0)  
        glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(60.0, float(width)/float(height), 4.0, 55.0)
        glRotate(180,0,0,1)       
        glTranslate(0,0,-8)
        glMatrixMode(GL_MODELVIEW)       
    
    def dibujoFondo(self,frame,idTextura,imgTextura,ix,iy):        
        glBindTexture(GL_TEXTURE_2D, idTextura)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, imgTextura)
        glLoadIdentity() 
        glPushMatrix()
        glEnable(GL_TEXTURE_2D)      
        self.graficoFondo() 
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        
    def dibujandoLineaCilindroColorAncho(self,xi,yi,zi,xf,yf,zf,color,ancho):
        
        xi,yi,zi=self.coordenadasReales3D(xi,yi,zi)
        xf,yf,zf=self.coordenadasReales3D(xf,yf,zf)
       
        glPointSize(ancho)
        glColor4f(color[0],color[1],color[2],color[3])
        
        glBegin(GL_LINES)
        glVertex3f(xi,yi,zi)        
        glVertex3f(xf,yf,zf)
        glEnd()

        glColor3f(1,1,1)  
   
    
    def dibujandoRectanguloCilindro(self,xf,yf,zf):
        
        xf,yf,zf=self.coordenadasReales3D(xf,yf,zf)

        glPointSize(2)
        glColor3f(0.7,0.5,0.8)
        glBegin(GL_QUADS)
        glVertex3f(0,-1,0)
        glVertex3f(xf,-1,zf)
        glVertex3f(xf,1,zf)
        glVertex3f(0,1,0)
        glColor3f(1,1,1)        

        glEnd() 


    def rotarTapaCilindro(self,anguloRotacionTapa,lugarRotacionx,lugarRotaciony,posicionx,posiciony):
            
            posicionx,posiciony=self.coordenadasReales(posicionx,posiciony)
            lugarRotacionx,lugarRotaciony=self.coordenadasReales(lugarRotacionx,lugarRotaciony)
            
            glPushMatrix() 
            glTranslate(lugarRotacionx,lugarRotaciony,0)
            glRotate(-anguloRotacionTapa,1,0,0)
            self.dibujandoCirculoSuperficie(1,posicionx,posiciony)
            glPopMatrix()

         
    def longitudArcoCirculoAvanceT(self,anguloInicial,anguloFinal,radio,direccion,posicionx,posiciony,color,ancho,plano):
       
         teta=anguloInicial
         pi=round(3.1415,2)
         longArco=anguloFinal-anguloInicial
         longArcoRadian=longArco*(3.1415)/180
         avanceFinal=pi-longArcoRadian

         while teta<=anguloFinal:
               radian=teta*(3.1415)/180        
               x=posicionx+direccion*round(radio*math.cos(radian),2)+direccion*avanceFinal
               y=posiciony+plano*(-1)*round(radio*math.sin(radian),2)
               self.graficoCirculo(x,y,color)           
               teta=teta+0.1

        
         self.dibujandoLineaCilindroColorAncho(0,posiciony+plano,0,direccion*avanceFinal,posiciony+plano,0,color,ancho) 
       
   
    def longitudArcoCilindroZ(self,anguloInicial,anguloFinal,radio,direccion,posicionx,posiciony,posicionz):
         colorMorado=(0.7,0.5,0.8,0.5)
         medianoAncho=1.5
         teta=anguloInicial
      
         pi=round(3.1415,2)
         longArco=anguloFinal-anguloInicial
         longArcoRadian=longArco*(3.1415)/180
         avanceFinal=pi-longArcoRadian
         while teta<=anguloFinal:
               radian=teta*(3.1415)/180               

               x=posicionx+direccion*round(radio*math.cos(radian),2)+direccion*avanceFinal#+(angRadian)
               y=posiciony
               z=posicionz-round(radio*math.sin(radian),2)
               self.graficoCilindro(x,y,z)  
               self.dibujandoLineaCilindroColorAncho(x,1,z,x,-1,z,colorMorado,medianoAncho) 
                   
               teta=teta+0.1
       
         self.dibujandoLineaCilindroColorAncho(0,posiciony,posicionz+1,direccion*avanceFinal,posiciony,posicionz+1,colorMorado,medianoAncho) 
         self.dibujandoRectanguloCilindro(direccion*avanceFinal,0,posicionz+1)      
         
    def dibujandoTriangulo(self,x1,y1,z1,x2,y2,z2,x3,y3,z3):

         x1f,y1f,z1f=self.coordenadasReales3D(x1,y1,z1)
         x2f,y2f,z2f=self.coordenadasReales3D(x2,y2,z2)
         x3f,y3f,z3f=self.coordenadasReales3D(x3,y3,z3)

         glBegin(GL_TRIANGLES)        
         glVertex3f(x1f,y1f,z1f) 
         glVertex3f(x2f,y2f,z2f)
         glVertex3f(x3f,y3f,z3f)        
         glEnd()

  
    
    def dibujandoCilindro2(self,radio,altura,ubicacionX,ubicacionY,ubicacionZ):
         ubicacionX,ubicacionY,ubicacionZ=self.coordenadasReales3D(ubicacionX,ubicacionY,ubicacionZ)
         puntos=360
         pi=round(3.1415,2)
            

         glColor3f(0.9,0.8,0.4)
         glBegin(GL_TRIANGLE_FAN)        
         glVertex3f(ubicacionX,ubicacionY,ubicacionZ)   
         i=0         
         while i<=puntos :            
        
            anguloArco=2*pi*(i/puntos)  
            x=ubicacionX+round(radio*math.cos(anguloArco),2)
            y=ubicacionY+round(radio*math.sin(anguloArco),2)
            glVertex3f(x,y,-(ubicacionZ))
            i=i+1         
         glEnd()
         
         glBegin(GL_TRIANGLE_FAN)        
         glVertex3f(ubicacionX,ubicacionY,ubicacionZ-altura)   
         i=0
         while i<=puntos :            
                
            anguloArco=2*pi*(i/puntos)
            x=ubicacionX+round(radio*math.cos(anguloArco),2)
            y=ubicacionY+round(radio*math.sin(anguloArco),2)
            glVertex3f(x,y,-(ubicacionZ+altura))

            i=i+1         
         glEnd()
         
         glBegin(GL_LINES)  

         glColor4f(0.7,0.5,0.8,0.5)   
         i=0
         puntosi=720
       
         while i<=puntosi :            
            anguloArco=2*pi*(i/puntos)
            x=ubicacionX+round(radio*math.cos(anguloArco),2)
            y=ubicacionY+round(radio*math.sin(anguloArco),2)
            glVertex3f(x,y,-(ubicacionZ+altura))
            glVertex3f(x,y,-(ubicacionZ))
            i=i+1         
         glEnd()       

         glColor3f(1,1,1)

    def dibujandoCirculoSuperficie(self,radio,ubicacionX,ubicacionY):
         ubicacionX,ubicacionY,zf=self.coordenadasReales3D(ubicacionX,ubicacionY,0)
         puntos=36
         pi=round(3.1415,2)
         circulo=1

         glColor3f(0.9,0.8,0.4)
         glBegin(GL_TRIANGLE_FAN)        
         glVertex3f(ubicacionX,ubicacionY,0)   
         i=0
         while i<=puntos :
             circulo=2*pi*radio*(i/puntos)
             x=ubicacionX+round(radio*math.cos(circulo),2)
             y=ubicacionY+round(radio*math.sin(circulo),2)
             glVertex3f(x,y,0)
             i=i+1         
         glEnd()
         glColor3f(1,1,1)
    

    
    def graficoCirculo(self,x,y,color): 
        glColor3f(color[0],color[1],color[2])
        xf,yf,zf=self.coordenadasReales3D(x,y,0)
        glPointSize(2)        
       # glColor3f(0.9,0.8,0.4)
        glBegin(GL_POINTS)        
        glVertex3f(xf,yf,0)   
        glEnd()
        glColor3f(1.0, 1.0, 1.0)


    def graficoCilindro(self,x,y,z):

        xf,yf,zf=self.coordenadasReales3D(x,y,z)
        glPointSize(2)
        glColor3f(0.7,0.5,0.8)
        glBegin(GL_POINTS)        
        glVertex3f(xf,yf,zf)   
        glEnd()
    
    
    def coordenadasReales(self,x,y):
        xf=x*(-1)
        yf=y*(-1)
        return xf,yf

    def coordenadasReales3D(self,x,y,z):
        xf=x*(-1)
        yf=y*(-1)
        return xf,yf,z
    
    def moviendoPlano(self,plano,distancia):

        miLista=list(plano)
        
        fila1=list(miLista[0])
        valorx= fila1[0]
        valorx=distancia[0]+valorx
        fila1.insert(0,valorx)
        fila1.pop(1)

        fila2=list(miLista[1])
        valorx= fila2[0]
        valorx=distancia[0]+valorx
        fila2.insert(0,valorx)
        fila2.pop(1)

        fila3=list(miLista[2])
        valorx= fila3[0]
        valorx=distancia[0]+valorx
        fila3.insert(0,valorx)
        fila3.pop(1)
        
        fila4=list(miLista[3])
        valorx= fila4[0]
        valorx=distancia[0]+valorx
        fila4.insert(0,valorx)
        fila4.pop(1)
        
        miLista=[fila1,fila2,fila3,fila4]

        fila1=list(miLista[0])
        valory= fila1[1]
        valory=distancia[1]+valory
        fila1.insert(1,valory)
        fila1.pop(2)

        fila2=list(miLista[1])
        valory= fila2[1]
        valory=distancia[1]+valory
        fila2.insert(1,valory)
        fila2.pop(2)

        fila3=list(miLista[2])
        valory= fila3[1]
        valory=distancia[1]+valory
        fila3.insert(1,valory)
        fila3.pop(2)
                  
        fila4=list(miLista[3])
        valory= fila4[1]
        valory=distancia[1]+valory
        fila4.insert(1,valory)
        fila4.pop(2)

        miLista=[fila1,fila2,fila3,fila4]
        
        fila1=list(miLista[0])
        valorz= fila1[2]
        valorz=distancia[2]+valorz
        fila1.insert(2,valorz)
        fila1.pop(3)

        fila2=list(miLista[1])
        valorz= fila2[2]
        valorz=distancia[2]+valorz
        fila2.insert(2,valorz)
        fila2.pop(3)

        fila3=list(miLista[2])
        valorz= fila3[2]
        valorz=distancia[2]+valorz
        fila3.insert(2,valorz)
        fila3.pop(3)
        
        fila4=list(miLista[3])
        valorz= fila4[2]
        valorz=distancia[2]+valorz
        fila4.insert(2,valorz)
        fila4.pop(3)

        fila=(tuple(fila1),tuple(fila2),tuple(fila3),tuple(fila4))
   
        return fila

      

    def graficandoPlanoDelPrisma(self,punto1,punto2,punto3,punto4,dx,dy,dz,cx,cy,cz,ejeGiro,anguloRotacion,color):
          
          p1f,p2f,p3f,p4f=self.graficandoPuntosPlano(punto1,punto2,punto3,punto4)
          plano=(p1f,p2f,p3f,p4f)
          dxf,dyf,dzf=self.coordenadasReales3D(dx,dy,dz)
          #distancia
          distancia=(dxf,dyf,dzf)
          planoFinal=self.moviendoPlano(plano,distancia)
          #cordenadas  
          cxf,cyf,czf=self.coordenadasReales3D(cx,cy,cz)          
          ejeCoordenadas=(cxf,cyf,czf)
          self.dibujoPlano(anguloRotacion,ejeGiro,ejeCoordenadas,planoFinal,color)


    def graficandoPuntosPlano(self,punto1,punto2,punto3,punto4):
            punto1=self.coordenadasReales3D(punto1[0],punto1[1],punto1[2])
            punto2=self.coordenadasReales3D(punto2[0],punto2[1],punto2[2])
            punto3=self.coordenadasReales3D(punto3[0],punto3[1],punto3[2])
            punto4=self.coordenadasReales3D(punto4[0],punto4[1],punto4[2])
            return punto1,punto2,punto3,punto4    


    def graficoLineaColorU(self,xi,yi,zi,xf,yf,zf,color):
        
        xi,yi,zi=self.coordenadasReales3D(xi,yi,zi)
        xf,yf,zf=self.coordenadasReales3D(xf,yf,zf)  

        glColor4f (color[0],color[1],color[2],color[3]) 
        glLineWidth(2)
        
        glBegin(GL_LINES)
        glVertex3f(xi,yi,zi)
        glVertex3f(xf,yf,zf)
        glEnd()
        
        glColor4f(1.0,1.0,1.0,0.5) 


    def posicionCoordenadasPrisma(self):
        colorBlanco=(1,1,1,0.5)
        glPushMatrix()
        glTranslate(0,0,2)
        self.graficoLineaColorU(-1,-1,0,-1,1,0,colorBlanco)
        self.graficoLineaColorU(-1,-1,0,1,-1,0,colorBlanco)
        self.graficoLineaColorU(-1,-1,0,-1,-1,-3,colorBlanco)     
        glPopMatrix()
    
    def graficandoCoordenadas(self,l): 
       colorBlanco=(1,1,1,0.5)
       self.graficoLineaColorU(-l,-l,0,-l,l,0,colorBlanco)
       self.graficoLineaColorU(-l,-l,0,l,-l,0,colorBlanco)
       self.graficoLineaColorU(-l,-l,0,-l,-l,0,colorBlanco)   
    
    def graficoCuadrilatero(self,x1,y1,x2,y2,x3,y3,x4,y4,color):

        x1,y1=self.coordenadasReales(x1,y1)
        x2,y2=self.coordenadasReales(x2,y2)  
        x3,y3=self.coordenadasReales(x3,y3)
        x4,y4=self.coordenadasReales(x4,y4)
        self.graficoCuadradoPadre(x1,y1,x2,y2,x3,y3,x4,y4,color)  
    
   

    def graficoCuadradoPadre(self,x1,y1,x2,y2,x3,y3,x4,y4,color):        
       
        glLineWidth(3)      

        glColor4f(color[0],color[1],color[2],color[3]) 

        glBegin(GL_LINES)        
        
        glVertex3f(x1,y1,0)
        glVertex3f(x2,y2,0)

        glVertex3f(x2,y2,0)
        glVertex3f(x3,y3,0)

        glVertex3f(x3,y3,0)
        glVertex3f(x4,y4,0)

        glVertex3f(x4,y4,0)
        glVertex3f(x1,y1,0)
        
        glColor3f(1,1,1)
        glEnd()

   
    def graficoPrismaPintaT(self,x1,y1,x2,y2,x3,y3,x4,y4,color):
        x1,y1=self.coordenadasReales(x1,y1)
        x2,y2=self.coordenadasReales(x2,y2)  
        x3,y3=self.coordenadasReales(x3,y3)
        x4,y4=self.coordenadasReales(x4,y4)
        self.graficoPrismaPintaPadre(x1,y1,x2,y2,x3,y3,x4,y4,color)


    
    def graficoPrismaPintaPadre(self,x1,y1,x2,y2,x3,y3,x4,y4,color):        
       
        glLineWidth(3)      

        glColor4f(color[0],color[1],color[2],color[3]) 

        glBegin(GL_QUADS)        
        
        glVertex3f(x1,y1,0)       
        glVertex3f(x2,y2,0)
        glVertex3f(x3,y3,0)       
        glVertex3f(x4,y4,0)       
        glColor3f(1,1,1)
        
        glEnd()   
     
    def graficoCuadrilateroSimulacion(self,x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4):

        x1,y1,z1=self.coordenadasReales3D(x1,y1,z1)
        x2,y2,z2=self.coordenadasReales3D(x2,y2,z2)  
        x3,y3,z3=self.coordenadasReales3D(x3,y3,z3)
        x4,y4,z4=self.coordenadasReales3D(x4,y4,z4)
        
        glColor4f (0.900, 0.100, 0.900,0) 
        glLineWidth(1)       
        glBegin(GL_QUADS)        
        glVertex3f(x1,y1,z1)
        glVertex3f(x2,y2,z2) 
        glVertex3f(x3,y3,z3)
        glVertex3f(x4,y4,z4)            
        glEnd()      
        glColor3f(1.0,1.0,1.0)   


    def pintarCuadradoT(self,x1,y1,x2,y2,x3,y3,x4,y4,color): #  area izq, plano2

        glColor4f(color[0],color[1],color[2],color[3])          

        x1,y1=self.coordenadasReales(x1,y1)
        x2,y2=self.coordenadasReales(x2,y2)  
        x3,y3=self.coordenadasReales(x3,y3)
        x4,y4=self.coordenadasReales(x4,y4)  
      
        glBegin(GL_QUADS)        
        glVertex3f(x1,y1,0)
        glVertex3f(x2,y2,0) 
        glVertex3f(x3,y3,0)
        glVertex3f(x4,y4,0)       
        glEnd()
        glColor3f(1.0,1.0,1.0) 

    
    def dibujoPlano(self, anguloRotacion,ejeGiro, ejeCoordenadas,plano,color):              
          glPushMatrix() 
          glTranslate(ejeCoordenadas[0],ejeCoordenadas[1],ejeCoordenadas[2])
          glRotate(anguloRotacion,ejeGiro[0],ejeGiro[1],ejeGiro[2])
          glColor4f(color[0],color[1],color[2],0.5)

          glBegin(GL_QUADS)
          glVertex3f(plano[0][0],plano[0][1],plano[0][2])
          glVertex3f(plano[1][0],plano[1][1],plano[1][2])
          glVertex3f(plano[2][0],plano[2][1],plano[2][2])
          glVertex3f(plano[3][0],plano[3][1],plano[3][2])
          glEnd()   
        # glDisable(GL_BLEND)
          glColor3f(1,1,1)
          glLineWidth(2)
          glBegin(GL_LINES)
          
          glVertex3f(plano[0][0],plano[0][1],plano[0][2])
          glVertex3f(plano[1][0],plano[1][1],plano[1][2])

          glVertex3f(plano[1][0],plano[1][1],plano[1][2])
          glVertex3f(plano[2][0],plano[2][1],plano[2][2])

          glVertex3f(plano[2][0],plano[2][1],plano[2][2])
          glVertex3f(plano[3][0],plano[3][1],plano[3][2])
          
          glVertex3f(plano[3][0],plano[3][1],plano[3][2])
          glVertex3f(plano[0][0],plano[0][1],plano[0][2])

          glEnd()        
          glPopMatrix()
          glColor3f(1,1,1)
          
   
    def graficoPlanoSimulacion(self,x,y,z,puntoLimte):
        xf,yf,zf=self.coordenadasReales3D(x,y,z)
        
        glBegin(GL_QUADS)
        
       
       # glColor4f(0.7,0.5,0.8,0.5)
        glColor4f(0.439, 0.463, 0.929,0.5)
        glVertex3f(-xf,yf, puntoLimte)
        glVertex3f(-xf,yf,-zf)
        glVertex3f(-xf,-yf,-zf)
        glVertex3f(-xf,-yf,puntoLimte)
        
        glColor4f(0.5,0.7,0.9,0.5)
        glVertex3f(-xf, -yf, puntoLimte)
        glVertex3f(-xf,-yf,-zf)
        glVertex3f(xf,-yf,-zf)
        glVertex3f(xf,-yf,puntoLimte)

        glColor4f(0.5,0.8,0.6,0.5)
        glVertex3f(xf, -yf, puntoLimte)
        glVertex3f(xf,-yf,-zf)
        glVertex3f(xf,yf,-zf)
        glVertex3f(xf,yf,puntoLimte)
        
        glColor4f(0.902,0.91, 0.31,0.5)
        # glColor4f(0.7,0.2,0.2,0.5)
        glVertex3f(-xf, yf, puntoLimte)
        glVertex3f(-xf,yf,-zf)
        glVertex3f(xf,yf,-zf)
        glVertex3f(xf,yf,puntoLimte)

       # # glColor4f(0.9, 0.4, 0.3,0.5) #0.7,0.2,0.2,0.5
        glColor4f (0.900, 0.100, 0.900,0.6)
        glVertex3f(-xf, yf, -zf)
        glVertex3f(xf,yf,-zf)
        glVertex3f(xf,-yf,-zf)
        glVertex3f(-xf,-yf,-zf)
       
        
        #glColor4f(0.9,0.8,0.4,0.5)
        glColor4f (0.900, 0.100, 0.900,0.6)
        glVertex3f(-xf, yf, puntoLimte)
        glVertex3f(xf,yf,puntoLimte)
        glVertex3f(xf,-yf,puntoLimte)
        glVertex3f(-xf,-yf,puntoLimte)

       
        glColor4f(1.0, 1.0, 1.0, 1.0)
        glEnd()  


    def graficoCuboEsqueleticoVariableVolumen(self,x1,y1,z1,x2,y2,z2):
        x1,y1,z1=self.coordenadasReales3D(x1,y1,z1)
        x2,y2,z2=self.coordenadasReales3D(x2,y2,-z2)
        glLineWidth(2)
        glBegin(GL_LINES)

        #--------------base-----------
        #vertice posterior vertical derecha
        glVertex3f(x1, y1,z1)
        glVertex3f(x2, y1, z1)
        # vertice posterior horizontal inferior
        glVertex3f(x2, y1, z1)
        glVertex3f(x2,y2,z1)
        # vertice posterior horizontal superior
        glVertex3f(x2, y2, z1)
        glVertex3f(x1, y2, z1)
        #vertice posterior vertical izquierda
        glVertex3f(x1, y2, z1)
        glVertex3f(x1, y1, z1)

         #--------------tapa-----------
        #vertice posterior vertical derecha
        glVertex3f(x1, y1,z2)
        glVertex3f(x2, y1, z2)
        # vertice posterior horizontal inferior
        glVertex3f(x2, y1, z2)
        glVertex3f(x2,y2,z2)
        # vertice posterior horizontal superior
        glVertex3f(x2, y2, z2)
        glVertex3f(x1, y2, z2)
        #vertice posterior vertical izquierda
        glVertex3f(x1, y2, z2)
        glVertex3f(x1, y1, z2)

        #--------------aristas-----------
        glVertex3f(x1, y1,z1)
        glVertex3f(x1, y1, z2)

        glVertex3f(x2, y1,z1)
        glVertex3f(x2, y1, z2)

        glVertex3f(x2, y2,z1)
        glVertex3f(x2, y2, z2)

        glVertex3f(x1, y2,z1)
        glVertex3f(x1, y2, z2)
        
        glEnd()

  
    def graficoFondo(self):
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-9.5, -7.2, -4.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(9.5, -7.2, -4.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(9.5, 7.2, -4.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-9.5, 7.2, -4.0)    
        glEnd()     

    
   
    def graficoPlanoUnitarioColorido(self,p1,p2,p3,p4,color):
                      
            glLineWidth(1.5)  
            glBegin(GL_LINES)
            glColor4f(1.0,1.0,1.0,1.0)

            glVertex3f(p1[0],p1[1],p1[2])
            glVertex3f(p2[0],p2[1],p2[2])

            glVertex3f(p2[0],p2[1],p2[2])
            glVertex3f(p3[0],p3[1],p3[2])

            glVertex3f(p3[0],p3[1],p3[2])
            glVertex3f(p4[0],p4[1],p4[2])

            glVertex3f(p4[0],p4[1],p4[2])
            glVertex3f(p1[0],p1[1],p1[2])
            
            glEnd()    

            glPushMatrix()
            glEnable(GL_BLEND)  
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            glBegin(GL_QUADS)
                  
            glColor4f(color[0],color[1],color[2],color[3])
            glVertex3f(p1[0],p1[1],p1[2])
            glVertex3f(p2[0],p2[1],p2[2])
            glVertex3f(p3[0],p3[1],p3[2])
            glVertex3f(p4[0],p4[1],p4[2])   
               
            glEnd()
            glDisable(GL_BLEND)   
            glPopMatrix()
            glColor4f(1.0,1.0,1.0,1.0)

       
    def graficoCuboSecuencial8Cubos(self,color,interruptor1,interruptor2,interruptor3,interruptor4,interruptor5,interruptor6,interruptor7,interruptor8):
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,0,0,0,color,interruptor1)
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,1,0,0,color,interruptor2)
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,0,0,1,color,interruptor3)
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,1,0,1,color,interruptor4)  

        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,0,1,0,color,interruptor5) 
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,1,1,0,color,interruptor6)
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,0,1,1,color,interruptor7)
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,1,1,1,color,interruptor8)

    def graficoCuboSecuencial27Cubos(self,color,interruptor1,interruptor2,interruptor3,interruptor4,interruptor5,interruptor6,interruptor7
                                          ,interruptor8,interruptor9,interruptor10,interruptor11,interruptor12,interruptor13,interruptor14,
                                           interruptor15,interruptor16,interruptor17,interruptor18,interruptor19,interruptor20,interruptor21,
                                           interruptor22,interruptor23,interruptor24,interruptor25,interruptor26,interruptor27): 
               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,-1,-1,-1,color,interruptor1)
               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,0,-1,-1,color,interruptor2)
               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,1,-1,-1,color,interruptor3)
                                       
               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,-1,-1,0,color,interruptor4)
               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,0,-1,0,color,interruptor5)
               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,1,-1,0,color,interruptor6)

               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,-1,-1,1,color,interruptor7)
               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,0,-1,1,color,interruptor8)
               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,1,-1,1,color,interruptor9)

               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,-1,0,-1,color,interruptor10)
               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,0,0,-1,color,interruptor11)
               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,1,0,-1,color,interruptor12)

               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,-1,0,0,color,interruptor13)
               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,0,0,0,color,interruptor14)
               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,1,0,0,color,interruptor15)

               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,-1,0,1,color,interruptor16)
               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,0,0,1,color,interruptor17)
               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,1,0,1,color,interruptor18)

               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,-1,1,-1,color,interruptor19)
               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,0,1,-1,color,interruptor20)
               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,1,1,-1,color,interruptor21)

               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,-1,1,0,color,interruptor22)
               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,0,1,0,color,interruptor23)
               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,1,1,0,color,interruptor24)

               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,-1,1,1,color,interruptor25)    
               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,0,1,1,color,interruptor26)  
               self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,1,1,1,color,interruptor27)

    
    def graficoPrismaSecuencial(self,color,interruptor1,interruptor2,interruptor3,interruptor4): 

        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,-1,0,0,color,interruptor1)  
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,0,0,0,color,interruptor1)                                
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,1,0,0,color,interruptor1)
    
        
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,-1,-1,0,color,interruptor1)
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,0,-1,0,color,interruptor1)                              
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,1,-1,0,color,interruptor1)                      



        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,-1,0,-1,color,interruptor2)
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,0,0,-1,color,interruptor2)                                      
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,1,0,-1,color,interruptor2)


        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,-1,-1,-1,color,interruptor2)
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,0,-1,-1,color,interruptor2)                                       
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,1,-1,-1,color,interruptor2)                                      


        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,-1,0,-2,color,interruptor3)
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,0,0,-2,color,interruptor3)                                        
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,1,0,-2,color,interruptor3)

        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,-1,-1,-2,color,interruptor3)
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,0,-1,-2,color,interruptor3)
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,1,-1,-2,color,interruptor3)

        
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,-1,0,1,color,interruptor4)                                                
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,0,0,1,color,interruptor4)                                               
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,1,0,1,color,interruptor4)


        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,-1,-1,1,color,interruptor4)
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,0,-1,1,color,interruptor4)                                               
        self.graficoPrismaUnitarioColorido2(0.5,0.5,0.5,1,-1,1,color,interruptor4)
              


    def graficoPrismaUnitarioColorido2(self,lx,ly,lz,dx,dy,dz,color,interruptor):
            
        if interruptor==1:  
            # base inferior 
           
            punto11=(-lx,-ly,-lz)
            punto12=(lx,-ly,-lz)
            punto13=(lx,-ly,lz)
            punto14=(-lx,-ly,lz)
           

            # base superior
            punto21=(-lx,ly,-lz)
            punto22=(lx,ly,-lz)
            punto23=(lx,ly,lz)
            punto24=(-lx,ly,lz)
                                        
             
            # lado izquierdo
            punto31=(-lx,-ly,-lz)
            punto32=(-lx,ly,-lz)
            punto33=(-lx,ly,lz)
            punto34=(-lx,-ly,lz)
            
            # lado derecho   
            punto41=(lx,-ly,lz)
            punto42=(lx,-ly,-lz)
            punto43=(lx,ly,-lz)
            punto44=(lx,ly,lz)

            #  lado posterior

            punto51=(-lx,-ly,-lz)
            punto52=(lx,-ly,-lz)
            punto53=(lx,ly,-lz)
            punto54=(-lx,ly,-lz)

            #lado frontal
            punto61=(-lx,-ly,lz)
            punto62=(lx,-ly,lz)
            punto63=(lx,ly,lz)
            punto64=(-lx,ly,lz)

            p11f,p12f,p13f,p14f=self.graficandoPuntosPlano(punto11,punto12,punto13,punto14)
            p21f,p22f,p23f,p24f=self.graficandoPuntosPlano(punto21,punto22,punto23,punto24)
            p31f,p32f,p33f,p34f=self.graficandoPuntosPlano(punto31,punto32,punto33,punto34)
            p41f,p42f,p43f,p44f=self.graficandoPuntosPlano(punto41,punto42,punto43,punto44)
            p51f,p52f,p53f,p54f=self.graficandoPuntosPlano(punto51,punto52,punto53,punto54)
            p61f,p62f,p63f,p64f=self.graficandoPuntosPlano(punto61,punto62,punto63,punto64)
              
            
            
            plano1=(p11f,p12f,p13f,p14f)
            plano2=(p21f,p22f,p23f,p24f)
            plano3=(p31f,p32f,p33f,p34f)
            plano4=(p41f,p42f,p43f,p44f)
            plano5=(p51f,p52f,p53f,p54f)
            plano6=(p61f,p62f,p63f,p64f)
            
            dx,dy,dz=self.coordenadasReales3D(dx,dy,dz)


            distancia=(dx,dy,dz)
           
                    
            p11f,p12f,p13f,p14f=self.moviendoPlano(plano1,distancia)
            p21f,p22f,p23f,p24f=self.moviendoPlano(plano2,distancia)
            p31f,p32f,p33f,p34f=self.moviendoPlano(plano3,distancia)
            p41f,p42f,p43f,p44f=self.moviendoPlano(plano4,distancia)
            p51f,p52f,p53f,p54f=self.moviendoPlano(plano5,distancia)
            p61f,p62f,p63f,p64f=self.moviendoPlano(plano6,distancia)
                        
            self.graficoPlanoUnitarioColorido(p11f,p12f,p13f,p14f,color)
            self.graficoPlanoUnitarioColorido(p21f,p22f,p23f,p24f,color)
            self.graficoPlanoUnitarioColorido(p31f,p32f,p33f,p34f,color)
            self.graficoPlanoUnitarioColorido(p41f,p42f,p43f,p44f,color)
            self.graficoPlanoUnitarioColorido(p51f,p52f,p53f,p54f,color)
            self.graficoPlanoUnitarioColorido(p61f,p62f,p63f,p64f,color)        

    
    def grafico2rpi(self,distanciaX,distanciaY,color):
        glColor4f(color[0],color[1],color[2],color[3])
        glPushMatrix()
        glTranslate(distanciaX,distanciaY,0)
        self.dibujoTexto18("2",0.2,-0.5)
        self.dibujoTexto18("r",-0.36,-0.5)
        self.graficoLineaColorU(0.02,0.65,0,0.32,0.65,0,color)
        self.graficoLineaColorU(0.12,0.65,0,0.12,0.48,0,color)
        self.graficoLineaColorU(0.22,0.65,0,0.22,0.48,0,color)
        
        glPopMatrix()
        glColor4f(1.0,1.0,1.0,1.0)
    
    
    def graficoPirCuadrado(self,distanciaX,distanciaY,color):
        glColor4f(color[0],color[1],color[2],color[3])
        glPushMatrix()
        glTranslate(distanciaX,distanciaY,0)
        self.dibujoTexto18("r",-0.35,-0.5)
        self.dibujoTexto10("2",-0.55,-0.7)
        self.graficoLineaColorU(0,0.65,0,0.3,0.65,0,color)
        self.graficoLineaColorU(0.1,0.65,0,0.1,0.48,0,color)
        self.graficoLineaColorU(0.2,0.65,0,0.2,0.48,0,color)
       
        glPopMatrix()
        glColor4f(1.0,1.0,1.0,1.0)

    
    def graficoPi(self,distanciaX,distanciaY,color):
        glColor4f(color[0],color[1],color[2],color[3])
        glPushMatrix()
        glTranslate(distanciaX,distanciaY,0)        
        self.graficoLineaColorU(0,0.65,0,0.3,0.65,0,color)
        self.graficoLineaColorU(0.1,0.65,0,0.1,0.48,0,color)
        self.graficoLineaColorU(0.2,0.65,0,0.2,0.48,0,color)       
        glPopMatrix()
        glColor4f(1.0,1.0,1.0,1.0)


    def dibujoTexto18(self,text, x, y):
         glRasterPos2f(x, y)
         for character in text:
        # glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(character))
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(character))

    def dibujoTexto10(self,text, x, y):
        glRasterPos2f(x, y)
        for character in text:
            # glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(character))
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, ord(character))
                
          
    

