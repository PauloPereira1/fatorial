num = int(input('Digite o número: '))
fatorial = 1
for numero in range(1,num+1):
    fatorial *= numero
print ('O fatorial de', numero, 'e:', fatorial)