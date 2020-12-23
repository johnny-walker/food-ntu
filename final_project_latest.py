# 引入 tkinter 模組
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import requests, json 

# 建立主視窗 Frame
window = tk.Tk()

# 設定視窗標題
window.title('吃什麼小幫手')

# 設定視窗大小為 300x300，視窗（左上角）在螢幕上的座標位置為 (250, 150)
window.geometry("320x500+250+150")

# background color
window.configure(background='white')


all_data_list = []  # a list collecting all data needed
    
#############################################################################################################
    
    
####################################### page7 ###############################################################


def next_button_function_budget():
    if len(budget_list) ==0:
        all_data_list.append('無預算限制')
    else:
        all_data_list.append(budget_list[-1])
    # print(all_data_list)
    label_page7.destroy()
    com_time_page7.destroy()
    button_page7.destroy()

#綁定事件
def handle_budget(event):
    budget_list.append(com_time_page7.get())
    #print(cv.get())
    #print("time")

# 紀錄所有選過的時間(之後只選最後一筆)
budget_list = []

# set up a label
label_page7 = tk.Label(window,            # 文字標示所在視窗
                 #bg = '#EEBB08',         #  背景顏色
                 font = ('Arial', 10),    # 字型與大小
                 width = 60, height = 2,
                 text = '本次用餐的預算是多少元?')  # 顯示文字
                 
label_page7.grid(column=0, row=0, columnspan =  12)
              
                 
# combobox

cv_page7 = tk.StringVar()
com_time_page7 = ttk.Combobox(window ,textvariable=cv_page7)
com_time_page7.grid(row = 1, column = 0, columnspan = 12)
#設置下拉數據
com_time_page7["value"]=("請選擇預算", "$100以內", "$101-$200", "$201-$300", "$301-500", "無預算限制")
                   

#設置默認值
com_time_page7.current(0)
com_time_page7.bind("<<ComboboxSelected>>", handle_budget) #等同於textvariable=cv這個變量

button_page7 = tk.Button(window,          # 按鈕所在視窗
                         bg = 'light blue',
                         text = '下一題',  # 顯示文字
                         command = next_button_function_budget
                         ) # 按下按鈕所執行的函數
                   
button_page7.grid(row = 3,column = 0, columnspan = 12)

####################################### page6 ###############################################################3


def next_button_function_people():
    label_page6.destroy()
    com_time_page6.destroy()
    button_page6.destroy()
    if len(people_list) ==0:
        all_data_list.append('無資料')
    else:
        all_data_list.append(people_list[-1])

#綁定事件
def handle_people(event):
    people_list.append(com_time_page6.get())
    #print(cv.get())
    #print("time")

# 紀錄所有選過的時間(之後只選最後一筆)
people_list = []

# set up a label
label_page6 = tk.Label(window,            # 文字標示所在視窗
                 #bg = '#EEBB08',         #  背景顏色
                 font = ('Arial', 10),    # 字型與大小
                 width = 60, height = 2,
                 text = '多少人要一起吃呢?')  # 顯示文字
                 
label_page6.grid(column=0, row=0, columnspan =  12)
              
                 
# combobox

cv_page6 = tk.StringVar()
com_time_page6 = ttk.Combobox(window ,textvariable=cv_page6)
com_time_page6.grid(row = 1, column = 0, columnspan = 12)
#設置下拉數據
com_time_page6["value"]=("請選擇人數","外帶","1","2","3","4","5","6","7","8","9","10","10+")
                   

#設置默認值
com_time_page6.current(0)
com_time_page6.bind("<<ComboboxSelected>>", handle_people) #等同於textvariable=cv這個變量

button_page6 = tk.Button(window,          # 按鈕所在視窗
                         bg = 'light blue',
                         text = '下一題',  # 顯示文字
                         command = next_button_function_people
                         ) # 按下按鈕所執行的函數
                   
button_page6.grid(row = 3,column = 0, columnspan = 12)

