import os
import pandas as pd
import csv
import time

def get_son_path(path):
    dir_son = []
    dirs = os.listdir(path)
    for dir in dirs:
        if os.path.isdir(os.path.join(path, dir)):
            dir_son.append(os.path.join(path, dir))
    return dir_son

def touch_xlsx(path, path2):  # 根据path的子路径下的文件夹名字创建表格，放到path2下
    files = os.listdir(path)
    excel_list = []
    for file in files:
        if os.path.isdir(os.path.join(path, file)):
            df = pd.DataFrame()
            excel_name = file + '.xlsx'
            df.to_excel(os.path.join(path2, excel_name))
            excel_list.append(os.path.join(path2, excel_name))
    return excel_list

def create_excel(path, excel_file):  # 将path文件夹下的csv写入excel_file
    writer = pd.ExcelWriter(excel_file)
    for dir in os.listdir(path):
        filepath = os.path.join(path, dir)
        if not os.path.getsize(filepath):
            csv_df = pd.DataFrame()
        else:
            csv_file = pd.read_csv(filepath, encoding='gbk')
            csv_df = pd.DataFrame(csv_file)
        csv_df.to_excel(writer, sheet_name=str(dir[:-4]), index=0)
    writer.save()
    writer.close()
    print(excel_file,' is finished.')

def main():
    # Full path
    path = 'D:/data/source'
    target = 'D:/data/target'
    start_time = time.perf_counter()
    print('Data is outputing.Wait a minute,please...')
    path_list, excel_list = get_son_path(path), touch_xlsx(path, target)
    for i in range(len(path_list)):
        create_excel(path_list[i], excel_list[i])
    end_time = time.perf_counter()
    print('Awesome,Spend time %s\'s to process %s files' %
          (end_time - start_time, len(path_list)))

main()
