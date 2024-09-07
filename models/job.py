class Job:

    def __init__(self, titulo, descricao, modelo_contratacao, senioridade, site_busca):
        self.titulo: str = titulo
        self.descricao: str = descricao
        self.modelo_contratacao: str = modelo_contratacao
        self.senioridade: str = senioridade
        self.site_busca = site_busca