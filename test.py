# 引入 tkinter 模組
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import requests, json 
from PIL import Image, ImageTk
from selection_method import *
from project_main import *

# 建立主視窗 Frame
window = tk.Tk()

# 設定視窗標題
window.title('吃什麼小幫手')

# 設定視窗大小為 426x640，視窗（左上角）在螢幕上的座標位置為 (250, 150)
window.geometry("426x640+250+150")

# background color
window.configure(background='white')

# Create a photoimage object of the image in the path
imageFile = "Food.jpg"
image = os.getcwd() + "/images/" + imageFile
im = Image.open(image)
resized = im.resize((80, 60),Image.ANTIALIAS)
tkimage = ImageTk.PhotoImage(resized)
#img_label = tk.Label(window,                    # 文字標示所在視窗
#                        image = tkimage        # 顯示文字 
#                    )   
#img_label.grid(column=0, row = 0, columnspan = 12)

ans_label = tk.Label(window,                    # 文字標示所在視窗
                     bg = '#FFFF33',            #  背景顏色
                     font = ('Arial', 12),      # 字型與大小
                     width = 60, height = 20,
                     text = "推薦結果如下：\n推薦結果如下：\n推薦結果如下：\n推薦結果如下：\n推薦結果如下：\n推薦結果如下：\n",
                     image = tkimage)      # 顯示文字
ans_label.grid(column=0, row=0, columnspan =  12)
ans_label.config(compound = 'right')

window.mainloop()

