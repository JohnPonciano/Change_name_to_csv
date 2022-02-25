
import re 
import os
import shutil
import pandas as pd

main_folder = r'img'
csv_file = r'csv_editavel.csv'

def rename_file(file):

    matricula_csv = pd.read_csv(csv_file, sep=',', usecols=['matricula', 'img'])
    check_matriculas = matricula_csv.loc[0:, 'matricula'].to_list()
    check_row_img = matricula_csv.loc[0:,'img'].to_list()

    for row_file in check_row_img:

        if file == row_file:
            for row in check_matriculas:
                matricula_index = check_matriculas.index(row)
                img_index = check_row_img.index(row_file)
                # print("Line Name", row)
                # print("Matricula INDEX", matricula_index)
                # print("IMG INDEX", img_index)
                if matricula_index == img_index:
                    row_file,file_extension = os.path.splitext(row_file)
                    file_name, file_extension = os.path.splitext(file)
                    file_name_numbers = re.findall(r'\d+',file_name)
                    file_name_numbers = row
                    return f'{file_name_numbers}{file_extension}'
                else:
                    continue
        else:
            continue

def files_loop(root,dirs,files):
    for file in files:
        new_file_name = rename_file(file)
        old_file_full_path = os.path.join(root,file)
        new_file_full_path = os.path.join(root,new_file_name)
        print(f'Movendo {file} para {new_file_name}')
        shutil.move(old_file_full_path, new_file_full_path)

def main_loop():
    for root, dirs, files in os.walk(main_folder):
        files_loop(root,dirs, files)

if __name__ == '__main__':
    main_loop()

