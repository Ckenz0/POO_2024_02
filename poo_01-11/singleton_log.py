import datetime 

class LogManager:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super(LogManager, cls).__new__(cls, *args, **kwargs)
        return cls.__instance
    
    def config(self, log_to_file, log_file):
        self.log_to_file = log_to_file
        self.log_file = log_file

    def log(self, mensagem, level="INFO"):
        timestamp = datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S")
        log_msg = f"[{timestamp}] {level}:{mensagem}"
        
        if self.log_to_file:
            try:
                with open(self.log_file, "a", encoding="utf-8") as f:
                    f.write(log_msg)
            except Exception as e:
                print(f"Erro ao abrir o arquivo {e}")
        else:
            print(log_msg)

logger = LogManager()
logger.config(log_to_file=True, log_file ="app.log")
logger.log("Log de informação\n")
logger.log("Log de warning\n", "WARNING")
logger.log("Log de erro", "ERROR")
