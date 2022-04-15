import csv
from shutil import which
import matplotlib.pyplot as plt 

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
  reader = csv.reader(f)
  header_row = next(reader)

  # ファイルから最高気温を取得する
  highs = []
  for row in reader:
    high = int(row[5])
    highs.append(high)

# 最高気温のグラフを描画する
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs,c='red')

# グラフにフォーマットを指定する
plt.title("Daily high temperasures, July 2018",fontsize=24)
plt.xlabel('',fontsize=16)
plt.ylabel("Temperasure (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()