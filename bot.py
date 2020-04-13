import discord
from discord.ext import commands
import meme

#commands to invoke your bot from discord
client = commands.Bot(command_prefix = ('.','!'))


@client.event
async def on_ready():
    print('Bot status: online')

@client.command()
async def memes(ctx,sub='memes'):
    output = meme.get_meme(sub)
    try:
        for i in range(len(output)):
            await ctx.channel.send(file=discord.File(output[i]))
    except:
        await ctx.send('Oof something went wrong... Try changing subreddit')

client.run('DISCORD-BOT TOKEN HERE')