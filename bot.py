import discord
import os
import dia_semana


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
        await message.channel.send(dia_semana())


client.run(os.getenv('DISCORD_TOKEN'))
