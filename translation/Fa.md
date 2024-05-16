<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>


<h1 align="center">محاسبه BMI😁</h1>


### 🌏 Readme in [English](https://github.com/jokernets/face-plot/tree/main/Fa.md)


<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>
<p align="center">
<img src="https://img.shields.io/badge/language-python-blue?style"/><img src="https://img.shields.io/github/stars/jokernets/face-plot"/><img src="https://img.shields.io/github/forks/jokernets/face-plot"/>
</p>

   


<h4 align="center">🛑Time to study 10 minutes⚠👁‍🗨</h4>

Table of contents✅✔
=================
<!--ts-->
   * 🔸[Installation⚠]()
   * 🔸[About Code👨🏽‍💻]()
   * 🔸[Mor Example💯🌏]()
     * 🥇[Project Video📺](#video-image-of-the-app-)
   * 🎁[`CONNECT ME🎃`]()
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
1. ماژول های لازم را وارد کرده اید: «tkinter»، «ttk» و «PIL» (برای کار با تصاویر).
2. شما یک نمونه «Tk()» با نام «root» ایجاد کرده‌اید.
3. عنوان پنجره را روی "Bmi Calculator" تنظیم کرده اید.
4. اندازه پنجره روی 300x515 پیکسل تنظیم شده است.
5. اندازه پنجره قابل تغییر نیست.
6. رنگ پس زمینه روی '#f0f1f5' تنظیم شده است.

- مراحل بعدی:
- برای ورودی کاربر باید ویجت‌ها (برچسب‌ها، دکمه‌ها، فیلدهای ورودی و غیره) را به رابط کاربری گرافیکی خود اضافه کنید.
- منطق محاسبه BMI را پیاده سازی کنید.
- نمایش BMI محاسبه شده به کاربر.
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
1. شما تابعی به نام "bmi()" تعریف کرده اید.
2. داخل تابع:
- ورودی کاربر برای قد و وزن را بازیابی می کنید.
- ارتفاع را از سانتی متر به متر (با تقسیم بر 100) تبدیل کنید.
    - BMI را با استفاده از فرمول محاسبه کنید: $$ \text{BMI} = \frac{\text{weight (kg)}}{\text{height (m)}^2} $$
- مقدار BMI را به یک عدد صحیح گرد کنید.
    - BMI محاسبه شده را چاپ کنید.
- متن "label1" را با BMI محاسبه شده به روز کنید.

3. در مرحله بعد، چند عبارت شرطی دارید:

- اگر BMI کمتر یا مساوی 18.5 باشد، متن "label2" را روی "Underweight" تنظیم می کنید و بلافاصله آن را با "You have Lower" بازنویسی می کنید. (که به نظر اشتباه تایپی است).
 - اگر BMI بیشتر از 25 باشد، متن "label2" را روی "Normal" تنظیم می کنید و بلافاصله آن را با "You have upper" بازنویسی می کنید (یک اشتباه تایپی دیگر).
- در غیر این صورت (اگر BMI کمتر یا مساوی 18.5 و بزرگتر از 25 نباشد)، متن "label2" را روی "Oobs" (احتمالاً به معنای "چاق") تنظیم می کنید و "label3" را با "تن سالم" به روز می کنید. "

چند نکته را باید در نظر گرفت:

- حتماً اشتباهات تایپی برچسب های خود را برطرف کنید.
- ممکن است بخواهید دسته BMI (به عنوان مثال، "کم وزنی"، "طبیعی"، "چاق") را بر اساس مقدار BMI محاسبه شده نمایش دهید.
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
2. **برچسب جعبه پایین:**
- شما یک برچسب با عرض 72 و ارتفاع 18 ایجاد کرده اید.
- رنگ پس‌زمینه این برچسب «آبی روشن» است.
- در پایین رابط کاربری گرافیکی شما قرار می گیرد و به مرکز متصل می شود.
3. **برچسب‌های تصویر ("app_image" و "app_image1"):**
- شما یک تصویر به نام "box.png" را دو بار بارگذاری کرده اید (یک بار برای "app_image" و یک بار برای "app_image1".
- اندازه هر دو تصویر را به 90x90 پیکسل تغییر داد.
- ایجاد برچسب برای هر تصویر ('Label') با ارتفاع و بالشتک مشخص.
    - "app_image" در مختصات (40، 100) و "app_image1" در مختصات (160، 100) قرار گرفته است.
- نقطه لنگر برای هر دو تصویر در گوشه شمال غربی (`anchor="nw"`) تنظیم شده است.
4. **برچسب تصویر مقیاس:**
- شما یک تصویر به نام "scale.png" را با استفاده از "PhotoImage" بارگذاری کرده اید.
- یک برچسب برای نمایش این تصویر ایجاد کرد.
- رنگ پس زمینه این برچسب "سبک آبی" است.
- آن را در مختصات (-10، 250) قرار داد

[دریافت فایل]()
```python
# Frame  ===============================================================================
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

## قرارگیری اسلایدر ها 
1. ** لغزنده 1 (` لغزنده`):**
- با استفاده از «ttk.Scale» یک نوار لغزنده افقی ایجاد کرده اید.
- دامنه نوار لغزنده از 0 تا 200 است.
- تابع 'slider_changed' هر زمان که مقدار لغزنده تغییر کند فراخوانی می شود.
- داخل "slider_changed":
   - مقدار فعلی اسلایدر را با استفاده از «current_value.get()» بازیابی می کنید.
   - مقدار را به یک رشته فرمت شده با دو رقم اعشار تبدیل کنید.
   - متغیر `Height` (که فکر می کنم مربوط به محاسبه BMI باشد) را با این مقدار به روز کنید.
   - اندازه یک تصویر با نام "man.png" را بر اساس اندازه محاسبه شده تغییر دهید.
   - تصویر نمایش داده شده در "secondimage" (که فکر می کنم یک برچسب دیگر است) را با تصویر تغییر اندازه به روز کنید.
    - موقعیت "secondimage" را بر اساس اندازه محاسبه شده تنظیم کنید.
   - همچنین رنگ پس‌زمینه نوار لغزنده را با استفاده از «style» پیکربندی کرده‌اید.
2. ** لغزنده 2 (`slider2`):**
- مشابه اسلایدر اول، لغزنده افقی دیگری را با استفاده از "ttk.Scale" ایجاد کرده اید.
- محدوده نیز از 0 تا 200 است.
- تابع `slider_changed2` زمانی فراخوانی می شود که مقدار لغزنده تغییر کند.
- داخل «slider_changed2»:
  - مقدار فعلی لغزنده دوم را با استفاده از «current_value2.get()» بازیابی می کنید.
  - مقدار را به یک رشته فرمت شده با دو رقم اعشار تبدیل کنید.
  - متغیر "وزن" (که من فرض می کنم مربوط به محاسبه BMI است) را با این مقدار به روز کنید.
```python
###############  slider 1

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

## ➕Run :
1. **ورودی ارتفاع ('ارتفاع'):**
- یک ویجت ورودی ('Entry') برای کاربر ایجاد کرده اید تا ارتفاع خود را وارد کند.
- "متغیر متن" روی "Height" تنظیم شده است، که من فرض می کنم یک متغیر "StringVar" است.
- عرض فیلد ورودی 5 کاراکتر تنظیم شده است.
- اندازه فونت 20، رنگ پس زمینه سفید و رنگ متن سیاه است.
- مرز (`bd`) روی 0 تنظیم شده است (بدون حاشیه).
- تراز متن در مرکز قرار دارد.
- فیلد ورودی در مختصات (50، 130) قرار دارد.
2. **ورودی وزن ('وزن'):**
- مشابه ورودی قد، یک ویجت ورودی برای وزن ایجاد کرده اید.
- "متغیر متن" روی "وزن" تنظیم شده است.
- سایر ویژگی ها (عرض، فونت، پس زمینه، رنگ متن و غیره) مانند ورودی ارتفاع هستند.
 - فیلد ورودی در مختصات (170، 130) قرار دارد.
3. **برچسب تصویر دوم (`تصویر دوم):**
- شما یک برچسب با پس زمینه آبی روشن ایجاد کرده اید.
- این برچسب در حال حاضر خالی است (هیچ تصویری نمایش داده نمی شود).
- در مختصات (300، 515) قرار دارد.

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
1. **برچسب تصویر دوم (`تصویر دوم):**
- شما یک برچسب دیگر با پس زمینه آبی روشن ایجاد کرده اید.
- این برچسب در حال حاضر خالی است (هیچ تصویری نمایش داده نمی شود).
- در مختصات (300، 515) قرار دارد.
2. **برچسب‌های نمایش BMI ('label1', 'label2', و 'label3'):**
- `label1`: یک برچسب بزرگ (اندازه قلم 60) برای نمایش BMI محاسبه شده.
- "label2": یک برچسب کوچکتر (اندازه قلم 12) برای نمایش دسته BMI (به عنوان مثال، "کم وزن"، "طبیعی"، "چاق").
- "label3": یک برچسب حتی کوچکتر (اندازه قلم 5) برای اطلاعات بیشتر (به عنوان مثال، "تن سالم").
- همه برچسب ها دارای پس زمینه آبی روشن هستند.
3. **دکمه "مشاهده گزارش":**
- دکمه ای با عنوان "مشاهده گزارش" اضافه کرده اید.
- با کلیک روی دکمه، عملکرد "bmi" فعال می شود.
- دکمه دارای سبک سفارشی (اندازه فونت 10، رنگ پس زمینه و رنگ متن).
- در مختصات (130، 270) قرار دارد.
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


# `𝐂𝐨𝐧𝐧𝐞𝐜𝐭 𝐌𝐞`🎈🎃

<a herf="https://www.buymeacoffee.com/jokernets"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="180px">
<a href="mailto:joker.until33@gmail.com"><img align="center" width="60px" src="https://github.com/edent/SuperTinyIcons/raw/master/images/svg/gmail.svg" style="max-width: 100%;"></a><a href="https://www.linkedin.com/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/mohammadfallahnejad/" height="40" width="60" /></a>
