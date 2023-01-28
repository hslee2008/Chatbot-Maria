import random as r
import dict, os

def intro():
  print(r'''
 __  __   ___                        .--.
|  |/  `.'   `.                      |__|
|   .-.  .-.   '            .-,.--.  .--.
|  |  |  |  |  |     __     |  .-. | |  |     __
|  |  |  |  |  |  .:--.'.   | |  | | |  |  .:--.'.
|  |  |  |  |  | / |   \ |  | |  | | |  | / |   \ |
|  |  |  |  |  | `" __ | |  | |  '-  |  | `" __ | |
|__|  |__|  |__|  .'.''| |  | |      |__|  .'.''| |
                 / /   | |_ | |           / /   | |_
                 \ \._,\ '/ |_|           \ \._,\ '/
                  `--'  `"                 `--'  `"
Maria Version 1.0.0
© 2021 by Hyunseung Lee
''')


def randitem(arr):
  print(r.choice(arr))

def ask():
  return input(">>> ").lower().strip()


def learnNewThing():
  learn = input("Let me learn!(y, n): ")

  if learn == "y":
    with open(r".\dict.py", "a", encoding="UTF-8") as f:
      f.write('urd.update(' + str({input("Title: "): {"ur": input("User Response seperated by commas: ").split(','), "cr": input("Computer Response seperated by commas: ").split(','), "keyword": input("Keywords seperated by commas: ").split(',')}}) + ')')
      randitem(["learned a new thing!", "thanks!", "wow. it is good to konw that", "^_____^"])
  elif learn == "n":
    return
  else:
    randitem(["Please try again", r"¯\(°_o)/¯", "Try again...", "Entred the wrong thing!"])
    learnNewThing()


def check():
  ur = ask()

  for i in dict.urd.values():
    if ur in i["ur"]:
      if isinstance(i["cr"], str):
        exec(i["cr"])
      else:
        randitem(i["cr"])
      return
    else:
      for a in i["keyword"]:
        if a in ur:
          randitem(i["cr"])
          return

  randitem(["Hmmm... ◑﹏◐", "What?", "I could not understand when you use " + ur, "what do you mean by " + ur, "please try again"])
  learnNewThing()
  return

def clearConsole():
  os.system("cls")

def main():
  while True:
    try: check()
    except KeyboardInterrupt:
      print('\n\n' + r.choice(["(っ °Д °;)っ", "Bye!", "See you later!", "See ya!"]) + "\n")
      exit()
