import discord


async def embed_maker(name=None, description=None, field_data=None, inline=False, thumbnail=None, color=discord.Color.black(), bot=None):
    if not bot:
        return
    embed = discord.Embed(
        title=f"{name}", description=description, color=color)
    for index, value in enumerate(field_data):
        embed.add_field(name=field_data[index][0], value=field_data[index][1], inline=inline)
    if thumbnail:
        embed.set_thumbnail(url=thumbnail)
    return  embed
