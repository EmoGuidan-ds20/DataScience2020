import csv
import json

def json_to_csv():
    json_file = open("data/评论4.json", "r", encoding='utf8')  #输入需要转换格式的json文件
    csv_file = open("text.csv", "w",newline='')   #转换后的文件名和文件类型
    item_list = json.load(json_file)
    head=[]
    rows= [[]for i in range(1500)]
    head.append(' ')
    j=0
    for key in item_list[0][1]:
        rows[j].append(key)
        j+=1
    for i in range(len(item_list)):
        head.append(item_list[i][0])
        j=0
        for key in item_list[i][1]:
            rows[j].append(item_list[i][1][key])
            j+=1
    # csv文件写入对象
    csv_writer = csv.writer(csv_file)
    # 先写入表头字段数据
    csv_writer.writerow(head)
    # 再写入表的值数据
    csv_writer.writerows(rows)

    csv_file.close()
    json_file.close()

if __name__ == "__main__":
    json_to_csv()