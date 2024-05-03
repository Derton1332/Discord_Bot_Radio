import discord
from discord.ext import commands
import nacl


# Создаем объект Intents с нужными намерениями
intents = discord.Intents.default()
intents.messages = True  # Для чтения сообщений
intents.message_content = True  # Важно для обработки содержания сообщений
intents.guilds = True
intents.voice_states = True

# Создаем экземпляр бота с указанными намерениями
bot = commands.Bot(command_prefix='%', intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user.name} успешно запущен и готов к работе!')

@bot.command()
async def play(ctx, url: str = None):
    if url is None:
        await ctx.send("Пожалуйста, укажите URL радиостанции. Например: %play <URL>")
        return

    if ctx.author.voice is None:
        await ctx.send("Подключитесь к голосовому каналу!")
        return

    channel = ctx.author.voice.channel
    try:
        voice_client = await channel.connect()
    except discord.ClientException:
        voice_client = ctx.voice_client

    if voice_client.is_playing():
        voice_client.stop()

    ffmpeg_executable_path = 'C:\\YOURPATH\\discord bot\\bin\\ffmpeg.exe'
    voice_client.play(discord.FFmpegPCMAudio(url, executable=ffmpeg_executable_path), after=lambda e: print('Player error: %s' % e) if e else None)
    await ctx.send(f"Сейчас играет: {url}")


@bot.command()
async def stop(ctx):
    voice_client = ctx.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
        await ctx.send("Радио остановлено.")

# Вставьте токен вашего бота здесь
bot.run('BOT TOKEN')






