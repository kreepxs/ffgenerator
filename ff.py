import random

def generate_random_code(length):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(chars) for _ in range(length))

num_codes = int(input('Quantos códigos você quer gerar? '))
for _ in range(num_codes):
    code = generate_random_code(8)
    print(f'Código gerado: {code}')

print('Siga a @eternalsleepz no instagram')
