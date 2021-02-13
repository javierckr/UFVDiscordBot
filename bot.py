from discord.ext import commands
#from discord.ext import commands
import os
import funciones
# Para cargar variables de entorno
from dotenv import load_dotenv

load_dotenv()


# Comando para llamar al bot
bot = commands.Bot(command_prefix=',')


@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def buses(ctx):
    await ctx.send('-- Los horarios del bus 659 son: a--\n 8:44 am ')


@bot.command()
async def dia(ctx):
    await ctx.send(funciones.dia_semana.dia_de_la_semana())


@bot.command()
async def tareas(ctx):
    await ctx.send(funciones.googlecal.main())

bot.run(os.getenv('DISCORD_TOKEN'))
