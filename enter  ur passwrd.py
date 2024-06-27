import gooeypie as gp
import re

# Open and read the content of the file "cian is cute.txt"
with open("cian is cute.txt", "r") as file:
    file_content = file.read()

# Function to update advice text based on current advice list
def idkwhattocallthis():
    advice_list = [listlist, length_advice5, speshspesh, upiesupies, numnum]
    updated_advice_list = list(filter(None, advice_list))
    advice.text = "\n".join(updated_advice_list)

# Function to check if a string contains any uppercase letters
def contains_uppercase(s):
    for char in s:
        if char.isupper():
            return True
    return False

# Function to check if a string contains more than two uppercase letters
def contains_more_than_two_uppercase(s):
    count = 0
    for char in s:
        if char.isupper():
            count += 1
        if count > 2:
            return True
    return False

# Initialize global variables
eye = 2
pattern = r'\d'  # Regex pattern to match digits
length_advice5 = "add more characters"
numnum = "Add some numbers"
speshspesh = "Add some special characters like #, @, !, etc."
upiesupies = "Add some uppercase characters"
listlist = ""

advice_list = "  "
updated_advice_list = "  "

# Event handler for toggling password visibility
def EYE(event):
    global eye
    eye += 1
    text_box.toggle()

# Event handler for updating the password score and advice
def textbox(event):
    global length_advice5
    global advice_list
    global updated_advice_list
    global speshspesh
    global upiesupies
    global numnum
    global listlist
    text = text_box.text
    print(text)
    score = 0

    # Check password length and update score and advice
    if len(text) > 5: 
        length_advice5 = "add more characters"
        idkwhattocallthis()
        score += 10
    else:  
        length_advice5 = "add more characters"
        idkwhattocallthis()
    if len(text) > 7: 
        score += 10
        length_advice5 = "add more characters!"
        idkwhattocallthis()
    if len(text) > 9:
        score += 5
        length_advice5 = "Add More characters!"
        idkwhattocallthis()
    if len(text) > 11:
        score += 5
        length_advice5 = "you have a good amount but adding more characters always helps!"
        idkwhattocallthis()
    if len(text) > 14:
        score += 5
        length_advice5 = "you have a good amount but adding more characters always helps!"
        idkwhattocallthis()
    if len(text) > 19:
        score += 5
        length_advice5 = ""
        idkwhattocallthis()
    
    # Check for special characters and update score and advice
    if not text.isalnum():
        score += 10
        speshspesh = ""
        idkwhattocallthis()
    else:
        speshspesh = "Add some special characters like #, @, !, etc."
        idkwhattocallthis()
    
    # Check for uppercase characters and update score and advice
    if contains_more_than_two_uppercase(text):
        score += 10
        upiesupies = ""
        idkwhattocallthis()
    else:
        if contains_uppercase(text):
            score += 5
            upiesupies = "Add a couple more uppercase characters"
            idkwhattocallthis()
        else:
            upiesupies = "Add some uppercase characters"
            idkwhattocallthis()
    
    # Check for numbers and update score and advice
    num_count = len(re.findall(pattern, text))
    if num_count >= 2:
        score += 10
        numnum = ""
        idkwhattocallthis()
    elif num_count == 1:
        score += 5
        numnum = "Add one more number"
        idkwhattocallthis()
    else:
        numnum = "Add some numbers"
        idkwhattocallthis()

    # Check if the password is in the common passwords file
    if text in file_content:
        score = 0 
        listlist = "This password is one of the most commonly used passwords in the world!\nmight wanna change it"
        idkwhattocallthis()
    else: 
        listlist = ""
        idkwhattocallthis()

    # Update the label based on the score
    if len(text) == 0:
        label.text = "Enter A Password And Have It Rated"
    elif text == "Sam":
        label.text = "ginger"
    elif score >= 70:
        label.text = "Password Rating:\n5 Stars! ★★★★★"
    elif score >= 60:
        label.text = "Password Rating:\n4 Stars ★★★★"
    elif score >= 40:
        label.text = "Password Rating:\n3 Stars ★★★"
    elif score >= 30:
        label.text = "Password Rating:\n2 Stars ★★"
    elif score >= 20:
        label.text = "Password Rating:\n1 Star ★"
    else: 
        label.text = "Password Rating:\nZero Stars"

# Initialize the advice list
advice_list = [
    length_advice5,
    speshspesh,
    upiesupies,
    numnum,
    listlist
]

# Create the GooeyPie app and set its dimensions
app = gp.GooeyPieApp("Enter ur Passwrd")
app.width = 410
app.height = 125

# Create tab container and set its dimensions
tabs_cont = gp.TabContainer(app)
tabs_cont.width = 410
tabs_cont.height = 125

# Create tabs for the tab container
tab1_tab = gp.Tab(tabs_cont, 'Password')
tab2_tab = gp.Tab(tabs_cont, 'Feedback')

# Create the show password button
eye_btn = gp.Button(tab1_tab, 'Show Password', EYE)

# Create the text box for password input
if eye % 2 != 0:
    text_box = gp.Input(tab1_tab)
    text_box.add_event_listener('change', textbox)
else:
    text_box = gp.Secret(tab1_tab)
    text_box.add_event_listener('change', textbox)

# Create the advice label
advice = gp.Label(tab2_tab, "\n".join(updated_advice_list))
text_box.add_event_listener('change', textbox)

# Create the label for displaying password rating
label = gp.Label(tab1_tab, 'Enter A Password And Have It Rated')

# Arrange the elements in the grid
tab1_tab.set_grid(2, 2)
tab1_tab.add(text_box, 1, 1)
tab1_tab.add(label, 2, 1)
tab1_tab.add(eye_btn, 1, 2, align='center')

tab2_tab.set_grid(1, 2)
tab2_tab.add(advice, 1, 1)

# Add tabs to the tab container
tabs_cont.add(tab1_tab)
tabs_cont.add(tab2_tab)

# Add the tab container to the app
app.set_grid(2, 2)
app.add(tabs_cont, 2, 2, fill=True, stretch=True)

# Run the app
app.run()
