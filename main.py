import discord

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("O BOT ESTÁ ONLINE")


@client.event
async def on_message(message):
    content = message.content.lower()
    channel = message.channel
    author = message.author.name
    mention = message.author.mention

    # Previnir erro
    if(author == "BotDeTest"):
        return

    if(content == "bom dia" and channel.name == "bom-dia"):
        await channel.send("bom dia " + mention)

    if(content == "cima"):
        await message.add_reaction("⬆")

@client.event
async def on_member_join(member):
    channel = client.get_channel(791756036322361354)
    await channel.send("bom dia" + member.mention)



client.run("SEU TOKEN")
