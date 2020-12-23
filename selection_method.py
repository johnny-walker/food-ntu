def money_selection(df, money_range):
    money_list = df[4].tolist()
    money_list = [money_list[i].split(" ") for i in range(len(money_list))]
    money_bool = [False for i in range(len(money_list))]
    for i in range(len(money_list)):
        for money in money_range:
            if money in money_list[i]:
                money_bool[i] = True
                break
    return df[money_bool]

def place_selection(df, place_range):
    place_list = df[1].tolist()
    place_bool = [False for i in range(len(place_list))]
    for i in range(len(place_list)):
        for place in place_range:
            if place == place_list[i]:
                place_bool[i] = True
                break
    return df[place_bool]

def type_selection(df, type_range):
    type_list = df[5].tolist()
    type_bool = [False for i in range(len(type_list))]
    for i in range(len(type_list)):
        for food_type in type_range:
            if food_type == type_list[i]:
                type_bool[i] = True
                break
    return df[type_bool]

#主食
def staple_selection(df, staple_range):
    staple_list = df[7].tolist()
    staple_list = [staple_list[i].split(" ") for i in range(len(staple_list))]
    staple_bool = [False for i in range(len(staple_list))]
    for i in range(len(staple_list)):
        for s in staple_range:
            if s in staple_list[i]:
                staple_bool[i] = True
                break
    return df[staple_bool]

##內用外帶
def here_go_selection(df, here_go_range):
    if here_go_range == "內用":
        here_go_range = ["有"]
    elif here_go_range == "外帶":
        here_go_range = ["無"]
    elif here_go_range == "都可以":
        here_go_range = ["有", "無"]
    here_go_list = df[9].tolist()
    here_go_bool = [False for i in range(len(here_go_list))]
    for i in range(3,len(here_go_list)):
        if here_go_list[i] in here_go_range:
            here_go_bool[i] = True
    return df[here_go_bool]

# 問題六:幾人同行
def people_selection(df, people_range):
    people_list = df[10].tolist()
    people_bool = [False for i in range(len(people_list))]
    for i in range(1, len(people_list)):
        if people_list[i] == "50+":
            people_list[i] = 10000
        else:
            people_list[i] = int(people_list[i])
        if people_list[i] >= people_range:
            people_bool[i] = True
    return df[people_bool]

#葷素
def meat_selection(df, meat_range):
    meat_list = df[8].tolist()
    meat_bool = [False for i in range(len(meat_list))]
    if meat_range == "無肉不歡":
        meat_range = ["葷"]
    elif meat_range == "葷":
        meat_range = ["葷", "有提供素食", "全素"]
    elif meat_range == "素":
        meat_range = ["有提供素食", "全素"]
    for i in range(len(meat_list)):
        for meat in meat_range:
            if meat == meat_list[i]:
                meat_bool[i] = True
    return df[meat_bool]

def time_selection(df, time_range):
    today, current_time = time_range[0], time_range[1]
    date_list = df[11].tolist()
    # rearrange the time to list
    for i in range(3, len(date_list)):
        if type(date_list[i]) == str:
            if " " in date_list[i]:    
                date_list[i] = date_list[i].split(" ")
            else:
                date_list[i] = [date_list[i]]
            
            for j in range(len(date_list[i])):
                if "," in date_list[i][j]:
                    date_list[i][j] = date_list[i][j].split(",")
                else:
                    date_list[i][j] = [date_list[i][j]]
                
                for k in range(len(date_list[i][j])):
                    if "/" in date_list[i][j][k]:
                        date_list[i][j][k] = date_list[i][j][k].split("/")
                    else:
                        date_list[i][j][k] = [date_list[i][j][k]]        
    # time selection start
    time_bool = [False for i in range(len(df))]
    for i in range(3,len(date_list)):
        for j in range(len(date_list[i])):
            if today in date_list[i][j][0][0]:
                for k in range(len(date_list[i][j][1])):
                    if date_list[i][j][1][0] != "**":
                        open_time  = int(date_list[i][j][1][k][:4])
                        close_time = int(date_list[i][j][1][k][5:])
                        if current_time <= close_time and current_time >= open_time:
                            time_bool[i] = True
    return df[time_bool]
