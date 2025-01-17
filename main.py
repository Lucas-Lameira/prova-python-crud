from exibir_dados_api import exibir_dados_api
from criar_banco import conexao
from utils import menu, limpar_tela
from cadastra_empresa import cadastrar_empresa

from ler_dados import \
    exibir_servicos_empresa, \
    pesquisar_uma_empresa, \
    listar_empresas, \
    listar_servicos_prestados, \
    isAlgumDado, \
    pesquisar_por_campo

from validacao import input_cnpj, menu_input
from novo_servico_prestado import cadastrar_serivico_prestado

from update import atualizar_empresa
from delete import deletar_empresa

if conexao() == 0:
    raise Exception("DEU RUIM")


isTrue = True
while isTrue:

    # print menu list
    menu()
    answer = menu_input(1, 11)

    # no switch case
    if answer == 1:
        exibir_dados_api()

    if answer == 2:
        cadastrar_empresa(0)

    elif answer == 3:
        listar_empresas()

    elif answer == 4:
        isOk = isAlgumDado()
        if not isOk:
            print("....")
        else:
            cnpj = input_cnpj()
            pesquisar_uma_empresa(cnpj)

    elif answer == 5:
        if listar_empresas() == 0:
            print("....")
        else:
            cnpj = input_cnpj()
            exibir_servicos_empresa(cnpj)

    elif answer == 6:
        cadastrar_serivico_prestado()

    elif answer == 7:
        if listar_empresas() == 0:
            print("....")
        else:
            cnpj = input_cnpj()
            listar_servicos_prestados(cnpj)

    elif answer == 8:
        if listar_empresas() == 0:
            print("....")
        else:
            cnpj = input_cnpj()
            atualizar_empresa(cnpj)

    elif answer == 9:
        if listar_empresas() == 0:
            print("....")
        else:
            cnpj = input_cnpj()
            deletar_empresa(cnpj)

    elif answer == 10:
        pesquisar_por_campo()


    elif answer == 11:
        print("saindo.....")
        break

    # check if the user wants to continue
    answer = input("Deseja continuar s/n: ")
    answer = answer.lower()
    while answer != 's' and answer != 'n':
        print("Digite 's' pra sim ou 'n' para não")
        answer = input("Deseja continuar s/n: ")

    if answer == 'n':
        isTrue = False
    limpar_tela()
