import discord
from discord.ext import commands
import youtube_dl

TOKEN = ('MTA5ODU2MTk4NDY0OTIzNjUwMQ.GW98Ea.AFScV1koerez7B411deacUS00jE0dBBi_W2GXA')
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='play', name='p')
async def play(ctx, *, search):
    query = f'ytsearch:{search}'
    voice_channel = ctx.author.voice.channel

    with youtube_dl.YoutubeDL() as ydl:
        info = ydl.extract_info(query, download=False)
        url = info['entries'][0]['url']

    voice_client = await voice_channel.connect()
    player = await voice_client.create_ytdl_player(url)
    player.start()


bot.run('MTA5ODU2MTk4NDY0OTIzNjUwMQ.GW98Ea.AFScV1koerez7B411deacUS00jE0dBBi_W2GXA')
