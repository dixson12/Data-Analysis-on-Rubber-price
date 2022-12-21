import os
from bs4 import BeautifulSoup
import pandas as panda
from matplotlib import pyplot as pyplot



def check_file():
   try:
      f = open("price_data.txt", "r")
      try:
         f = open("filtered_price_data.txt", "r")
         months=['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jun', 'Mar', 'Apr', 'May', 'Feb', 'Jan']
         drawing_graphs("filtered_price_data.txt",months)
      
      except:
         reading_file()

      
   except:
      print("creating data file")
      checkprice(1)
      
      

def checkprice(file_count):
   i=0
   if file_count>3:
      reading_file()
   else:
      bool=True
      file="C:/Users/shihab/Downloads/messages{}.html".format(file_count)
      with open(file) as file:
         soup = BeautifulSoup(file, 'html.parser')
      while bool:
         try:
               value=soup.select('div.text')[i].get_text().strip()
               if len(value)==63:
                  filter_value=value[0:9]
                  filter_first_value=value[35:40]
                  filter_second_value=value[58:63]
                  print(filter_value,filter_first_value,filter_second_value)
                  f = open("price_data.txt", "a")
                  f.write(filter_value + ","+filter_first_value+","+filter_second_value+os.linesep)
                  i=i+1
               else:
                  print("false value")
                  i=i+1
         except:
               print("out of range")
               file_count=file_count+1
               print("loop continue")
               checkprice(file_count)
               break
					
def reading_file():
   months=[]
   dic={}
   file="C:/Users/shihab/Downloads/price_data.txt"
   f = open(file, "r")
   for data in f:
      if len(data)==22:
         current_month=data[3:6]
         full_data=data[0:23]
         print(full_data)
         if current_month in months:
            print("month already exist")
            key=current_month           
            dic.setdefault(key, [])
            dic[key].append(full_data)
         else:
            months.append(current_month)
            key=current_month
            dic.setdefault(key, [])
            dic[key].append(full_data)
      else:
         print("New Line")
   loop_month(dic)

def loop_month(dic):
   print("sorting data please wait >>>>>")
   sorted_months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
   for month in sorted_months:
      months_sorting(dic,month)
   f = open("filtered_price_data.txt", "a")
   f.write("date,first_quality,second_quality"+os.linesep)
   for month in sorted_months:
      for price_data in dic[month]:
         f = open("filtered_price_data.txt", "a")
         f.write(price_data+os.linesep)
   print("sorting data completed <><>")
   print("creating data file")
   print("data file creation completed")
   drawing_graphs("filtered_price_data.txt",sorted_months)


def months_sorting(dic,month):
   sorted=True
   while sorted:
      cheking_sort=False
      for i in range((len(dic[month]))-1):
         if (dic[month][i][0:2]) > (dic[month][i+1][0:2]):
            value_store1=dic[month][i]
            value_store2=dic[month][i+1]
            dic[month][i]=value_store2
            dic[month][i+1]=value_store1
            cheking_sort=True
         elif cheking_sort==False and i==(len(dic[month])-2):
            sorted=False




def drawing_graphs(file,months):
   table = panda.read_csv(file, usecols=["date","first_quality","second_quality"])
   filtered_year=table.drop_duplicates(subset=["date"])
   pyplot.plot(filtered_year.date,filtered_year.first_quality)
   pyplot.plot(filtered_year.date,filtered_year.second_quality)
   pyplot.legend(["First Quality" , "Second Quality"])
   pyplot.xticks(rotation=90)
   pyplot.xlabel("date")
   pyplot.ylabel("price")
   pyplot.show()
   for current_month in months:
      month = table[table['date'].str.contains(current_month)]
      filtered_month=month.drop_duplicates(subset=["date"])
      print(filtered_month)
      pyplot.plot(filtered_month.date,filtered_month.first_quality)
      pyplot.plot(filtered_month.date,filtered_month.second_quality)
      pyplot.legend(["First Quality" , "Second Quality"])
      pyplot.xticks(rotation=90)
      pyplot.xlabel("date")
      pyplot.ylabel("price")
      pyplot.show()

check_file()


