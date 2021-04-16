# Gah, replit must be doing something with this code
main = raw_input('Well, it is the final class of the day and you are bored and tired. You think of throwing a rock at him (do not ask how), just out of spite since you are VERY cranky. Do you throw it at him?')

if main == 'Yes':
  print('You throw it at him. Your teacher angrily stares at you and yells "Mr Alan, I will be seeing you in detention!". Great, just what you needed to end a Monday.')


if main == 'No':
  print('You end up not throwing it at him, but you end up falling asleep. You wake up to a very angry teacher in front of you, who yells "Tired, Alan? Well, you aren not gonna be tired when I send you to detention!". This is why you hate mondays.')

main2 = raw_input('About 20 minutes later, the time comes. 2:30. Now, usually you would be all happy to leave this school, but YOU have to stay until 3:30 because of that idiot that gave you detention. You are sitting in a desk. Do you do your homework or try to escape?')

if main2 == "Homework":
  print("Nerd.... YOU FAIL!")

if main2 == "Escape":
  main3 = raw_input('So, you choose to escape? HOW are you gonna escape? The window, vents, or the door?')
# The window choice is broken for some reason
if main3 == "Window":
  print("The window is locked, doofus.")
if main3 == "Door":
  print("It's also locked, you idiot.")
if main3 == "Vents":
  main4 = raw_input("You use a desk to climb into the vents, and enter the main section of the vents. Which direction do you go? North, West, or South?")
if main4 == "North":
  print("Dead end.")
if main4 == "South":
  print("You go backwards and fall out the vents, and land on the desk. It was painful, but you manage to get up. Unfourtunately, a teacher walked in and saw you. YOU FAILED.")
if main4 == "West":
  main5 = raw_input("You go west. After about a minute or so, you finally see a exit. You climb out of the vents. You run out the door, but you are quickly stopped by a guard.'Hey! Where do you think you're going?' Crud. Do you lie to him, or tell the truth?'")
if main5 == "Truth":
  print('Why would you choose this? He sends you back to the detention room. You failed.')
if main5 == "Lie":
  print("You lie to him. You try to say you were in a after school club, but there ARE no after school clubs on Monday. You're busted, and HE knows too. He takes you back inside and takes you to the detention room, with a extra hour and a half added to your time, so now you leave at 5. Great. Now you're back at where you started.")
print("TO BE CONTINUED... BUY THE FULL EPISODE TO SEE WHAT HAPPENS TO ALAN, AND CONTINUE THE STORY.")