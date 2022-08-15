from cpf import Documento, DocCpf, DocCnpj

# dados para testes
cpf1 = 12345678900
obj_cpf1 = DocCpf(cpf1)
print(obj_cpf1)
print(obj_cpf1.doc_formatado())

# cpf2 = 123456789
# obj_cpf2 = DocCpf(cpf2)
# print(obj_cpf2)
# print(obj_cpf2.doc_formatado())

doc = 12345678912
obj_doc = Documento.criar_novo(doc)
print(obj_doc.doc_formatado())

doc = 123456789
obj_doc = Documento.criar_novo(doc)
