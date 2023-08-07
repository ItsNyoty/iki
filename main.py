import os
import json
import discord
from discord.ext import commands
import praw
import random
import json
import urllib


reddit = praw.Reddit(client_id='REDDIT CLIENT ID',
                     client_secret='REDDIT CLIENT SECRET',
                     user_agent='IKI bot by ItsNyoty')

token = "TOKEN"


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = False
        super().__init__(command_prefix=commands.when_mentioned_or('!'), intents=intents, owner_ids=[YOUR OWN ID],)

client = Bot()

   
@client.event
async def on_ready():
    print("-------------------------------------------------------------------")
    print(f'Logged in as {client.user.name} | {client.user.id}')
    print("-------------------------------------------------------------------")
    serveramount = len(client.guilds)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'in {serveramount} servers!, Prefix = !'))
    await client.load_extension('jishaku')
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(f"IKI has restarted.")

@client.command(name='sync')
async def sync(ctx):
    await client.tree.sync(guild=discord.Object(id=LOGCHANNEL)) 
    await ctx.reply(f'Synced.')
    
@client.hybrid_command(name="invite", description="Get the invitelink")
async def invite(ctx):
    await ctx.send('https://discord.com/api/oauth2/authorize?client_id=1036588724340920361&permissions=276555638849&scope=applications.commands%20bot')

@client.hybrid_command(name="meme", description="Get a meme")
async def meme(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some memes")
    def get_memes_urls(limit=10):
        req_subreddits = ["memes", "dankmemes", "terriblefacebookmemes"]
        
        meme_list = []
        for req_subreddit in req_subreddits:
            subreddit = reddit.subreddit(req_subreddit)
            for submission in subreddit.new(limit=(limit//len(req_subreddits)) +50):
                meme_list.append(
                ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
        random.shuffle(meme_list)
        return meme_list
    
    meme_list = get_memes_urls(1)
    for meme_set in meme_list[:1]:
        response_permalink = meme_set[0]
        response_title = meme_set[1]
        response_url = meme_set[2]
        colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
        random.shuffle(colors)
        emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
        emb.set_image(url=response_url)
        await ctx.send(embed=emb)

@client.hybrid_command(name="redheads", description="NSFW | Get a naked redhead")
async def redheads(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some redheads")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=1000):
            req_subreddits = ["redheads"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="hentai", description="NSFW | Get a hentai picture")
async def hentai(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some hentai")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["hentai"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="nsfw", description="NSFW | Get an nsfw picture")
async def nsfw(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some nsfw")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["nsfw"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="femboys", description="NSFW | Get a femboy picture")
async def femboys(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some femboys")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["FemBoys"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="teen", description="NSFW | Get a naked teen picture")
async def teen(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some teens")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["LegalTeens"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="gonewild", description="NSFW | They really go wild")
async def gonewild(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some girls that gone wild")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["gonewild"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="porn", description="NSFW | yeah just porn")
async def porn(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some porn")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["porn"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="collegesluts", description="NSFW | Collegegirls go wild these days")
async def collegesluts(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some wild collegegirls")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["collegesluts"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="rule34", description="NSFW | If it exists, there is porn of it")
async def rule34(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some rule34")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["rule34"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="petite", description="NSFW | Little girls (18+)")
async def petite(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some petite girls")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["PetiteGoneWild"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="asian", description="NSFW | Asian Girls like to go wild")
async def asian(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some wild asian girls")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["AsiansGoneWild"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="pussy", description="NSFW | Just a cat")
async def pussy(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some pussys")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["pussy"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="milf", description="NSFW | Just a mommy we would like to fuck")
async def milf(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some mils")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["milf"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="boobs", description="NSFW | Just a set of boobs")
async def boobs(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some boobs")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["boobs"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="latina", description="NSFW | Just a latina")
async def latina(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some latinas")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["latinas"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="lesbian", description="NSFW | Just two girls")
async def lesbian(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some lesbians")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["lesbians"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="dwbp", description="NSFW | Dad would be proud")
async def dwbp(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some girls with proud dads")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["gonewild"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="ass", description="NSFW | Just an ass")
async def ass(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some bunda")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["asshole"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="fitgirl", description="NSFW | Just a fitgirl")
async def fitgirl(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some fitgirls")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["fitgirls"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="jerkbuds", description="NSFW | Need a helping hand?")
async def jerkbuds(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some jerkbuddies")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["jerkofftoceleb"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="btbf", description="NSFW | Just borned to be fucked")
async def btbf(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some girls that we're born to be fucked")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["BornToBeFucked"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="goth", description="NSFW | Just a goth")
async def goth(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some goths")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["gothsluts"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="cock", description="NSFW | Just a massive cock")
async def cock(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some cocks")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["massivecock"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="men", description="NSFW | Just some men i guess")
async def men(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some naked men")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["MenGW"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="banana", description="Get a banana")
async def banana(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some bananas")
    def get_memes_urls(limit=1000):
        req_subreddits = ["banana"]
        
        meme_list = []
        for req_subreddit in req_subreddits:
            subreddit = reddit.subreddit(req_subreddit)
            for submission in subreddit.new(limit=(limit//len(req_subreddits)) +50):
                meme_list.append(
                ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
        random.shuffle(meme_list)
        return meme_list
    
    meme_list = get_memes_urls(1)
    for meme_set in meme_list[:1]:
        response_permalink = meme_set[0]
        response_title = meme_set[1]
        response_url = meme_set[2]
        colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
        random.shuffle(colors)
        emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
        emb.set_image(url=response_url)
        await ctx.send(embed=emb)

@client.hybrid_command(name="fortnite", description="NSFW | Fortnitekid")
async def fortnite(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some fortniteporn")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["FortniteNSFW"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="valorant", description="NSFW | Valorantkid")
async def valorant(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some valorant porn")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["valorantrule34"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")

@client.hybrid_command(name="overwatch", description="NSFW | Overwatchkid")
async def overwatch(ctx):
    channel = client.get_channel(LOGCHANNEL)
    await channel.send(ctx.author.mention + f" ({ctx.author}) has tried to see some overwatchporn")
    if ctx.channel.is_nsfw():
        def get_memes_urls(limit=10):
            req_subreddits = ["overwatch_porn"]
            
            meme_list = []
            for req_subreddit in req_subreddits:
                subreddit = reddit.subreddit(req_subreddit)
                for submission in subreddit.new(limit=(limit//len(req_subreddits)) +10):
                    meme_list.append(
                    ["https://reddit.com" + submission.permalink, submission.title, submission.url])
                
            random.shuffle(meme_list)
            return meme_list
    
        meme_list = get_memes_urls(1)
        for meme_set in meme_list[:1]:
            response_permalink = meme_set[0]
            response_title = meme_set[1]
            response_url = meme_set[2]
            colors = [0xff0000, 0x00ff00, 0x0000ff, 0x000000,
                  0xffffff, 0xffff00, 0x00ffff, 0xff00ff]
            
            random.shuffle(colors)
            emb = discord.Embed(title=response_title,
                            url=response_permalink, color=colors[0])
            emb.set_image(url=response_url)
            await ctx.send(embed=emb)
    else:
        await ctx.send(":warning: This channel must be NSFW")
        
client.run(token)
