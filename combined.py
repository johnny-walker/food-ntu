# 引入 tkinter 模組
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import requests, json 
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


all_data_list = []  # a list collecting all data needed
    

# define pages
################################################## page_place 想在哪兒覓食呢 ############################################
label_page1 = None
lstbox_page1 = None
next_btn_page1 = None

def create_page_place():
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
        create_page_type()
    
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


################################################## page_type 想吃哪一種國家的料理呢 #########################################
label_page2 = None
lstbox_page2  = None
next_btn_page2  = None
  
def create_page_type():  
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
        create_page_staple()
    
    # question display
    label_page2 = tk.Label( window, 
                            text = "想吃哪一種國家的料理呢？", 
                            font = ("Arial", 12),  
                            width = 60, height = 2)
    label_page2.grid(column = 3, row = 0, columnspan =  12, sticky = tk.NE + tk.SW)

    # 列出該題所有選項
    options = tk.StringVar()
    options.set("中式 西式 台式 美式 港式 韓式 日式 東南亞料理 南洋料理 中東料理 雲南料理")

    # 把所有選項都放在框框中
    lstbox_page2 = tk.Listbox(window, listvariable = options, selectmode = "multiple")
    lstbox_page2.selection_set(0)   # select first one
    lstbox_page2.grid(column = 3, row = 1, rowspan = 2, columnspan = 12, sticky = tk.NE + tk.SW) 
    

    next_btn_page2 = tk.Button( window,          # 按鈕所在視窗
                                bg = 'light blue',
                                text = '下一題',  # 顯示文字
                                command = next_button_function_type) # 按下按鈕所執行的函數
                    
    next_btn_page2.grid(column = 3, row = 5, columnspan = 12, sticky = tk.NE + tk.SW)


####################################### page_staple 想吃什麼種類的主食？###############################################

label_page3 = None
lstbox_page3 = None
next_btn_page3 = None

def create_page_staple():
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
        create_page_meat()
    
    
    # question display
    label_page3 = tk.Label( window, 
                            text = "想吃什麼種類的主食？", 
                            font = ("Arial", 12),  
                            width = 60, height = 2)
    label_page3.grid(column = 3, row = 0, columnspan =  12, sticky = tk.NE + tk.SW)

    # 列出該題所有選項
    options = tk.StringVar()
    options.set("米食 麵食 鍋物 排餐 輕食 漢堡 烤物 披薩 胡椒餅 沙拉 三明治 派 滷味 餃類 糕點 炸物")

    # 把所有選項都放在框框中
    lstbox_page3 = tk.Listbox(window, listvariable = options, selectmode = "multiple")#, bg = '#FFC0CB')
    lstbox_page3.selection_set(0)   # select first one
    lstbox_page3.grid(column = 3, row = 1, rowspan = 2, columnspan = 12, sticky = tk.NE + tk.SW) 
    

    next_btn_page3 = tk.Button( window,          # 按鈕所在視窗
                                bg = 'light blue',
                                text = '下一題',  # 顯示文字
                                command = next_button_function_staple) # 按下按鈕所執行的函數
                    
    next_btn_page3.grid(column = 3, row = 5, columnspan = 12, sticky = tk.NE + tk.SW)

############################################ page_meat 吃素食嗎? ################################################# 
label_page5 = None
radioValue_page5 = None
radioOne_page5 = None
radioTwo_page5 = None
radioThree_page5 = None
#labelValue_page5 = None
next_btn_page5 = None

