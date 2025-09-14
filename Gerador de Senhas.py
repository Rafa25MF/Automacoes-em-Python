import string as st
import numpy as np

for rafa in range(0, 10):
    print('-=' * 22)
    print('             GERADOR DE SENHAS')
    print('-=' * 22)
    letras = st.ascii_letters
    numeros = st.digits
    especial = st.punctuation
    algarismos = (letras + numeros)

    senha = np.random.choice(list(algarismos),6)
    senha1 = np.random.choice(list(algarismos),8)
    senha2 = np.random.choice(list(algarismos),10)
    senha3 = np.random.choice(list(algarismos), 12)
    senha4 = np.random.choice(list(algarismos), 14)

    print('Escolha uma SENHA para poder gerar:')
    res = int(input('Senha de quandos digitos 6, 8, 10, 12 ou 14? '))

    if res == 6:
        print(''.join(senha))
    elif res == 8:
        print(''.join(senha1))
    elif res == 10:
        print(''.join(senha2))
    elif res == 12:
        print(''.join(senha3))
    elif res == 14:
        print(''.join(senha4))