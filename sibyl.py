from crime_coefficient import coefficient
import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix=":")


@bot.event
async def on_ready():
	print("Sibyl System is ready !")
	await bot.change_presence(activity=discord.Game(':analyse'))


@bot.command(name="analyse")
async def analyse(ctx, member: discord.Member):
	await ctx.channel.send("🧠 Calculating the crime coefficient of " + member.name + " ...", delete_after=3)
	asset = member.avatar_url_as(format="png", size=1024)
	coefficient(asset, member.name, member.id)
	await ctx.channel.send(file=discord.File(member.name + ".png"))
	os.remove(member.name + ".png")

with open("token", "r", encoding="utf-8") as f:
	botToken = f.read()

bot.run(botToken)
