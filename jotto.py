import random
import time

"""
JOTTOCHECKER v1.0 by Morgan
a is the word that is being guessed
b is the word that the player just guessed, it is blank for now but will work
    when the program actually runs
The program should run until the word is guessed. I do not check for
    erroneous inputs (for instance, if you make a typo, it can't reverse that)
    so make sure to be careful when inputting words.
Oh yeah, also make sure your input is all caps, I think this is case sensitive
"""
playerDict = {}
doogis = []
doogisBank = []

def initiate():
  inFile = "bigwordlist.txt"
  with open(inFile, 'r') as f:
    wordLines = f.readlines()
    for wordLine in wordLines:
        wordLine = wordLine.strip('\n')
        words = wordLine.split()
        doogis.extend(words)
  print(len(doogis))
  inFile = "wordbank.txt"
  with open(inFile, 'r') as f:
    wordLines = f.readlines()
    for wordLine in wordLines:
        wordLine = wordLine.strip('\n')
        words = wordLine.split()
        doogisBank.extend(words)
  print(len(doogisBank))

async def jotto(message):
  msg = message.content.split()
  b = "FAILURE"
  if len(msg) > 1:
    b = msg[1]
  else:
    await message.channel.send("You need to include a guess")
    return
  if len(b) != 5:
    await message.channel.send("Your guess needs to be 5 letters")
    return
  if b.upper() not in doogisBank:
    await message.channel.send(b + " is not a valid 5 letter word.")
    return
  a = ''
  
  if message.author.nick not in playerDict:
    random.shuffle(doogis)
    a = "joker"
    playerDict[message.author.nick] = [a, 0]
  
  c = playerDict.get(message.author.nick)
  a = c[0]

  await message.channel.send("==========================================")
  #playerDict[message.author.nick[1]] = playerDict[message.author.nick[1]] + 1
  aDict = {}
  for letter in a:
      if letter not in aDict:
          aDict[letter] = 1
      else:
          aDict[letter] = aDict[letter] + 1
  #await message.channel.send ("TURN " + str(playerDict[message.author.nick[1]]))
  await message.channel.send("Word Guessed: " + b)
  #print("Letter Frequency Count of Word to Guess: ")
  #print(aDict)
  for letter in b:
      if letter in aDict:
          if aDict[letter] > 0:
              aDict[letter] = aDict[letter] - 1
  counter = 0
  for letter in aDict:
      counter = counter + aDict[letter]
  #print("Letters not in the Word Guessed:")
  #print(aDict)
  #print("Letters shared by the Word to Guess and Word Guessed:")
  await message.channel.send("GUESS " + ": " + str(5 - counter))
  await message.channel.send("==========================================")
  if (a == b):
    await message.channel.send("The word has been guessed!")
    playerDict.pop(message.author.nick)