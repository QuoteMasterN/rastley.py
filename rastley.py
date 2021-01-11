import discord
import scraper
import re

class MyClient(discord.Client):
    async def on_ready(self):
        print("Rastley is online!")
    
    # check for rick roll in a message
    async def on_message(self, message):
        # return if message author is a bot
        if message.author.bot: return

        # check if there's a link in the message using regex and store all links in urls
        urls = re.findall("(?P<url>https?://[^\s]+)", message.content)

        # check each url in urls for a rick roll
        for url in urls:
            if scraper.searchForRick(url):
                await message.channel.send("<@" + str(message.author.id) + ">  https://youtu.be/Ux0YNqhaw0I")



token = input("What is the bot token? ")
client = MyClient()
client.run(token)