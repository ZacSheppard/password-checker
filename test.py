import gooeypie as gp
import re

# Load file content
with open("cian is cute.txt", "r") as file:
    file_content = file.read()

# Initialize eye variable and pattern
eye = 2
pattern = r'\d'

# Function to toggle the input box visibility
def EYE(event):
    global eye, text_box
    eye += 1
    
    # Remove the existing text box
    app.remove(text_box)

    # Toggle between Input and Secret based on the value of eye
    if eye % 2 != 0:
        text_box = gp.Input(app)
    else:
        text_box = gp.Secret(app)

    # Add the event listener to the new text box
    text_box.add_event_listener('change', textbox)
    
    # Re-add the text box to the app
    app.add(text_box, 1, 1)
    app.set_grid(2, 2)
    app.add(label, 2, 1)
    app.add(eye_btn, 1, 2, align='center')
    
    # Refresh the app
    app.run()

# Function to evaluate the input text and update the label
def textbox(event):
    text = text_box.text
    print(text)
    score = 0
    if len(text) > 5: 
        score += 10
    if len(text) > 7: 
        score += 10
    if len(text) > 9:
        score += 5
    if len(text) > 13:
        score += 5
    if not text.isalnum():
        score += 20
    if text.isdigit():
        score += 10
    if re.search(pattern, text):
        score += 10
    if text in file_content:
        score = 0 

    if len(text) == 0:
        label.text = ""
    elif text == "bladee":
        label.text = "greasy"
    elif text == "Sam":
        label.text = "ginger"
    elif score >= 50:
        label.text = "pretty decent"
    elif score >= 20:
        label.text = "ehh"
    else: 
        label.text = "bad"

# Create the application window
app = gp.GooeyPieApp(">:)")
app.width = 400
app.height = 100

# Create the sneak peek button
eye_btn = gp.Button(app, 'sneak peek?', EYE)

# Initial text box setup
if eye % 2 != 0:
    text_box = gp.Input(app)
else:
    text_box = gp.Secret(app)

# Add event listener to the text box
text_box.add_event_listener('change', textbox)

# Create the label for feedback
label = gp.Label(app, '')

# Set the grid layout and add widgets to the app
app.set_grid(2, 2)
app.add(text_box, 1, 1)
app.add(label, 2, 1)
app.add(eye_btn, 1, 2, align='center')

# Run the application
app.run()
