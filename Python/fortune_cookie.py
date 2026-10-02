import random

def fortune():
  message = [
"Don't pursue happiness – create it.",
'All things are difficult before they are easy.',
'The early bird gets the worm, but the second mouse gets the cheese.',
'Someone in your life needs a letter from you.',
"Don't just think. Act!",
'Your heart will skip a beat.',
'The fortune you search for is in another cookie.',
"Help! I'm being held prisoner in a Chinese bakery!"
  ]

  fortune = random.randint(1,8)
  
  if fortune == 1:
    print(message[0])
  elif fortune == 2:
    print(message[1])
  elif fortune == 3:
    print(message[2])
  elif fortune == 4:
    print(message[3])
  elif fortune == 5:
    print(message[4])
  elif fortune == 6:
    print(message[5])
  elif fortune == 7:
    print(message[6])
  elif fortune == 8:
    print(message[7])
    
fortune()