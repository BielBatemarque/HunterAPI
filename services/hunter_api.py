from models.http_request import HttpRequest
from models.job import Job

class HunterApi(HttpRequest):


    def __init__(self):
        super().__init__()
        self.base_utl = "http://localhost"
        
    def enviar_job(self, job: Job) -> str:
        headers = {
            "Content-Type": "application/json"
        }

        self.abrir_requisicao(link=self.base_utl, headers=headers, json=job.__dict__)
        self.enviar_requisicao()

        if self.resposta.status_code >= 200 and self.resposta.status_code < 400:
            pass

        

