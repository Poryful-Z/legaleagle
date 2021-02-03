import discord
import os
import random
import time

piplups = ["https://cdn.discordapp.com/attachments/265667089732206592/806255185864949791/47d9be5856cf55d937ba28fd525ca22c.png", "https://cdn.discordapp.com/attachments/265667089732206592/806255249995071549/97ftcj3vio031.png", "https://cdn.discordapp.com/attachments/265667089732206592/806255269952487434/YwxZ0G-T.png", "https://cdn.discordapp.com/attachments/265667089732206592/806255295826231346/1200px-Dawn_Piplup.png", "https://cdn.discordapp.com/attachments/265667089732206592/806255319596531722/5f2ecca11341463537cc008106132cdf.png", "https://cdn.discordapp.com/attachments/265667089732206592/806255365964300348/e1e5d4938bc6559c45a3d6dd2c3f6180--dino-mad.png"]

async def processCommand(message):
  msg = message.content.lower()

  if msg.startswith("eagle!agent"):
    await agent(message)

  elif msg.startswith("eagle!shinx"):
    await shinx(message)
  
  elif msg.startswith("eagle!jolsone"):
    await jolsone(message)

async def agent(message):
  await message.channel.send("hey guys this morning i was walking my dog and then i slipped on ice and fell on my ass and because i drank so much water last night and hadnt had my morning pee yet when i hit the ground i pissed myself so now im a little sore and smell like piss so responses may be slow")

async def jolsone(message):
  random.shuffle(piplups)
  await message.channel.send(piplups[0])

async def shinx(message):
  await message.channel.send("https://cdn.discordapp.com/attachments/756304803398680612/799404404389707776/image0.png")