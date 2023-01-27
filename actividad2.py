

class MenuCalculadora:
    
    def _init_(self):
       pass

    def suma(self, a, b):
         self.num1=a
         self.num2=b
         self.res= self.num1+self.num2
         print("La suma es: {}".format(self.res)) 

    def resta(self, a, b):
         self.num1=a
         self.num2=b
         self.res= self.num1-self.num2
         print("La resta es: {}".format(self.res)) 

    def multiplicacion(self, a, b):
         self.num1=a
         self.num2=b
         self.res= self.num1*self.num2
         print("La multiplicación es: {}".format(self.res)) 
    
    def division(self, a, b):
         self.num1=a
         self.num2=b
         try:
          self.res= self.num1/self.num2
          print("La division es: {}".format(self.res))
         except ZeroDivisionError:
          print("La división entre cero no es posible")
         
          

def main():
    
    opcion = 0

    while True :
      
      print("""
      ¿qué operacion quieres hacer?
      1) Sumar
      2) Restar
      3) Multiplicar
      4) Dividir
      5) Salir
      """)
      opcion = int(input("Selecciona una: "))

      obj=MenuCalculadora()


      if opcion == 1:
        n1= int(input("Ingresa el primer numero: "))
        n2= int(input("Ingresa el segundo numero: "))        
        obj.suma(n1,n2)
        
      elif opcion == 2:
          n1= int(input("Ingresa el primer numero: "))
          n2= int(input("Ingresa el segundo numero: "))
          obj.resta(n1,n2)

      elif opcion == 3:
          n1= int(input("Ingresa el primer numero: "))
          n2= int(input("Ingresa el segundo numero: "))
          obj.multiplicacion(n1,n2)

      elif opcion == 4:
          n1= int(input("Ingresa el primer numero: "))
          n2= int(input("Ingresa el segundo numero: "))          
          obj.division(n1,n2)

      elif opcion == 5:
        print("Apagando......")
        break

      
    
    
    
if __name__=='__main__':
    main()