'''
######################################## page4 ##############################################################


def delete_all_page4():
    label_page4.destroy()
    com_time_page4.destroy()
    button_page4.destroy()
    if len(time_list) ==0:
        all_data_list.append('無資料')
    else:
        all_data_list.append(time_list[-1])

#綁定事件
def handle_time(event):
    time_list.append(com_time_page4.get())
    #print(cv.get())
    #print("time")

# 紀錄所有選過的時間(之後只選最後一筆)
time_list = []

# set up a label
label_page4 = tk.Label(window,            # 文字標示所在視窗
                 #bg = '#EEBB08',         #  背景顏色
                 font = ('Arial', 10),    # 字型與大小
                 width = 60, height = 2,
                 text = '預計的用餐時間是幾點呢?')  # 顯示文字
                 
label_page4.grid(column=0, row=0, columnspan =  12)
              
                 
# combobox

cv_page4 = tk.StringVar()
com_time_page4 = ttk.Combobox(window ,textvariable=cv_page4)
com_time_page4.grid(row = 1, column = 0, columnspan = 12)
#設置下拉數據
com_time_page4["value"]=("請選擇時間","11:00-11:30","11:30-12:00","12:00-12:30","12:30-13:00","13:00-13:30",
                   "13:30-14:00","14:00-15:00","15:00-16:00","16:00-17:00",
                   "17:00-17:30","17:30-18:00","18:00-18:30","18:30-19:00",
                   "19:00-19:30","19:30-20:00","20:00-20:30","20:30-21:00")

#設置默認值
com_time_page4.current(0)
   
com_time_page4.bind("<<ComboboxSelected>>", handle_time) #等同於textvariable=cv這個變量

button_page4 = tk.Button(window,          # 按鈕所在視窗
                         bg = 'light blue',
                         text = '下一題',  # 顯示文字
                         command = delete_all_page4
                         ) # 按下按鈕所執行的函數
                   
button_page4.grid(row = 3,column = 0, columnspan = 12)


############################################ page5 #######################################################

def next_button_function_weekend():
    label_page5.destroy()
    com_time_page5.destroy()
    button_page5.destroy()
    if len(week_list) ==0:
        all_data_list.append('無資料')
    else:
        all_data_list.append(week_list[-1])

#綁定事件
def handle_week(event):
    week_list.append(com_time_page5.get())
    #print(cv.get())
    #print("time")

# 紀錄所有選過的時間(之後只選最後一筆)
week_list = []

# set up a label
label_page5 = tk.Label(window,            # 文字標示所在視窗
                 #bg = '#EEBB08',         #  背景顏色
                 font = ('Arial', 10),    # 字型與大小
                 width = 60, height = 2,
                 text = '要在星期幾用餐呢?')  # 顯示文字
                 
label_page5.grid(column=0, row=0, columnspan =  12)
              
                 
# combobox

cv2 = tk.StringVar()
com_time_page5 = ttk.Combobox(window ,textvariable=cv2)
com_time_page5.grid(row = 1, column = 0, columnspan = 12)
#設置下拉數據
com_time_page5["value"]=("請選擇星期","星期一","星期二","星期三","星期四","星期五","星期六","星期日")

#設置默認值
com_time_page5.current(0)

    
com_time_page5.bind("<<ComboboxSelected>>", handle_week) #等同於textvariable=cv這個變量

button_page5 = tk.Button(window,          # 按鈕所在視窗
                         bg = 'light blue',
                         text = '下一題',  # 顯示文字
                         command = next_button_function_weekend
                         ) # 按下按鈕所執行的函數
                   
button_page5.grid(row = 3,column = 0, columnspan = 12)

'''
##########################################################################################################

def query_temperature():
    api_key = "499fe73dfae42a6cbc10dbcccb010983"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Taipei" #input("Enter city name : ") 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    response = requests.get(complete_url) 
    x = response.json() 
    if x["cod"] != "404": 
        y = x["main"] 
        current_temperature = y["temp"] 
        return int(current_temperature - 273.15)
    else:
        return 20
        
def next_button_function_temp():
    if radioValue_page10.get() == 1:
        temp = query_temperature()
        all_data_list.append(temp)
    elif radioValue_page10.get() == 2:
        all_data_list.append('N/A')
    label_page10.destroy()
    rdioOne_page10.destroy()
    rdioTwo_page10.destroy()   
    labelValue_page10.destroy()
    button_page10.destroy()


# set up a label
label_page10 = tk.Label(window,                 # 文字標示所在視窗
                 #bg = '#EEBB08',         #  背景顏色
                 font = ('Arial', 10),   # 字型與大小
                 width = 60, height = 2,
                 text = '要不要善用天氣小精靈推薦你適合的食物呢?')  # 顯示文字
               
label_page10.grid(column = 0, row = 0, columnspan = 12)


# set up radiobuttons
radioValue_page10 = tk.IntVar() 

rdioOne_page10 = tk.Radiobutton(window, text = '好呀',
                               variable = radioValue_page10, value = 1) 
rdioTwo_page10 = tk.Radiobutton(window, text = '先不要',
                               variable = radioValue_page10, value = 2) 
                           

rdioOne_page10.grid(column = 0, row = 1, columnspan = 6, sticky = tk.NE + tk.SW)
rdioTwo_page10.grid(column = 6, row = 1, columnspan = 6, sticky = tk.NE + tk.SW)


# set a label showing your choice
labelValue_page10 = tk.Label(window, textvariable = radioValue_page10)

labelValue_page10.grid(column=0, row=2, columnspan =  12)


