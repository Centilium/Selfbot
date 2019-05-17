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

					if cmd == "Centilium":
						if len(args) == 0:
							await channel.send("Centilium Esport est une jeune équipe gamer sur Fortnite. N'hésitez pas à nous rejoindre sur Twitch et Youtube.")
						else:
							await channel.send("Usage: .centilium")
					
					if cmd == "ytb":
						if len(args) == 0:
							await channel.send("Notre chaîne Youtube : https://www.youtube.com/channel/UCatpNP30Oo0F9fxtLMKMj3w")
                                                              
						else:
							await channel.send("Usage: .ytb")
					
					if cmd == "twitch": 
						if len(args) == 0:
							message.delete();
							await channel.send("Notre chaîne Twitch : https://www.twitch.tv/teamcentilium")
						
						else:
							await channel.send("Usage: .twitch")
							
					if cmd == "log": 
						if len(args) == 0:
							message.delete();
							await users.get("570345320215609344").send(" <@" +  message.author.id + "> souhaite changer le salon de patchs :  " + "`" + message.content + "`" + "  je vous en informe")
						
						else:
							await channel.send("Usage: .log")
						
					if cmd == "me": 
						if len(args) == 0:
							message.delete();
							await channel.send("Ce selfbot créer par Nigary est disponible gratuitement par : https://github.com/Centilium/Selfbot")
						
						else:
							await channel.send("Usage: .me")
						
					if cmd == "aide": 
						if len(args) == 0:
							message.delete();
							await channel.send("!aide : ce message \n !twitch : Mon Twitch \n !ytb : Mon Youtube \n !me : le lien pour le selfbot")
						
						else:
							await channel.send("Usage: .aide")

					if cmd == "streamname":
						if len(args) >= 1:
							STREAM['name'] = ' '.join(args)
							await channel.send("Streamname a était changé.")
						else:
							await channel.send("Usage: .streamname <name>")

					if cmd == "streamgame":
						if len(args) >= 1:
							newgame = ' '.join(args)
							if newgame == "none":
								STREAM['details'] = None
							else:
								STREAM['details'] = newgame
	
							await channel.send("Streamgame a était changé.")
						else:
							await channel.send("Usage: .streamgame <name>")

					if cmd == "streamurl":
						if len(args) >= 1:
							STREAM['url'] = ' '.join(args)
							await channel.send("Streamurl a était changé.")
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
									await channel.send("Le Stream vient de commencer")
									return

							await channel.send("You have to define a ``streamname`` et ``streamurl``!")
						else:
							await channel.send("Usage: .streamstart")

					if cmd == "streamstop":
						if len(args) == 0:
							await client.change_presence(activity=None)
							await channel.send("Le stream vient de s'arreter")
							return
						else:
							await channel.send("Usage: .streamstop")

client.run(TOKEN, bot=False)
