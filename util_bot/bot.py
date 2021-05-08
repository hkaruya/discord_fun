from datetime import datetime as time
from discord.ext import commands
import random as rand
import os

bot = commands.Bot(command_prefix='!', case_insensitive=True)

@bot.event
async def on_ready():
    print ('Logged in -> {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.name == 'bot-haven':
        if message.content.lower() == 'hello':
            await message.channel.send('world!')
        if 'flip a coin' in message.content:
            rand.seed(time.now())
            coin = rand.randint(0,1)
            if 0 == coin:
                await message.channel.send('heads!')
            else:
                await message.channel.send('tails!')

    await bot.process_commands(message)


@bot.command()
async def echo(ctx, msg):
    await ctx.send(msg)

from discord.ext import commands
@bot.command(name='quit', help='((hopefully)) shuts down bot')
@commands.has_role('SuperAdmin')
async def shutdown(ctx):
    if 'bot-haven' == ctx.message.channel.name:
        await ctx.send('aite bro damn!')
        await bot.close()
        print ('Logging out {0.user}'.format(bot))

bot.run(os.getenv('TOKEN'))
#print(os.getenv('TOKEN'))
