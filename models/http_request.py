import requests

class HttpRequest:

    def __init__(self):
        self.session: requests.Session = requests.Session()
        self.requisicao = requests.Request = None
        self.resposta: requests.Response = None

    def abrir_requisicao(self, link: str, method: str = "GET", param = None, data = None, json = None, headers = None, files = None):
        """Abre a requisição com o link e os parâmetros fornecidos."""

        self.requisicao = requests.Request(
            method, 
            link, 
            params=param, 
            data=data, 
            json=json, 
            headers=headers,
            files=files
        )

    def enviar_requisicao(self, permitir_redirecionamento = True, stren_de_dados = False, cert=None, **kwargs):
        """Envia a requisição."""

        if not hasattr(self, "session"):
            self.session = requests.Session()

        requisicao_final = self.session.prepare_request(self.requisicao)

        self.resposta = self.session.send(
            requisicao_final,
            allow_redirects=permitir_redirecionamento, 
            stream=stren_de_dados,
            cert=cert,
            verify=False,
            **kwargs
        )