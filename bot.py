from discord.ext import commands
import discord
import os
import io
import funciones
from datetime import datetime

# Para cargar variables de entorno
from dotenv import load_dotenv

load_dotenv()


# Comando para llamar al bot
bot = commands.Bot(command_prefix=',', description='Bot de discord de la UFV')


@bot.event
async def on_ready():
    print('Iniciado. Nombre: [{0.user.name}], ID: [{0.user.id}]'.format(bot))
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
    imagen_generada = funciones.imagen_dinamica.generar_imagen(ctx.author)
    with io.BytesIO() as image_binary:
        imagen_generada.save(image_binary, 'PNG')
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename='Horario.jpg'))

@bot.command()
async def fecha(ctx):
    """ Dice la fecha actual """

    currentDay = str(datetime.now().day)
    currentMonth = datetime.now().month
    currentYear = str(datetime.now().year)

    await ctx.send("Hoy es " + funciones.dia_de_la_semana() + ", día " + currentDay + " de " + funciones.mes_actual(currentMonth) + " de " + currentYear)


bot.run(os.getenv('DISCORD_TOKEN'))
