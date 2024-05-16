###################################################
#         
#                 bmi CalCulator
#                 github : jokernets
####################################################


#importing libraries=============================================================
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

#saved Variable===================================================================
colorname = "#f0f1f5"
box_image="C:/ordibehesht-pro/week-3/BMI caculato/main/image/box.PNG"
scale_image="C:/ordibehesht-pro/week-3/BMI caculato/main/image/scale.PNG"
man_image="C:/ordibehesht-pro/week-3/BMI caculator/main/man.png"
#creating window===================================================================
root = Tk()
root.title('Bmi Calculator')
root.geometry('300x515')
root.resizable(False,False)
root.configure(bg=colorname)



# Start BMI Function===============================================================

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

# Frame  ===============================================================================
frame=Frame(root,bg="#48c9b0",width=290,height=40)
frame.place(x=5,y=30)

top_lbl=Label(frame,text="BMI CACULATOR",font=("Sylfaen 20 bold"),bg="#48c9b0",fg="black")
top_lbl.place(x=30,y=0)

#bottom box==========================================================================
Label(root, width=72, height=18, bg="lightblue").pack(side="bottom", anchor="center")


#importing main Image to PIl =====================================================
img = Image.open("C:/ordibehesht-pro/week-3/BMI caculator/main/image/box.png")
img = img.resize((90, 90))
img = ImageTk.PhotoImage(img)
app_image = Label(root, height=130, padx=130, anchor="nw", image=img, bg=colorname)
app_image.place(x=40, y=100)

img1 = Image.open("C:/ordibehesht-pro/week-3/BMI caculator/main/image/box.png")
img1 = img1.resize((90, 90))
img1 = ImageTk.PhotoImage(img1)
app_image1 = Label(root, height=120, padx=120, anchor="nw", image=img, bg=colorname)
app_image1.place(x=160, y=100)

#scale===============================================================================
scale = PhotoImage(file='C:/ordibehesht-pro/week-3/BMI caculator/main/image/scale.png')
Label(root, image=scale, bg="lightblue").place(x=-10, y=250)



# created Slider 1 =====================================================================
current_value = tk.DoubleVar()
def get_current_value():
    return '{: .2f}'.format(current_value.get())


def slider_changed(event):
    Height.set(get_current_value())
    size=int(float(get_current_value()))
    img = (Image.open("C:/ordibehesht-pro/week-3/BMI caculator/main/image/man.png"))
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


# slider 2 ====================================================================

current_value2 = tk.DoubleVar()
def get_current_value2():
    return '{: .2f}'.format(current_value2.get())
def slider_changed2(event):
    Weight.set(get_current_value2())
# COMMAND TO CHANGE BACKGROUND COLOR OF SCALE
style2 = ttk.Style()
style2.configure("TScale", background=colorname)
slider2 = ttk.Scale(root, from_=0, to=200, orient="horizontal", style="TScale",
                    command=slider_changed2, variable=current_value2)
slider2.place(x=170, y=200)

#Entry===========================================================================
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

# Labels ==================================================================================
label1 = Label(root, font=("arial 60 bold"), bg="lightblue", fg="#fff")
label1.place(x=130, y=310)

label2 = Label(root, font=("arial 12 bold"), bg="lightblue", fg="#3b3a3a")
label2.place(x=130, y=400)

label3 = Label(root, font=("arial 5 bold"), bg="lightblue", fg="#fff")
label3.place(x=130, y=440)

# Button view report =================================================================================
Button(root, text="View Report", command=bmi, width=15, height=2,bd=0, font=("arial 10 bold"), bg="#1f6e68",
       fg="white",activeforeground="white",activebackground="#1f6e68").place(x=130, y=270)


root.mainloop()
print("GITHUB : JOKERNETS")
