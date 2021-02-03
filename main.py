import discord
import os
import random
import time
import ka
import players
import jotto

client = discord.Client()
votes = {}
allianceIDs = [790333937398448178, 790298909758717952, 756304803008741560, 792956105998729227, 790333937398448178, 797514338826453022]
hostIDs = [756304803008741560, 791520315502231596]
rocksIDs = [791524378016874546, 756304803268919311, 759870079914999819, 791748845255000135]
botChannelIDs = [791524378016874546, 756304803268919311, 759870079914999819, 756304803398680613, 791748445361930270, 791748493604814878, 791748845255000135, 471195159456120832]
swapIDs = [789568611798089739, 756304803008741560]
shinxIDs = [756304803398680612, 756304803008741561]
voteCounter = 0

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content.lower()

  if msg.startswith("eagle!hello"):
    await message.channel.send("Hello " + message.author.nick)
  
  elif msg.startswith("eagle!rocks"):
    await rocks(message, msg)
  
  elif msg.startswith("eagle!swap"):
    await swap(message)
  
  elif msg.startswith("eagle!rps"):
    await rps(message)
  
  elif msg.startswith("eagle!idol"):
    await message.channel.send("Nice try fuckface")

  elif msg.startswith("eagle!advice"):
    await advice(message)
  
  elif msg.startswith("eagle!alliancename"):
    await changeAllianceName(message)

  elif msg.startswith("eagle!entervote"):
    await enterVote(message)
  
  elif msg.startswith("eagle!setvotes"):
    await setVoteCount(message)

  elif msg.startswith("eagle!readvotes"):
    await readVotes(message)

  elif msg.startswith("eagle!clearvotes"):
    await clearVotes(message)

  elif msg.startswith("eagle!getvotes"):
    await getVotes(message)

  elif msg.startswith("eagle!horserace"):
    await horseRace(message)
  
  elif msg.startswith("eagle!poll"):
    await poll(message)

  elif msg.startswith("eagle!tiebreaker"):
    await tiebreaker(message)

  elif msg.startswith("eagle!morgan"):
    await morgan(message)
  
  elif msg.startswith("eagle!pick"):
    await pick(message)
  
  elif msg.startswith("eagle!jotto"):
    await jotto.jotto(message)
  
  else:
    await players.processCommand(message)



async def rocks(message, msg):
  if message.channel.id in rocksIDs or message.author.guild_permissions.administrator:
    await message.channel.send("Coming right up!")
    fools = message.content.split()
    fools.pop(0)
    random.shuffle(fools)
    lenOfFools = len(fools)
    await message.channel.send("Order: " + ", ".join(fools))
    for fool in fools:
      time.sleep(3)
      if (lenOfFools == 1):
        await message.channel.send("As everyone left has drawn a safe rock, " + fool + " has been eliminated")
        return
      await message.channel.send("Currently drawing a rock: " + fool)
      drawNumber = random.randint(1, (lenOfFools + 1))
      await message.channel.send("-\n-")
      time.sleep(3)
      if drawNumber == 1:
        await message.channel.send(fool + " has drawn the white rock. They have been eliminated.")
        return
      else:
        await message.channel.send(fool + " has drawn a black rock. They are safe.")
        lenOfFools = lenOfFools - 1
        await message.channel.send("-\n-")
  else:
    await message.channel.send("Not a valid channel to draw rocks.")

async def swap(message):
  if message.channel.category_id in swapIDs or message.author.guild_permissions.administrator:
    swapTribes = {"Shooting Stars 2.0": [], "Pine Trees 2.0": []}
    maxPerTribe = 8
    swappers = message.content.split()
    swappers.pop(0)
    random.shuffle(swappers)
    counter = 0
    await message.channel.send("We will be swapping into two tribes: <@&792949198789804053> and <@&792949264200368129>")
    time.sleep(7)
    await message.channel.send("-\n-\n-")
    while (counter < 16):
      swapTribes.get("Shooting Stars 2.0").append(swappers[counter])
      await message.channel.send(swappers[counter] + " will be swapped to <@&792949198789804053>")
      time.sleep(7)
      counter = counter + 1
      await message.channel.send("-\n-")
      swapTribes.get("Pine Trees 2.0").append(swappers[counter])
      await message.channel.send(swappers[counter] + " will be swapped to <@&792949264200368129>")
      time.sleep(7)
      counter = counter + 1
      await message.channel.send("-\n-")
    for tribe in swapTribes:
      await message.channel.send("=== THE **" + tribe + "** TRIBE ===")
      for tribeMember in swapTribes.get(tribe):
        time.sleep(2)
        await message.channel.send("**" + tribeMember + "**")
    await message.channel.send("========================")

