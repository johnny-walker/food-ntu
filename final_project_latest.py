# 引入 tkinter 模組
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import requests, json 

# 建立主視窗 Frame
window = tk.Tk()

# 設定視窗標題
window.title('吃什麼小幫手')

# 設定視窗大小為 640x480，視窗（左上角）在螢幕上的座標位置為 (250, 150)
window.geometry("640x480+250+150")

# background color
window.configure(background='white')


all_data_list = []  # a list collecting all data needed
    
#############################################################################################################
  
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

# define pages
################################################## page1 想在哪兒覓食呢 ############################################
label_page1 = None
lstbox_page1 = None
next_btn_page1 = None

def create_page1():
    def next_button_function_location():
        location_list = list()
        selection = lstbox_page1.curselection()
        for each_chosen in selection:
            selected_ans = lstbox_page1.get(each_chosen)
            location_list.append(selected_ans)
        # print(staple_list)  # 記錄已選答案的list
        # clear current page
        all_data_list.append(location_list)
        label_page1.destroy()
        lstbox_page1.destroy()
        next_btn_page1.destroy()
        # create next page
        create_page2()
    
    # question display
    label_page1 = tk.Label(window, 
                    text = "想在哪兒覓食呢？", 
                    font = ("Arial", 12),  
                    width = 60, height = 2)
    label_page1.grid(column = 3, row = 0, columnspan =  12, sticky = tk.NE + tk.SW)

    # 列出該題所有選項
    options = tk.StringVar()
    options.set("水源市場到師大分部 水源市場到正門 正門到台電大樓  溫州街 118 台大學餐 台科大學餐 長興")

    # 把所有選項都放在框框中
    lstbox_page1 = tk.Listbox(window, listvariable = options, selectmode = "multiple")
    lstbox_page1.selection_set(0)   # select first one
    lstbox_page1.grid(column = 3, row = 2, columnspan = 12, sticky = tk.NE + tk.SW) 
    

    next_btn_page1 = tk.Button( window,          # 按鈕所在視窗
                                bg = 'light blue',
                                text = '下一題',  # 顯示文字
                                command = next_button_function_location) # 按下按鈕所執行的函數
                    
    next_btn_page1.grid(column = 3, row = 12, columnspan = 12, sticky = tk.NE + tk.SW)


################################################## page2 想吃哪一種國家的料理呢 #########################################
label_page2 = None
lstbox_page2  = None
next_btn_page2  = None
  
def create_page2():  
    def next_button_function_type():
        type_list = list()
        selection = lstbox_page2.curselection()
        for each_chosen in selection:
            selected_ans = lstbox_page2.get(each_chosen)
            type_list.append(selected_ans)
        # print(type_list)  # 記錄已選答案的list
        # clear current page
        all_data_list.append(type_list)
        label_page2.destroy()
        lstbox_page2.destroy()
        next_btn_page2.destroy()
        # create next page
        create_page3()
    
    # question display
    label_page2 = tk.Label( window, 
                            text = "想吃哪一種國家的料理呢？", 
                            font = ("Arial", 12),  
                            width = 60, height = 2)
    label_page2.grid(column = 3, row = 0, columnspan =  12, sticky = tk.NE + tk.SW)

    # 列出該題所有選項
    options = tk.StringVar()
    options.set("中式 西式 台式 泰式 美式 港式 韓式 日式 埃及式 俄式 歐式 義式 印度式 德式 東南亞料理 南洋料理 中東料理 雲南料理")

    # 把所有選項都放在框框中
    lstbox_page2 = tk.Listbox(window, listvariable = options, selectmode = "multiple")
    lstbox_page2.selection_set(0)   # select first one
    lstbox_page2.grid(column = 3, row = 1, rowspan = 2, columnspan = 12, sticky = tk.NE + tk.SW) 
    

    next_btn_page2 = tk.Button( window,          # 按鈕所在視窗
                                bg = 'light blue',
                                text = '下一題',  # 顯示文字
                                command = next_button_function_type) # 按下按鈕所執行的函數
                    
    next_btn_page2.grid(column = 3, row = 5, columnspan = 12, sticky = tk.NE + tk.SW)


####################################### page3 想吃什麼種類的主食？###############################################

label_page3 = None
lstbox_page3 = None
next_btn_page3 = None

