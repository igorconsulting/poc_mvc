def introduction_page():
    message = """
        Sistema Cadastral

        * Cadastrar Pessoa - 1
        * Buscar Pessoa por Nome - 2
        * Sair - 0
    """

    print(message)

    command = input('Comando: ')

    return command

