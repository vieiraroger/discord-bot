import discord

client = discord.Client()

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
async def on_menber_join(menber):
    channel = client.get_channel("791756036322361354")
    await channel.send("bom dia" + menber.mention)



client.run("SEU TOKEN")