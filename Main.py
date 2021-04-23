# Importing discord.py to my program
import discord
from discord.ext import commands
import requests
import aiohttp
import robloxapi
import os
# Creating my client
client = commands.Bot(command_prefix=';')

# Command stuff


@client.command(name='visits')
async def gstats(ctx):
    game_universe = 1563582267
    r = requests.get(f'https://games.roblox.com/v1/games?universeIds={game_universe}')
    data = r.json()

    await ctx.send(f'St. Catharines Game Visits: **{data["data"][0]["visits"]}**')

@client.command(name='search')
async def rosearch(ctx, roblox_name: str):
    r = requests.get(f'https://api.roblox.com/users/get-by-username?username={roblox_name}')
    json = r.json()
    if not json.get('Id') or not json.get('Username'):
        await ctx.send(':x: That user was not found.')

    d = requests.get(f'https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={json["Id"]}&size=48x48&format=Png&isCircular=false')
    data = d.json()

    i = requests.get(f'https://users.roblox.com/v1/users/{json["Id"]}')
    data1 = i.json()

    embed = discord.Embed(title = roblox_name, description = f"[{roblox_name}](https://www.roblox.com/users/{json['Id']}/profile) is one of millions of users on ROBLOX, playing, creating, trading and more!", colour = discord.Colour.dark_blue())
    embed.add_field(name = f"Username", value = roblox_name)
    embed.add_field(name = "ID", value = json["Id"])
    embed.add_field(name = "Profile Link", value = f"https://www.roblox.com/users/{json['Id']}/profile", inline=False)
    embed.set_footer(icon_url=ctx.author.avatar_url, text = f"Requested by: {ctx.author}")
    embed.add_field(name = "Bio", value = data1["description"])
    embed.set_thumbnail(url = data["data"][0]["imageUrl"])
    await ctx.send(embed=embed)


@client.command(name="cmds")
async def command_help_send(context):
    helpEmbed = discord.Embed(Title="Niagara Bot Commands", description="", color=0x00ff00)
    helpEmbed.add_field(name="tban", value="Used to temporarily ban roblox users from the patrol map", inline=False)
    helpEmbed.add_field(name="pban", value="Used to permanently ban roblox users from the patrol map", inline=False)
    helpEmbed.add_field(name="manualadd", value="Used to blacklist roblox groups", inline=False)
    helpEmbed.add_field(name="search", value="Used to search users on the Roblox site", inline=False)
    helpEmbed.add_field(name="visits", value="Shows how many total visits/plays the current patrol map has", inline=False)
    helpEmbed.set_footer(text="Scripted by ReaIAbstract")
    await context.message.channel.send(embed=helpEmbed)

@client.command(name="tban")
async def create_card(context, roblox_name: str, *, reason = None):

    role = discord.utils.find(lambda r: r.name == 'Administrative Staff', context.guild.roles)

    if role in context.author.roles:

        if reason == None:
            await context.message.channel.send(":x: You must give me a ban reason!")
        else:
         
          r = requests.get(f'https://api.roblox.com/users/get-by-username?username={roblox_name}')
          json = r.json()
    
          if not json.get('Id') or not json.get('Username'):
            await context.send(':x: That user was not found.')

          robloxid = json["Id"]
          card = (f"{roblox_name}:{robloxid}")
          print(f"Banned user: **{card}** from St. Catharines Servers! Requested By: {context.message.author}")
          await context.message.channel.send(f"Banned user: **{card}** from St. Catharines Servers! Requested By: {context.message.author}")

          list_id = "6067e6698edb0541971738f6"
          key = "0ab94a4079cda7f2f40479344e1bb71f"
          token = "fff1c4153474619ef5604ecf5a9ca6d61f0b10d2ba8abbb8473effbd592632c5"
          ban_id_label = "6067e6698edb054197173b30"
          ban_reason_with_name = (f"{reason}, ban added by {context.message.author}")

          url = f"https://api.trello.com/1/cards"
          querystring = {"name": card, "idList": list_id, "key": key, "token": token, "desc": ban_reason_with_name, "idLabels": ban_id_label}
          response = requests.request("POST", url, params=querystring)
          card_id = response.json()["id"]
          return card_id
    else:
        await context.message.channel.send(":x: You don't have the required permission for this command!")
 
@client.command(name="pban")
async def create_card(context, roblox_name: str, *, reason = None):

    role = discord.utils.find(lambda r: r.name == 'Administrative Staff', context.guild.roles)

    if role in context.author.roles:

        if reason == None:
            await context.message.channel.send(":x: You must give me a ban reason!")
        else:
        
          r = requests.get(f'https://api.roblox.com/users/get-by-username?username={roblox_name}')
          json = r.json()
    
          if not json.get('Id') or not json.get('Username'):
            await context.send(':x: That user was not found.')

          robloxid = json["Id"]
          card = (f"{roblox_name}:{robloxid}")
          print(f"Banned user: **{card}** from St. Catharines Servers! Requested By: {context.message.author}")
          await context.message.channel.send(f"Banned user: **{card}** from St. Catharines Servers! Requested By: {context.message.author}")

          list_id = "6067eb2b19587180ae70cec4"
          key = "0ab94a4079cda7f2f40479344e1bb71f"
          token = "fff1c4153474619ef5604ecf5a9ca6d61f0b10d2ba8abbb8473effbd592632c5"
          ban_id_label = "60680ad3c764ef22147fc8ba"
          ban_reason_with_name = (f"{reason}, ban added by {context.message.author}")

          url = f"https://api.trello.com/1/cards"
          querystring = {"name": card, "idList": list_id, "key": key, "token": token, "desc": ban_reason_with_name, "idLabels": ban_id_label}
          response = requests.request("POST", url, params=querystring)
          card_id = response.json()["id"]
          return card_id
    else:
        await context.message.channel.send(":x: You don't have the required permission for this command!")
 

@client.command(name="manualadd")
async def create_card(context, roblox_name: str, *, reason = None):

    role = discord.utils.find(lambda r: r.name == 'Administrative Staff', context.guild.roles)

    if role in context.author.roles:

        if reason == None:
            await context.message.channel.send(":x: You must give me a ban reason!")
        else:
    
          card = roblox_name
          print(f"Card Added: **{card}** Requested By: {context.message.author}")
          await context.message.channel.send(f"Card Added: **{card}** Requested By: {context.message.author}")

          list_id = "6067e6698edb0541971738ef"
          key = "0ab94a4079cda7f2f40479344e1bb71f"
          token = "fff1c4153474619ef5604ecf5a9ca6d61f0b10d2ba8abbb8473effbd592632c5"
          ban_id_label = "6067e6698edb054197173b3a"
          ban_reason_with_name = (f"{reason}, ban added by {context.message.author}")

          url = f"https://api.trello.com/1/cards"
          querystring = {"name": card, "idList": list_id, "key": key, "token": token, "desc": ban_reason_with_name, "idLabels": ban_id_label}
          response = requests.request("POST", url, params=querystring)
          card_id = response.json()["id"]
          return card_id
    else:
        await context.message.channel.send(":x: You don't have the required permission for this command!")
 


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("BOT SHUTTING DOWN || 1 HOUR"))
    print("[BOT ONLINE!]")

#Running my bot
client.run(os.environ['DISCORD_TOKEN'])
