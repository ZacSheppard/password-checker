import gooeypie as gp
import re

with open("cian is cute.txt", "r") as file:
    file_content = file.read()

def idkwhattocallthis():
    advice_list = [length_advice,sigma]
    updated_advice_list = list(filter(None, advice_list))
    advice.text = "\n".join(updated_advice_list)
    


eye = 2
pattern = r'\d'
length_advice = "rizz"
sigma = "cian is my king"
advice_list = ""
updated_advice_list = ""
def EYE(event):
    global eye
    eye =+ 1
    text_box.toggle()
    

def textbox(event):
    global length_advice
    global advice_list
    global updated_advice_list
    text = text_box.text
    print(text)
    score = 0

    if len(text) > 5: 
        length_advice = ""
        idkwhattocallthis()
        score += 10
    else:  
        length_advice = "add more characters"
        idkwhattocallthis()
    if len(text) > 7: 
        score += 10
    if len(text) > 9:
        score += 5
    if len(text) > 11:
        score += 5
    if len(text) > 14:
        score += 5
    if len(text) > 19:
        score += 5
    if not text.isalnum():
        score = score + 20
    if text.isdigit():
        score = score + 10
    if text.isupper():
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
    elif score >= 70:
        label.text = "awesome sauce"
    elif score >= 60:
        label.text = "very good"
    elif score >= 40:
        label.text = "good"
    elif score >= 30:
        label.text = "ok"
    elif score >= 20:
        label.text = "ehh"
    else: 
        label.text = "bad "
    
    
advice_list = [
    length_advice,
    length_advice]

app = gp.GooeyPieApp(">:)")
app.width = 400
app.height = 100
tabs_cont = gp.TabContainer(app)
tabs_cont.width = 400
tabs_cont.height = 100
tab1_tab = gp.Tab(tabs_cont, 'Password')
tab2_tab = gp.Tab(tabs_cont, 'Feedback')


eye_btn = gp.Button(tab1_tab, 'sneak peek?', EYE)


if eye % 2 != 0:
    text_box = gp.Input(tab1_tab)
    text_box.add_event_listener('change', textbox)
else:
    text_box = gp.Secret(tab1_tab)
    text_box.add_event_listener('change', textbox)

advice = gp.Label(tab2_tab,("\n".join(updated_advice_list)))
text_box.add_event_listener('change', textbox)



label = gp.Label(tab1_tab, '')
tab1_tab.set_grid(2,2)
tab1_tab.add(text_box, 1, 1)
tab1_tab.add(label, 2, 1)
tab1_tab.add(eye_btn, 1, 2, align='center')

tab2_tab.set_grid(1,2)
tab2_tab.add(advice, 1,1)

tabs_cont.add(tab1_tab)
tabs_cont.add(tab2_tab)

app.set_grid(2,2)
app.add(tabs_cont, 2, 2, fill=True, stretch=True)

app.run()