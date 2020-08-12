import pandas as pd
import numpy as np
import sys

def split_csv(path,row_num,dest_path,type="csv",dest_type="excel",encoding="utf-8"):
    if type=="csv":
        df = pd.read_csv(path,header=0)
        file_name = path.split("/")[-1].replace('.csv',"")
    elif type == "excel":
        df = pd.read_excel(path,header=0)
        file_name = path.split("/")[-1].replace('.xls',"").replace(".xlsx","")

    if dest_type == "excel":
        end = ".xls"
    elif dest_type == "csv":
        end = ".csv"

    keys = df.keys()

    arr = [keys]
    index = 0
    file_index = 0

    for i in df.iterrows():
        i = i[1]
        # print(i)
        if index < row_num:
            arr.append([i[k]for k in keys])
            index += 1
        else:
            index=0
            print(len(arr))
            narr = np.array(arr)
            ndf = pd.DataFrame(narr)
            print(dest_path+file_name+str(file_index)+end)
            if dest_type == "excel":
                ndf.to_excel(dest_path+file_name+" _" + str(file_index)+end,encoding)
            elif dest_type == "csv":
                ndf.to_csv(dest_path + file_name + "_" + str(file_index) + end)
            file_index += 1
            arr = [keys]
    if len(arr)> 0:
        narr = np.array(arr)
        ndf = pd.DataFrame(narr)
        print(dest_path + file_name + str(file_index) + end)
        if dest_type == "excel":
            ndf.to_excel(dest_path + file_name + "_" + str(file_index) + end, encoding)
        elif dest_type == "csv":
            ndf.to_csv(dest_path + file_name + "_" +str(file_index) + end)

if __name__ == "__main__":
    args = sys.argv[1:]
    print(args,len(args))
    if len(args) < 4:
        print("no enough parameter: example[/Users/liaicheng/Documents/sfda_gov_qixie_jinkou.csv,10000 /Users/liaicheng/Documents/ csv]")
    else:
        path = args[0]
        row_num = args[1]
        dest_path =args[2]
        type = args[3]
        dest_type = args[5] if len(args)==5 else type
        encoding = args[6] if len(args) == 6 else "utf-8"
        split_csv(path,int(row_num),dest_path,type,dest_type,encoding)
