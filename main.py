from asyncio import sleep
import discord
from discord.ext import commands
import os

from discord.ui import Select, View


intents = discord.Intents.all()

client = commands.Bot(command_prefix=commands.when_mentioned_or("+"), caseinsensitive=True, intents=intents, help_command=None)
my_secret = os.environ['token']

#help_command=None

async def status():
    while True:
        await client.wait_until_ready()
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                               name=f"{len(client.guilds)} guilds and "
                                                                    f"{len(client.users)} users"))
        await sleep(10)
        await client.change_presence(activity=discord.Game(type=discord.ActivityType.playing, name='+help'))
        await sleep(15)
        await client.change_presence(activity=discord.Game(name='24/7 Hosting'))
        await sleep(10)
        await client.change_presence(activity=discord.Game(name='Developed by Modern x Keiz'))
        await sleep(10)
        await client.change_presence(activity=discord.Game(name='BETA Out Soon | Expect Bugs'))
        await sleep(10)


@client.event
async def on_ready():
    print("==================")
    print("Logged in as")
    print('{}'.format(client.user.name))
    print("{}".format(client.user.id))
    print("==================")
    print('Servers connected to:')
    for guild in client.guilds:
      members = len(guild.members)
      print(f'{guild.name} ({members}) Owner: {guild.owner}')
    print("==================")
    await client.loop.create_task(status())

@client.event
async def on_guild_join(guild):
  for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('Hey there! my prefix is "+", To know more about my commands use "+help" ')
        break

@client.command(pass_context=True)
async def update(ctx):

    embed=discord.Embed(title="Merciful - Update v0.01", description="We have added some new features as well as renovating the help command! Here are some of the new updates.")
    embed.add_field(name="Music", value="(Temporarily disabled due to bugs.)", inline=True)
    embed.add_field(name="24/7", value="Our bot is online 24/7! ", inline=True)
    embed.add_field(name="Renovated our help command", value="You can take a look by running the command +help!", inline=True)
    embed.set_footer(text="For any concerns/suggestions please contact modern#6666 or Ziek#1860 via PM.")
  
    for server in client.guilds:
        for channel in server.text_channels:
            try:
                await channel.send(embed=embed)
            except Exception:
                continue
            else:
                break

class testing(View):
      
        @discord.ui.select(placeholder="Category",options=[
          discord.SelectOption(label="Moderation", value="1"),
          discord.SelectOption(label="Support", value="2"),
          discord.SelectOption(label="Useful", value="3")
        ])

      
        async def select_callback(self, select, interaction):
            select.disable=True
            if select.values[0] == "1":
              embedMod=discord.Embed(title="Moderation", description="List of moderation commands!")
              embedMod.add_field(name="Ban", value="Bans a member from the server", inline=True)   
              embedMod.add_field(name="Clear", value="Clears channel's messages", inline=True) 
              embedMod.add_field(name="Nuke", value="Clears an entire channel", inline=False) 
      
              await interaction.response.edit_message(embed=embedMod)
              
            if select.values[0] == "2":
              embedSup=discord.Embed(title="Support", description="List of support commands!") 
              embedSup.add_field(name="Invite", value="Get the invite for the bot", inline=True) 
              embedSup.add_field(name="Prefix", value="Get the prefix of the bot", inline=False)
              
              await interaction.response.edit_message(embed=embedSup)
            if select.values[0] == "3":
              embedusef=discord.Embed(title="Useful", description="List of useful commands!")
              embedusef.add_field(name="AFK", value="Sets your status to AFK", inline=True)
              embedusef.add_field(name="Avatar", value="Checks a user's avatar", inline=False)
              embedusef.add_field(name="Membercount", value="Checks the servers memebr count", inline=True)
              embedusef.add_field(name="Nickname", value="Changes a users nickname", inline=True)
              embedusef.add_field(name="Ping", value="Check the bots ping!", inline=True)
              embedusef.add_field(name="Role", value="undefined", inline=True)
              embedusef.add_field(name="Roleinfo", value="Gets info of a Role", inline=True)
              embedusef.add_field(name="Sinfo", value="undefined", inline=True)
              embedusef.add_field(name="Snipe", value="Snipes deleted messages!", inline=True)
              embedusef.add_field(name="Unnick", value="Removes users nickname", inline=True)
              embedusef.add_field(name="Userinfo", value="Gets a users info", inline=True)
              
              await interaction.response.edit_message(embed=embedusef)      

@client.command()
async def help(ctx):
  view = testing()
  embed=discord.Embed(description="Merciful Commands")
  embed.set_author(name="Help")
  embed.add_field(name="Moderation", value="1", inline=True)
  embed.add_field(name="Support", value="2", inline=True)
  embed.add_field(name="Useful", value="3", inline=True)
      
  await ctx.send(embed=embed, view=view)
      
@client.command()
@commands.has_any_role(912939172766036048, 913347218902229032)
async def servers(ctx):
  for guild in client.guilds:
    members = len(guild.members)
    await ctx.send(f'{guild.name} ({members}) Owner: {guild.owner}')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} loaded.')
    print(f'{extension} loaded by {ctx.author}')


@client.command()
@commands.has_any_role(912939172766036048, 913347218902229032)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} unloaded.')
    print(f'{extension} unloaded by {ctx.author}')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} reloaded.')
    print(f'{extension} reloaded by {ctx.author}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(my_secret)