def create_page_meat():     
    def next_button_function_vegan():
        if radioValue_page5.get() == 1:
            all_data_list.append('素')
        elif radioValue_page5.get() == 2:
            all_data_list.append('葷')
        elif radioValue_page5.get() == 3:
            all_data_list.append('無肉不歡')   
        # clear current page
        radioOne_page5.destroy()
        radioTwo_page5.destroy()
        radioThree_page5.destroy()    
        label_page5.destroy()
        #labelValue_page5.destroy()
        next_btn_page5.destroy()
        # create next page
        create_page_weather()

    #vege_list = []

    # set up a label
    label_page5 = tk.Label( window,                 # 文字標示所在視窗
                            #bg = '#EEBB08',         #  背景顏色
                            font = ('Arial', 12),   # 字型與大小
                            width = 60, height = 2,
                            text = '吃素食嗎?')  # 顯示文字
                
    label_page5.grid(column = 0, row = 0, columnspan = 12)


    # set up radiobuttons
    radioValue_page5 = tk.IntVar() 

    radioOne_page5 = tk.Radiobutton(window, text='素', anchor = 'w',
                                    variable = radioValue_page5,value = 1) 
    radioTwo_page5 = tk.Radiobutton(window, text='葷素皆可', anchor = 'w',
                                    variable = radioValue_page5,value = 2) 
    radioThree_page5 = tk.Radiobutton(window, text='無肉不歡', anchor = 'w',
                                    variable = radioValue_page5,value = 3)                               
    radioValue_page5.set(1)

    radioOne_page5.grid(column=0, row=1, columnspan = 12, sticky = tk.NE + tk.SW)
    radioTwo_page5.grid(column=0, row=2, columnspan = 12, sticky = tk.NE + tk.SW)
    radioThree_page5.grid(column=0, row=3, columnspan = 12, sticky = tk.NE + tk.SW)

    # set a label showing your choice
    #labelValue_page5 = tk.Label(window, textvariable = radioValue_page5)
    #labelValue_page5.grid(column=3, row=9, columnspan =  12)


    # set a button
    next_btn_page5 = tk.Button( window,          # 按鈕所在視窗
                                bg = 'light blue',
                                text = '下一題',  # 顯示文字
                                command = next_button_function_vegan) # 按下按鈕所執行的函數
                    
    next_btn_page5.grid(column = 0, row = 4, columnspan = 12)


################################# page_weather 要不要善用天氣小精靈推薦你適合的食物呢? ##################################### 
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

def create_page_weather():
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
        create_page_here_go()


    # set up a label
    label_page6 = tk.Label( window,                 # 文字標示所在視窗
                            #bg = '#EEBB08',         #  背景顏色
                            font = ('Arial', 12),   # 字型與大小
                            width = 60, height = 2,
                            text = '現在溫度是'+ str(temperature) + '度，要不要善用天氣小精靈推薦你適合的食物呢?')  # 顯示文字
                
    label_page6.grid(column = 0, row = 0, columnspan = 12)

    # set up radiobuttons
    radioValue_page6 = tk.IntVar() 
    radioOne_page6 = tk.Radiobutton(window, text = '好呀', anchor = 'w',
                                    variable = radioValue_page6, value = 1) 
    radioTwo_page6 = tk.Radiobutton(window, text = '先不要', anchor = 'w',
                                    variable = radioValue_page6, value = 2) 
    radioValue_page6.set(1)                            

    radioOne_page6.grid(column = 0, row = 1, columnspan = 12, sticky = tk.NE + tk.SW)
    radioTwo_page6.grid(column = 0, row = 2, columnspan = 12, sticky = tk.NE + tk.SW)


    # set a label showing your choice
    #labelValue_page6 = tk.Label(window, textvariable = radioValue_page6)
    #labelValue_page6.grid(column=6, row=8, columnspan =  12)


    # set a button
    next_btn_page6 = tk.Button( window,          # 按鈕所在視窗
                                bg = 'light blue',
                                text = '下一題',  # 顯示文字
                                command = next_button_function_temp) # 按下按鈕所執行的函數
                    
    next_btn_page6.grid(column = 0, row = 3, columnspan = 12)



################################################ page_here_go 內用還是外帶呢? #######################################
label_page4 = None
radioValue_page4 = None
rdioOne_page4 = None 
rdioTwo_page4 = None
rdioThree_page4 = None
#labelValue_page4 = None
next_btn_page4 = None

