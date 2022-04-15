import csv
from datetime import datetime
from shutil import which
import matplotlib.pyplot as plt 

#シトカとデス・バレーのファイルの読み込み
s_filename='data/sitka_weather_2018_simple.csv'
dv_filename = 'data/death_valley_2018_simple.csv'

#シトカのデータ作成
with open(s_filename) as sf:
  s_reader = csv.reader(sf)
  s_header_row = next(s_reader)

  s_dates,s_highs = [],[]
  for s_row in s_reader:
    s_date = datetime.strptime(s_row[2],'%Y-%m-%d')
    try:
      s_high = int(s_row[5])
    except ValueError:
      print(f"Missing data for {s_date}")
    else:
      s_dates.append(s_date)
      s_highs.append(s_high)




  
# デス・バレーの作成
with open(dv_filename) as dvf:
  dv_reader = csv.reader(dvf)
  dv_header_row = next(dv_reader)

  dv_dates, dv_highs = [] , []
  for dv_row in dv_reader:
    dv_date = datetime.strptime(dv_row[2],'%Y-%m-%d')
    try:
      dv_high = int(dv_row[4])
    except ValueError:
      print(f"Missing data for {dv_date}")
    else:
      dv_dates.append(dv_date)
      dv_highs.append(dv_high)


#二つのデータからグラフの描画
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(s_dates,s_highs,c='blue')
ax.plot(dv_dates,dv_highs,c='red')
plt.ylim(0,150)
#グラフにフォーマット指定をする
plt.title('Daily High Temperasures -2018\nSitka and Death Valley ',fontsize=24)
plt.xlabel('',fontsize=16)
plt.ylabel('Temperasure (F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=24)

plt.show()



