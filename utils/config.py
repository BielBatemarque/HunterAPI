from configparser import ConfigParser
import os

class Config:
    parser = ConfigParser()

    def salvar_arquivo_cfg():
        Config.parser.write(open("configuracao.cfg", "w"))

    def ler_arquivo_cfg():
        if not os.path.exists("configuracao.cfg"):
            Config.salvar_arquivo_cfg()

        return Config.parser.read("configuracao.cfg")
    
    def retorna_preferenciais_de_busca():
        """
            retorna os dados que estão nas variaveis do CFG
        """

        Config.ler_arquivo_cfg()

        if not Config.parser.has_section("portal"):
            Config.parser.add_section("portal")
            Config.parser.set("portal", "url", "")

        try:
            return {
                "portal" : Config.parser.get("portal", "url"),
                "url" : Config.parser.get("portal", "nome"),
                "vaga": Config.parser.get("portal", "vaga"),
            }

        except:
            print("impossivel de retornar os dados")