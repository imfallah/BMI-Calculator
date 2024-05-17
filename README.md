<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>


<h1 align="center"> BMI Calcultor</h1>


### 🌏 Readme in [فارسی](https://github.com/jokernets/face-plot/tree/main/Fa.md)


<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>
<p align="center">
<img src="https://img.shields.io/badge/language-python-blue?style"/><img src="https://img.shields.io/github/stars/jokernets/BMI-Calculator"/><img src="https://img.shields.io/github/forks/jokernets/BMI-Calculator"/>
</p>

   


<h4 align="center">🛑Time to study 10 minutes⚠👁‍🗨</h4>

Table of contents✅✔
=================
<!--ts-->
   * 🔸[Installation⚠]()
   * 🔸[About Code👨🏽‍💻]()
   * 🔸[Mor Example💯🌏]()
     * 🥇[Project Video📺](#video-image-of-the-app-)
   * 🎁[`CONNECT ME🎃`](#%F0%9D%90%82%F0%9D%90%A8%F0%9D%90%A7%F0%9D%90%A7%F0%9D%90%9E%F0%9D%90%9C%F0%9D%90%AD-%F0%9D%90%8C%F0%9D%90%9E)
<!--te-->







# Installation⚠ [Download Image&Source code]()

## Install the Library with pip:

```python
pip install tk
pip install pillow
```
Update existing installation:`pip3 install (YOUR LIBRARY) --upgrade`
(update as often as possible because this library is under active development)

# Abot Code🎃:

## ➕ Creat Window:
1. You've imported the necessary modules: `tkinter`, `ttk`, and `PIL` (for working with images).
2. You've created a `Tk()` instance named `root`.
3. You've set the window title to "Bmi Calculator".
4. The window size is set to 300x515 pixels.
5. The window is not resizable.
6. The background color is set to `#f0f1f5`.

- Next steps:
- You'll need to add widgets (labels, buttons, entry fields, etc.) to your GUI for user input.
- Implement the BMI calculation logic. 
- Display the calculated BMI to the user.
```python
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
colorname = "#f0f1f5"
root = Tk()
root.title('Bmi Calculator')
root.geometry('300x515')
root.resizable(False,False)
root.configure(bg=colorname)
```

➕ Func bmi :
1. You've defined a function called `bmi()`.
2. Inside the function:
   - You retrieve the user's input for height and weight.
   - Convert the height from centimeters to meters (by dividing by 100).
   - Calculate the BMI using the formula: $$ \text{BMI} = \frac{\text{weight (kg)}}{\text{height (m)}^2} $$
   - Round the BMI value to an integer.
   - Print the calculated BMI.
   - Update the text of `label1` with the calculated BMI.

3. Next, you have some conditional statements:

   - If the BMI is less than or equal to 18.5, you set the text of `label2` to "Underweight" and then immediately overwrite it with "You have Lower!" (which seems like a typo).
   - If the BMI is greater than 25, you set the text of `label2` to "Normal" and then immediately overwrite it with "You have upper" (another typo).
   - Otherwise (if the BMI is not less than or equal to 18.5 and not greater than 25), you set the text of `label2` to "Oobs" (probably meant "Obese") and update `label3` with "Healthy Body."

A few things to consider:

- Make sure to fix the typos in your labels.
- You might want to display the BMI category (e.g., "Underweight," "Normal," "Obese") based on the calculated BMI value.
```python
def bmi():
    h = float(Height.get())
    w = float(weight.get())

    # convert height into metr
    m = h / 100
    bmi = round(float(w / m ** 2))
    print(bmi)
    label1.config(text=bmi)
    if bmi <= 18.5:
        label2.config(text="Under weight")
        label2.config(text="You have Lower!")
    if bmi > 25:
        label2.config(text="Normal")
        label2.config(text="You have upper")
    else:
        label2.config(text="Oobs")
        label3.config(text="Healty Body")
```

## ➕:
1. **Bottom Box Label:**
   - You've created a label with a width of 72 and height of 18.
   - The background color of this label is "lightblue."
   - It's placed at the bottom of your GUI, anchored to the center.
2. **Image Labels (`app_image` and `app_image1`):**
   - You've loaded an image named "box.png" twice (once for `app_image` and once for `app_image1`).
   - Resized both images to 90x90 pixels.
   - Created labels for each image (`Label`) with specified heights and padding.
   - Positioned `app_image` at coordinates (40, 100) and `app_image1` at coordinates (160, 100).
   - The anchor point for both images is set to the northwest corner (`anchor="nw"`).
3. **Scale Image Label:**
   - You've loaded an image named "scale.png" using `PhotoImage`.
   - Created a label to display this image.
   - The background color of this label is "lightblue."
   - Positioned it at coordinates (-10, 250)

[Download File]()
```python
# Frame  ====================================================
frame=Frame(root,bg="#48c9b0",width=290,height=40)
frame.place(x=5,y=30)

top_lbl=Label(frame,text="BMI CACULATOR",font=("Sylfaen 20 bold"),bg="#48c9b0",fg="black")
top_lbl.place(x=30,y=0)
#bottom box
Label(root, width=72, height=18, bg="lightblue").pack(side="bottom", anchor="center")
img = Image.open("box.png")
img = img.resize((90, 90))
img = ImageTk.PhotoImage(img)
app_image = Label(root, height=130, padx=130, anchor="nw", image=img, bg=colorname)
app_image.place(x=40, y=100)
img1 = Image.open("box.png")
img1 = img1.resize((90, 90))
img1 = ImageTk.PhotoImage(img1)
app_image1 = Label(root, height=120, padx=120, anchor="nw", image=img, bg=colorname)
app_image1.place(x=160, y=100)
#scale
scale = PhotoImage(file="scale.png")
Label(root, image=scale, bg="lightblue").place(x=-10, y=250)
```
<img src="https://github.com/jokernets/BMI-calce/blob/main/main/image/1.png" width=300 height=500></img>

1. **Slider 1 (`slider`):**
   - You've created a horizontal slider using `ttk.Scale`.
   - The slider ranges from 0 to 200.
   - The `slider_changed` function is called whenever the slider value changes.
   - Inside `slider_changed`:
     - You retrieve the current value of the slider using `current_value.get()`.
     - Convert the value to a formatted string with two decimal places.
     - Update the `Height` variable (which I assume is related to BMI calculation) with this value.
     - Resize an image named "man.png" based on the calculated size.
     - Update the image displayed in `secondimage` (which I assume is another label) with the resized image.
     - Adjust the position of `secondimage` based on the calculated size.
   - You've also configured the background color of the slider using `style`.
2. **Slider 2 (`slider2`):**
   - Similar to the first slider, you've created another horizontal slider using `ttk.Scale`.
   - The range is also from 0 to 200.
   - The `slider_changed2` function is called when the slider value changes.
   - Inside `slider_changed2`:
     - You retrieve the current value of the second slider using `current_value2.get()`.
     - Convert the value to a formatted string with two decimal places.
     - Update the `Weight` variable (which I assume is related to BMI calculation) with this value.
     - 
```python
## slider 1

current_value = tk.DoubleVar()
def get_current_value():
    return '{: .2f}'.format(current_value.get())
def slider_changed(event):
    Height.set(get_current_value())
    size=int(float(get_current_value()))
    img = (Image.open("man.png"))
    resized_image = img.resize((50,10+size))
    photo2=ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=40,y=480-size)
    secondimage.image=photo2
# COMMAND TO CHANGE BACKGROUND COLOR OF SCALE
style = ttk.Style()
style.configure("TScale", background=colorname)
slider = ttk.Scale(root, from_=0, to=200, orient="horizontal", style="TScale",
                   command=slider_changed, variable=current_value)
slider.place(x=40, y=200)
######   slider 2 #############
current_value2 = tk.DoubleVar()
def get_current_value2():
    return '{: .2f}'.format(current_value2.get())
def slider_changed2(event):
    Weight.set(get_current_value2())
# COMMAND TO CHANGE BACKGROUND COLOR OF SCALE
style2 = ttk.Style()
style2.configure("TScale", background=colorname)
slider2 = ttk.Scale(root, from_=0, to=200, orient="horizontal", style="TScale",command=slider_changed2, variable=current_value2)
slider2.place(x=170, y=200)
```
<img src="https://github.com/jokernets/BMI-calce/blob/main/main/image/2.png" width=300 height=500></img>
## ➕Run :
1. **Height Entry (`height`):**
   - You've created an entry widget (`Entry`) for the user to input their height.
   - The `textvariable` is set to `Height`, which I assume is a `StringVar` variable.
   - The width of the entry field is set to 5 characters.
   - Font size is 20, background color is white, and text color is black.
   - The border (`bd`) is set to 0 (no border).
   - The text alignment is centered.
   - The entry field is positioned at coordinates (50, 130).
2. **Weight Entry (`weight`):**
   - Similar to the height entry, you've created an entry widget for weight.
   - The `textvariable` is set to `Weight`.
   - Other properties (width, font, background, text color, etc.) are the same as for the height entry.
   - The entry field is positioned at coordinates (170, 130).
3. **Second Image Label (`secondimage`):**
   - You've created a label with a light blue background.
   - This label is currently empty (no image displayed).
   - It's positioned at coordinates (300, 515).

```python
Height = StringVar()
Weight = StringVar()
height = Entry(root, textvariable=Height, width=5, font="arial 20", bg="white", fg="#000", bd=0, justify=CENTER)
height.place(x=50, y=130)
Height.set(get_current_value())
weight = Entry(root, textvariable=Weight, width=5, font="arial 20", bg="white", fg="#000", bd=0, justify=CENTER)
weight.place(x=170, y=130)
Weight.set(get_current_value2())
secondimage = Label(root, bg="lightblue")
secondimage.place(x=300, y=515)
```

## :
1. **Second Image Label (`secondimage`):**
   - You've created another label with a light blue background.
   - This label is currently empty (no image displayed).
   - It's positioned at coordinates (300, 515).
2. **BMI Display Labels (`label1`, `label2`, and `label3`):**
   - `label1`: A large label (font size 60) for displaying the calculated BMI.
   - `label2`: A smaller label (font size 12) for displaying BMI category (e.g., "Underweight," "Normal," "Obese").
   - `label3`: An even smaller label (font size 5) for additional information (e.g., "Healthy Body").
   - All labels have a light blue background.
3. **"View Report" Button:**
   - You've added a button labeled "View Report."
   - The button triggers the `bmi` function when clicked.
   - The button has a custom style (font size 10, background color, and text color).
   - It's positioned at coordinates (130, 270).
```python
secondimage = Label(root, bg="lightblue")
secondimage.place(x=300, y=515)
label1 = Label(root, font=("arial 60 bold"), bg="lightblue", fg="#fff")
label1.place(x=130, y=310)
label2 = Label(root, font=("arial 12 bold"), bg="lightblue", fg="#3b3a3a")
label2.place(x=130, y=400)
label3 = Label(root, font=("arial 5 bold"), bg="lightblue", fg="#fff")
label3.place(x=130, y=440)
Button(root, text="View Report", command=bmi, width=15, height=2,bd=0, font=("arial 10 bold"), bg="#1f6e68",
       fg="white",activeforeground="white",activebackground="#1f6e68").place(x=130, y=270)
root.mainloop()
```
## More Examples and Showcase 👑

### Video image of the APP 📺

<img src="https://github.com/jokernets/BMI-calce/blob/main/main/image/csd.png" width=300 height=500></img>
<img src="https://github.com/jokernets/BMI-calce/blob/main/main/image/bmigif.gif" width=300 height=500></img>
# `𝐂𝐨𝐧𝐧𝐞𝐜𝐭 𝐌𝐞`🎈🎃

<a herf="https://www.buymeacoffee.com/jokernets"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="180px">
<a href="mailto:joker.until33@gmail.com"><img align="center" width="60px" src="https://github.com/edent/SuperTinyIcons/raw/master/images/svg/gmail.svg" style="max-width: 100%;"></a><a href="https://www.linkedin.com/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/mohammadfallahnejad/" height="40" width="60" /></a>
