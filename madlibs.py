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
else: #edge case if someone selects a different number
    print("Invalid choice. Please select 1, 2, or 3.")

#Note: in python if runs if true, then elif(else if) or multile Adds additional conditions to check after the initial if
# and only the last condition can be else, acts as a catch all when all else fails#

#Lets create all the variables for the first story

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


story_one_template = f'''This weekend I am going camping with {story_one_inputs[0]}. I packed my lantern, sleeping bag, and
{story_one_inputs[1]}. I am so {story_one_inputs[2]} to {story_one_inputs[3]} in a tent. I am {story_one_inputs[4]} we
might see a {story_one_inputs[5]}, they are kind of dangerous. We are going to hike, fish, and {story_one_inputs[6]}.
I have heard that the {story_one_inputs[7]} lake is great for {story_one_inputs[8]}. Then we will
{story_one_inputs[9]}hike through the forest for {story_one_inputs[10]} {story_one_inputs[11]}. If I see a
{story_one_inputs[12]} {story_one_inputs[13]} while hiking, I am going to bring it home as a pet! At night we will tell
{story_one_inputs[14]} {story_one_inputs[15]} stories and roast {story_one_inputs[16]} around the campfire!!'''

#Notes from chat: Use triple quotes (""" or ''') to define a multiline string in Python. This avoids issues with line breaks 
# and makes your code easier to read. ALSO nstead of {input}, you should reference the elements of your story_one_inputs list using placeholders like {story_one_inputs[0]}, 
# {story_one_inputs[1]}, etc. since input is reserved method by python to take user inputs#

print("---------------------------------")
print("HERE IS YOUR COMPLETE STORY:")
print("\n")

print(story_one_template)