# # Pylance: disable reportUndefinedValue
# from pyscript import document


# def create_story(event): #define a function
#     #we want to extract the inputs and loop through them, and then use fstring concatentaion to place 
#     # them in the right place within the story
#     # Inputs are gathered dynamically using a loop and stored in a list for use in the template.#
#     event.preventDefault()  # Prevent the form from submitting and reloading the page
#     print("Form submitted!")  # This should appear in the browser console (use Python's print() in PyScript)

#     inputs = [document.querySelector(f"#input-{i}").value for i in range(17)]  #selct the input value using the id, get the value of each, and loop through them from 0 -17 (akak 16 total inputs)

#     #now lets use contatenation
#     story_template = f"""
#     This weekend I am going camping with {inputs[0]}. I packed my lantern, sleeping bag, and
#     {inputs[1]}. I am so {inputs[2]} to {inputs[3]} in a tent. I am {inputs[4]} we
#     might see a {inputs[5]}, they are kind of dangerous. We are going to hike, fish, and {inputs[6]}.
#     I have heard that the {inputs[7]} lake is great for {inputs[8]}. Then we will
#     {inputs[9]}hike through the forest for {inputs[10]} {inputs[11]}. If I see a
#     {inputs[12]} {inputs[13]} while hiking, I am going to bring it home as a pet! At night we will tell
#     {inputs[14]} {inputs[15]} stories and roast {inputs[16]} around the campfire!!
# """

#     #lets target the output div and update it with the final story using innerText.
#     output_div = document.querySelector("#output")
#     output_div.innerText = story_template

# form = document.querySelector("#madlibs-form")
# form.addEventListener("submit", create_story)



from pyscript import document

def create_story(event):
    event.preventDefault()  # Prevent the form from submitting and reloading the page
    print("Form submitted!")  # This should appear in the browser console (use Python's print() in PyScript)

    inputs = [document.querySelector(f"#input-{i}").value for i in range(17)]

    story_template = f"""
    This weekend I am going camping with {inputs[0]}. I packed my lantern, sleeping bag, and
    {inputs[1]}. I am so {inputs[2]} to {inputs[3]} in a tent. I am {inputs[4]} we
    might see a {inputs[5]}, they are kind of dangerous. We are going to hike, fish, and {inputs[6]}.
    I have heard that the {inputs[7]} lake is great for {inputs[8]}. Then we will
    {inputs[9]}hike through the forest for {inputs[10]} {inputs[11]}. If I see a
    {inputs[12]} {inputs[13]} while hiking, I am going to bring it home as a pet! At night we will tell
    {inputs[14]} {inputs[15]} stories and roast {inputs[16]} around the campfire!!
    """

    output_div = document.querySelector("#output")
    output_div.innerText = story_template

# Attach event listener to form
form = document.querySelector("#madlibs-form")
form.addEventListener("submit", create_story)
