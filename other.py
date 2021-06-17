import discord
import os
import random

client = discord.Client()


def roll_die(sides=6):
    return random.randint(1, sides)


def roll_d4():
    return roll_die(4)


def roll_d6():
    return roll_die(6)


def roll_d8():
    return roll_die(8)


def roll_d10():
    return roll_die(10)


def roll_d12():
    return roll_die(12)


def roll_d20():
    return roll_die(20)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    responses = {
        '69': 'Nice',
        'del': 'https://compote.slate.com/images/e8c8b102-a841-42dc-b4cd-1bc74276b3dd.jpg',
        'fireball': 'FIREBALLL: {} Fire damage'.format(roll_d6() * 8),
        'get your shit together': 'https://www.youtube.com/watch?v=-tGL-buZ94Y',
        'lou': 'LOU: *Cape billows furiously*',
        'no one gives a fuck': 'https://www.youtube.com/watch?v=xX3JgSJ-dN0',
        'roscoe': 'ROSCOE: *Cape billows even more furiously*',
    }

    lower_case_message = message.content.lower()

    for response in responses.keys():
        if response in lower_case_message:
            await message.channel.send(responses[response])


client.run(os.getenv('TOKEN'))