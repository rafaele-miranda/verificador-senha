import getpass

def gerador_senha():
    cont = 0
    nome = input("Digite seu nome: ")
    senha = getpass.getpass("Digite a senha: ")
    
    while cont < 3:
        verificacao = getpass.getpass(f"Olá {nome}! Digite a senha criada: ")
        if senha == verificacao:
            print(f"Seja bem vindo(a) ao nosso sistema!")
            return
        elif senha!= verificacao:
            cont +=1 
            print(f"Senha incorreta! Tentativas restantes {3 - cont}")
        
    print("Número máximo de tentativas permitido. Acesso bloqueado.")
   
gerador_senha()