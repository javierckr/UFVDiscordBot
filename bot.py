import discord
import os
from dia_semana import dia_de_la_semana
# Para cargar variables de entorno
from dotenv import load_dotenv

load_dotenv()


client = discord.Client()


@client.event
async def on_ready():
    print('Iniciado con cuenta: {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(',buses'):
        await message.channel.send('--- Los horarios de los buses son: --- \n1234')
    elif message.content.startswith(',dia'):
        await message.channel.send(dia_de_la_semana())

client.run(os.getenv('DISCORD_TOKEN'))
