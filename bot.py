import asyncio
import os
import random

import discord
import discord_emojis
from discord.ext import commands
from dotenv import load_dotenv

from get_fact import get_fact
from get_insult import get_insult

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.emojis = True
intents.guilds = True
intents.dm_messages = True
intents.guild_messages = True
intents.guild_reactions = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


async def get_fact_from_api(channel_id: int):
    while True:
        channel = bot.get_channel(channel_id)
        if channel:
            fact = await get_fact()
            if fact is None:
                print("Ошибка получения факта")
                await asyncio.sleep(5)
            else:
                await channel.send(fact)
            delay = random.uniform(900, 2700)
            print(f"{delay=}")
            await asyncio.sleep(delay)
        else:
            print("Похоже меня кикнули :(")
            await asyncio.sleep(5)


@bot.event
async def on_message(message):
    if message.author == bot.user or not (message.channel.id in [556628665840959498, 1478624689780822017]):
        return None
    emojis = list(discord_emojis.EMOJIS)
    reactions_cnt = random.randint(1, 5)
    reactions = random.sample(emojis, reactions_cnt)
    for reaction in reactions:
        await message.add_reaction(reaction)
    insult = await get_insult()
    await message.reply(insult)
    return None


@bot.event
async def on_ready():
    channel_id = 556628665840959498
    channel_id_zao = 1478624689780822017
    bot.loop.create_task(get_fact_from_api(channel_id))
    bot.loop.create_task(get_fact_from_api(channel_id_zao))


bot.run(os.getenv("TOKEN"))