def create_page3():
    def next_button_function_staple():
        staple_list = list()
        selection = lstbox_page3.curselection()
        for each_chosen in selection:
            selected_ans = lstbox_page3.get(each_chosen)
            staple_list.append(selected_ans)
        # print(staple_list)  # 記錄已選答案的list
        # clear current page
        all_data_list.append(staple_list)
        label_page3.destroy()
        lstbox_page3.destroy()
        next_btn_page3.destroy()
        # create next page
        create_page4()
    
    
    # question display
    label_page3 = tk.Label( window, 
                            text = "想吃什麼種類的主食？", 
                            font = ("Arial", 12),  
                            width = 60, height = 2)
    label_page3.grid(column = 3, row = 0, columnspan =  12, sticky = tk.NE + tk.SW)

    # 列出該題所有選項
    options = tk.StringVar()
    options.set("飯 麵 水餃 河粉 輕食 冬粉 米粉 炸物 壽司 生魚片 牛排 漢堡 鍋物 烤肉 披薩 粄條 胡椒餅 沙拉 三明治")

    # 把所有選項都放在框框中
    lstbox_page3 = tk.Listbox(window, listvariable = options, selectmode = "multiple")#, bg = '#FFC0CB')
    lstbox_page3.selection_set(0)   # select first one
    lstbox_page3.grid(column = 3, row = 1, rowspan = 2, columnspan = 12, sticky = tk.NE + tk.SW) 
    

    next_btn_page3 = tk.Button( window,          # 按鈕所在視窗
                                bg = 'light blue',
                                text = '下一題',  # 顯示文字
                                command = next_button_function_staple) # 按下按鈕所執行的函數
                    
    next_btn_page3.grid(column = 3, row = 5, columnspan = 12, sticky = tk.NE + tk.SW)



################################################## page4 內用還是外帶呢? #######################################
label_page4 = None
radioValue_page4 = None
rdioOne_page4 = None 
rdioTwo_page4 = None
rdioThree_page4 = None
#labelValue_page4 = None
next_btn_page4 = None

def create_page4():
    def next_button_function_eatin():
        if radioValue_page4.get() == 1:
            all_data_list.append('內用')
        elif radioValue_page4.get() == 2:
            all_data_list.append('外帶')
        elif radioValue_page4.get() == 3:
            all_data_list.append('內用外帶皆可')       
        # clear current page
        label_page4.destroy()
        rdioOne_page4.destroy()
        rdioTwo_page4.destroy()
        rdioThree_page4.destroy()
        label_page4.destroy()
        #labelValue_page4.destroy()
        next_btn_page4.destroy()
        # create next page
        create_page5()
    

    # set up a label
    label_page4 = tk.Label(window,                 # 文字標示所在視窗
                    #bg = '#EEBB08',         #  背景顏色
                    font = ('Arial', 12),   # 字型與大小
                    width = 60, height = 2,
                    text = '內用還是外帶呢?')  # 顯示文字

    # place                 
    label_page4.grid(column=3, row=0, columnspan =  12)


    # set up three radiobuttons
    radioValue_page4 = tk.IntVar() 

    rdioOne_page4 = tk.Radiobutton( window, text='內用',
                                    variable=radioValue_page4, value = 1) 
    rdioTwo_page4 = tk.Radiobutton( window, text='外帶',
                                    variable=radioValue_page4, value = 2) 
    rdioThree_page4 = tk.Radiobutton(window, text='皆可',
                                     variable=radioValue_page4, value = 3)
    radioValue_page4.set(1)


    rdioOne_page4.grid(column=3, row=3, columnspan =  12, sticky = tk.W + tk.W)
    rdioTwo_page4.grid(column=3, row=5, columnspan =  12, sticky = tk.W + tk.W)
    rdioThree_page4.grid(column=3, row=7, columnspan =  12, sticky = tk.W + tk.W)

    # set a label showing your choice
    #labelValue_page4 = tk.Label(window, textvariable = radioValue_page4)
    #labelValue_page4.grid(column=3, row=9, columnspan =  12)

    # set a button
    next_btn_page4 = tk.Button( window,          # 按鈕所在視窗
                                bg = 'light blue',
                                text = '下一題',  # 顯示文字
                                command = next_button_function_eatin
                                ) # 按下按鈕所執行的函數
                    
    next_btn_page4.grid(column = 6, row=10, columnspan = 12)


############################################ page5 吃素食嗎? ################################################# 
label_page5 = None
radioValue_page5 = None
radioOne_page5 = None
radioTwo_page5 = None
radioThree_page5 = None
#labelValue_page5 = None
next_btn_page5 = None