def create_page_here_go():
    def next_button_function_eatin():
        if radioValue_page4.get() == 1:
            all_data_list.append('內用')
        elif radioValue_page4.get() == 2:
            all_data_list.append('外帶')
        elif radioValue_page4.get() == 3:
            all_data_list.append('都可以')       
        # clear current page
        label_page4.destroy()
        rdioOne_page4.destroy()
        rdioTwo_page4.destroy()
        rdioThree_page4.destroy()
        label_page4.destroy()
        #labelValue_page4.destroy()
        next_btn_page4.destroy()
        # create next page
        create_page_people()
    

    # set up a label
    label_page4 = tk.Label(window,                 # 文字標示所在視窗
                    #bg = '#EEBB08',         #  背景顏色
                    font = ('Arial', 12),   # 字型與大小
                    width = 60, height = 2,
                    text = '內用還是外帶呢?')  # 顯示文字

    # place                 
    label_page4.grid(column=0, row=0, columnspan =  12)


    # set up three radiobuttons
    radioValue_page4 = tk.IntVar() 

    rdioOne_page4 = tk.Radiobutton( window, text='內用', anchor = 'w',
                                    variable=radioValue_page4, value = 1) 
    rdioTwo_page4 = tk.Radiobutton( window, text='外帶', anchor = 'w',
                                    variable=radioValue_page4, value = 2) 
    rdioThree_page4 = tk.Radiobutton(window, text='都可以', anchor = 'w',
                                     variable=radioValue_page4, value = 3)
    radioValue_page4.set(1)


    rdioOne_page4.grid(column=0, row=1, columnspan =  12, sticky = tk.NE + tk.SW)
    rdioTwo_page4.grid(column=0, row=2, columnspan =  12, sticky = tk.NE + tk.SW)
    rdioThree_page4.grid(column=0, row=3, columnspan =  12, sticky = tk.NE + tk.SW)

    # set a label showing your choice
    #labelValue_page4 = tk.Label(window, textvariable = radioValue_page4)
    #labelValue_page4.grid(column=3, row=9, columnspan =  12)

    # set a button
    next_btn_page4 = tk.Button( window,          # 按鈕所在視窗
                                bg = 'light blue',
                                text = '下一題',  # 顯示文字
                                command = next_button_function_eatin
                                ) # 按下按鈕所執行的函數
                    
    next_btn_page4.grid(column = 0, row=4, columnspan = 12)


####################################### page_people 多少人要一起吃呢? #######################################################
label_page7 = None
com_time_page7 = None
next_btn_page7 = None

# 紀錄所有選過的時間(之後只選最後一筆)
people_list = []

def create_page_people():
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
        create_page_budget()

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
    com_time_page7["value"]=("請選擇人數","0","1","2","3","4","5","6","7","8","9","10","10+")
    #設置默認值
    com_time_page7.current(2)
    
    # handle selection
    com_time_page7.bind("<<ComboboxSelected>>", handle_people) #等同於textvariable=cv這個變量

    next_btn_page7 = tk.Button( window,          # 按鈕所在視窗
                                bg = 'light blue',
                                text = '下一題',  # 顯示文字
                                command = next_button_function_people
                                ) # 按下按鈕所執行的函數
                    
    next_btn_page7.grid(row = 3, column = 0, columnspan = 12)

  
    
################################## page_budget 本次用餐的預算是多少元? ######################################################
label_page8 = None
com_budget_page8 = None
next_btn_page8 = None

# 紀錄所有選過的時間(之後只選最後一筆)
budget_list = []

def create_page_budget():
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
        get_result(all_data_list)

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
    com_budget_page8["value"]=("請選擇預算", "$", "$$", "$$$", "$$$$", "$$$$$", "無預算限制")
    #設置默認值
    com_budget_page8.current(1)

    # handle selection
    com_budget_page8.bind("<<ComboboxSelected>>", handle_budget) #等同於textvariable=cv這個變量

    next_btn_page8 = tk.Button( window,          # 按鈕所在視窗
                                bg = 'light blue',
                                text = '下一題',  # 顯示文字
                                command = next_button_function_budget
                                ) # 按下按鈕所執行的函數
                    
    next_btn_page8.grid(row = 3, column = 0, columnspan = 12)

######################################### query database from quiz selections ########################################
# print the result
def print_result(result, number):
    for i in range(min(len(result),number)):
        target = result.loc[i]
        print(f"---------------------------------------------------------")
        print(f"推薦您的第 {i+1} 家餐廳資訊如下：")
        print(f"餐廳：{target[0]}")
        print(f"地址：{target[2]}")
        print(f"價位：{target[3]}")
        print(f"營業時間：{target[11]}")
        if all_data_list[4] != "N/A":
            print(f"天氣：{target[13]}")
    print(f"---------------------------------------------------------")

