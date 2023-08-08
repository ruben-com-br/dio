# --- funcoes

def req(msg):
  if msg == "menu":
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuario
    [lu] Listar Usuarios
    [nc] Nova Conta
    [lc] Listar Contas
    [q] Sair

    => """
    return input(menu)
  elif msg == "valor_deposito":
    return  float(input("Informe o valor do depósito: "))
  elif msg == "valor_saque":
    return  float(input("Informe o valor do saque: "))
  elif msg == "cpf":
    return input("Informe o CPF do usuário: ")
  elif msg == "nome":
    return input("Informe o nome completo: ")
  elif msg == "data_nascimento":
    return input("Informe a data de nascimento (dd-mm-aaaa): ")
  elif msg == "endereco":
    return input("Informe o endereço( logradouro - numero - bairro - cidade/sigral estado: ")
  
  else:
    print("Opção de REQ não encontrada: "+msg)

def res(msg,saldo=0,extrato=0):
  if msg == "valor_invalido":
    print("Operação falhou! O Valor informado é invalido.")
  elif msg == "falha_excedeu_saldo":
    print("Operação falhou! Você não tem saldo suficiente")
  elif msg == "falha_excedeu_limite":
    print("Operação falhou! O valor do saque excede o limite.")
  elif msg == "falha_excedeu_saques":
    print("Operação falhou! Número máximo de saques excedidos.")
  elif msg == "falha_valor_saque_invalido":
    print("Operação falhou! O Valor informado é inválido.")
  elif msg == "extrato":
    print("\n================EXTRATO=================")
    print("Não foram realizadas movimentações." if not extrato else extrato)  
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===========================================")
  elif msg == "opcao_invalida":
    print("Operação invalida, por favor selecione novamente a operacao desejada.")
  elif msg == "sair":
    print("Saindo. Programa sendo Encerrado!")
  elif msg == "conta_criada":
    print(" Contra criada com sucesso!")
  elif msg == "usuario_ja_cadastrado":
    print("Usuário já cadastrado")
  elif msg == "usuario_criado":
    print("Usuário Criado com sucesso!")
  elif msg == "usuario_inexistente":
    print(f"usuario {saldo} inexistente")
  elif msg == "listar_usuarios":
    usuarios = saldo
    for usuario in usuarios:
      print(usuario)
  elif msg == "listar_contas":
    contas = saldo
    for conta in contas:
      print(conta)
  else:
    print("Opção de RES não encontrada: "+msg)

def deposito(saldo,extrato):
  valor = req("valor_deposito")
  if validar_deposito_valor(valor):
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
  return saldo, extrato

def validar_deposito_valor(valor):
  if valor > 0:
    return True
  else:
    res("valor_invalido")
    return False

def filtrar_usuarios(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_usuario(usuarios):
  cpf = req("cpf")
  
  if validar_usuario_cadastrado(cpf,usuarios):
    nome = req("nome")
    data_nascimento = req("data_nascimento")
    endereco = req("endereco")
    usuarios.append({"nome":nome,"data_nascimento":data_nascimento,"cpf": cpf,"endereco": endereco})
    res("usuario_criado")

  return usuarios

def validar_usuario_cadastrado(cpf,usuarios):
  if filtrar_usuarios(cpf,usuarios) == None:
    return True
  
  res("usuario_ja_cadastrado")
  return False

def criar_conta(usuarios,contas,agencia,numero_conta):
  cpf = req("cpf")
  if validar_usuario_existente(cpf,usuarios):
    contas.append({"agencia":agencia,"numero_conta":numero_conta,"usuario":cpf})
    numero_conta += 1
    res("conta_criada")
  return contas,numero_conta

def validar_usuario_existente(cpf,usuarios):
  if filtrar_usuarios(cpf,usuarios) == None:
    res("usuario_inexistente",cpf)
    return False
  
  return True

def saque(saldo,extrato,numero_saques,LIMITE_SAQUES,limite):
  valor = req("valor_saque")
  
  if validar_saque(valor,saldo,numero_saques,LIMITE_SAQUES,limite):
    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    numero_saques += 1

  return saldo, extrato, numero_saques

def validar_saque(valor,saldo,numero_saques,LIMITE_SAQUES,limite):
  excedeu_saldo = valor>saldo
  excedeu_limite = valor> limite
  excedeu_saques = numero_saques >= LIMITE_SAQUES
  valor_saque_invalido = valor <=0
  
  if excedeu_saldo:
    res("falha_excedeu_saldo")
  elif excedeu_limite:
    res("falha_excedeu_limite")
  elif excedeu_saques:
    res("falha_excedeu_saques")
  elif valor_saque_invalido:
    res("valor_invalido")
  else:
    return True
  return False

def main():
  saldo = 0
  limite = 500
  extrato = ""
  numero_saques = 0
  LIMITE_SAQUES = 3
  AGENCIA = "0001"
  usuarios = []
  contas = []
  numero_conta = 1

  while True:
    opcao = req("menu")

    if opcao == "d":
      saldo, extrato = deposito(saldo, extrato) 
    elif opcao == "s":
      saldo, extrato, numero_saques = saque(saldo,extrato,numero_saques,LIMITE_SAQUES,limite)     
    elif opcao == "e":
      res("extrato")
    elif opcao == "nc":
      contas,numero_conta = criar_conta(usuarios,contas,AGENCIA,numero_conta)
    elif opcao == "nu":
      usuarios = criar_usuario(usuarios)
    elif opcao == "lu":
      res("listar_usuarios",usuarios)
    elif opcao == "lc":
      res("listar_contas",contas)
    elif opcao == "s":
      res("sair")
      break
    else:
      res("opcao_invalida")
      
# --- Principal ----  
main()