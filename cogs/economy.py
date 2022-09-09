import discord
from discord.ext import commands
import random
import json

class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Economy is running")
        
@commands.command()
async def bank(self, ctx):
	await check_acc(ctx.author)

	user = ctx.author

	users = await bank_data()

	wallet_amt = users[str(user.id)]['wallet']
	bank_amt = users[str(user.id)]['bank']


	em = discord.Embed(title = f"{ctx.author.name}'s balance")
	em.add_field(name = "wallet", value = wallet_amt)
	em.add_field(name = "bank", value = bank_amt)
	await ctx.send(embed = em)

@commands.command()
async def beg(self, ctx):
	await check_acc(ctx.author)

	user = ctx.author

	users = await bank_data()

	earnings = random.randrange(101)

	await ctx.send(f"You look poor so someone gave you {earnings} mc")


	users[str(user.id)]['wallet'] += earnings

	with open('mc.json','w') as f:
		json.dump(users,f)


async def check_acc(user):

	users = await bank_data()

	if str(user.id) in users:
		return False

	else:
		users[str(user.id)] = {}
		users[str(user.id)]['wallet'] = 0
		users[str(user.id)]['bank'] = 420
	
	with open('mc.json','w') as f:
		json.dump(users,f)
	return True	


async def bank_data():
	with open('mc.json','r') as f:
		users = json.load(f)

	return users

async def update_bank(user, change = 0, mode = "wallet"):
  users = await bank_data()
  
def setup(client):
    client.add_cog(Economy(client))
