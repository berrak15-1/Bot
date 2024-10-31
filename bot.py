
import discord
from discord.ext import commands
import os 
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
@bot.command()
async def rastgele(ctx):
    ImageName=random.choice(os.listdir(r"C:\Users\MELEK\kodland\images"))
    with open(f"images\{ImageName}","rb") as f:
        Resim=discord.File(f)
    await ctx.send(file=Resim)

@bot.command()
async def animal(ctx):
    AnimalImageName=random.choice(os.listdir(r"C:\Users\MELEK\kodland\cartoon_images"))
    with open(f"animal_images\{AnimalImageName}","rb") as f:
        Resim=discord.File(f)
    await ctx.send(file=Resim)

@bot.command()
async def copy(ctx, arg, c = 1):
    await ctx.send(arg * c)

@bot.command()
async def topla(ctx, a: int, b: int):
    await ctx.send(a + b)
@bot.command()
async def çıkar(ctx, a: int, b: int):
    await ctx.send(a - b)
@bot.command()
async def çarp(ctx, a: int, b: int):
    await ctx.send(a * b)
@bot.command()
async def böl(ctx, a: int, b: int):
    await ctx.send(a / b)


@bot.command()
async def çevre(ctx):
    cozumler = ['geri dönüşüme önem vermelisiniz', 'tek kullanımlık ürünleri kullanmaktan kaçınmalısınız',
                'naylon poşetler yerine bez çanta kullanmalısınız', 'pet şişe yerine matara kullanmalısınız',
                'kağıt vb. şeyleri tasarruflu kullanmalısınız']
    oneri = random.choice(cozumler)
    await ctx.send(oneri)
@bot.command()
async def ayrıştırma_kıyafetler(ctx):
    bilgi = "Kıyafet ve giysilerinizi geri dönüşüm kutularına atmalısınız onlar orada toplanır ve tesislere gönderilir."
    await ctx.send(bilgi)
@bot.command()
async def ayrıştırma_elektronik(ctx):
    bilgi2 = "Onları elektronik atık toplama merkezlerine götürmelisiniz."
    await ctx.send(bilgi2)






