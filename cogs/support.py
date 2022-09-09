
import discord
from discord.ext import commands




class Support(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Support is running")

    @commands.command()
    async def prefix(self, ctx):
        embed = discord.Embed(title="Merciful", color=0x000000)
        embed.add_field(name="My prefix is +", value="Use +help to get started!")
        await ctx.send(embed=embed)
        print(f'prefix has been run in {ctx.guild} by {ctx.author}')

    @commands.command(aliases=["inv"])
    async def invite(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        roles = [role for role in member.roles]

        embed = discord.Embed(color=0x000000, timestamp=ctx.message.created_at,
                              title=f"**{self.client.user.name} invite **",
                              url="https://discord.com/api/oauth2/authorize?client_id=1015968841026781184&permissions=8&scope=bot")
        embed.add_field(name="Support", value="[Discord Invite](https://discord.gg/vct)", inline=True)
        embed.set_thumbnail(
            url="https://media.discordapp.net/attachments/912954530176565268/913270050394366002/merc.png?width=461&height=461")
       
        await ctx.send(embed=embed)
        print(f'invite has been run in {ctx.guild} by {ctx.author}')

    

def setup(client):
    client.add_cog(Support(client))
