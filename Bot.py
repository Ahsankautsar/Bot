import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def Cara_mengatasi_sampah_di_lingkungan(ctx, count_heh = 5):
    await ctx.send('''
1.Memisahkan Sampah 
2.Mengolah Sampah Organik 
3.Mengolah Sampah Anorganik 
4.Mengolah Sampah Berbahaya 
5.Mengolah Sampah Elektronik 
                   ''')
    
@bot.command()
async def Cara_pengelolaan_polusi_udara(ctx, count_heh = 5):
    await ctx.send('''
1.Promosikan Angkutan Umum
2.Kontrol Emisi Kendaraan
3.Ruang Hijau
4.Pengelolaan Limbah
5.Kesadaran dan Pendidikan
                   ''')
    
@bot.command()
async def Cara_melindungi_diri_dari_bahaya_polusi_udara(ctx, count_heh = 5):
    await ctx.send('''
1.Gunakan Masker Pelindung
2.Menjaga gaya hidup sehat
3.Menciptakan udara bersih dalam ruangan
4.Memantau indeks kualitas udara
                   ''')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    with open('M2L1\\Slide4.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)



bot.run("MTE1NzI2NDExMDI1ODQ5MTQwMg.GQSaBx.xJRhhHiemPuLqVrR4O9MJzu9M7TyaFZ_CLJbUg")
