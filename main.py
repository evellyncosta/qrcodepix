
import easygui
from pixqrcodegen import Payload


msg = "Digite os dados do PIX"
title = "Gerador de QR Code do PIX"
field_names = ["Nome", "E-mail", "Valor", "Cidade", "Loja"]
field_values = easygui.multenterbox(msg, title, field_names)

if field_values is not None:
    nome, email, valor, cidade, loja = field_values
    payload = Payload(nome, email, valor, cidade, loja)
    qr_code_data = payload.gerarPayload()


    easygui.buttonbox(
        image="pixqrcodegen.png",
        msg="QR Code do PIX",
        choices=["Fechar"] # Tamanho da imagem na janela
    )



