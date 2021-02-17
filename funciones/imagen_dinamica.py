import funciones
import time
from PIL import Image, ImageDraw, ImageFont

def generar_imagen(author):

    base = Image.open("./recursos/images/mountains.jpg").convert("RGBA")
    txt = Image.new("RGBA", base.size, (255,255,255,0))

    fnt1 = ImageFont.truetype("./recursos/fonts/UbuntuMono-Regular.ttf", 44)
    fnt2 = ImageFont.truetype("./recursos/fonts/digital-7.ttf", 330)
    fnt3 = ImageFont.truetype("./recursos/fonts/OpenSans-Regular.ttf", 100)
    fnt4 = ImageFont.truetype("./recursos/fonts/OpenSans-Light.ttf", 40)

    d = ImageDraw.Draw(txt)

    current_time = time.strftime('%H:%M:%S')
    horario_actual = funciones.get_horario()
    dia_semana_actual = funciones.dia_de_la_semana()

    w1, h1 = d.textsize(horario_actual, font=fnt1)
    w2, h2 = d.textsize(current_time, font=fnt2)
    w3, h3 = d.textsize(dia_semana_actual, font=fnt3)

    wi = 1920

    d.text(((wi-w1)/2,700), horario_actual, font=fnt1, fill=(255,255,255,255))
    d.text(((wi-w2)/2,260), current_time, font=fnt2, fill=(255,255,255,255)) 
    d.text(((wi-w3)/2,539), dia_semana_actual, font=fnt3, fill=(255,255,255,255))

    clase = "No establecido"
    for role in author.roles:
        first_char = str(role)[0]
        if first_char.isdigit():
            clase = str(role)

    d.text((20,20), "Pedido por: \n" + author.name + "#" + str(author.discriminator) + " (" + clase + ")", font=fnt4, fill=(255,255,255,255))    

    return(Image.alpha_composite(base, txt))