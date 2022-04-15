import csv
from datetime import datetime
from shutil import which
import matplotlib.pyplot as plt 

filename='data/sitka_weather_2018_simple.csv'
with open(filename) as f:
  reader = csv.reader(f)
  header_row = next(reader)

  dates, rainfalls = [],[]
  for row in reader:
    current_date  = datetime.strptime(row[2],'%Y-%m-%d')
    rainfall = float(row[3])
    dates.append(current_date)
    rainfalls.append(rainfall)

#降水量のグラフを描画する
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,rainfalls,c='red')
#グラフにフォーマットを指定する
plt.title("Daily rainfall temperasures - 2018\nSitka",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Rainfall',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()