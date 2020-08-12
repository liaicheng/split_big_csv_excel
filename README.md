# split_big_csv_excel
## requirement
any python version
pip install pandas
pip install numpy
pip install xlrd

## usage
python split_big_file.py {source_file} {every_file_row_num} {destination_path} {source_type} {destination_type} {encoding}
* example
python split_big_file.py /Users/liaicheng/Documents/sfda_gov_qixie_jinkou.csv 10000 /Users/liaicheng/PycharmProject/split_big_csv_excel/data/ csv excel gb2312