def create_page5():     
    def next_button_function_vegan():
        if radioValue_page5.get() == 1:
            all_data_list.append('素')
        elif radioValue_page5.get() == 2:
            all_data_list.append('葷素皆可')
        elif radioValue_page5.get() == 3:
            all_data_list.append('葷')   
        # clear current page
        radioOne_page5.destroy()
        radioTwo_page5.destroy()
        radioThree_page5.destroy()    
        label_page5.destroy()
        #labelValue_page5.destroy()
        next_btn_page5.destroy()
        # create next page
        create_page6()

    #vege_list = []

    # set up a label
    label_page5 = tk.Label( window,                 # 文字標示所在視窗
                            #bg = '#EEBB08',         #  背景顏色
                            font = ('Arial', 12),   # 字型與大小
                            width = 60, height = 2,
                            text = '吃素食嗎?')  # 顯示文字
                
    label_page5.grid(column = 3, row = 0, columnspan = 12)


    # set up radiobuttons
    radioValue_page5 = tk.IntVar() 

    radioOne_page5 = tk.Radiobutton(window, text='素',
                                    variable = radioValue_page5,value = 1) 
    radioTwo_page5 = tk.Radiobutton(window, text='葷素皆可',
                                    variable = radioValue_page5,value = 2) 
    radioThree_page5 = tk.Radiobutton(window, text='無肉不歡(只吃葷)',
                                    variable = radioValue_page5,value = 3)                               
    radioValue_page5.set(1)

    radioOne_page5.grid(column=3, row=3, columnspan = 12, sticky = tk.W + tk.W)
    radioTwo_page5.grid(column=3, row=5, columnspan = 12, sticky = tk.W + tk.W)
    radioThree_page5.grid(column=3, row=7, columnspan = 12, sticky = tk.W + tk.W)

    # set a label showing your choice
    #labelValue_page5 = tk.Label(window, textvariable = radioValue_page5)
    #labelValue_page5.grid(column=3, row=9, columnspan =  12)


    # set a button
    next_btn_page5 = tk.Button( window,          # 按鈕所在視窗
                                bg = 'light blue',
                                text = '下一題',  # 顯示文字
                                command = next_button_function_vegan) # 按下按鈕所執行的函數
                    
    next_btn_page5.grid(column = 3, row = 10, columnspan = 12)

################################# page6 要不要善用天氣小精靈推薦你適合的食物呢? ########################################### 
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

label_page6 = None
radioValue_page6 = None
radioOne_page6 = None
radioTwo_page6 = None
#labelValue_page6 = None
next_btn_page6 = None
temperature = query_temperature()

def create_page6():
    def next_button_function_temp():
        if radioValue_page6.get() == 1:
            all_data_list.append(temperature)
        elif radioValue_page6.get() == 2:
            all_data_list.append('N/A')
        # clear current page 
        radioOne_page6.destroy()
        radioTwo_page6.destroy()   
        label_page6.destroy()
        #labelValue_page6.destroy()
        next_btn_page6.destroy()
        # create next page
        create_page7()


    # set up a label
    label_page6 = tk.Label( window,                 # 文字標示所在視窗
                            #bg = '#EEBB08',         #  背景顏色
                            font = ('Arial', 12),   # 字型與大小
                            width = 60, height = 2,
                            text = '現在溫度是'+ str(temperature) + '度，要不要善用天氣小精靈推薦你適合的食物呢?')  # 顯示文字
                
    label_page6.grid(column = 0, row = 0, columnspan = 12)

    # set up radiobuttons
    radioValue_page6 = tk.IntVar() 
    radioOne_page6 = tk.Radiobutton(window, text = '好呀',
                                    variable = radioValue_page6, value = 1) 
    radioTwo_page6 = tk.Radiobutton(window, text = '先不要',
                                    variable = radioValue_page6, value = 2) 
    radioValue_page6.set(1)                            

    radioOne_page6.grid(column = 6, row = 3, columnspan = 12, sticky = tk.W + tk.W)
    radioTwo_page6.grid(column = 6, row = 5, columnspan = 12, sticky = tk.W + tk.W)


    # set a label showing your choice
    #labelValue_page6 = tk.Label(window, textvariable = radioValue_page6)
    #labelValue_page6.grid(column=6, row=8, columnspan =  12)


    # set a button
    next_btn_page6 = tk.Button( window,          # 按鈕所在視窗
                                bg = 'light blue',
                                text = '下一題',  # 顯示文字
                                command = next_button_function_temp) # 按下按鈕所執行的函數
                    
    next_btn_page6.grid(column = 6, row = 10, columnspan = 12)


