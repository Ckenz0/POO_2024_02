class Manipulador:
    def soma(self, a, b):
        return a+b

    def invert_string(self, texto):
        return texto[::-1]
    
    def ePar(self, n):
        if n%2 == 0:
            return True

        else:
            return False

    def fatorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.fatorial(n-1)

    def criar_arquivo(self, nome, texto):
        with open(nome, "w") as f:
            f.write(texto)
        return True 
    
    def ler_arquivo(self, nome):
        with open(nome, "r") as f:
            return f.read()