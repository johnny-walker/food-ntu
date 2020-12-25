from selection_method import *
import pandas as pd
import random
import time, datetime
import os

def load_data():
    path = os.path.join(os.path.dirname(__file__),"data_new.csv")
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
def random_pick(df, number=5):
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

# # print the result
# def print_result(result, number):
#     for i in range(min(len(result),number)):
#         target = result.loc[i]
#         print(f"---------------------------------------------------------")
#         print(f"推薦您的第 {i+1} 家餐廳資訊如下：")
#         print(f"餐廳：{target[0]}")
#         print(f"地址：{target[2]}")
#         print(f"價位：{target[3]}")
#         print(f"營業時間：{target[11]}")
#         if all_data_list[6] == 1:
#             print(f"天氣：{target[13]}")
#     print(f"---------------------------------------------------------")

# def string_result(result, number):
#     output = ""
#     for i in range(min(len(result),number)):
#         target = result.loc[i]
#         output += "---------------------------------------------------------\n"
#         output += f"推薦您的第 {i+1} 家餐廳資訊如下：\n"
#         output += f"餐廳：{target[0]}\n"
#         output += f"地址：{target[2]}\n"
#         output += f"價位：{target[3]}\n"
#         output += f"營業時間：{target[11]}\n"
#         if all_data_list[6] == 1:
#             output += f"天氣：{target[13]}\n"
#     output += "---------------------------------------------------------\n"
#     return output

# # get result
# def get_result(all_data_list, number = 5):

#     df = load_data()
#     time_range = ["一", 1200]
#     place_range = all_data_list[0]
#     type_range = all_data_list[1]
#     staple_range = all_data_list[2]
#     meat_range = all_data_list[3]
#     weather_range = all_data_list[4]
#     here_go_range = all_data_list[5]
#     people_range = int(all_data_list[6])
#     money_range = all_data_list[-1]

#     # select
#     df_select = df.copy()
#     if len(df_select) != 0:
#         df_select = time_selection(df_select, time_range)
#     if len(df_select) != 0:
#         df_select = place_selection(df_select, place_range)
#     if len(df_select) != 0:
#         df_select = type_selection(df_select, type_range)
#     if len(df_select) != 0:
#         df_select = staple_selection(df_select, staple_range)
#     if len(df_select) != 0:
#         df_select = here_go_selection(df_select, here_go_range)
#     if len(df_select) != 0:
#         if here_go_range != "外帶":
#             df_select = people_selection(df_select, people_range)
#     if len(df_select) != 0:
#         df_select = meat_selection(df_select, meat_range)
#     if len(df_select)!= 0 and (call_weather ==True) :
#         df_select = weather_selection(df_select, weather_range)
#     # if len(df_select) != 0:
#     df_select = money_selection(df_select, money_range)

#     if len(df_select) != 0:
#         result = random_pick(df_select, number=5)
#         print_result(result, number)
#         return string_result(result, number)
#     else:
#         print("沒找到>_< 再試一次吧QQ")
#         return "沒找到>_< 再試一次吧QQ"

