import os 
jr=0
while jr!=2:
    print("-"*25 , 'Tela Inicial' , '-'*25)
    print('1-CADASTRAR \n 2-LER \n 3-DELETAR \n 4-ATUALIZAR \n 5-SAIR')
    op=int(input("EScolha uma opção:"))
    if op==1:
        qt=int(input('QUANTOS CADASTRO VOCÊ DESEJA FAZER:'))
        x=0
        while x<qt:
            print( "-"*15 , "CADASTRO PESSOAL" ,"-"*15)
            nom=input("Digite seu nome:")
            c=input("Digite seu cpf:")
            id=input("Digite sua idade:")
            cep=input("Digite seu cep:")
            sen=input("Crie uma senha:")
            f=0
            while f!=2:
                print('Você deseja confirma seus dados acima?')
                print("1-Sim,desejo confirma meus dados. \n 2-Não,desejo refazer novamente.")
                esc=int(input('Escolha uma opção:'))
                if esc==1:
                    print('Seus dados salvos')
                    arq = open('CRUD 3.txt','a')
                    arq.write("---Cadastro----\n")
                    arq.write("Nome: "+nom+'\n')
                    arq.write("CPF: "+c+'\n')
                    arq.write("Idade:"+id+'\n')
                    arq.write("Cep:"+cep+'\n')
                    arq.write("Senha:"+sen+'\n')
                    arq.close()
                    x+=1
                    f=2
                if esc==2:
                    f=2

    if op==2:
        if os.path.exists('CRUD 3.txt'):
            arq = open('CRUD 3.txt','r')
            arqr = arq.readlines()
            cont=1
            for linha in arqr:
                if "---Cadastro---" in linha:
                    print("---Cadastro ",cont,"---")
                    cont=cont+1
                else:
                    print(linha, end="")
            arq.close()
        else:
            print("Sem cadastros")
    if op==3:
        print('~Qual opcão você deseja para deletar seus dados? \n 1-Desejo deletar apena 1 dado. \n 2-Desejo deletar todos oe meus dados.')
        ka=int(input('Escolha uma opção:'))

        if ka==1:
            if os.path.exists('CRUD 3.txt'):
                arq = open('CRUD 3.txt','r')
                arqr = arq.readlines()
                cont=1
                for linha in arqr:
                    if "---Cadastro---" in linha:
                        print("---Cadastro ",cont,"---")
                        cont=cont+1
                    else:
                        print(linha, end="")
                arq.close()
                qulc=int(input(" Qual você deseja deletar: "))
                arq = open('CRUD 3.txt','r')
                arq2 = arq.readlines()
                quantas_linhas = (len(arq2))
                linhas_verificada = qulc*6
                if linhas_verificada<=quantas_linhas:
                    lista=[]
                    for dado in arq2:
                        lista.append(dado)
                    os.remove('CRUD 3.txt')
                    arq = open('CRUD 3.txt','a')
                    qulc=qulc*6
                    del lista[qulc-6:qulc]
                    for dado in lista:
                        arq.write(dado)
                    arq.close()
                else:
                    print(" Não há essa cadastros")
                    arq.close()
            else:
                print("Sem cadastros")
        elif ka==2:
            if os.path.exists('CRUD 3.txt'):
                os.remove('CRUD 3.txt')
                print("Cadastros deletados")
    elif op==4:
        print("1 - Desejo atualizar um dado 2 - Desejo atualizar todos os dados ")
        atu=input("Qual deseja ? ")
        if atu=="1":
            if os.path.exists('CRUD 3.txt'):
                arq = open('CRUD 3.txt','r')
                arqr = arq.readlines()
                cont=1
                for linha in arqr:
                    if "---Cadastro---" in linha:
                        print("---Cadastro ",cont,"---")
                        cont=cont+1
                    else:
                        print(linha, end="")
                arq.close()
                qulc=int(input(" Qual você deseja atualizar: "))
                arq=open('CRUD 3.txt','r')
                arq2 = arq.readlines()
                quantas_linhas = (len(arq2))
                linhas_verificada = qulc*6
                if linhas_verificada<=quantas_linhas:
                    lista=[]
                    for dado in arq2:
                        lista.append(dado)
                    os.remove('CRUD 3.txt')
                    arq = open('CRUD 3.txt','a')
                    qulc=qulc*6
                    lista[qulc-5]="Nome:"+input("Digite seu nome:")+'\n'
                    lista[qulc-4]="CPF: "+input("Digite seu cpf:")+'\n'
                    lista[qulc-3]="Idade:"+input("Digite sua idade:")+'\n'
                    lista[qulc-2]="Cep:"+input("Digite seu cep:")+'\n'
                    lista[qulc-1]="Senha:"+input("Digite sua senha:")+'\n'
                    for dado in lista:
                        arq.write(dado)
                    arq.close()
                else:
                    print(" Não há essa cadastros")
                    arq.close()
        elif atu=="2":
            if os.path.exists('CRUD 3.txt'):
                arq = open('CRUD 3.txt','r')
                arqr = arq.readlines()
                cont=1
                for linha in arqr:
                    if "---Cadastro---" in linha:
                        print("---Cadastro ",cont,"---")
                        cont=cont+1
                    else:
                        print(linha, end="")
                arq.close()
                arq=open('CRUD 3.txt','r')
                arq2 = arq.readlines()
                quantas_linhas = (len(arq2))
                qulc = 1
                os.remove('CRUD 3.txt')
                while qulc<=quantas_linhas/6:
                    arq = open('CRUD 3.txt','a')
                    print( "-"*15 , "CADASTRO ATUALIZANDO" ,"-"*15)
                    nom=input("Digite seu nome:")
                    c=input("Digite seu cpf:")
                    id=input("Digite sua idade:")
                    cep=input("Digite seu cep:")
                    sen=input("Digite sua senha:")
                    f=0
                    while f!=2:
                        print('Você deseja confirma seus dados acima?')
                        print("1-Sim,desejo confirma meus dados. \n 2-Não,desejo refazer novamente.")
                        esc=int(input('Escolha uma opção:'))
                        if esc==1:
                            print('Seus dados salvos')
                            arq = open('CRUD 3.txt','a')
                            arq.write("---Cadastro----\n")
                            arq.write("Nome: "+nom+'\n')
                            arq.write("CPF: "+c+'\n')
                            arq.write("Idade"+id+'\n')
                            arq.write("Cep"+cep+'\n')
                            arq.write("Senha"+sen+'\n')
                            arq.close()
                            qulc+=1
                            f=2
                        if esc==2:
                            f=2
                    arq.close()
    elif op==5:
        u=0
        while u == 0:
            fec=input("Você deseja sair do programa\n1 - Sim\n2 - Não\n")
            if fec=="1":
                print("Fim do programa.")
                u=1
                jr=2
            elif fec=="2":
                u=1
                jr=0
            else:
                print("Essa opção não existe!!")


