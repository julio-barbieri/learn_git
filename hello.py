def Pessoa(nome):
    return f"Bem-vindo {nome}"

def Carro(marca, modelo, ano):
    return f"Você dirige um {marca} {modelo} ano {ano} cor chumbo"


def CalculaMedia(km, litros):
    return f"Seu veículo faz em média {km / litros} quilometros por litro"

print(Pessoa("Julio"))
print(Carro("Fiat", "Argo", "2021"))
print(CalculaMedia(500, 45))
