agenda={}
def adicionarContato(nome: str, telefone: str) -> None:
    agenda[nome] = telefone
    print("Contato adicionado com sucesso!")

def editarContato(nome: str, telefone: str) -> None:
    if nome in agenda.keys():
        agenda[nome] = telefone
        print("Telefone alterado com sucesso!")
    else:
        print("O Contato não existe na base: ")
def pesquisarContato(nome: str) -> None:
    if nome in agenda.keys():
        print("\n ------------------")
        print(f"Contato: {nome}")
        print(f"Telefone: {agenda[nome]}")
        print("\n ------------------")
    else:
        print("O Contato não existe na base: ")

def deletarContato(nome: str) -> None:
    if nome in agenda.keys():
       del agenda[nome]
       print("Contato removido da agenda!")
    else:
        print("O Contato não existe na base: ")

def listarTodos():
    for nome in agenda:
        print("\n ------------------")
        print(f"Contato: {nome}")
        print(f"Telefone: {agenda[nome]}")
        print("\n ------------------")

while True:
    print("----------- Bem Vindo ao Menu ----------")
    opcao = int(input("1 - Adicionar Contato \n"
                      "2 - Editar Contato \n"
                      "3 - Pesquisar Contato \n"
                      "4 - Deletar Contato \n"
                      "5 - Listar Contato \n"
                      "6 - Sair \n"
                      "---------------------------------------- \n"
                      "Selecione uma opção: "))
    if opcao == 1:
        nome = input("Digite o nome do contato: ")
        tel = input("Digite o telefone do contato: ")
        adicionarContato(nome, tel)
    elif opcao == 2:
        nome = input("Digite o nome do contato que você deseja alterar: ")
        tel = input("Digite o novo telefone do contato: ")
        editarContato(nome, tel)
    elif opcao == 3:
        nome = input("Digite o nome do contato a pesquisar: ")
        pesquisarContato(nome)
    elif opcao == 4:
        nome = input("Digite o nome do contato a deletar: ")
        deletarContato(nome)
    elif opcao == 5:
        listarTodos()
    elif opcao == 6:
        break
    else: print("Opção inválida!")
