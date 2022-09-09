import discord
from discord.ext import commands


class Antinuke(commands.Cog):
      def __init__(self, client):
        self.client = client

      @commands.Cog.listener()
      async def on_ready(self):
        print("Anti Nuke Is Running")

      
def setup(client):
    client.add_cog(Antinuke(client))
