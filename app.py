import qrcode  # Baixando a Biblioteca

url = 'https://flexalugueis.herokuapp.com/' # Colocar o item

# Criando a o obejto
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5)

qr.add_data(url)
qr.make(fit=True)

# Criando a imagem
img = qr.make_image(fill='black', black_color='white')

img.show()
