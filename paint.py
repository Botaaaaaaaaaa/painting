import tkinter as tk
from tkinter import colorchooser
from PIL import Image,ImageDraw

win=tk.Tk()
win.geometry("600x700")

imgi=Image.new("RGB",(win.winfo_width(),win.winfo_height()))
draw_img = ImageDraw.Draw(imgi)


win.title("PAINT")

img=tk.PhotoImage(file="C:/Users/user/Downloads/taskpy/pngtree.png")
win.iconphoto(False,img)

win.columnconfigure(6,weight=1)
win.rowconfigure(2,weight=1)

BRUSH_SIZE=10
COLOUR="red"

def choose_colour():
    global COLOUR
    tgb,hex = colorchooser.askcolor()
    
    COLOUR=hex
    lb_colour.config(bg=hex)

def change_brush_size(event):
    global BRUSH_SIZE
    BRUSH_SIZE=v.get()

def save_img():
    imgi.save("painting.png")

def fill_canva():
    canva.config(bg=COLOUR)

def clear_canva():
    canva.delete("all")

def draw(event):
    x1,y1 = event.x-BRUSH_SIZE,event.y-BRUSH_SIZE
    x2,y2 = event.x+BRUSH_SIZE,event.y+BRUSH_SIZE

    canva.create_oval(x1,y1,x2,y2,fill=COLOUR,width=0)
    draw_img.ellipse((x1,y1,x2,y2),fill=COLOUR,width=0)


canva=tk.Canvas(win,bg="yellow")
canva.grid(column=0,row=2,columnspan=9,sticky="nswe")
canva.bind("<B1-Motion>",draw)

lb1=tk.Label(text="Params: ").grid(row=1,column=0)

btn_clean=tk.Button(text="CLEAR",command=clear_canva)
btn_clean.grid(row=1,column=1)

btn_choose=tk.Button(text="Choose colour",command=choose_colour)
btn_choose.grid(row=1,column=2)

btn_save=tk.Button(text="SAVE",command=save_img)
btn_save.grid(row=1,column=8)

lb_colour=tk.Label(text="",bg="red",width=10)
lb_colour.grid(row=1,column=4)

btn_fill=tk.Button(text="FILL",command=fill_canva)
btn_fill.grid(row=1,column=5)

v=tk.IntVar()
v.set(BRUSH_SIZE)
scale_brush=tk.Scale(win,variable=v,from_=0,to_=100,orient=tk.HORIZONTAL,command=change_brush_size)
scale_brush.grid(row=1,column=7)

lb_brush=tk.Label(text="Brush size:").grid(row=1,column=6)

win.mainloop()