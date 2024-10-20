'''Descrição:


Você foi contratado para desenvolver um sistema básico de gerenciamento de funcionários para uma pequena empresa. O sistema deve ser capaz de receber e armazenar informações sobre os funcionários e realizar operações básicas de manipulação desses dados.

Requisitos:

Utilize a função input() -  realizar um cadastro coletando dados do usuário, como nome, cidade e estado em que reside, idade, escolaridade, cargo e salário.
 

Funcionalidades do Sistema:

O sistema deve oferecer as seguintes funcionalidades:

Adicionar um novo funcionário ao sistema, solicitando informações como nome, cargo, salário, e-mail, etc.


Atualizar as informações de um funcionário existente com base em um identificador único (como um número de identificação ou nome). Exibir informações de um funcionário específico.

Listar todos os funcionários cadastrados.

Permitir a remoção de um funcionário do sistema.



Observações Finais: Certifique-se de implementar um sistema de identificação único para cada funcionário. Valide as entradas do usuário para garantir que as operações sejam realizadas corretamente e sem erros. Documente adequadamente seu código com comentários explicativos para ajudar na compreensão. Esse projeto permite aos alunos praticar e consolidar conceitos fundamentais em Python, como operadores, estruturas de controle, estruturas de dados e funções, enquanto constroem um aplicativo útil para gerenciar informações de funcionários de uma empresa fictícia.
'''

print('\n:: GERENCIAMENTO DE FUNCIONÁRIOS ::\n')

lista_funcionarios = []
id_funcionario = 1

while True:
    print('\nDigite a opção desejada:')
    print('1. Adicionar Funcionário')
    print('2. Atualizar Funcionário')
    print('3. Exibir Funcionário Específico')
    print('4. Listar Todos os Funcionários')
    print('5. Remover Funcionário')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        funcionario = {
            'ID': id_funcionario,
            'nome': input('Digite o nome do funcionário: '),
            'cidade': input('Digite a cidade do funcionário: '),
            'estado': input('Digite o estado do funcionário: '),
            'idade': int(input('Digite a idade do funcionário: ')),
            'escolaridade': input('Digite a escolaridade do funcionário: '),
            'cargo': input('Digite o cargo do funcionário: '),
            'salário': float(input('Digite o salário do funcionário: ')),
            'email': input('Digite o email do funcionário: ')
        }

        lista_funcionarios.append(funcionario)
        print(f"\nFuncionário {funcionario['nome']} adicionado com sucesso!")
        id_funcionario += 1

    elif opcao == '2':
        id_atualizar = int(input("Digite o ID do funcionário a ser atualizado: "))
        encontrado = False

        for funcionario in lista_funcionarios:
            if funcionario["ID"] == id_atualizar:
                print(f"Atualizando dados do funcionário {funcionario['nome']}")

                funcionario['nome'] = input(f"Novo nome ({funcionario['nome']}): ") or funcionario['nome']
                funcionario['cidade'] = input(f"Nova cidade ({funcionario['cidade']}): ") or funcionario['cidade']
                funcionario['estado'] = input(f"Novo estado ({funcionario['estado']}): ") or funcionario['estado']
                funcionario['idade'] = int(input(f"Nova idade ({funcionario['idade']}): ") or funcionario['idade'])
                funcionario['escolaridade'] = input(f"Nova escolaridade ({funcionario['escolaridade']}): ") or funcionario['escolaridade']
                funcionario['cargo'] = input(f"Novo cargo ({funcionario['cargo']}): ") or funcionario['cargo']
                funcionario['salário'] = float(input(f"Novo salário ({funcionario['salário']}): ") or funcionario['salário'])
                funcionario['email'] = input(f"Novo email ({funcionario['email']}): ") or funcionario['email']

                print(f"\nFuncionário {funcionario['nome']} atualizado com sucesso!")
                encontrado = True
                break

        if not encontrado:
            print(f"\nFuncionário com ID {id_atualizar} não encontrado.")

    elif opcao == '3':
        id_exibir = int(input('Digite o ID do funcionário: '))
        encontrado = False

        for funcionario in lista_funcionarios:
            if funcionario["ID"] == id_exibir:
                print(f"\nFuncionário {funcionario['nome']}:")
                for chave, valor in funcionario.items():
                    print(f"{chave.capitalize()}: {valor}")
                encontrado = True
                break

        if not encontrado:
            print(f"\nFuncionário com ID {id_exibir} não encontrado.")

    elif opcao == '4':
        if not lista_funcionarios:
            print('\nNenhum funcionário cadastrado.')
        else:
            print('\nLista de Funcionários Cadastrados:')
            for funcionario in lista_funcionarios:
                print(f"{funcionario['ID']}, {funcionario['nome']}, {funcionario['cidade']}, "
                      f"{funcionario['estado']}, {funcionario['idade']}, {funcionario['escolaridade']}, "
                      f"{funcionario['cargo']}, {funcionario['salário']}, {funcionario['email']}")

    elif opcao == '5':
        id_remover = int(input('Digite o ID do funcionário a ser removido: '))
        removido = False

        for i, funcionario in enumerate(lista_funcionarios):
            if funcionario['ID'] == id_remover:
                funcionario_removido = lista_funcionarios.pop(i)
                print(f"\nFuncionário {funcionario_removido['nome']} removido com sucesso!")
                removido = True
                break

        if not removido:
            print(f"\nFuncionário com ID {id_remover} não encontrado.")

    else:
        print('Opção inválida! Tente novamente.')

