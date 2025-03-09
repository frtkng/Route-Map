import folium
import pandas as pd

# CSVファイルから緯度経度を読み込み
data = pd.read_csv('lat_lon_list.csv')

# 最初の座標を基準にマップの中心を設定
center_lat, center_lon = data.iloc[0]['latitude'], data.iloc[0]['longitude']

# Folium地図オブジェクトを作成
m = folium.Map(location=[center_lat, center_lon], zoom_start=12)

# 緯度経度をすべて地図上にプロット
for _, row in data.iterrows():
    folium.Marker(location=[row['latitude'], row['longitude']]).add_to(m)

# HTMLファイルとして地図を保存
m.save('location_map.html')

print("地図が 'location_map.html' に保存されました。ブラウザで開いて表示してください。")