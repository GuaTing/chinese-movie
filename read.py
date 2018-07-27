import json
import re
with open("唐山大地震.json",'r') as load_f:
    load_dict = load_f.read()
    test = re.sub('\'', '\"', load_dict)
    print(test)
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
print("name:",name)
#讀取電影id
print("id:",id)
# 讀取電影上映時間
print('data:', data)
# 讀取電影國家及地區
print('country:', country)
# 讀取電影片長
print('length:', length)
#
print('film:',film)
#讀取電影演員
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
