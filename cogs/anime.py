import discord
from discord.ext import commands
import requests
import aiohttp

class Anime(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def wallpaper(self, ctx):
   async with aiohttp.ClientSession() as cs:
     async with cs.get('https://shiro.gg/api/images/wallpapers') as r:
        res = await r.json()
        embed = discord.Embed(
          title = "Here's your wallpaper!",
          description = f"Generated wallpaper in {self.bot.latency} ms!",
          color=0xe3be66 
        )
        embed.set_image(url=res['url'])
        await ctx.reply(embed=embed)
 



def setup(bot):
  bot.add_cog(Anime(bot))