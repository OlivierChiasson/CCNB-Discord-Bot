import discord
from discord import client, RawReactionActionEvent, Intents
from discord.ext.commands import Bot

client = Bot(command_prefix='$', intents=Intents.all())
TOKEN = 'PUT TOKEN HERE'


emojiA = '\N{NEGATIVE SQUARED LATIN CAPITAL LETTER A}'
emojiB = '\N{NEGATIVE SQUARED LATIN CAPITAL LETTER B}'
emojiC = '\N{REGIONAL INDICATOR SYMBOL LETTER C}'
emojiD = '\N{REGIONAL INDICATOR SYMBOL LETTER D}'
emojiCheck = '\N{WHITE HEAVY CHECK MARK}'
emojiX = '\N{CROSS MARK}'
emojiHandsUp = '\N{RAISED HAND WITH FINGERS SPLAYED}'


@client.event
async def on_ready():
    print(f'Bot connected as {client.user}')

@client.event
async def on_message(message):
    if message.author.guild_permissions.administrator:
        if message.content == '*abc':
            await message.delete()
            embed=discord.Embed(title="A / B / C", description="Veuillez sélectionner une ou plusieurs options avec les réactions ci-dessous", color=0x00ff00)
            msg = await message.channel.send(embed=embed)
            await msg.add_reaction(emojiA)
            await msg.add_reaction(emojiB)
            await msg.add_reaction(emojiC)


        if message.content == '*abcd':
            await message.delete()
            embed=discord.Embed(title="A / B / C / D", description="Veuillez sélectionner une ou plusieurs options avec les réactions ci-dessous", color=0x00ff00)
            msg = await message.channel.send(embed=embed)
            await msg.add_reaction(emojiA)
            await msg.add_reaction(emojiB)
            await msg.add_reaction(emojiC)
            await msg.add_reaction(emojiD)


        if message.content == '*question':
            await message.delete()
            embed = discord.Embed(title="Avez-vous des questions?",
                                  description="Veuillez sélectionner une des options avec les réactions ci-dessous", color=0x00ff00)
            msg = await message.channel.send(embed=embed)

            await msg.add_reaction(emojiCheck)
            await msg.add_reaction(emojiX)


        if message.content == '*vraifaux':
            await message.delete()
            embed = discord.Embed(title="Vrai ou Faux?",
                                  description="Veuillez sélectionner une des options avec les réactions ci-dessous", color=0x00ff00)
            msg = await message.channel.send(embed=embed)

            await msg.add_reaction(emojiCheck)
            await msg.add_reaction(emojiX)

        if message.content == '*main':
            await message.delete()
            embed = discord.Embed(title="Vous avez une question?",
                                  description="Appuyer sur la réaction ci-dessous pour lever votre main", color=0x00ff00)
            msg = await message.channel.send(embed=embed)

            await msg.add_reaction(emojiHandsUp)


@client.event
async def on_raw_reaction_add(RawReactionActionEvent):
    botID = str(client.user.id)
    guild_id = RawReactionActionEvent.guild_id
    guild = client.get_guild(guild_id)
    member = guild.get_member(RawReactionActionEvent.user_id)

    if str(RawReactionActionEvent.emoji) == '🖐':
        if str(member.id) != botID:
            if member.nick is not None:
                if emojiHandsUp not in member.nick:
                    await member.edit(nick="!"+emojiHandsUp+" "+member.nick)

                else:
                    return
            else:
                await member.edit(nick="!"+emojiHandsUp+""+member.name)
        else:
            return
    else:
        return


@client.event
async def on_raw_reaction_remove(RawReactionActionEvent):
    guild_id = RawReactionActionEvent.guild_id
    guild = client.get_guild(guild_id)
    member = guild.get_member(RawReactionActionEvent.user_id)
    if str(RawReactionActionEvent.emoji) == '🖐':
        if member.nick is not None:
            if emojiHandsUp in member.nick:
                removedEmojiName = member.nick.replace("!"+emojiHandsUp, "")
                await member.edit(nick=removedEmojiName)
            else:
                return
        else:
            return
    else:
        return


@client.event
async def on_raw_reaction_clear(RawReactionActionEvent):
    channel = client.get_channel(RawReactionActionEvent.channel_id)

    print("working")
    message = await channel.fetch_message(RawReactionActionEvent.message_id)
    embed = message.embeds[0]
    print(embed.title)
    if embed.title == "A / B / C":
        print("true")
        await message.add_reaction(emojiA)
        await message.add_reaction(emojiB)
        await message.add_reaction(emojiC)

    elif embed.title == "A / B / C / D":
        await message.add_reaction(emojiA)
        await message.add_reaction(emojiB)
        await message.add_reaction(emojiC)
        await message.add_reaction(emojiD)
    elif embed.title == "Avez-vous des questions?":
        await message.add_reaction(emojiCheck)
        await message.add_reaction(emojiX)
    elif embed.title == "Vrai ou Faux?":
        await message.add_reaction(emojiCheck)
        await message.add_reaction(emojiX)
    elif embed.title == "Vous avez une question?":
        await message.add_reaction(emojiHandsUp)
    pass
client.run(TOKEN)