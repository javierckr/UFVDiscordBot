import discord
import os
import funciones
# Para cargar variables de entorno
from dotenv import load_dotenv

load_dotenv()


client = discord.Client()

# Comando para llamar al bot
cmd = ','


@client.event
async def on_ready():
    print('Iniciado con cuenta: {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(cmd + 'buses'):
        await message.channel.send('--- Los horarios de los buses son: --- \n1234')
    elif message.content.startswith(cmd + 'dia'):
        await message.channel.send(funciones.dia_semana.dia_de_la_semana())
    elif message.content.startswith(cmd + 'tareas'):
        await message.channel.send(funciones.googlecal.main())

client.run(os.getenv('DISCORD_TOKEN'))
