print("Select Your Story!")
print("Select number 1, 2, or 3 to choose which story you would like\n 1.A Camping We Will Go! \n 2.My Stay at the Hospital \n 3.Enchanted Forest")

story_type = int(input("Whihc number story would you like?: "))

story_one = "A Camping We Will Go!"
story_two = "My Stay at the Hospital"
story_three = "Enchanted Forest"

if story_type == 1:
  print(f"Great! You've selected the story.....{story_one}")
elif story_type == 2:
  print(f"Great! You've selected the story.....{story_two}")
elif story_type == 3:
  print(f"Great! You've selected the story.....{story_three}")
else: #edge case if someone selects a differnt number
    print("Invalid choice. Please select 1, 2, or 3.")

#Note: in pyton if runs if true, then elif(else if) or multile Adds additional conditions to check after the initial if
# and only the last condition can be else, acts as a catch all when all else fails#

#Lets create all the variables for the first story

# Lets create all the variables for the first story
one = input("Proper Noun (Person’s Name): ")
two = input("Noun: ")
three = input("Adjective (Feeling): ")
four = input("Verb: ")
five = input("Adjective (Feeling): ")
six = input("Animal: ")
seven = input("Verb: ")
eight = input("Color: ")
nine = input("Verb (ending in ing): ")
ten = input("Adverb (ending in ly): ")
eleven = input("Number: ")
twelve = input("Measure of Time: ")
thirteen = input("Color: ")
fourteen = input("Animal: ")
fifteen = input("Number: ")
sixteen = input("Silly Word: ")
seventeen = input("Noun: ")



story_one_inputs = []
#lets put the users answers into a list to loop through and add to the template usinf f-strings later on
story_one_inputs.extend([one, two, three, four, five, 
    six, seven, eight, nine, ten, 
    eleven, twelve, thirteen, fourteen, 
    fifteen, sixteen, seventeen])

print(story_one_inputs)