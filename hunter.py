from utils.logger import Logger
from utils.config import Config

class Hunter():

    def __init__(self) -> None:
        self.config = Config.retorna_preferenciais_de_busca()

    def iniciar_busca(self):
        Logger.debug("Inicando busca...")
        


        

if __name__ == '__main__':
    hunter = Hunter()

    hunter.buscar()