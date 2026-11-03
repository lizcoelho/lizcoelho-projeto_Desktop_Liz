
from models.cliente import Cliente
from models.pet import Pet
from models.atendente import Atendente
from models.gerente import Gerente
from models.banho import Banho
from models.tosa import Tosa
from models.consulta import Consulta
from models.agendamento import Agendamento
from models.petshop import PetShop
from models.venda import Venda
from models.dinheiro import Dinheiro
from models.pix import Pix
from models.cartao import Cartao
from models.sistema_pagamento import SistemaPagamento

# Criando cliente e pets
cliente1 = Cliente("Ana")

pet1 = Pet("Mel", "Cachorro")
pet2 = Pet("Luna", "Gato")

cliente1.adicionar_pet(pet1)
cliente1.adicionar_pet(pet2)

# Criando funcionários
atendente1 = Atendente("Maria", 2000)
gerente1 = Gerente("Carlos", 4000)

# Exibindo informações
print(cliente1)
cliente1.listar_pets()

print("\nFuncionários:")
print(atendente1)
atendente1.atender_cliente()

print(gerente1)
gerente1.gerenciar_petshop()


# Criando serviços
servicos = [
    Banho(50),
    Tosa(70),
    Consulta(120)
]

# Executando os serviços
print("\nServiços do Pet Shop:")

for servico in servicos:
    print(servico)
    servico.executar(pet1)


# Criando um agendamento
agendamento1 = Agendamento(
    cliente1,
    pet1,
    Banho,
    50,
    "10/11/2026"
)

# Testando a dependência
petshop = PetShop()

petshop.confirmar_agendamento(agendamento1, atendente1)

# Criando uma venda
venda1 = Venda(cliente1)

# Adicionando itens à venda
venda1.adicionar_item("Banho", 1, 50)
venda1.adicionar_item("Tosa", 2, 70)
venda1.adicionar_item("Ração", 1, 90)

# Exibindo a venda
venda1.exibir_venda()

# Testando o sistema de pagamento
print("\nFormas de pagamento:")

sistema = SistemaPagamento()

pagamentos = [
    Dinheiro(),
    Pix(),
    Cartao()
]

for pagamento in pagamentos:
    sistema.processar_pagamento(venda1, pagamento)
    