# # Database Connection 20-10-2022
# import datetime
# import mysql.connector
#
# name = input("Please Enter You Name :")
# eng = int(input("Enter English Number :"))
# urdu = int(input("Enter Urdu Number :"))
# math = int(input("Enter Math Number :"))
# total_num = eng + urdu + math
# print(f"{name} Your Total Number {total_num} :")
# pre = (total_num * 100) / 300
# cureent = datetime.datetime.now()
# print(f"{name} Your Precantage is {pre} ")
#
# # data save in file
# f = open("studentdata.txt", "a")
# f.write(f"{name}\n Your English Number {eng}\n Your Math Number {math}\n Your Urdu Number  {urdu}\n Your Total Number {total_num}\n Your Precantage Number {pre}\n Your Cureent {cureent}\n ")
# f.close()
#
# # database connection
# DBcon = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "",
#     database = "studentrec"
# )
#
# cursor = DBcon.cursor()
#
# insert_query = "INSERT INTO `std`( `name`, `english`, `math`, `urdu`, `total_num`, `per`, `cur`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
# mari_value = [name,eng,math,urdu,total_num,pre,cureent]
#
# cursor.execute(insert_query,mari_value)
# DBcon.commit()
# DBcon.close()

# 22\oct\2022

import pandas
from openpyxl.workbook import Workbook
import lxml
#
# khaadi = {
#     "name" : ["Fabrics 3 Piece Suit","Fabrics 3 Piece Suit","Fabrics 3 Piece Suit","Fabrics 3 Piece Suit","Fabrics 3 Piece Suit","Fabrics 3 Piece Suit","Fabrics 3 Piece Suit","Fabrics 3 Piece Suit"],
#     "information" : ["Essentials Printed Top Bottoms Dupatta","Essentials Printed Top Bottoms","Essential Printed Top Bottoms Dupatta","Essential Printed Top Bottoms Dupatta","Casuals Knits Printed T-shirt","Essential Dyed Embroidered Kurta","Essential Printed Top Bottoms Dupatta","Signature Printed Embroidered Kurta"],
#     "price" : [2.214,2.152,3.190,3.490,1.490, 3.843,3.490,5.490]
# }
#
# convert_table = pandas.DataFrame(khaadi)
# print(convert_table)
#
# # save data in excel
# convert_table.to_excel("AhadFile.xlsx",index=False)
# # save data in csv
# convert_table.to_csv("AhadFile.csv")
# # save data in xml
# convert_table.to_xml("AhadFile.xml")
# # save data in json
# convert_table.to_json("AhadFile.js")


# 25\oct\2022
# Fetch commits form Github
# Pydriller

from pydriller import Repository
import pandas
import  lxml
# make dishes
Name, Email, Date, Msg = [] , [] , [] , []
# Fetch Data

for a in Repository(path_to_repo="https://github.com/Kaggle/kaggle-api").traverse_commits():
    Name.append(a.committer.name)
    Email.append(a.committer.email)
    Date.append(a.committer_date)
    Msg.append(a.msg)

# Save Data in Dictionary
Github_Dict ={
    "nm": Name,
    "em": Email,
    "dn": Date,
    "nms": Msg,
}
# Save Data into CSV
Convert_to_Table = pandas.DataFrame(Github_Dict)
Convert_to_Table.to_csv("RepositoryData.csv",index=False)
Convert_to_Table.to_xml("RepositoryData.xml")

print("Data Save Successfully")