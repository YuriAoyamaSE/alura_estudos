class Documento:
    @staticmethod
    def criar_novo(documento):
        doc_str = str(documento)
        if len(doc_str) == 11:
            return DocCpf(doc_str)
        if len(doc_str) == 14:
            return DocCnpj(doc_str)
        # if len(doc_str) == 20:
        #     return DocQualquer(doc_str)
        else:
            raise ValueError("Documento incorreto!")

class DocCpf:
    def __init__(self, documento: int) -> None:
        documento = str(documento)
        self.cpf = documento
        # if self.cpf_valido(documento):
        #    self.cpf = documento
        # else: 
        #     raise ValueError("CPF inválido: CPF possui 11 dígitos")
        
    # def cpf_valido(self, documento) -> bool:
    #     return len(documento) == 11
    
    def doc_formatado(self) -> str:
        cpf = self.cpf
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    
    def __str__(self) -> str:
        return self.cpf
    
class DocCnpj:
    def __init__(self, documento: int) -> None:
        documento = str(documento)
        self.cnpj = documento
        # if self.cnpj_valido(documento):
        #    self.cnpj = documento
        # else: 
        #     raise ValueError("cnpj inválido: cnpj possui 14 dígitos")
        
    # def doc_valido(self, documento) -> bool:
    #     return len(documento) == 14
    
    def doc_formatado(self) -> str:
        cnpj = self.cnpj
        return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
    
    def __str__(self) -> str:
        return self.cnpj