# set a button
button_page10 = tk.Button(window,          # 按鈕所在視窗
                         bg = 'light blue',
                         text = '下一題',  # 顯示文字
                         command = next_button_function_temp) # 按下按鈕所執行的函數
                   
button_page10.grid(row = 3,column = 0, columnspan = 12)
    

############################################ page1 ####################################################### 


def next_button_function_vegan():
    if radioValue_page1.get() == 1:
        all_data_list.append('素')
    elif radioValue_page1.get() == 2:
        all_data_list.append('葷素皆可')
    elif radioValue_page1.get() == 3:
        all_data_list.append('葷')
    label_page1.destroy()
    rdioOne_page1.destroy()
    rdioTwo_page1.destroy()
    rdioThree_page1.destroy()    
    labelValue_page1.destroy()
    button_page1.destroy()

vege_list = []

# set up a label
label_page1 = tk.Label(window,                 # 文字標示所在視窗
                 #bg = '#EEBB08',         #  背景顏色
                 font = ('Arial', 10),   # 字型與大小
                 width = 60, height = 2,
                 text = '吃素食嗎?')  # 顯示文字
               
label_page1.grid(column = 0, row = 0, columnspan = 12)


# set up radiobuttons
radioValue_page1 = tk.IntVar() 

rdioOne_page1 = tk.Radiobutton(window, text='素',
                               variable = radioValue_page1,value = 1) 
rdioTwo_page1 = tk.Radiobutton(window, text='葷素皆可',
                               variable = radioValue_page1,value = 2) 
rdioThree_page1 = tk.Radiobutton(window, text='無肉不歡(只吃葷)',
                               variable = radioValue_page1,value = 3)                               

rdioOne_page1.grid(column=0, row=1, columnspan = 4, sticky = tk.NE + tk.SW)
rdioTwo_page1.grid(column=4, row=1, columnspan = 4, sticky = tk.NE + tk.SW)
rdioThree_page1.grid(column=8, row=1, columnspan = 4, sticky = tk.NE + tk.SW)

# set a label showing your choice
labelValue_page1 = tk.Label(window, textvariable = radioValue_page1)

labelValue_page1.grid(column=0, row=2, columnspan =  12)


# set a button
button_page1 = tk.Button(window,          # 按鈕所在視窗
                         bg = 'light blue',
                         text = '下一題',  # 顯示文字
                         command = next_button_function_vegan) # 按下按鈕所執行的函數
                   
button_page1.grid(row = 3,column = 0, columnspan = 12)


################################################## page2 ################################################


def next_button_function_eatin():
    if radioValue_page2.get() == 1:
        all_data_list.append('內用')
    elif radioValue_page2.get() == 2:
        all_data_list.append('外帶')
    elif radioValue_page2.get() == 3:
        all_data_list.append('內用外帶皆可')       
    label_page2.destroy()
    rdioOne_page2.destroy()
    rdioTwo_page2.destroy()
    rdioThree_page2.destroy()
    labelValue_page2.destroy()
    button_page2.destroy()
    

# set up a label
label_page2 = tk.Label(window,                 # 文字標示所在視窗
                 #bg = '#EEBB08',         #  背景顏色
                 font = ('Arial', 10),   # 字型與大小
                 width = 60, height = 2,
                 text = '內用還是外帶呢?')  # 顯示文字

# place                 
label_page2.grid(column=0, row=0, columnspan =  12)


# set up three radiobuttons
radioValue_page2 = tk.IntVar() 

rdioOne_page2 = tk.Radiobutton(window, text='內用',
                               variable=radioValue_page2, value = 1) 
rdioTwo_page2 = tk.Radiobutton(window, text='外帶',
                               variable=radioValue_page2, value = 2) 
rdioThree_page2 = tk.Radiobutton(window, text='皆可',
                                 variable=radioValue_page2, value = 3)

rdioOne_page2.grid(column=0, row=1, columnspan =  4, sticky = tk.NE + tk.SW)
rdioTwo_page2.grid(column=4, row=1, columnspan =  4, sticky = tk.NE + tk.SW)
rdioThree_page2.grid(column=8, row=1, columnspan =  4, sticky = tk.NE + tk.SW)

labelValue_page2 = tk.Label(window, textvariable = radioValue_page2)

labelValue_page2.grid(column=0, row=2, columnspan =  12)

# set a button
button_page2 = tk.Button(window,          # 按鈕所在視窗
                         bg = 'light blue',
                         text = '下一題',  # 顯示文字
                         command = next_button_function_eatin
                         ) # 按下按鈕所執行的函數
                   
button_page2.grid(row = 3,column = 0, columnspan = 12)


####################################### page3 ############################################################



##################################################### page8 ####################################################


