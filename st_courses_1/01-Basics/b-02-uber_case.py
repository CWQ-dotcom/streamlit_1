# 官网案例

import pandas as pd
import streamlit as st
import numpy as np

st.title("Uber pickups in NYC")

DATE_COLUMN = "date/time"
# 该数据集是关于用户的乘车时间在纽约上车地点的分布统计
DATA_PATH = "data/uber-raw-data-sep14.csv"

# 1、加载数据
# @st.cache：将数据集加载完后保存到内存中，下次无需加载
@st.cache
# nrows表示在读取CSV文件时读取多少行数据
def load_data(nrows):
    # 借助pandas读取CSV文件
    data = pd.read_csv(DATA_PATH, nrows=nrows)
    # lambda将列名转换为小写，axis设置为列；inplace基于data本身进行修改
    data.rename(lambda x:str(x).lower(), axis='columns', inplace=True) # 列名转换为小写
    # 日期类型转换
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    # 返回处理后的数据
    return data

# print作用，信息的输出
data_load_state = st.text("Loading data...")
data = load_data(10000)
data_load_state.text("Loading data is done!")

# 2、查看数据
st.subheader("Raw Data")
st.write(data.head(10))

# 3、绘制直方图（每小时的载客量）
st.subheader("Number of pickups by hour")
hist_values = np.histogram(data[DATE_COLUMN].dt.hour,
                           bins=24,
                           range=(0,24))[0]
st.bar_chart(hist_values)

# 4、在地图上绘制
st.subheader("Map of all pickups")
st.map(data)

# 5、 查看某个时刻的乘客分布
hour_to_filter = st.slider('hour', 0, 23, 17) # 0-23点，默认 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

