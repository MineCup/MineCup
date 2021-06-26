from discord import Client, Intents
from config import token, channel, guild_id, messages


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

    async def on_message(self, message):
        if message.author == self.user:
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
