from groupy import Client


file = open("groupMeToken.txt", 'r')
fileLines = file.readlines()
token = fileLines[0][0:-1]

client = Client.from_token(token)

groups = list(client.groups.list_all())

while True:
  print("What is the name group would you like to analyze? ")
  groupName = input()

  groupChoice = groups[0]

  for group in groups:
    index = group.name.find(groupName)
    if index != -1:
      groupChoice = group
      break

  print(groupChoice.name)
  print("If this is the group you want to analyze, then type \'Y\'. If not, then type \'N\' and give a unique substring of the name: ")
  response = input()
  if response == 'Y':
    break

all_messages = list(groupChoice.messages.list().autopage())

lastMessage = all_messages[-1].text
indexOfAdded = lastMessage.find("added")

print("The creator of the group is: " + lastMessage[0:indexOfAdded])

print("What word would you like to search for? ")
word = input()

numOfWords = 0
text = ''
indexOfWord = 0

for message in all_messages:
  text = message.text
  if text != None:
    while True:
      index = text.find(word)
      if index != -1:
        numOfWords += 1
        text = text[index]
      else:
        break

print("\'" + word + "\' occured " + str(numOfWords) + " times in " + groupChoice.name) 