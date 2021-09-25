from discord import Client, Intents
from asyncio import sleep
from BOT.config import token
from BOT.rating import rating
from memory_profiler import memory_usage

guild_id = 856327254178791424

channel = {"reactions": 858274253714227200,
           "map_pool": 858026868354449468}

messages = {"map_pool": 858278776236015638}


def start(services):
    class MyClient(Client):
        def __init__(self):
            intents = Intents.default()
            intents.members = True
            intents.guilds = True
            super().__init__(intents=intents)

        async def on_ready(self):
            print("Discordo!")
            guild = client.get_guild(guild_id)
            for chan in channel:
                channel[chan] = guild.get_channel(channel[chan])
            while True:
                print(f"MiB: {memory_usage()[0]}")
                await rating(services)
                await sleep(60)

        async def on_message(self, message):
            if message.author == self.user:
                return

            if message.guild:

                if "http://" in message.content or "https://" in message.content:
                    try:
                        checkWords = ["steam", "discord", "air", "gift", "giv", "mont", "new", "end", "free"]
                        checkWordsRus = ["стим", "нитро", "разд", "месяц"]
                        checkWordsCount = 0
                        checkWordsRusCount = 0
                        for word in checkWords:
                            if word in message.content.lower():
                                checkWordsCount += 1
                        for word in checkWordsRus:
                            if word in message.content.lower():
                                checkWordsRusCount += 1
                        if checkWordsRusCount > 2:
                            await message.delete()
                            return
    
                        if checkWordsCount > 3:
                            await message.delete()
                            return
                        if checkWordsRusCount + checkWordsCount > 4:
                            await message.delete()
                            return
                        
                    except:
                        return

                if message.channel == channel["reactions"]:
                    await message.add_reaction(":upp:858281420820840458")
                    await message.add_reaction(":down:858281431108288542")

                if message.content.startswith("*add") and message.channel == channel["map_pool"]:
                    new_map = message.content[5:]
                    mes = await channel["map_pool"].fetch_message(messages["map_pool"])
                    await mes.edit(content=f"{mes.content}\n{new_map}")
                    await message.add_reaction(":TickYes:858281449677520927")

                if message.content.startswith("*rem") and message.channel == channel["map_pool"]:
                    del_map = message.content[5:]
                    mes = await channel["map_pool"].fetch_message(messages["map_pool"])
                    await mes.edit(content=mes.content.replace(f"\n{del_map}", ""))
                    await message.add_reaction(":TickYes:858281449677520927")

    client = MyClient()
    client.run(token["bot"])
