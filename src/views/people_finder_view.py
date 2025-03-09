import os
from typing import Dict
from utils import ConsoleUtils

class PeopleFinderView:
    def __init__(self, clear_screen: bool = True):
        """View para cadastro de pessoas."""
        self.clear_screen = clear_screen

    def find_person_view(self) -> Dict:
        """
        Exibe a interface para buscar uma pessoa pelo nome.

        Returns:
            Dict[str, str]: Dicionário contendo o nome informado.
        """
        if self.clear_screen:
            ConsoleUtils.clear_console()

        print('=== Buscar Pessoa ===\n\n')
        name = self.get_valid_name()

        return {"name": name}

    def get_valid_name(self) -> str:
        """Obtém um nome válido para busca."""
        while True:
            name = input('Determine o nome da pessoa para busca: ').strip()

            if name:
                return name
            
            print("Erro: O nome não pode estar vazio!")