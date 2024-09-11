#Exemplificação de um app Bancario utilizando conhecimentos como comando While,If,print e input

#Declarando as Variaveis op(operacao) e senha
op=""
senha=2018

#O comando While aparece aqui pra que a mensagem se repita até que o usuario insira o numero 0 ,
#Ou seja ,assim que a variavel op for igual a zero,o sistema se encerra 
#Utiliza se o If pra que assim que o Usuario aperte uma opçao receba uma mensagem correspondente
while op != 0:
  op=int(input("[0]Sair /n [1]saque /n[2]extrato /n: "))

  if op==1:
     saque=int(input("[1]deseja prosseguir?SIM! /n [0]NAO,Cancelar /n:"))
     if saque==1:
       senha=int(input("insira sua senha de 4 digitos:"))
       if senha==2018:
          print("saque sendo efetuado...")
          print("concluido com sucesso")
       else:
          print("senha invalida,nao podemos prosseguir ") 

   

#Como algo normal em app bancario,a variavel senha fica guardada no sistema pra que quando inserida(caso seja Verdadeira) possibilite 
#o usuario acessar seus dados com segurança        
  elif op==2:
     senha=int(input("insira sua senha de 4 digitos:"))
     if senha==2018:
          print("extrato emitido com sucesso")
     else:
          print("senha invalida,tente novamente mais tarde ") 
  
  else :
         print("saindo da plataforma")