def next_button_function_staple():
    staple_list = list()
    selection = lstbox_page8.curselection()
    for each_chosen in selection:
        selected_ans = lstbox_page8.get(each_chosen)
        staple_list.append(selected_ans)
    # print(staple_list)  # 記錄已選答案的list
    all_data_list.append(staple_list)
    label_page8.destroy()
    lstbox_page8.destroy()
    next_btn_page8.destroy()
  
  
# question display
label_page8 = tk.Label(window, 
                 text = "想吃什麼種類的主食？", 
                 font = ("Arial", 10),  
                 width = 60, height = 2)
label_page8.grid(column = 0, row = 0, columnspan =  12, sticky = tk.NE + tk.SW)

# 列出該題所有選項
options = tk.StringVar()
options.set("飯 麵 水餃 河粉 輕食 冬粉 米粉 炸物 壽司 生魚片 牛排 漢堡 鍋物 烤肉 披薩 粄條 胡椒餅 沙拉 三明治")

# 把所有選項都放在框框中
lstbox_page8 = tk.Listbox(window, listvariable = options, selectmode = "multiple", bg = '#FFC0CB')
lstbox_page8.grid(column = 0, row = 1, rowspan = 2, columnspan = 12, sticky = tk.NE + tk.SW) 
 

next_btn_page8 = tk.Button(window,          # 按鈕所在視窗
                  bg = 'light blue',
                  text = '下一題',  # 顯示文字
                  command = next_button_function_staple) # 按下按鈕所執行的函數
                   
next_btn_page8.grid(column = 0, row = 3, columnspan = 12, sticky = tk.NE + tk.SW)




################################################## page9 #######################################################

def next_button_function_type():
    type_list = list()
    selection = lstbox.curselection()
    for each_chosen in selection:
        selected_ans = lstbox.get(each_chosen)
        type_list.append(selected_ans)
    # print(type_list)  # 記錄已選答案的list
    all_data_list.append(type_list)
    label.destroy()
    lstbox.destroy()
    next_btn.destroy()
  
  
# question display
label = tk.Label(window, 
                 text = "想吃哪一種國家的料理呢呢？", 
                 font = ("Arial", 10),  
                 width = 60, height = 2)
label.grid(column = 0, row = 0, columnspan =  12, sticky = tk.NE + tk.SW)

# 列出該題所有選項
options = tk.StringVar()
options.set("中式 西式 台式 泰式 美式 港式 韓式 日式 埃及式 俄式 歐式 義式 印度式 德式 東南亞料理 南洋料理 中東料理 雲南料理")

# 把所有選項都放在框框中
lstbox = tk.Listbox(window, listvariable = options, selectmode = "multiple")
lstbox.grid(column = 0, row = 1, rowspan = 2, columnspan = 12, sticky = tk.NE + tk.SW) 
 

next_btn = tk.Button(window,          # 按鈕所在視窗
                  bg = 'light blue',
                  text = '下一題',  # 顯示文字
                  command = next_button_function_type) # 按下按鈕所執行的函數
                   
next_btn.grid(column = 0, row = 3, columnspan = 12, sticky = tk.NE + tk.SW)

###################################################################################################################3

def next_button_function_location():
    location_list = list()
    selection = lstbox_page11.curselection()
    for each_chosen in selection:
        selected_ans = lstbox_page11.get(each_chosen)
        location_list.append(selected_ans)
    # print(staple_list)  # 記錄已選答案的list
    all_data_list.append(location_list)
    label_page11.destroy()
    lstbox_page11.destroy()
    next_btn_page11.destroy()
  
  
# question display
label_page11 = tk.Label(window, 
                 text = "想在哪兒覓食呢？", 
                 font = ("Arial", 10),  
                 width = 60, height = 2)
label_page11.grid(column = 0, row = 0, columnspan =  12, sticky = tk.NE + tk.SW)

# 列出該題所有選項
options = tk.StringVar()
options.set("水源市場到師大分部 水源市場到正門 正門到台電大樓  溫州街 118 台大學餐 台科大學餐 長興")

# 把所有選項都放在框框中
lstbox_page11 = tk.Listbox(window, listvariable = options, selectmode = "multiple")
lstbox_page11.grid(column = 0, row = 1, rowspan = 2, columnspan = 12, sticky = tk.NE + tk.SW) 
 

next_btn_page11 = tk.Button(window,          # 按鈕所在視窗
                  bg = 'light blue',
                  text = '下一題',  # 顯示文字
                  command = next_button_function_location) # 按下按鈕所執行的函數
                   
next_btn_page11.grid(column = 0, row = 3, columnspan = 12, sticky = tk.NE + tk.SW)


#################################################### run the site ################################################

print(all_data_list)

window.mainloop()

print(all_data_list) # 