####################################### page7 多少人要一起吃呢? #######################################################
label_page7 = None
com_time_page7 = None
next_btn_page7 = None

# 紀錄所有選過的時間(之後只選最後一筆)
people_list = []

def create_page7():
    def next_button_function_people():
        if len(people_list) ==0:
            all_data_list.append('無資料')
        else:
            all_data_list.append(people_list[-1])
        # clear current page
        label_page7.destroy()
        com_time_page7.destroy()
        next_btn_page7.destroy()
        # create next page
        create_page8()

    #綁定事件
    def handle_people(event):
        people_list.append(com_time_page7.get())
        #print(cv.get())
        #print("time")

    # set up a label
    label_page7 = tk.Label( window,            # 文字標示所在視窗
                            #bg = '#EEBB08',         #  背景顏色
                            font = ('Arial', 12),    # 字型與大小
                            width = 60, height = 2,
                            text = '多少人要一起吃呢?')  # 顯示文字
                    
    label_page7.grid(column=0, row=0, columnspan =  12)
              
                 
    # combobox

    cv_page7 = tk.StringVar()
    com_time_page7 = ttk.Combobox(window ,textvariable=cv_page7)
    com_time_page7.grid(row = 1, column = 0, columnspan = 12)
    #設置下拉數據
    com_time_page7["value"]=("請選擇人數","外帶","1","2","3","4","5","6","7","8","9","10","10+")
                    

    #設置默認值
    com_time_page7.current(2)
    com_time_page7.bind("<<ComboboxSelected>>", handle_people) #等同於textvariable=cv這個變量

    next_btn_page7 = tk.Button( window,          # 按鈕所在視窗
                                bg = 'light blue',
                                text = '下一題',  # 顯示文字
                                command = next_button_function_people
                                ) # 按下按鈕所執行的函數
                    
    next_btn_page7.grid(row = 3, column = 0, columnspan = 12)

  
    
################################## page8 本次用餐的預算是多少元? ######################################################
label_page8 = None
com_budget_page8 = None
next_btn_page8 = None

# 紀錄所有選過的時間(之後只選最後一筆)
budget_list = []

def create_page8():
    def next_button_function_budget():
        if len(budget_list) == 0:
            all_data_list.append('無預算限制')
        else:
            all_data_list.append(budget_list[-1])
        # print(all_data_list)
        # clear current page
        label_page8.destroy()
        com_budget_page8.destroy()
        next_btn_page8.destroy()
        # start to query the result from quizs
        query_restaurant()

    #綁定事件
    def handle_budget(event):
        budget_list.append(com_budget_page8.get())
        #print(cv.get())
        #print("time")


    # set up a label
    label_page8 = tk.Label( window,            # 文字標示所在視窗
                            #bg = '#EEBB08',         #  背景顏色
                            font = ('Arial', 12),    # 字型與大小
                            width = 60, height = 2,
                            text = '本次用餐的預算是多少元?')  # 顯示文字
                    
    label_page8.grid(column=0, row=0, columnspan =  12)
                
    # combobox
    cv_page8 = tk.StringVar()
    com_budget_page8 = ttk.Combobox(window ,textvariable=cv_page8)
    com_budget_page8.grid(row = 1, column = 0, columnspan = 12)
    #設置下拉數據
    com_budget_page8["value"]=("請選擇預算", "$100以內", "$101-$200", "$201-$300", "$301-500", "無預算限制")
                    

    #設置默認值
    com_budget_page8.current(1)
    com_budget_page8.bind("<<ComboboxSelected>>", handle_budget) #等同於textvariable=cv這個變量

    next_btn_page8 = tk.Button( window,          # 按鈕所在視窗
                                bg = 'light blue',
                                text = '下一題',  # 顯示文字
                                command = next_button_function_budget
                                ) # 按下按鈕所執行的函數
                    
    next_btn_page8.grid(row = 3, column = 0, columnspan = 12)

########################################### create first page to  ##############################################
def query_restaurant():
    # add code to query food
    print("query result")

create_page1()

print(all_data_list)
window.mainloop()

