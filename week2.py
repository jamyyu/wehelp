print("===Task1===")
def find_and_print(messages, current_station):
# your code here
    greenline={"Songshan":1,"Nanjing Sanmin":2,"Taipei Arena":3,"Nanjing Fuxing":4,"Songjiang Nanjing":5,"Zhongshan":6,
    "Beimen":7,"Ximen":8,"Xiaonanmen":9,"Chiang Kai-Shek Memorial Hall":10,
    "Guting":11,"Taipower Building":12,"Gongguan":13,"Wanlong":14,"Jingmei":15,
    "Dapinglin":16,"Qizhang":17,"Xiaobitan":17.1,"Xindian City Hall":18,"Xindian":19}
    # 抓出訊息中的捷運站,比對是否為 greenline 字典中有的捷運站,有的裝進序列中
    stations=[]
    for key in messages:
        information=messages[key]
        #print(information)
        for key in greenline:
            if key in information:
                station=key
                stations.append(station)        
    #print(stations)
    # 輸入的捷運站換成 greenline 字典的 value
    if current_station in greenline:
        current_station_number=greenline[current_station]
        #print(current_station_number)
    else:
        print("你不在新店線上喔！")
        return
    # stations 中的捷運站換成 greenline 字典的 value，再跟current_station_number作比較，算出距離後放入 distance 字典
    distance={}
    if stations!=[]:
        for i in stations:
            #print(greenline[i])
            if i !="Xiaobitan" and current_station_number !=17.1: #我跟朋友的站都不是小碧潭
                absolute_difference=abs(greenline[i]-current_station_number)
                distance[i]=absolute_difference
            elif i=="Xiaobitan" and current_station_number ==17.1: #我跟朋友都是小碧潭
                absolute_difference=abs(greenline[i]-current_station_number)
                distance["Xiaobitan"]=absolute_difference    
            elif i=="Xiaobitan" and current_station_number !=17.1: #朋友在小碧潭   
                absolute_difference=abs(greenline["Qizhang"]-current_station_number)+1
                distance["Xiaobitan"]=absolute_difference
            elif i!="Xiaobitan" and current_station_number==17.1:  #我在小碧潭
                absolute_difference=abs(greenline[i]-(current_station_number-0.1))+1  
        #print(distance)
    else:
        print("沒有朋友在新店線上喔！")
        return
    # 找 distance 字典中值最小的，抓到的 key 會是最靠近的捷運站
    for key in distance:
        closest_station=min(distance, key=lambda x: distance[x])
    #print(closest_station)
    # 把 closest_station 去對 messages 裡面的值，抓出人名
    for key in messages:
        if closest_station in messages[key]:
            print(key)

messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}
find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian





print("===Task2===")
# 先依時間選出可能的候選人
# 都沒有人有空print("No Service")
# 有空的人依照再乎費用(低)還是評分(高)去選
# 被預約的時間寫到列表裡
appointment={}
# your code here, maybe
def book(consultants, hour, duration, criteria):
# your code here
    global appointment # 聲明全域變數
    # 得出bookedtime的集合
    bookedtime={hour} 
    i=0
    while i<duration:
        hour=hour+1
        i+=1
        bookedtime.add(hour) 
        #print(hour)
        #print(bookedtime)
    # 預約者輸入的顧問名單，創建顧問字典（每個顧問先加入空集合）
    name_sets={}
    for consultant in consultants:
        name_sets[consultant["name"]]=set() 
    #print(name_sets)
    # 把顧問名單加到appintment字典，如果已有重複的key則不加入
    for key, value in name_sets.items():
        if key not in appointment:
            appointment[key]=value
    #print(appointment)
    # 用集合交集，核對顧問的時間是否可以，可以的先加到 available 列表
    available=[]
    for key, value in appointment.items():
        intersection=value & bookedtime
        if intersection:
            continue
        else:
            available.append(key)
    #print(available)
    if available==[]:
        print("No Service")
        return
    #print(available)
    # consultant["name"] 的值在 available (可選候選人序列)中，把可以人選的字典放入 compare 序列
    compare=[]
    for consultant in consultants:
        if consultant["name"] in available:
            compare.append(consultant)
    #print(compare)
    # 拿到最終要比較的字典，去找依照 criteria 的最優解
    if compare!=[]:
        if criteria== "price":
            best_criteria_person = min(compare, key=lambda x: x["price"])
            print((best_criteria_person["name"]))
        elif criteria== "rate":
            best_criteria_person = max(compare, key=lambda x: x["rate"])
            print((best_criteria_person["name"]))
    # 找到最優解之後寫入 appointment 作預約（問題：字典已有的key，找到key把新的set加入新資料。）
    #print(appointment)
        time=bookedtime|appointment[best_criteria_person["name"]] #取聯集
        if best_criteria_person["name"] in appointment:
            appointment[best_criteria_person["name"]].update(time)
    #print(appointment)
    
consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
]
book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John




print("===Task3===")
# 把名子當陣列
# len (name)去看名字奇數還偶數，取第幾個值
# 作一個名字跟中間名的字典
# 再做一個字典計算value
# 找出value計算為１的 key 印出來
# 試錯歷程：一開始只抓出中間名，放到字典計算數量，發現這樣最後無法印出名字，只印出中間名，還是要能對應本名。
 
def func(*data):
    name_dic={}
    for name in data:
        n=len(name)
        if n%2==1: #n為奇數
            i=int(n/2-0.5)
        else:
            i=int(n/2)
        middle_name=name[i]
        name_dic[name]=middle_name
    #print(name_dic)
    value_counts = {}
    for value in name_dic.values():
        if value in value_counts:
            value_counts[value]+= 1
        else:
            value_counts[value]= 1
    #print(value_counts)
    found=False
    for key, value in value_counts.items():
        if value == 1: #雙等號用於比較操作，非單等號！ 
            unique_middle_names=key
            for key, value in name_dic.items():
                if value == unique_middle_names:
                    print(key)
                    found=True
    if not found:
        print("沒有")
        
    
              
func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安




print("===Task4===")
def get_number(index):
    list=[0]
    number=0
    for i in range(1,index+1):
        if i%3==0:
            number=list[i-1]-1
        else:
            number=list[i-1]+4
        list.append(number)
    result=list[index]
    print(result)
    

get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70