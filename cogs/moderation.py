import discord
from discord.ext import commands
import asyncio

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation is running")

    @commands.command(aliases=['purge, c'])
    @commands.has_permissions(manage_messages = True)
    async def clr(self, ctx, amount=2):
        await ctx.channel.purge(limit = amount)
        embed=discord.Embed(title=f"**{amount} messages have been cleared.**", color=0x000000)
        embed.set_footer(text=f"Cleared by {ctx.author.name}", icon_url=ctx.author.avatar_url) 
        message = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await message.delete()
        print(f'clear has been run in {ctx.guild} by {ctx.author}')
        print(f"{amount} messages cleared by {ctx.author} in {ctx.guild}")

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member : discord.Member, reason=None):
            embed=discord.Embed(title=f"You have been banned from {ctx.guild.name}.\nReason: {reason}.", color=0x000000)
            embed.set_author(name="Mericful Moderation", icon_url="https://media.discordapp.net/attachments/912954530176565268/913270050394366002/merc.png")
            embed.set_footer(text=f"Banned by {ctx.author}")
            await member.send(embed=embed)
            embed=discord.Embed(title=f"{member} was banned.\nReason: {reason}.", color=0x000000)
            embed.set_author(name="Mericful Moderation", icon_url="https://media.discordapp.net/attachments/912954530176565268/913270050394366002/merc.png")
            embed.set_footer(text=f"Banned by {ctx.author}")
            await ctx.send(embed=embed)
            await member.ban(reason=reason)
            print(f'ban has been run in {ctx.guild} by {ctx.author}')
            print(f"{member} was banned from {ctx.guild} by {ctx.author} for {reason}")
    
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def nuke(self, ctx, channel_name):
      await ctx.message.delete()
      name = channel_name
      channel_id = int(''.join(i for i in channel_name if i.isdigit())) 
      existing_channel = self.client.get_channel(channel_id)
      if existing_channel:
        await existing_channel.clone(reason="Has been nuked")
        embed=discord.Embed(title=f"Nuked Channel ({name})", color=0x000000, timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/831122045538009108/834050266335805470/2Q.png")
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        await existing_channel.delete()
      else:
        await ctx.send(f'No channel named **{channel_name}** was found')
      print(f'nuke has been run in {ctx.guild} by {ctx.author}')



    
def setup(client):
    client.add_cog(Moderation(client))
