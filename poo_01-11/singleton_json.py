import json

class ConfigManager:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(ConfigManager, cls).__new__(cls, *args, **kwargs)
            cls.__instance.dicionario = {}
        return cls.__instance

    def carregar_configuracao(self):
        try:
            with open("poo_01-11/config_arq.json", "r", encoding="utf-8") as f:
                self.dicionario = json.load(f)
                print("Configurações carregadas:", self.dicionario)
        except FileNotFoundError:
            print("Arquivo não encontrado. Criando um novo arquivo")
            self.dicionario = {"Teste": "Configuração padrão"}
            self.salvar_configuracao()

    def salvar_configuracao(self):
        with open("poo_01-11/config_arq.json", "w", encoding="utf-8") as f:
            json.dump(self.dicionario, f, indent=4)
            print("Configurações salvas no arquivo.")

config = ConfigManager()
config.carregar_configuracao()

config.dicionario["Tema"] = "claro"

print(config.dicionario["Tema"])

config.dicionario["Conexão"] = "1"

print(config.dicionario["Conexão"])

config.salvar_configuracao()