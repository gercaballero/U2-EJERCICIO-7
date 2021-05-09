class Hora:
    __hora=-1
    __minutos=-1
    __segundos=-1

    def __init__(self,hora=0,minutos=0,segundos=0):
        if not isinstance(hora, int) or not isinstance(minutos, int) or not isinstance(segundos, int):
            return
        self.__hora=hora
        self.__minutos=minutos
        self.__segundos=segundos
        self.Verificar()
    def __str__(self):
        return ('{}:{}:{}'.format(self.__hora,self.__minutos,self.__segundos))
    def Mostrar(self):
        if self.__hora==-1 and self.__minutos==-1 and self.__segundos==-1:
            print('FECHA NO CREADA POR DATOS INCORRECTOS')
        else:
            print('{}:{}:{}'.format(self.__hora,self.__minutos,self.__segundos))
    
    def Verificar(self):
        if self.__segundos>=60:
            self.__segundos=self.__segundos%60
            self.__minutos=self.__minutos+1
        if self.__minutos>=60:
            self.__minutos=self.__minutos%60
            self.__hora=self.__hora+1
        if self.__hora>=24:
            self.__hora=self.__hora%24
    def gethora(self):
        return int(self.__hora)
    def getmin(self):
        return int(self.__minutos)
    def getseg(self):
        return int(self.__segundos)