import discord
import random
from discord.ext import commands
import os

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_member_join(member):
    global joined
    print(f'{member} has joined')
    with open("stats.txt", "a") as f:
        f.write(f'User {member}, has joined\n')


@client.event
async def on_member_remove(member):
    global joined
    with open("stats.txt", "a") as f:
        f.write(f'User {member}, has left\n')
    print(f'{member} has left')


async def update_stats():
    await client.wait_until_ready()
    global messages, joined
    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f'Messages {messages}')
        except Exception as e:
            print(e)


@client.event
async def on_message(message):
    UserID = message.author
    print(UserID)
    await client.process_commands(message)
    with open("stats.txt", "a") as f:
        f.write(f'Message by: User: {UserID}, Message: {message.content}\n')


@client.command(aliases=["8Ball", "8ball", "eightball", "EightBall", "eightBall", "Eightball"])
async def _8Ball(ctx, *, question):
    responses = ["As I see it, yes",
                 "Ask again later",
                 "Better not tell you now",
                 "Cannot predict now",
                 "Concentrate and ask again",
                 "Don’t count on it",
                 "It is certain",
                 "It is decidedly so",
                 "Most likely",
                 "My reply is no",
                 "My sources say no",
                 "Outlook good",
                 "Outlook not so good",
                 "Reply hazy try again",
                 "Signs point to yes",
                 "Very doubtful",
                 "Without a doubt",
                 "Yes",
                 "Yes, definitely",
                 "You may rely on it"]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def ping(ctx):  # Checks latency
    await ctx.send(f'Pong! Latency is: {round(client.latency * 1000)}ms')


@client.command()
async def clear(ctx, ammount=1):
    await ctx.channel.purge(limit=ammount)


# @client.command()
# async def kick(ctx, member: discord.member, *, reason="None"):
# await member.kick(reason=reason)
# await ctx.send(f'Kicked {member.mention}')
# with open("stats.txt", "a") as f:
# f.write(f'User {member}, has been kicked for {reason}\n')


# @client.command()
# async def ban(ctx, member: discord.member, *, reason="None"):
# await member.ban(reason=reason)
# await ctx.send(f'Banned {member.mention}')
# with open("stats.txt", "a") as f:
# f.write(f'User {member}, has been banned for {reason}\n')


# @client.command()
# async def unban(ctx, *, member):
    # banned_users = await ctx.guild.bans()
    # member_name, member_discriminator = member.split("#")

# for ban_entry in banned_users:
# user = ban_entry.banned_users
# if (user.name, user.discriminator) == (member_name, member_discriminator):
# await ctx.guild.unban(user)
# await ctx.send(f'Unbanned {user.mention}')
# with open("stats.txt", "a") as f:
# f.write(f'User: {user}, has been unbanned\n')


@client.command()
async def roll(ctx):
    await ctx.send(random.randint(1, 100))


# @client.command()
# async def play(ctx):
    # channel = ctx.message.author.voice.voice_channel
    # await client.join_voice_channel(channel)


# @client.command()
# async def stop(ctx):
    # server = ctx.message.server
    # voice_client = client.voice_client_in(server)
    # await voice_client.disconnect()


client.run(os.getenv('TOKEN'))
