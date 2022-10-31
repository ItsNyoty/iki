import os
import json
import discord
from discord.ext import commands
import asyncpraw
import random
import json
import urllib


token = "TOKEN"


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = False
        super().__init__(command_prefix=commands.when_mentioned_or('!'), intents=intents, owner_ids=[OWNER 1],)

client = Bot()
   
@client.event
async def on_ready():
    print("-------------------------------------------------------------------")
    print(f'Logged in as {client.user.name} | {client.user.id}')
    print("-------------------------------------------------------------------")
    serveramount = len(client.guilds)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'in {serveramount} servers!, Prefix = !'))
    await client.load_extension('jishaku')

@client.command(name='sync')
async def sync(ctx):
    await client.tree.sync(guild=discord.Object(id=MAIN DISCORD SERVER ID)) 
    await ctx.reply(f'Synced.')
    
@client.hybrid_command(name="meme", description="Get a meme")
async def meme(ctx):
    memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')
    
    memeData = json.load(memeAPI)
    
    memeUrl = memeData['url']
    memeName = memeData['title']
    memePoster = memeData['author']
    memeSub = memeData['subreddit']
    memeLink = memeData['postLink']
    
    embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    embed.set_image(url=memeUrl)
    embed.set_footer(text=f"Meme by: {memePoster} | Subreddit {memeSub}")
    await ctx.send(embed=embed)
    
@client.hybrid_command(name="redheads", description="NSFW | Get a naked redhead")
async def redheads(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/redheads/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")
        
@client.hybrid_command(name="hentai", description="NSFW | Get a hentai picture")
async def hentai(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/hentai/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")
        
@client.hybrid_command(name="nsfw", description="NSFW | Get a nsfw picture")
async def nsfw(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/nsfw/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")
    
@client.hybrid_command(name="femboys", description="NSFW | Get a femboy picture")
async def femboys(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/FemBoys/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="teen", description="NSFW | Get a naked teen picture")
async def teen(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/LegalTeens/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="gonewild", description="NSFW | They really go wild")
async def gonewild(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/gonewild/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="porn", description="NSFW | yeah just porn")
async def porn(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/porn/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="collegesluts", description="NSFW | Collegesluts go wild these days")
async def collegesluts(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/collegesluts/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")
    
@client.hybrid_command(name="rule34", description="NSFW | If it exists, there is porn of it")
async def collegesluts(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/rule34/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")
    
@client.hybrid_command(name="petite", description="NSFW | Little girls")
async def petite(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/PetiteGoneWild/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")
    
@client.hybrid_command(name="asian", description="NSFW | Asian Girls like to go wild")
async def asian(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/AsiansGoneWild/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")
    
@client.hybrid_command(name="pussy", description="NSFW | Just a cat? ")
async def pussy(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/pussy/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="milf", description="NSFW | Just a mommy we would like to fuck ")
async def milf(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/milf/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")
        
@client.hybrid_command(name="boobs", description="NSFW | Just a set of boobs")
async def boobs(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/boobs/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="latina", description="NSFW | Just a latina ")
async def latina(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/latinas/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="lesbian", description="NSFW | Just two girls ")
async def lesbian(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/lesbians/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="dwbp", description="NSFW | Dad would be proud")
async def dwbp(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/DadWouldBeProud/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="ass", description="NSFW | Just an ass ")
async def ass(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/asshole/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="fitgirl", description="NSFW | Just a fitgirl ")
async def fitgirl(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/fitgirls/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="jerkbuds", description="NSFW | Need a helping hand?")
async def jerkbuds(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/jerkofftoceleb/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="btbf", description="NSFW | Just borned to be fucked ")
async def btbf(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/BornToBeFucked/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="goth", description="NSFW | Just a goth")
async def goth(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/gothsluts/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="cock", description="NSFW | Just a massive cock")
async def goth(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/massivecock/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="men", description="NSFW | Just some men i guess")
async def goth(ctx):
    if ctx.channel.is_nsfw():
    	memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme/MenGW/')
    
    	memeData = json.load(memeAPI)
    
    	memeUrl = memeData['url']
    	memeName = memeData['title']
    	memePoster = memeData['author']
    	memeSub = memeData['subreddit']
    	memeLink = memeData['postLink']
    
    	embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
    	embed.set_image(url=memeUrl)
    	embed.set_footer(text=f"By: {memePoster} | Subreddit {memeSub}")
    	await ctx.send(embed=embed)
    else:
    	await ctx.send(":warning: This channel must be NSFW")
client.run(token)
