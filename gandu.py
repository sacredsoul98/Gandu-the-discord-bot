import discord
import os
from dotenv import load_dotenv

#credentials- token discord
load_dotenv('.env')

client= discord.Client()

@client.event
async def on_ready():
    print('We have logged in!'.format(client))


@client.event
async def on_message(message):
    if message.author ==client.user:
        return
    
    if message.content.startswith('/hello'):
        await message.channel.send('Hello gandu!')


#this line will run the token when it is given directly to it. which is not possible to do so when hosting on repl.it as we have to store these in a '.env' file which has all the secret keys and tokens
client.run(os.getenv('TOKEN'))


