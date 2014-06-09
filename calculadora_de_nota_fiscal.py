def _login_():
    login = input('Digite o usuário em maiusculo: ')
    login2 =  input('Digite a senha: ')
    usuario = ('MARLON')
    senha = ('jesus')
    if login == usuario and login2 == senha:
        print('Você está logado')
        conta()
    else:
        print('Senha ou usuario não corresponde')

def pergunta():
    print('\nDeseja continuar o programa?')
    print('Digite 1 para SIM')
    print('Digite 2 para NÃO')
    perg = int(input('DIGITE O NUMERO: '))
    perg1 = (1)
    perg2 = (2)

    if perg == 1:
        conta()
    elif perg == 2:
        print('Parabéns, voce me fez perder tempo!')
    else:
        print('Essa opção não existe!')
        
def conta():
    quat = int(input("\nQuantidade: "))
    valor = float(input("Valor da nota: "))
    total = 0
    for num in range(quat):
        num = num + 1
        print ("\n CALCULO %s" %num)
        n = int(input('Digite a quantidade %s:' %num))
        n2 = float(input('Digite o preço unitário %s:' %num))
        n3 = n * n2
        print ("Total %s:" %num, n3)
        total = total + n3
        if total == valor != quat == num:
            print("PODE PROTOCOLAR", total)
            pergunta()
        elif total >= valor or quat == num: 
            print("VALOR NÃO CONFERE")
            pergunta()
        if total >= valor or quat == num: break

_login_()





