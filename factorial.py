n1 = int(input("Escolhe um número para calcular o seu fatorial: "))

n2 = (n1 - 1)

conta = n1 * n2

n1 = n2

while n1 > 1:

    n2 = (n1 - 1)

    conta = conta * n2

    n1 = n2

print (conta)

input()
