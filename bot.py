# M2L2
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def cevre_kirliligi(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def hesapla(ctx, cevre: str, adet: int):
    token = 0
    cevre = cevre.lower() 
    if cevre == "cam":
        token = 15 if adet >= 2 else 10
    elif cevre == "plastik":
        token = 5 if adet >= 2 else 2
    elif cevre == "kağıt":
        token = 3 if adet >= 2 else 1
    
    if token > 0:
        await ctx.send(f"Kazandığın token: {token}")
    else:
        await ctx.send("Lütfen geçerli bir tür girin (cam, plastik, kağıt).")
        
bot.run("w")
