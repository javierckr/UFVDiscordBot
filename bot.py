from discord.ext import commands
import discord
import os
import io
import funciones
from PIL import Image, ImageDraw, ImageFont
import time

# Para cargar variables de entorno
from dotenv import load_dotenv

load_dotenv()


# Comando para llamar al bot
bot = commands.Bot(command_prefix=',', description='Bot de discord de la UFV')


@bot.event
async def on_ready():
    print('Iniciado. Nombre: [{0.user.name}], ID: [{0.user.id}]'.format(bot))
    print(funciones.chiste.main())
    await bot.change_presence(activity=discord.Streaming(name="Matemáticas para la ingeniería", url="https://linux.org/"))


@bot.command()
async def ping(ctx):
    """ Comando para hacer ping al bot """
    await ctx.send('pong')


@bot.command()
async def buses(ctx):
    """ Comando que dice el horario de los buses """
    await ctx.send('-- Los horarios del bus 659 son: a--\n 8:44 am ')


@bot.command()
async def dia(ctx):
    """ Comando que dice las asignaturas del día """
    await ctx.send(funciones.dia_semana.dia_de_la_semana())


@bot.command()
async def tareas(ctx):
    """ Comando que te muestra las 10 siguientes tareas del calendario de las universidad """
    await ctx.send("```\n"+funciones.googlecal.main(1)+"```")


@bot.command()
async def examenes(ctx):
    """ Comando que te muestra los 10 siguientes exámenes o entregas importantes"""
    await ctx.send("```\n"+funciones.googlecal.main(0)+"```")


@bot.command()
async def enlaces(ctx):
    """ Comando para ver las url de interés """
    await ctx.send("Canvas: https://ufv-es.instructure.com/login/canvas\n"
                   "Portal Universitario: https://ssofv.ufv.es/public_oam_ufv_ufv/oam/login.jsp\n"
                   "Página principal: https://www.ufv.es/")

@bot.command()
async def horario(ctx):
    """ Genera horario actual """

    # argumentos temporales!!
    base = Image.open("./recursos/images/mountains.jpg").convert("RGBA")
    
    txt = Image.new("RGBA", base.size, (255,255,255,0))

    fnt1 = ImageFont.truetype("./recursos/fonts/UbuntuMono-Regular.ttf", 44)
    fnt2 = ImageFont.truetype("./recursos/fonts/digital-7.ttf", 330)
    fnt3 = ImageFont.truetype("./recursos/fonts/OpenSans-Regular.ttf", 100)
    fnt4 = ImageFont.truetype("./recursos/fonts/OpenSans-Light.ttf", 40)

    # get a drawing context
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
    for role in ctx.author.roles:
        first_char = str(role)[0]
        if first_char.isdigit():
            clase = str(role)

    d.text((20,20), "Pedido por: \n" + ctx.author.name + "#" + str(ctx.author.discriminator) + " (" + clase + ")", font=fnt4, fill=(255,255,255,255))    

    out = Image.alpha_composite(base, txt)

    with io.BytesIO() as image_binary:
        out.save(image_binary, 'PNG')
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename='Horario.jpg'))


if "1".isdigit():
    print("si")
bot.run(os.getenv('DISCORD_TOKEN'))

