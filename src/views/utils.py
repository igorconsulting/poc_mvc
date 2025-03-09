import os

class ConsoleUtils:
    """Classe utilitária para operações no console."""
    
    @staticmethod
    def clear_console():
        """Limpa o console, independente do sistema operacional."""
        os.system('cls||clear')
