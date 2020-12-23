import pandas as pd
import random
import time, datetime
import os
from selection_method import *

def load_data():
    path = os.path.join(os.path.dirname(__file__),"data_new.csv")
    # path = "c:\\Users\\A315\\Desktop\\meal2.csv"
    df = pd.read_csv(path, header=None, encoding="utf-8")
    # 去除標題
    df = df[1:]
    return df

def get_current_time():
    # weekday
    weekday = ["一", "二", "三", "四", "五","六","日"]

    # hour and minute
    hour   = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    output = ""
    if hour < 10:
        output += "0"+str(hour)
    else:
        output += str(hour)
    if minute < 10:
        output += "0"+str(minute)
    else:
        output += str(minute)
    return [weekday[datetime.datetime.now().weekday()],int(output)]

# random
def random_pick(df, number):
    df_list = df[0].tolist()
    number = min(number, len(df_list))
    result = random.sample(df_list, number)
    selection_bool = [False for i in range(len(df))]
    for i in range(len(selection_bool)):
        for name in result:
            if name == df_list[i]:
                selection_bool[i] = True
                break
    return df[selection_bool].reset_index()

# print the result
def print_result(number):
    for i in range(min(len(result),number)):
        target = result.loc[i]
        print(f"---------------------------------------------------------")
        print(f"推薦您的第 {i+1} 家餐廳資訊如下：")
        print(f"餐廳：{target[0]}")
        print(f"地址：{target[2]}")
        print(f"價位：{target[3]}")
        print(f"營業時間：{target[11]}")
    print(f"---------------------------------------------------------")
################################################################
############                                       #############
############                主程式開始               #############
############                                       #############
################################################################

# initial
df = load_data()
number = 10
money_range = ["$","$$"]
place_range = ["公館1","公館2","118"]
type_range = ["美式","西式"]
staple_range = ["麵食", "米食"]
# time_range = get_current_time()
time_range = ["一", 1200]
here_go_range = "都可以"
people_range = 5
meat_range = "葷"

# select
df_select = df.copy()
df_select = money_selection(df_select, money_range)
df_select = place_selection(df_select, place_range)
df_select = type_selection(df_select, type_range)
df_select = time_selection(df_select, time_range)
df_select = staple_selection(df_select, staple_range)
df_select = here_go_selection(df_select, here_go_range)
if here_go_range != "外帶":
    df_select = people_selection(df_select, people_range)
df_select = meat_selection(df_select, meat_range)


# random choose
result = random_pick(df_select,number)

# print the result
print_result(number)