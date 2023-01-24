
class OperasBas:
    #propiedades de clase
    n1=0
    n2=0
    res=0
    #constructor
    def __init__(self, a,b):
        self.n1= a
        self.n2= b

    #metodos de clase
    def suma(self):
        self.res=self.n1=self.n2
    def resta(self):
        self.res=self.n1=self.n2

def main():
    obj=OperasBas(3,2)
    obj.suma()  

if __name__=='__main__':
    main()      