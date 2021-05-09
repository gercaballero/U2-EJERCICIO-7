from claseHora import Hora
class FechaHora:
    __dia=0
    __mes=0
    __año=0
    __hora=0
    __minutos=0
    __segundos=0

    def __init__(self,dia=1,mes=1,año=2020,hora=0,minutos=0,segundos=0):
        if not isinstance(dia, int) or not isinstance(mes, int) or not isinstance(año, int) or not isinstance(hora, int) or not isinstance(minutos, int) or not isinstance(segundos, int):
            return
        self.__dia=dia           
        self.__mes=mes
        self.__año=año
        self.__hora=hora
        self.__minutos=minutos
        self.__segundos=segundos
        self.Verificar()
    
    def Mostrar(self):
        if self.__dia==0 and self.__mes == 0 and self.__año==0 and self.__hora==0 and self.__minutos==0 and self.__segundos==0:
            print('FECHA NO CREADA POR DATOS INCORRECTOS')
        else:
            print('{}/{}/{} - {}:{}:{}'.format(self.__dia,self.__mes,self.__año,self.__hora,self.__minutos,self.__segundos))
    def __str__(self):  
        return '{}/{}/{} - {}:{}:{}'.format(self.__dia,self.__mes,self.__año,self.__hora,self.__minutos,self.__segundos)
    def PonerEnHora(self,hr=-1,min=-1,seg=-1):
        if not isinstance(hr, int) and not not isinstance(min, int) and not isinstance(seg, int):
            print("TIPOS DE DATOS ENVIADOS SON INCORRECTOS")
            return
        if hr<-1 or hr>23 or min<-1 or min>59 or seg<-1 or seg>59:
            print ('FORMATO DE HORA INCORRECTO')
            return
        if hr!=-1:
            self.__hora=hr
        if min !=-1:
            self.__minutos=min
        if seg !=-1:
            self.__segundos=seg
    
    def AdelantarHora(self,hr=0,min=0,seg=0):
        if not isinstance(hr, int) and not not isinstance(min, int) and not isinstance(seg, int):
            print("TIPOS DE DATOS ENVIADOS SON INCORRECTOS")
            return
        self.__hora=self.__hora+hr
        self.__minutos=self.__minutos+min
        self.__segundos=self.__segundos+seg
        self.Verificar()

    def bisiesto(self):
        bandera=None
        if self.__año%4==0:
            bandera=True
            if self.__año%100==0:
                if self.__año%400==0:
                    bandera=True
                else:
                    bandera=False
        else:
            bandera=False
        return bandera
                
    def Verificar(self):
        if self.bisiesto(): 
            d=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            d=[31,28,31,30,31,30,31,31,30,31,30,31]
        if self.__segundos>=60:
            self.__segundos=self.__segundos%60
            self.__minutos=self.__minutos+1
        if self.__minutos>=60:
            self.__minutos=self.__minutos%60
            self.__hora=self.__hora+1
        if self.__hora>=24:
            self.__hora=self.__hora%24
            self.__dia=self.__dia+1
        while self.__mes>12:
            self.__mes=self.__mes-12
            self.__año=self.__año+1
        if self.__mes<1:
            self.__mes=12-abs(self.__mes)%12
            self.__año=self.__año-1
        while self.__dia>d[self.__mes-1] or self.__dia<1:
         if self.__mes in (2,3,4,5,6,7,8,9,10,11):
            if self.__dia>d[self.__mes-1]:
                self.__dia=self.__dia-d[self.__mes-1]
                self.__mes=self.__mes+1
            if self.__dia<=0:
                self.__dia=d[self.__mes-2]-abs(self.__dia)%d[self.__mes-2]
                self.__mes=self.__mes-1
         elif self.__mes == 1:
            if self.__dia>d[self.__mes-1]:
                self.__dia=self.__dia-d[self.__mes-1]
                self.__mes=self.__mes+1
            if self.__dia<=0:
                self.__dia=d[11]-abs(self.__dia)%d[11]
                self.__mes=12
                self.__año=self.__año-1
         elif self.__mes == 12:
            if self.__dia>d[11]:
                self.__dia=self.__dia-d[self.__mes-1]
                self.__mes=1
                self.__año=self.__año+1
            if self.__dia<=0:
                self.__dia=d[self.__mes-2]-abs(self.__dia)%d[self.__mes-2]
                self.__mes=self.__mes-1
                self.__año=self.__año+1
    def aSegundos(self):
        meses=0
        años=0
        dias=0
        horas=0
        minutos=0
        años=años+self.__año *31536000
        for i in range(1,self.__mes):
            if i in (11,4,6,9):
                meses=meses+ 2592000
            elif i in (1,3,5,7,8,10,12):
                meses=meses+ 2678400
            elif i == 2:
                if self.bisiesto():
                    meses=meses+ 2505600
                else:
                    meses=meses+ 2419200
        dias=dias+self.__dia*86400
        horas=horas+self.__hora*3600
        minutos=minutos+self.__minutos*60
        return int(años+meses+dias+horas+minutos+self.__segundos)

    def __gt__(self,otraFecha):
        band=None
        if type(otraFecha)==FechaHora:
            if self.aSegundos()>otraFecha.aSegundos():
             band=True
            else:
                band=False
        else:
            print('NO ES POSIBLE COMPARAR')
        return band

    def __add__(self, otra):
        if type(otra)==FechaHora:
            fecha=FechaHora(self.__dia+otraFecha.__dia,self.__mes+otraFecha.__mes,self.__año+otraFecha.__año,self.__hora+otraFecha.__hora,self.__minutos+otraFecha.__minutos,self.__segundos+otraFecha.__segundos)
        elif type(otra)==Hora:
            fecha=FechaHora(self.__dia,self.__mes,self.__año,self.__hora+otra.gethora(),self.__minutos+otra.getmin(),self.__segundos+otra.getseg())
        return fecha
    
    def __radd__(self,otra):
        if type(otra)==Hora:
            fecha=FechaHora(self.__dia,self.__mes,self.__año,self.__hora+otra.gethora(),self.__minutos+otra.getmin(),self.__segundos+otra.getseg())
        elif type(otra)==int:
            fecha=FechaHora(self.__dia+otra,self.__mes,self.__año,self.__hora,self.__minutos,self.__segundos)
        return fecha
    
    def __sub__(self,otra):
        if type(otra)==int:
            fecha=FechaHora(self.__dia-otra,self.__mes,self.__año,self.__hora,self.__minutos,self.__segundos)
        return fecha
        
    def __rsub__(self,otra):
        if type(otra)==int:
            fecha=FechaHora(self.__dia-otra,self.__mes,self.__año,self.__hora,self.__minutos,self.__segundos)
        return fecha
    

        