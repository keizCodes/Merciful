import asyncio
import discord
from discord.ext import commands


class Useful(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Useful is running")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Client latency is `{round(self.client.latency * 1000)}ms`')
        print(f'ping has been run in {ctx.guild} by {ctx.author}')

    @commands.command(aliases=["serverinfo"])
    async def sinfo(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        embed = discord.Embed(colour=0x000000, timestamp=ctx.message.created_at,
                              title=f"**Info for {ctx.guild.name}**")
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=member.avatar.url)

        embed.set_author(name=member.name, icon_url=member.avatar.url)

        embed.add_field(name="*Name*", value=ctx.guild.name)
        embed.add_field(name="*Owner*", value=str(ctx.guild.owner))

        embed.add_field(name="*Guild ID*", value=ctx.guild.id)
        embed.add_field(name="*Region*", value=ctx.guild.region)

        embed.add_field(name="*Membercount*", value=ctx.guild.member_count)
        embed.add_field(name='*Verification Level*', value=str(ctx.guild.verification_level))

        embed.add_field(name="*Highest role*", value=ctx.guild.roles[-2])
        embed.add_field(name="*Created At*", value=ctx.guild.created_at.__format__("%a, %#d %B %Y, %I:%M %p UTC"))

        await ctx.send(embed=embed)
        print(f'serverinfo has been run in {ctx.guild} by {ctx.author}')

    @commands.command(aliases=['ri', 'rolei'])
    async def roleinfo(self, ctx, *, role: discord.Role):  # b'\xfc'
        guild = ctx.guild
        since_created = (ctx.message.created_at - role.created_at).days
        role_created = role.created_at.strftime("%d %b %Y %H:%M")
        created_on = "{} ({} days ago)".format(role_created, since_created)
        users = len([x for x in guild.members if role in x.roles])
        if str(role.colour) == "#000000":
            colour = "default"
        else:
            colour = str(role.colour).upper()
        em = discord.Embed(title=f"Role info for {role.name}", colour=0x000000, timestamp=ctx.message.created_at)
        em.add_field(name="Role Name:", value=f" {role.name}")
        em.add_field(name="Role ID:", value=f"{role.id}")
        em.add_field(name="Users", value=users)
        em.add_field(name="Mentionable", value=role.mentionable)
        em.add_field(name="Hoist", value=role.hoist)
        em.add_field(name="Position", value=role.position)
        em.add_field(name="Managed", value=role.managed)
        em.add_field(name="Colour", value=colour)
        em.add_field(name='Creation Date', value=created_on)
        em.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=em)
        print(f'roleinfo has been run in {ctx.guild} by {ctx.author}')

    @commands.command(aliases=["whois"])
    async def userinfo(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        roles = [role for role in member.roles]
        embed = discord.Embed(color=0x000000, timestamp=ctx.message.created_at,
                              title=f"**User Info For __{member}__**")

        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=member.avatar.url)

        embed.set_author(name=member.name, icon_url=member.avatar.url)

        embed.add_field(name="*User ID:*", value=member.id)
        embed.add_field(name="*Display Name:*", value=member.display_name)

        embed.add_field(name="*Registered:*", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="*Joined:*", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

        embed.add_field(name="*Status*", value=str(member.status))
        embed.add_field(name="*Roles:*", value=", ".join([role.mention for role in roles]))
        embed.add_field(name="*Highest Role:*", value=member.top_role.mention)
        print(member.top_role.mention)
        await ctx.send(embed=embed)
        print(f'userinfo has been run in {ctx.guild} by {ctx.author}')

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def role(self, ctx, member: discord.Member, role: discord.Role):
        if role in member.roles:
            await member.remove_roles(role)
            embed = discord.Embed(title='Role Added', color=0x000000, timestamp=ctx.message.created_at)
            embed.add_field(name='Member:', value=f'{member.mention}')
            embed.add_field(name='Role:', value=f'{role}')
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
            await ctx.send(embed=embed)
        else:
            await member.add_roles(role)
            embed = discord.Embed(title='Role Added', color=0x000000, timestamp=ctx.message.created_at)
            embed.add_field(name='Member:', value=f'{member.mention}')
            embed.add_field(name='Role:', value=f'{role}')
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
            await ctx.send(embed=embed)
        print(f'role has been run in {ctx.guild} by {ctx.author}')

    @commands.command(aliases=['avatar', 'pfp'])
    async def av(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        embed = discord.Embed(colour=0x000000, timestamp=ctx.message.created_at,
                              title=f"** {member}'s avatar**")
        embed.set_author(name=member.name, icon_url=member.avatar.url)

        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=member.avatar.url)
        embed.set_image(url=member.avatar.url)
        await ctx.send(embed=embed)
        print(f'avatar has been run in {ctx.guild} by {ctx.author}')

    @commands.command(aliases=["mc"])
    async def membercount(self, ctx):

        a = ctx.guild.member_count
        b = discord.Embed(title=f"*Current member count for {ctx.guild.name}*", description=a, color=discord.Color((0x000000)))
        await ctx.send(embed=b)
        print(f'membercount has been run in {ctx.guild} by {ctx.author}')

    @commands.command()
    async def afk(self, ctx, mins):
        current_nick = ctx.author.nick
        await ctx.send(f"{ctx.author.mention} I set your AFK: {mins}")
        await ctx.author.edit(nick=f"{ctx.author.name} [AFK]")

        counter = 0
        while counter <= int(mins):
            counter += 1
            await asyncio.sleep(60)

            if counter == int(mins):
                await ctx.author.edit(nick=current_nick)
                await ctx.send(f"{ctx.author.mention} Is no longer AFK")
                print(f'{ctx.author} is no longer afk in {ctx.guild}')
                break
        print(f'afk has been run in {ctx.guild} by {ctx.author}')

    snipe_message_content = None
    snipe_message_author = None

    snipe_message_content = None
    snipe_message_author = None
    snipe_message_id = None

    @commands.Cog.listener()
    async def on_message_delete(self, message):

        global snipe_message_content
        global snipe_message_author
        global snipe_message_id

        snipe_message_content = message.content
        snipe_message_author = message.author.name
        snipe_message_id = message.id
        await asyncio.sleep(60)

        if message.id == snipe_message_id:
            snipe_message_author = None
            snipe_message_content = None
            snipe_message_id = None

    @commands.command()
    async def snipe(self, message):
      print(f'snipe has been run')
      if snipe_message_content is None:
          await message.channel.send("There is nothing to snipe.")
      else:
          embed = discord.Embed(description=f"{snipe_message_content}", color=0x000000)
          embed.set_footer(text=f"Requested by {message.author.name}#{message.author.discriminator}",
                            icon_url=message.author.avatar.url)
          embed.set_author(name=f"{snipe_message_author}")
          await message.channel.send(embed=embed)
          return

    @commands.command(pass_context=True)
    @commands.has_permissions(change_nickname=True)
    async def nick(self, ctx, member: discord.Member, nick):
        await member.edit(nick=nick)
        await ctx.send(f'**Nickname was changed for {member.mention}** ')
        print(f'nick has been run in {ctx.guild} by {ctx.author}')

    @commands.command(pass_context=True)
    @commands.has_permissions(change_nickname=True)
    async def unnick(self, ctx, member: discord.Member):
        reset = member.name
        await member.edit(nick=reset)
        await ctx.send(f"**Nickname reset for {member.mention}**")
        print(f'unnick has been run in {ctx.guild} by {ctx.author}')
    
    @commands.command()
    async def botinfo(self, ctx):
        member = ctx.message.author
        embed = discord.Embed(colour=0x000000, timestamp=ctx.message.created_at,
                            title=f"**Merciful Information**")
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=member.avatar.url)
        embed.set_author(name=member.name, icon_url=member.avatar.url)
        embed.add_field(name="*Ping*", value=round(self.client.latency * 1000)
        , inline=True)
        embed.add_field(name="*Developers*", value=('''modern#6666
Ziek#1860
'''), inline=True) 
        embed.add_field(name="*Membercount*", value=len(self.client.users)
        , inline=True)
        embed.add_field(name='*Servercount*', value=len(self.client.guilds)
        , inline=True)
        embed.add_field(name="*Support Server*", value=('''https://discord.gg/merciful
        '''), inline=True)
        embed.add_field(name="*Bot Invite*", value='''On Bots Profile
        ''', inline=True)
        await ctx.send(embed=embed)
        print(f'botinfo has been run in {ctx.guild} by {ctx.author}')


def setup(client):
    client.add_cog(Useful(client))
