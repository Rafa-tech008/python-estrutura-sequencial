#EST.DEC_LT01.15
#Declaração de variáveis
cat1: int=0
cat2: int=0

#Início
cat1=int(input("Valor do cateto 1 é: "))
cat2=int(input("O valor do cateto 2 é: "))
hip=((cat1**2)+(cat2**2))
print("O valor da hipotenusa é", hip**0.5)
#Fim
