# Bibliotecas: 
# - pip install qrcode
# - pip install qrcode[pil]

import qrcode

cont = input('Digite o que vai ter no QR Code: ')
img = qrcode.make(cont)
type(img)
img.save("chat.png")