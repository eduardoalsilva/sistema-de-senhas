from sistema_de_senhas import Senha

caixa_banco = Senha()
caixa_correios = Senha()
atendimento_hospital = Senha()

def banco():
    nome = input('Nome: ')
    caixa_banco.retirar_senha(nome)
    print(caixa_banco.senha)

def correios():
    nome = input('Nome: ')
    caixa_correios.retirar_senha(nome)
    print(caixa_correios.senha)

def hospital():
    nome = input('Nome: ')
    atendimento_hospital.retirar_senha(nome)
    print(atendimento_hospital.senha)

estabelecimento = '1'

while estabelecimento != '0':
    estabelecimento = input('Escolha o estabelecimento: \n1 - Banco \n2 - Correios \n3 - Hospital \n')

    if estabelecimento == '1':
        banco()

    elif estabelecimento == '2':
        correios()

    elif estabelecimento == '3':
        hospital()

    else:
        if estabelecimento == '0':
            break
        print('Escolha errada, tente novamente!')

