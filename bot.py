import discord
from discord.ext import commands
from discord.ext.commands import bot

client = commands.Bot(command_prefix="tokenhere")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def discordbirthday(ctx):
    await ctx.send(f"{ctx.author.mention} Discord's birthday is TODAY!! <a:tada:8375075708676342070>.")

@client.command()
async def credit(ctx):
        """See the important people that help make the bot possible!"""
        embed = discord.Embed(title="Credit", description=f"The person who created me and the only person who is developing is <@325695152242819084>", color=0x5539cc)
        await ctx.send(embed=embed)



@client.event
async def on_ready():
    print(f"I am online!  {client.user.name}")
    await client.change_presence(status=discord.Status.online, activity = discord.Game("Discord Birthday"))
    logs = client.get_channel(834580547194978314)
    await logs.send("<:online:754362486177660969> I am online, DBB Bot <:online:754362486177660969>")





@client.event
async def on_command_error(context, exception):
      await context.send(str(exception))

@client.command()
async def discordstream(ctx):
    await ctx.send(f"{ctx.author.mention} You can find the stream on youtube and twitch using these links <https://www.youtube.com/watch?v=BZKz16o9rms> <https://www.twitch.tv/discord>")

@client.command()
async def invite(ctx):
    await ctx.send(f"{ctx.author.mention} The invite link is <https://discord.com/api/oauth2/authorize?client_id=841445945282920547&permissions=0&scope=bot>")

@client.command()
async def discordbirthdaycountdown(ctx):
    await ctx.send(f"{ctx.author.mention} The countdown to May 13th is <https://www.timeanddate.com/countdown/birthday?iso=20210513T00&p0=1029&font=cursive&csz=1>")





client.load_extension("jishaku")
client.run("token")
