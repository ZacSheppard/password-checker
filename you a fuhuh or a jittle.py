import gooeypie as gp

def say_jittle(event):
    jittle_lbl.text = 'grrrrr ⚡👨🏿⚡'
    jittle_img.image = 'images/fuhuh_image.png'

def say_fuhuh(event):
    fuhuh_lbl.text = '𝔂𝓸𝓾 𝓻𝓮𝓪𝓵 𝓪𝓼𝓯 𝓿𝓻𝓸 🤝'
    fuhuh_img.image = 'images/jittle_image.png'
    

app = gp.GooeyPieApp('josh sigma')
app.width = 400
app.height = 200

jittle_btn = gp.Button(app, 'jittleyang', say_jittle)
jittle_lbl = gp.Label(app, '')
jittle_img = gp.Image(app, 'images/Empty.png')

fuhuh_btn = gp.Button(app, 'fuhuhlatoogan', say_fuhuh)
fuhuh_lbl = gp.Label(app, '')
fuhuh_img = gp.Image(app, 'images/Empty.png')



app.set_grid(3, 2)
app.add(jittle_btn, 1, 1, align='center')
app.add(jittle_lbl, 2, 1, align='center')
app.add(jittle_img, 3, 1, align ='center')

app.add(fuhuh_btn, 1, 2, align='center')
app.add(fuhuh_lbl, 2, 2, align='center')
app.add(fuhuh_img, 3, 2, align ='center')
app.run()