def string_result(result, number):
    results = []

    for i in range(min(len(result),number)):
        target = result.loc[i]
        output  = f"推薦您的第 {i+1} 家餐廳資訊如下：\n"
        output += f"餐廳：{target[0]}\n"
        output += f"地址：{target[2]}\n"
        output += f"價位：{target[3]}\n"
        output += f"營業時間：{target[11]}\n"
        if all_data_list[4] != "N/A":
            if target[13] == 'C':    
                output += f"冷冷的天最適合了~"
            elif target[13] == 'H':
                output += f"大熱天最適合了~"
            else:
                output += f"四季皆宜~"
        results.append(output)
    return results

# get result
def get_result(all_data_list, number = 5):
    print("query result from quiz:", all_data_list)

    df = load_data()
    time_range = ["一", 1200]
    place_range = all_data_list[0]
    type_range = all_data_list[1]
    staple_range = all_data_list[2]
    meat_range = all_data_list[3]
    weather_range = all_data_list[4]
    here_go_range = all_data_list[5]
    people_range = int(all_data_list[6])
    money_range = all_data_list[-1]

    # select
    df_select = df.copy()
    if len(df_select) != 0:
        print(time_range, len(df_select))
        df_select = time_selection(df_select, time_range)
    if len(df_select) != 0:
        print(place_range, len(df_select))
        df_select = place_selection(df_select, place_range)
    if len(df_select) != 0:
        print(type_range, len(df_select))
        df_select = type_selection(df_select, type_range)
    if len(df_select) != 0:
        print(staple_range, len(df_select))
        df_select = staple_selection(df_select, staple_range)
    if len(df_select) != 0:
        print(here_go_range, len(df_select))
        df_select = here_go_selection(df_select, here_go_range)
    if len(df_select) != 0:
        if here_go_range != "外帶":
            print(people_range, len(df_select))
            df_select = people_selection(df_select, people_range)
    if len(df_select) != 0:
        print(meat_range, len(df_select))
        df_select = meat_selection(df_select, meat_range)
    if len(df_select)!= 0 and (all_data_list[4] != "N/A"):
        print(weather_range, len(df_select))
        print(123)
        df_select = weather_selection(df_select, weather_range)
        print(len(df_select))
    # if len(df_select) != 0:
    df_select = money_selection(df_select, money_range)
    print("count:", len(df_select))

    if len(df_select) != 0:
        result = random_pick(df_select, number=5)
        create_result_page(string_result(result, number))
        return string_result(result, number)
    else:
        result = "沒找到>_< 再試一次吧QQ"
        create_no_result_page(result)
        print("沒找到>_< 再試一次吧QQ")
        return "沒找到>_< 再試一次吧QQ"

############################################### page_results ################################################
def create_item(no, data):
    data_height = 9

    color = '#ceddf0' if (no%2 == 0) else '#d7f7df'

    var = tk.StringVar()
    ans_label = tk.Label(window,                    # 文字標示所在視窗
                         bg = color,                #  背景顏色
                         font = ('Arial', 12),      # 字型與大小
                         width = 60, 
                         # height = data_height-2,
                         textvariable = var        # 顯示文字 
                        )        

    var.set(data)
    ans_label.grid(column=1, row = no * (data_height) + 5, columnspan = 12)

def create_result_page(results):
    # show title  "推薦結果如下："
    ans_label = tk.Label(window,                    # 文字標示所在視窗
                         bg = '#FFFF33',            #  背景顏色
                         font = ('Arial', 12),      # 字型與大小
                         width = 60, height = 2,
                         text = "推薦結果如下：")      # 顯示文字
    ans_label.grid(column=0, row=0, columnspan =  12)
    for i in range(0, len(results)): 
        create_item(i, results[i])

def create_no_result_page(message):
    ans_label = tk.Label(window,                    # 文字標示所在視窗
                         bg = '#FFFF33',            #  背景顏色
                         font = ('Arial', 12),      # 字型與大小
                         width = 60, height = 2,
                         text = message)      # 顯示文字
    ans_label.grid(column=0, row=0, columnspan =  12)

################ init the first page###############
create_page_place()

window.mainloop()

