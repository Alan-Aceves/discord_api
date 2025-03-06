import discord                 #   Libreria para conectar con Discord
from discord.ext import commands
from dotenv import load_dotenv #   Libreria para cargar variables de entorno
import os                      #   Libreria para mandar comandos de sistema
import requests                #   Libreria para mandar comandos de sistema
import time

load_dotenv()

token = os.getenv('token')

if token is None:
    raise ValueError("Token not load right.")
else:
    print("Token load with success "+ token)


intents = discord.Intents.all()
intents.messages = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def info (ctx):
    await ctx.send(' 🌟¡Bienvenidos a la tribu de ARK! Soy HLN-A y estaré aquí para guiarte en tu increíble viaje a través de este vasto y desafiante mundo.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'hola' in message.content.lower():
        await message.channel.send( f'¡Hola {message.author.name}!' )
    
    await bot.process_commands(message)


bot.run(token)


async def test (): 
    return False

async def test_1 (): 
    return False  

#hola