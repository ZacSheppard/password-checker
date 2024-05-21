import gooeypie as gp
import re

with open("cian is cute.txt", "r") as file:
    file_content = file.read()

eye = 2
pattern = r'\d'

def EYE(event):
    global eye
    eye =+ 3

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
        score = score + 20
    if text.isdigit():
        score = score + 10
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
        label.text = "bad "

app = gp.GooeyPieApp(">:)")
app.width = 400
app.height = 100

eye_btn = gp.Button(app, 'sneak peek?', EYE)


if eye % 2 != 0:
    text_box = gp.Input(app)
    text_box.add_event_listener('change', textbox)
else:
    text_box = gp.Secret(app)
    text_box.add_event_listener('change', textbox)





label = gp.Label(app, '')
app.set_grid(2,2)
app.add(text_box, 1, 1)
app.add(label, 2, 1)
app.add(eye_btn, 1, 2, align='center')

app.run()