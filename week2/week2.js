console.log("===Task1===")
function findAndPrint(messages, currentStation){
    const greenLine = {
    "Songshan":1, "Nanjing Sanmin":2, "Taipei Arena":3, "Nanjing Fuxing":4, "Songjiang Nanjing":5, "Zhongshan":6,
    "Beimen":7, "Ximen":8, "Xiaonanmen":9, "Chiang Kai-Shek Memorial Hall":10,
    "Guting":11, "Taipower Building":12, "Gongguan":13, "Wanlong":14, "Jingmei":15,
    "Dapinglin":16, "Qizhang":17, "Xiaobitan":17.1, "Xindian City Hall":18, "Xindian":19
    };
    // 抓出訊息中的捷運站,比對是否為 greenLine 物件中有的捷運站,有的裝進序列中
    let stations = [];
    Object.keys(messages).forEach(key => {
        let information = messages[key];
        Object.keys(greenLine).forEach(station => {
            if (information.includes(station)) {
                stations.push(station);
            }
        });
    });
    //console.log(stations);
    // 輸入的捷運站換成 greenLine 物件的資料
    if (!greenLine[currentStation]) {
        console.log("你不在新店線上喔！");
        return;
    }
    // 輸入的捷運站換成 greenLine 物件的資料
    let currentStationNumber = greenLine[currentStation];
    //console.log(currentStationNumber);
    // stations 中的捷運站換成 greenLine 物件相同成員的資料，再跟 currentStationNumber 作比較，算出距離後放入 distance 物件紀錄
    let distance = {};
    if(!stations == []){
        stations.forEach(i => {
            if(i !== "Xiaobitan" && currentStationNumber !== 17.1){
                distance[i] = Math.abs(greenLine[i] - currentStationNumber);
            }else if(i == "Xiaobitan" && currentStationNumber == 17.1){
                distance[i] = Math.abs(greenLine[i] - currentStationNumber)
            }else if(i == "Xiaobitan" && currentStationNumber !== 17.1){
                distance[i] = Math.abs(greenLine["Qizhang"] - currentStationNumber)+1
            }else if(i !== "Xiaobitan" && currentStationNumber == 17.1){
                distance[i] = Math.abs(greenLine[i] - (currentStationNumber-0.1))+1
            }
        }
        )
    }
        //console.log(distance);
    if (Object.keys(distance).length === 0) {
        console.log("沒有朋友在新店線上喔！");
        return;
    }
    // 找 distance 物件中資料值最小的，抓到的會是最靠近的捷運站，印出朋友名
    let closestStation = Object.keys(distance).reduce((a, b) => distance[a] < distance[b] ? a : b);
    Object.keys(messages).forEach(key => {
        if (messages[key].includes(closestStation)) {
            console.log(key);
        }
    });   
}

   
const messages={
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Leslie":"I'm at home near Xiaobitan station.",
"Vivian":"I'm at Xindian station waiting for you."
};
findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian





console.log("===Task2===")
var appointment={};
function book(consultants, hour, duration, criteria){
    // 得出bookedtime的集合
    var bookedtime=new Set([hour]);
    let i = 0;
    while(i<duration){
        hour+=1;
        i++;
        bookedtime.add(hour);
    }
    //console.log(bookedtime);
    // 預約者輸入的顧問名單，創建顧問字典（每個顧問先加入空集合）
    let name_sets = {};
    for (let i = 0; i < consultants.length; i++) {
        let consultant=consultants[i]; 
        name_sets[consultant["name"]]=new Set();
    }
    //console.log(name_sets);
    // 把顧問名單加到 appintment 字典，如果已有重複的 key 則不加入
    for (let key in name_sets){
        if (!(key in appointment)){
            let value = name_sets[key];
            appointment[key]=value
        }
    }
    //console.log(appointment)
    // 確認可用顧問，可以的先加到 available 列表
    let available = [];
    for (let key in appointment) {
        let intersection = new Set([...appointment[key]].filter(x => bookedtime.has(x)));
        if (intersection.size === 0) {
        available.push(key);
        }
    }
    if (available.length === 0) {
        console.log("No Service");
        return;
    }
    //console.log(available)
    //  available (可選候選人序列)中，把可以人選的物件放入 compare 序列
    let compare = consultants.filter(consultant => available.includes(consultant.name));
    //console.log(compare)
    // 依照 criteria 找最優解
    if (compare.length !== 0) {
        if (criteria === "price") {
            var best_criteria_person = compare.reduce((min, p) => (p.price < min.price ? p : min));
            console.log(best_criteria_person.name);    
        } else if (criteria === "rate") {
            var best_criteria_person = compare.reduce((max, p) => (p.rate > max.rate ? p : max));
            console.log(best_criteria_person.name);
        }
    //預約時間寫入 appointment 
        if (best_criteria_person.name in appointment) {
            let time = new Set([...bookedtime, ...appointment[best_criteria_person.name]])    
            appointment[best_criteria_person.name] = time;
        }                                   
    }
}
const consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
];
book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
            book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John





console.log("===Task3===")
function func(...data){
let name_obj={};
    for (let x=0;x<data.length;x++){
        let name=data[x];
        //console.log(name)
        let n=name.length;
        if(n%2==1){
            i=n/2-0.5;
        }else{
            i=n/2;
        }
        let middle_name=name[i];
        //console.log(middle_name)
        name_obj[name]=middle_name;
    }
//console.log(name_obj);  
let value_counts = {};
for (let value of Object.values(name_obj)){
    if(value in value_counts){
        value_counts[value]+=1;
    }else{
        value_counts[value]=1;
    }
}
//console.log(value_counts)
let found=false
for(let [key,value] of Object.entries(value_counts)){
    if(value==1){
        let unique_middle_names=key
        for(let [key,value] of Object.entries(name_obj)){
            if(value==unique_middle_names){
                console.log(key)
                found=true
            } 
        }
    }
}
if (found==false){
    console.log("沒有")
}
}
func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安





console.log("===Task4===")
/* 
0, 4, 8, 7, 11, 15, 14, 18, 22, 21, 25,...
+4 +4 -1 的順序 for 迴圈
設一個list[]用迴圈加入陣列的數字
最後印出 list[index]
*/
function getNumber(index){
    let list=[0];
    let number=0;
    for (let i=1;i<=index+1;i++){
        if(i%3==0){
        number=list[i-1]-1;
        }else{
        number=list[i-1]+4;
        }
    list.push(number);
    }
    result=list[index];
    console.log (result);
    }
    getNumber(1); // print 4
    getNumber(5); // print 15
    getNumber(10); // print 25
    getNumber(30); // print 70
    