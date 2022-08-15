import re

# padrao = "[0-9][a-z][0-9]"
# texto = "123 1a2 1cc aa1"
# resposta = re.search(padrao, texto)
# print(resposta)
# print(resposta.group())


# padrao_email = "\w{5,50}@[a-z]{3,10}.com(.br)?"
# texto = "aaabbbcc rodrigo123@gmail.com ccbbbaaa"
# resposta = re.search(padrao_email, texto)
# print(resposta.group())


class TelefonesBr:    
    
    def __init__(self, telefone):
        self.padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número incorreto!")

    def valida_telefone(self, telefone):
        resposta = re.findall(self.padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        resposta = re.search(self.padrao,self.numero)
        numero_formatado = "+{}({}){}-{}".format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3),
            resposta.group(4)
        )
        print(numero_formatado)
        
tel = "0557921648124"
obj_tel = TelefonesBr(tel)
print(obj_tel)
print(obj_tel.format_numero())
