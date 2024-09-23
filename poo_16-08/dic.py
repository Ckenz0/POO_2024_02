dic_tarefas = {}
id = 0

while True:
    print("Menu de gerenciamento")
    print("1) Adicionar tarefa")
    print("2) Visualizar tarefas")
    print("3) Remover tarefa")
    print("4) Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        desc_tarefa = str(input("Digite a descrição da tarefa: "))
        dic_tarefas[id] = desc_tarefa
        id += 1
    elif opcao == 2:
        if len(dic_tarefas) > 0:
            for k, v in dic_tarefas.items():
                print(k, v)
        else: 
            print("Não há tarefas")
    elif opcao == 3: 
        remove = int(input("Coloque a ID a ser removida: "))
        if remove in dic_tarefas:
            del dic_tarefas[remove]
        else: 
            print("Tarefa não encontrada")
    elif opcao == 4:
        break
    else:
        print("opção invalida")