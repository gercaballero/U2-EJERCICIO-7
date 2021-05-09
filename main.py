from claseFechaHora import FechaHora
from claseHora import Hora
import os

def test():
   f1=[31,12,2020,20,30,30]
   h1=[10,25,45]
   os.system('cls')
   print('---EJEMPLO---\n')                            
   fecha1=FechaHora(f1[0],f1[1],f1[2],f1[3],f1[4],f1[5])
   hora1=Hora(h1[0],h1[1],h1[2])
   print('FECHA 1 ---------> {}'.format(fecha1))
   print('HORA  1 ---------> {}'.format(hora1))
   input()
   print('FECHA 1 + HORA 1 = {}\n'.format(fecha1+hora1))
   print('HORA 1 + FECHA 1 = {}\n'.format(hora1+fecha1))
   print('FECHA 1 - 1 DIA = {}\n'.format(fecha1-1))
   print('1 DIA + FECHA 1 = {}\n'.format(1+fecha1))

if __name__ == '__main__':
   t=str(input('DESEA PROBAR EL TEST (S/N) : '))
   if t.lower()=='s':
        test()
        input()
   os.system('cls')
   d = int(input("Ingrese Dia: "))
   mes = int(input("Ingrese Mes: "))
   a = int(input("Ingrese Año: "))
   h = int(input("Ingrese Hora: "))
   m = int(input("Ingrese Minutos: "))
   s = int(input("Ingrese Segundos: "))
   f = FechaHora(d,mes,a,h, m, s)
   f.Mostrar()
   input()
   h1 = int(input("Ingrese Hora: "))
   m1 = int(input("Ingrese Minutos: "))
   s1 = int(input("Ingrese Segundos: "))
   r = Hora(h1, m1, s1)
   r.Mostrar()
   input()
   f2 = f +r
   f2.Mostrar()
   input()
   f3 = r + f
   f3.Mostrar()
   input()
   f4 = f3 - 1 # Al restar un número entero a un objeto FechaHora se debe restar la cantidad de
                   # días indicada por el número entero
   f4.Mostrar()
   input()
   f5= 1 + f2 # suma un día a un objeto FechaHora
   f5.Mostrar()
   input()
   