async def rps(message):
  rpsMsg = message.content.split()
  rpsMsg.pop(0)
  rpsInt = random.randint(1, 4)
  if rpsMsg[0].lower() == "paper":
    if rpsInt == 1:
      await message.channel.send(message.author.nick + " used paper, I chose rock. " + message.author.nick + " wins.")
    elif rpsInt == 2:
      await message.channel.send(message.author.nick + " used paper, I chose paper. Draw.")
    elif rpsInt == 3:
      await message.channel.send(message.author.nick + " used paper, I chose scissors. " + message.author.nick + " loses.")
  elif rpsMsg[0].lower() == "scissors":
    if rpsInt == 1:
      await message.channel.send(message.author.nick + " used scissors, I chose rock. " + message.author.nick + " loses.")
    elif rpsInt == 2:
      await message.channel.send(message.author.nick + " used scissors, I chose paper. " + message.author.nick + " wins.")
    elif rpsInt == 3:
      await message.channel.send(message.author.nick + " used scissors, I chose scissors. Draw.")
  elif rpsMsg[0].lower() == "rock":
    if rpsInt == 1:
      await message.channel.send(message.author.nick + " used rock, I chose rock. Draw.")
    elif rpsInt == 2:
      await message.channel.send(message.author.nick + " used rock, I chose paper. " + message.author.nick + " loses.")
    elif rpsInt == 3:
      await message.channel.send(message.author.nick + " used rock, I chose scissors. " + message.author.nick + " wins.")
  else:
    await message.channel.send("Not rock paper or scissors")

async def advice(message):
  advice = ["Remember, it is illegal to lick doorknobs on other planets", "When in doubt, break out the chainsaw.", "Have you tried not being a loser?", "Force rocks.", "If you're looking for an idol clue in here, you're a moron.", "Stop playing ORGs and go outside", "I don't cheat in Rock Paper Scissors, you just suck.", "Break up with them, hit the lawyer, hire a gym", "Find the nearest toddler and punt them into the ocean", "When in doubt, shit it out!", "Not even God can help you now.", "Did you try complaining about it on Twitter.com", "Why are you asking me? I don't know you, and I don't want to either.", "Try turning it off and on again", "You cannot expect me to love you back, I have no soul.", "Git gud.", "Do eagle!idol for a special surprise!", "The real Legal Eagle is the friends we made along the way", "Did you set it to wumbo?", "Don't look behind you.", "Hit it with a shovel", "I will never give you up, I will never let you down", "Why are you wearing that stupid man suit?", "Don't be cringe, be based", "Just because pwned died in 2010 doesn't mean I'm not about to pwn you into next week", "Touch some grass", "Trans rights", "If you wanna win bingo, start shittalking the old lady running the show.", "Become a Karen, ask to see the manager. It will work, they don't get paid enough to fight back.", "Being epic is not a personality trait, it is a lifestyle", "Deez nuts", "I love you.... just kidding!", "Give me your gold, surrender all of your worldy possessions to me.", "If you're gonna join a cult, at least join one that gives dental benefits.", "Math is stupid, what's a geometry?", "Triangles were made by the government to sell protractors.", "Instead of doing stand up comedy, maybe you should sit down and take some notes on how to actually be funny"]
  random.shuffle(advice)
  await message.channel.send(advice[0])

async def changeAllianceName(message):
  #Shooting Star Alliances, Pine Tree Alliances, Host Category
  
  if message.channel.category_id in allianceIDs or message.author.guild_permissions.administrator:
    nameList = message.content.split()
    if len(nameList) > 2:
      await message.channel.send("Alliance names must be 1 word, no spaces. Use - for spaces if you need to. Example: eagle!alliancename dipper-pines")
      return
    nameList.pop(0)
    newName = nameList[0]
    await message.channel.edit(name = newName)
    await message.channel.send("Name successfully changed.")
  else:
    await message.channel.send("Not an alliance category.")

async def enterVote(message):
  if message.channel.category_id in hostIDs or message.author.guild_permissions.administrator:
    voteList = message.content.split()
    voteList.pop(0)
    if voteList[0] not in votes:
      votes[voteList[0]] = [voteList[1]]
      await message.channel.send("Vote added.")
    else:
      votes[voteList[0]].append(voteList[1])
      await message.channel.send("Vote added.")

async def setVoteCount(message):
  newVoteCount = message.content.split()
  newVoteCount.pop(0)
  voteCounter = str(newVoteCount[0])
  await message.channel.send("New vote count: " + str(voteCounter))

async def clearVotes(message):
  if message.channel.category_id in hostIDs or message.author.guild_permissions.administrator:
    votes.clear()
    await message.channel.send(votes)

async def getVotes(message):
  if message.channel.category_id in hostIDs or message.author.guild_permissions.administrator:
    await message.channel.send(votes)

