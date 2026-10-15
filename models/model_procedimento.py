from models.model_pessoa_profissional_saude import ProfissionalSaude

class Procedimento:
    def __init__(self, id: int, descricao: str, custo: float, profissional: ProfissionalSaude):
        self.__id = id
        self.__descricao = descricao
        self.__custo = custo
        self.__profissional = profissional
        
    @property
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, id):
        if id is not None and not isinstance(id, int):
            raise TypeError("O ID deve ser inteiro.")
        self.__id = id
    
    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str) -> None:
        self.__descricao = descricao
        
    @property
    def custo(self) -> float:
        return self.__custo

    @custo.setter
    def custo(self, custo: float) -> None:
        self.__custo = custo
        
    @property
    def profissional(self) -> ProfissionalSaude:
        return self.__profissional
    
    @profissional.setter
    def profissional(self, profissional: ProfissionalSaude):
        self.__profissional = profissional
        
    def mostrar_detalhes(self) -> str:
        return f'ID: {self.__id}\nDescrição: {self.__descricao}\nCusto: {self.__custo}\nProfissional Responsável: {self.__profissional.nome}'
    
    def validar_custo(self) -> bool:
        if self.__custo > 0:
            return True
        else:
            return False
