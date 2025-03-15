from src.views.utils import ConsoleUtils
from typing import Dict, Optional

class PeopleRegisterView:
    def __init__(self, clear_screen: bool = True):
        """View para cadastro de pessoas."""
        self.clear_screen = clear_screen

    def registry_person_view(self, 
                             name: Optional[str] = None, 
                             age: Optional[str] = None, 
                             height: Optional[str] = None) -> Dict[str,
                                                                   str]:
        """
        Exibe a interface para registro de uma nova pessoa.

        Args:
            name (Optional[str]): Nome pré-preenchido, se fornecido.
            age (Optional[str]): Idade pré-preenchida, se fornecida.
            height (Optional[str]): Altura pré-preenchida, se fornecida.

        Returns:
            Dict[str, str]: Informações da nova pessoa.
        """
        if self.clear_screen:
            ConsoleUtils.clear_console()

        print('=== Cadastrar Nova Pessoa ===\n\n')

        name = name or input('Determine o nome da pessoa:\n').strip()
        age = age or self.get_valid_age()
        height = height or self.get_valid_height()

        return {"name": name, "age": age, "height": height}

    def get_valid_age(self) -> str:
        """Obtém uma idade válida do usuário."""
        while True:
            age = input('Determine a idade da pessoa:\n').strip()
            if age.isdigit() and 0 < int(age) < 120:
                return age
            print("Erro: Idade inválida! Insira um número entre 1 e 120.")

    def get_valid_height(self) -> str:
        """Obtém uma altura válida do usuário."""
        while True:
            height = input('Determine a altura da pessoa (em metros, ex: 1.75):\n').strip()
            try:
                height_value = float(height)
                if 0.5 < height_value < 2.5:
                    return height
            except ValueError:
                pass
            print("Erro: Altura inválida! Insira um valor numérico entre 0.5 e 2.5 metros.")