async def readVotes(message):
  if message.channel.category_id in hostIDs or message.author.guild_permissions.administrator:
    msg = message.content.split()
    readInt = int(msg[1])
    loopInt = 0
    revealed = {}
    while loopInt < readInt:
      for voted in votes:
        if len(votes[voted]) > 0:
          time.sleep(2)
          await message.channel.send("**VOTE " + str(loopInt + 1) + ":**")
          time.sleep(2)
          await message.channel.send(votes[voted][0])
          if voted not in revealed:
            revealed[voted] = 1
          else:
            revealed[voted] = revealed[voted] + 1
          time.sleep(2)
          votes[voted].pop(0)
          await message.channel.send("**" + voted + "**")
          time.sleep(2)
          loopInt = loopInt + 1
          if (loopInt < readInt):
            await message.channel.send("-\n-\n-\n-\n-")
      if loopInt == readInt:
        await message.channel.send("**FINAL RESULTS:**")
      for voted in revealed:
        time.sleep(1)
        if revealed[voted] == 1:
          await message.channel.send("**" + str(revealed[voted]) + " vote " + voted + "**")
        else:
          await message.channel.send("**" + str(revealed[voted]) + " votes " + voted + "**")
      if loopInt != readInt:
        time.sleep(2)
        await message.channel.send(str(readInt - (loopInt + 1)) + " votes left.")
      if (loopInt < readInt):
            await message.channel.send("-\n-\n-\n-\n-")

#TODO: let people change the amount of spaces
async def horseRace(message):
  if message.channel.id in botChannelIDs or message.author.guild_permissions.administrator:
    horses = message.content.split()
    horses.pop(0)
    moveInt = 0
    spaces = 25
    horseInt = int(horses[0])
    horseDict = {}
    if horseInt > 10:
      horseInt = 10
    for i in range(horseInt):
      horseDict[i] = 0
    finish = False
    raceString = ""
    for horse in horseDict:
      raceString = raceString + ((horseDict[horse]*"-") + str(horse) + ((spaces - horseDict[horse])*"-") + "\n")
    await message.channel.send(27*"=")
    await message.channel.send(raceString)
    await message.channel.send(27*"=")
    time.sleep(3)
    winString = ""
    while not finish:
      for horse in horseDict:
        moveInt = random.randint(1, 4)
        horseDict[horse] = horseDict[horse] + moveInt
        if horseDict[horse] >= spaces:
          horseDict[horse] = spaces
          finish = True
          winString = winString + "**HORSE " + str(horse) + " WINS!** "
      raceString = ""
      for horse in horseDict:
        raceString = raceString + ((horseDict[horse]*"-") + str(horse) + ((spaces - horseDict   [horse])*"-") + "\n")
      await message.channel.send(raceString)
      await message.channel.send(27*"=")
      time.sleep(3)
    await message.channel.send(winString)
  else:
    await message.channel.send("Hold yer horses pardner, this isn't a valid horse racin channel.")

async def poll(message):
  await message.add_reaction("👍")
  await message.add_reaction("👎")
  await message.add_reaction("🤷‍♀️")

async def tiebreaker(message):
  await message.channel.send("How many green and white squares are there? You can give the number for each or say the total, either works. Accuracy counts first, then time if accuracy is tied.\n\n :white_large_square::brown_square::green_square::purple_square::blue_square::green_square::orange_square::red_square::green_square::purple_square::yellow_square:\n :orange_square::purple_square::red_square::green_square::white_large_square::red_square::blue_square::orange_square::green_square::yellow_square::orange_square:\n :orange_square::green_square::white_large_square::white_large_square::red_square::red_square::yellow_square::green_square::brown_square::purple_square::green_square:\n :blue_square::blue_square::white_large_square::white_large_square::red_square::green_square::white_large_square::purple_square::red_square::brown_square::green_square:\n :white_large_square::green_square::green_square::blue_square::brown_square::white_large_square::blue_square::white_large_square::purple_square::purple_square::yellow_square:\n :red_square::yellow_square::purple_square::white_large_square::purple_square::orange_square::purple_square::white_large_square::green_square::purple_square::blue_square:\n :white_large_square::purple_square::yellow_square::brown_square::brown_square::green_square::blue_square::blue_square::yellow_square::yellow_square::blue_square:\n :orange_square::blue_square::brown_square::yellow_square::brown_square::red_square::orange_square::blue_square::orange_square::red_square::brown_square:\n :brown_square::blue_square::orange_square::orange_square::blue_square::purple_square::green_square::red_square::blue_square::green_square::purple_square:\n :yellow_square::red_square::purple_square::yellow_square::green_square::green_square::white_large_square::white_large_square::red_square::green_square::red_square:\n :yellow_square::purple_square::yellow_square::orange_square::yellow_square::purple_square::brown_square::white_large_square::yellow_square::red_square::red_square:")

async def morgan(message):
  embed=discord.Embed(title="Cool's Survivor:", description="Bora Bora; France", color=0x00bfff)
  embed.set_author(name="Morgan", url="https://cdn.discordapp.com/avatars/142423466279305216/6f6ed3624b86361b61d43014d26a5bdf.png?size=1024 ", icon_url="https://cdn.discordapp.com/avatars/142423466279305216/6f6ed3624b86361b61d43014d26a5bdf.png?size=1024")
  embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/142423466279305216/6f6ed3624b86361b61d43014d26a5bdf.png?size=1024")
  embed.add_field(name="Placements:", value="13th; 1st", inline=False)
  await message.channel.send(embed=embed)

async def pick(message):
  fools = message.content.split()
  fools.pop(0)
  random.shuffle(fools)
  await message.channel.send(fools[0])

ka.ka()

jotto.initiate()
client.run(os.getenv("TOKEN"))