import time
def save_add_text(path,text,index):
    times = []
    for i in range(0,5):
        times.append(time.localtime()[i])
    year,mon,day,hour,min = times[0],times[1],times[2],times[3],times[4]
    with open(path,"a+") as file:
        file.write(index +"\t" + text + "\t" + str(year) +"\t" + str(mon) +"\t" + str(day) + "\t" + "T" + "\n")

# 将新的文本放置在text文件的末尾
def read_new_text(path):
    count = 0
    data = []
    with open(path,"r") as file:
        file.seek(0,2)
        position = file.tell()
        while position >= 0 and count < 10:
            file.seek(position)
            last_char = file.read(1)
            if last_char == "\n":
                last_line = file.readline().strip()
                data.append(last_line)
                count += 1
                position -= len(last_line)
            position -= 1
    return data
    
if __name__ == "__main__":
    path = "text_add.txt"
    text = "111"
    # save_add_text(path,text)
    # for i in range(100):
    #     text = str(i)
    #     save_add_text(path,text)
    read_new_text(path)
    print(read_new_text(path))

    # print(time.localtime())