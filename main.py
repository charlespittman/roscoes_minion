# prereqs: pip3 install d20 discord pynacl

import json
import discord
import random
import d20

from discord.ext import commands
from random_magic_table import random_magic, surge
from wand_of_wonder import wonder

with open('secrets.json', 'r') as file:
    data = json.load(file)

TOKEN = data['token']

client = discord.Client()
bot = commands.Bot(command_prefix='/')

ATTRIBUTES = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']


@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    print(bot.guilds)
    await bot.change_presence(activity=discord.Game('with your mom.'))


@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


@bot.command()
async def horn(ctx):
    """What will eventually get this bot banned.
    Plays the DJ air horn effect.  Grants Disadvantage on Wisdom saves vs puns.

    Note: bot must already be in a voice channel."""
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('dj_horn.mp3'))
    ctx.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)


@bot.command()
async def bruh(ctx, name=None):
    """Get your shit together."""
    url = 'https://www.youtube.com/watch?v=-tGL-buZ94Y'
    await ctx.send(f'{name}, get it together. \n{url}' if name else url)


@bot.command()
async def deck(ctx):
    await ctx.send('Not implemented yet.')


@bot.command()
async def fireball(ctx, level=3):
    """Cast Fireball at base level"""
    await ctx.send(f'FIREBALL: {d20.roll("8d6")} fire damage!')


@bot.command(name='invite')
async def invite(ctx, group=None):
    """Post links to Roll20 and D&D Beyond for given group"""
    if group is None:
        await ctx.send('No group given.')
    elif group.lower() in 'hinterland':
        await ctx.send('Roll20: https://app.roll20.net/join/6181920/-9IaEw')
        await ctx.send('D&D Beyond: https://www.dndbeyond.com/campaigns/527568')
    else:
        await ctx.send("Campaign not found.")


@bot.command(name='mm')
async def magic_missile(ctx, level=1):
    if level < 1 or level > 9:
        await ctx.send("Level must be between 1 and 9.")
    else:
        rays = level + 2
        await ctx.send(f'MAGIC MISSILE: {rays} rays.')
        await ctx.send(f'{d20.roll("1d4+1 [force]")}')


@bot.command()
async def punish(ctx, other=None):
    """Ask for a random saving throw from a character
    Usage: !punish CHARACTER"""
    if not other:
        response = 'This command requires a target to punish.'
    else:
        response = f'{other}, make a {random.choice(ATTRIBUTES)} saving throw.'
    await ctx.send(response)


@bot.command(name='surge')
async def random_magic_surge(ctx, roll=None):
    """Roll on the d10000 wild magic table"""
    await ctx.send(surge(roll))


@bot.command(name='wonder')
async def wand_of_wonder(ctx, roll=None):
    """Zap the Wand of Wonder"""
    if roll:
        await ctx.send(wonder(int(roll)))
    else:
        await ctx.send(wonder(d20.roll("1d100").total))


@bot.command()
async def roll(ctx, formula=None):
    """Rolls dice
    Note: formula cannot include spaces."""
    if not formula:
        await ctx.send(d20.roll('1d20'))
    else:
        await ctx.send(d20.roll(formula))


@bot.command()
async def roll_stats(ctx):
    for attribute in ATTRIBUTES:
        await ctx.send(f'{attribute}: {d20.roll("4d6ro1kh3")}')


def eldritch_blast(rays=1, proficiency=5, mod=5, misc_bonus=0):
    ret = ['Bobby: ELDRITCH BLAST']
    for _ in range(rays):
        d20 = random.randint(1, 20)
        d10 = random.randint(1, 10)
        ret.append(
            'roll: {}+{}+{} = {}; dmg: {}+{}={}'.format(d20, proficiency, mod, sum([d20, proficiency, mod], ), d10, mod,
                                                        sum([d10, mod])))
    return '\n'.join(ret)


# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#
#     responses = {
#         'fireball': fireball(),
#         '69': 'Nice.',
#         'get your shit together': 'https://www.youtube.com/watch?v=-tGL-buZ94Y',
#         'no one gives a fuck': 'https://www.youtube.com/watch?v=xX3JgSJ-dN0',

#         '$chucks': '',
#         '$chucks20': '',
#         'march': 'https://www.youtube.com/watch?v=pwjLcwbT-xE',
#         'bobby': eldritch_blast(rays=3, proficiency=5, mod=5),
#         'lou': 'LOU: *Cape billows furiously*',
#         'roscoe': 'ROSCOE: *Cape billows even more furiously*',
#         'quotix': 'QUOTIX: I punch him in the dick.',
#         'toe': "TOE: Get in there, Lieutenant Squeakers!  Sergeant Dale, you're on deck!",
#         'sarris': 'SARRIS: Critical hit on a family member.',
#         'tpk': 'Rocks fall.  Everyone dies.',
#         'mad mage': '',
#         'dragonheist20': 'https://ddb.ac/campaigns/join/1361590763774279',
#     }
#
#     msg = message.content
#
#     lower_case_message = msg.lower()
#
#     for response in responses.keys():
#         if response in lower_case_message:
#             await message.channel.send(responses[response])


if __name__ == '__main__':
    # client.run(TOKEN)
    bot.run(TOKEN)
