class Senha():
    def __init__(self):
        self.senha = []

    def retirar_senha(self, nome):
        self.senha.append(nome)

    def chamar_senha(self):
        self.senha.pop(0)
        