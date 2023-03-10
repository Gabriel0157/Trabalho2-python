print("Hoje irei descobrir o/a personagem que você está pensando da série Stranger Things 4!")
print("")
print("O personagem é do sexo masculino ou feminino?")
sexo=input()
if sexo=="feminino":
    print("faz parte do grupo ou ajuda o grupo?")
    resposta=input()
    if resposta=="faz parte" or resposta=="faz parte do grupo" or resposta=="sim":
        print("é uma adulta ou uma adolescente?")
        idade=input()
        if idade=="adolescente":
            print("tem poderes?")
            habilidades=input()
            if habilidades=="sim":
                print("Então é a Eleven!")
            else:
                print("Então é a Max!")
        elif idade=="adulta":
            print("A personagem trabalha?")
            trabalha=input()
            if trabalha=="sim":
                print("Então é a Robin!")
            else:
                print("Então é a Nancy!")
    elif resposta=="ajuda" or resposta=="ajuda o grupo":
        print("aparece bastante na série?")
        resposta=input()                
        if resposta=="sim":
            print("é uma criança ou adulta?")
            resposta=input()
            if resposta=="criança":
                print("Então é a Erica!")
            else:
                print("Então é a Joyce!")
        else:
            print("Mamora com alguém do grupo?")
            resposta=input()
            if resposta=="sim":
                print("Então é a Suzie!")
            else:
                print("então é a Chrissy!")
else:
    print("faz parte do grupo?")
    resposta=input()
    if resposta=="sim":
        print("tem o cabelo meio grande?")
        resposta=input()
        if resposta=="sim":
            print("usa bone?")
            resposta=input()
            if resposta=="sim":
                print("Então é o Dustin!")
            else:
                print("Então é o Mike")
        else:
            print("Este personagem joga Basquete?")
            resposta=input()
            if resposta=="sim":
                print("Então é o lucas!")
            else:
                print("Então é o Will!")
    else:
        print("é jovem ou adulto?")
        resposta=input()
        if resposta=="jovem":
            print("ele trabalha?")
            resposta=input()
            if resposta=="sim":
                print("Então é o Steve!")
            else:
                print("Então é o Jonathan!")
        else:
            print("já foi policial?")
            resposta=input()
            if resposta=="sim":
                print("Então é o Jim Hopper!")
            else:
                print("Então é o Murray!")
