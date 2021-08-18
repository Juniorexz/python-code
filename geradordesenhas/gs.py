import random
import string

tamanho = int(input('Digite o tamanho de senha que deseja:')) #tamanho de quantidade de caracteres

chars = string.ascii_letters + string.digits + 'ç!@#$%&*()-=+,.;/?' #envolve letras maiusculas e minusculas


rnd = random.SystemRandom() #os.urandom(biblioteca que usa nummeros aleatorios)

print(''.join(rnd.choice(chars) for i in range(tamanho)))