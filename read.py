import json
import re
print("************菜單************")
print("--------1.電影的名字--------")
print("--------2.電影的ＩＤ--------")
print("--------3.電影的上映時間-----")
print("--------4.電影的國家及地區---")
print("--------5.電影的片長---------")
print("--------6.電影的類型---------")
print("--------7.電影的演員列表------")
print("--------8.電影的制作公司列表---")
print("--------9.電影的發行公司列表---")
print("--------10.電影的導演列表-----")
Name,number = input("請輸入需要得到的數據的電影名稱及需要獲取的信息序號：").split()
with open(Name+".json",'r') as load_f:
    load_dict = load_f.read()
    test = re.sub('\'', '\"', load_dict)
    # print(test)
    result = json.loads(test)
    actors = result["actor"]
    name = result["name"]
    id = result["id"]
    companys = result["company"]
    distributors = result["distributor"]
    directors = result["director"]
    data = result["data"]
    country =result["country"]
    length = result["length"]
    film = result["film"]
#讀取電影名字
if number=='1':
    print("name:",name)
#讀取電影id
if number=='2':
    print("id:",id)
#讀取電影上映時間
if number=='3':
    print('data:', data)
#讀取電影國家及地區
if number == '4':
    print('country:', country)
#讀取電影片長
if number=='5':
    print('length:', length)
#讀取電影類型
if number=='6':
    print('film:',film)
#讀取電影演員
if number == '7':
    a_arry =[]
    a_dict ={}
    a_x=0
    for a_x in range(0,20):
        if actors.split("、")[a_x]:
            a_arry.append(actors.split("、")[a_x])
            for actor in a_arry:
                a_chinese = ''.join(filter(lambda x: ord(x) > 255, actor)).strip()
                a_engish = ''.join(filter(lambda x: ord(x) < 255, actor)).strip()
                a_dict[a_chinese] = a_engish
        else:
            break
    print('actor:',a_dict)
#讀取電影制作公司
if number=='8':
    com_arry =[]
    com_dict ={}
    com_x=0
    for com_x in range(0,20):
        if companys.split("、")[com_x]:
            com_arry.append(companys.split("、")[com_x])
            for company in com_arry:
                com_chinese = ''.join(filter(lambda x: ord(x) > 255, company)).strip()
                com_engish = ''.join(filter(lambda x: ord(x) < 255, company)).strip()
                com_dict[com_chinese] = com_engish
        else:
            break
    print('company:',com_dict)
#讀取電影發行公司
if number=='9':
    dis_arry =[]
    dis_dict ={}
    dis_x=0
    for dis_x in range(0,20):
        if distributors.split("、")[dis_x]:
            dis_arry.append(distributors.split("、")[dis_x])
            for distributor in dis_arry:
                dis_chinese = ''.join(filter(lambda x: ord(x) > 255, distributor)).strip()
                dis_engish = ''.join(filter(lambda x: ord(x) < 255, distributor)).strip()
                dis_dict[dis_chinese] = dis_engish
        else:
            break
    print('distributor:',dis_dict)
#讀取電影導演
if number=='10':
    dir_arry =[]
    dir_dict ={}
    dir_x=0
    for dir_x in range(0,20):
        if directors.split("、")[dir_x]:
            dir_arry.append(directors.split("、")[dir_x])
            for director in dir_arry:
                dir_chinese = ''.join(filter(lambda x: ord(x) > 255, director)).strip()
                dir_engish = ''.join(filter(lambda x: ord(x) < 255, director)).strip()
                dir_dict[dir_chinese] = dir_engish
        else:
            break
    print('director:',dir_dict)
