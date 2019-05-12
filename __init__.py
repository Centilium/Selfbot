import os
import discord
from discord.ext import commands

PREFIX = os.environ["PREFIX"]
TOKEN = os.environ["TOKEN"]

STREAM = {
	"name": None,
	"details": None,
	"url": None
}

client = discord.Client()

@client.event
async def on_ready():
		print('Bot successfully started.')

@client.event
async def on_message(message):
		if message.author == client.user:
				if message.content.startswith(PREFIX):
					cmd = "".join(message.content.split(" ")[0:1]).replace(PREFIX, '')
					args = message.content.split(" ")[1:]
					channel = message.channel

					if cmd == "ping":
						if len(args) == 0:
							await channel.send("Pong! ceci est un test")
						else:
							await channel.send("Usage: .ping")
					
					if cmd == "ytb":
						if len(args) == 0:
							await channel.send("https://www.youtube.com/channel/UCatpNP30Oo0F9fxtLMKMj3w")
						else:
							await channel.send("Usage: .ytb")
					
					
					if cmd == "streamname":
						if len(args) >= 1:
							STREAM['name'] = ' '.join(args)
							await channel.send("Streamname has been changed.")
						else:
							await channel.send("Usage: .streamname <name>")

					if cmd == "streamgame":
						if len(args) >= 1:
							newgame = ' '.join(args)
							if newgame == "none":
								STREAM['details'] = None
							else:
								STREAM['details'] = newgame
	
							await channel.send("Streamgame has been changed.")
						else:
							await channel.send("Usage: .streamgame <name>")

					if cmd == "streamurl":
						if len(args) >= 1:
							STREAM['url'] = ' '.join(args)
							await channel.send("Streamurl has been changed.")
						else:
							await channel.send("Usage: .streamurl <url>")

					if cmd == "streaminfo":
						if len(args) == 0:
							msg = "Stream Infos:\n"
							msg += "Streamname: " + str(STREAM["name"]) + "\n"
							msg += "Streamgame: " + str(STREAM["details"]) + "\n"
							msg += "Streamurl: " + str(STREAM["url"]) + "\n"
							await channel.send(msg)
						else:
							await channel.send("Usage: .streaminfo")

					if cmd == "streamstart":
						if len(args) == 0:
							if STREAM["name"] != None:
								if STREAM["url"] != None:
									streaming = discord.Streaming(name=STREAM["name"], url=STREAM["url"], details=STREAM["details"])
									await client.change_presence(activity=streaming)
									await channel.send("Stream activity was updated!")
									return

							await channel.send("You have to define a ``streamname`` and a ``streamurl``!")
						else:
							await channel.send("Usage: .streamstart")

					if cmd == "streamstop":
						if len(args) == 0:
							await client.change_presence(activity=None)
							await channel.send("Stream activity was removed!")
							return
						else:
							await channel.send("Usage: .streamstop")

client.run(TOKEN, bot=False)
