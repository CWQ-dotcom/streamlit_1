import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

# 借助matplotlib，使用中文字符显示
matplotlib.rc("font", family='AR PL UMing CN')

# 1. st.write()
# 类似于print方法，打印效果
st.write("1. st.write()")
st.write(pd.DataFrame({
    '第一列': [1,2,3,4],
    '第二列': [10,20,30,40]}
))

# 2. st.line_chart()
# 显示折线图
st.write("2. st.line_chart()")
chart_data = pd.DataFrame(
    # 随机生成数据，20行3列的表格
    np.random.randn(20,3),
    # 列的名称
    columns=['a','b','c']
)
st.line_chart(chart_data)

# 3. st.map()
# 在地图上显示经纬度
st.write("3. st.map()")
map_data = pd.DataFrame(
    # 显示1000行2列数据，[50,50]经度范围，[37.76,-122.4]纬度范围
    np.random.randn(1000, 2) / [50,50] + [37.76,-122.4],
    # 两列：经度 纬度
    columns=['lat', 'lon']
)
st.map(map_data)

# 4. st.slider()
# 滑条或滑动条
st.write("4. st.slider()")
# 滑条名称
x = st.slider("x")
# 滑动出一个值会在页面上打印其平方值
st.write(x, "squred is", x*x)

# 5. st.text_input(label, key)
# 给出一个文本框输入内容,label为提示，key可理解为id
st.write("5. st.text_input()")
st.text_input("your name", key="name")
# 显示输入的值，st（streamlit）中session_state对话状态
st.session_state.name

# 6. st.checkbox() 多选框
st.write("6. st.checkbox()")
# 'Show dataframe'为提示信息，选中复选框，就会显示DataFrame中的信息
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns=['a','b','c']
    )
    chart_data


# 7. st.selectbox() 下拉选项
st.write("7. st.selectbox()")
df = pd.DataFrame({
    '第1列': [1,2,3,4],
    '第2列': [10,20,30,40]
})

option = st.selectbox(
    # 提示信息
    'which number do you like best?',
    # 选项内容
    df['第1列']
)

"you selected: ", option


# 8. st.sidebar 侧边栏
st.write("8. st.sidebar")
# selectbox侧边栏的下拉选项
add_selectbox = st.sidebar.selectbox(
    "通讯方式选项",
    ('微信','QQ','手机','邮件')
)
"下拉选项: ", add_selectbox

# 侧边栏的slider，后面仍有案例使用
add_slider = st.sidebar.slider(
    "选择一个范围的值",
    0.0, 100.0, (25.0, 75.0)
)
"值的范围: ", add_slider

# 9. st.radio() 单选
st.write("10. st.radio()")
# st.columns(2)表示创建两列
left_column, right_column = st.columns(2)
# 左边列设置
left_column.button("Press me!")
# 右边列设置
with right_column:
    chosen = st.radio(
        '手机品牌',
        ('苹果','华为','小米','三星')
    )
    st.write(f'你选择的品牌是: {chosen}')

# 10. st.progress() 进度条
st.write("10. st.progress()")
import time
st.write("模拟长时间的计算...")
# 添加placeholder（占位符）
latest_iteration = st.empty()
# bar为进度条，设置从0开始
bar = st.progress(0)
for i in range(100):
    # 更新进度条
    # 输出i的值范围是0-99
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    # 模拟程序运行耗时
    time.sleep(0.1)
'运行结束!'


# 11. st.file_uploader() 上传文件
st.write("11. st.file_uploader()")
upload_file = st.file_uploader(
    label = "上传数据集CSV文件"
)

if upload_file is not None:
    # 不为空，通过pandas读取文件
    df = pd.read_csv(upload_file)
    st.success("上传文件成功！")
else:
    st.stop() # 退出

# 选择横坐标和纵坐标属性
x_var = st.selectbox(
    label = "选择横坐标的属性",
    options = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
)

y_var = st.selectbox(
    label = "选择纵坐标的属性",
    options = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
)

# 企鹅类别
sns.set_style("darkgrid")  # 设置深色背景带网格线的风格
# 字典，定义了不同物种对应的标记样式
markers = {'Adelie':'s',     # 使用方形
           'Gentoo':'X',     # 使用叉叉
           'Chinstrap':'o'}  # 使用圆圈

# 散点图的展示
# 创建一个新的matplotlib图形（figure）和子图（axes）
# fig是整个图形对象，ax是用于绘制的子图对象
fig, ax = plt.subplots()
# scatterplot函数绘制散点图
ax = sns.scatterplot(data=df,
                     x=x_var,
                     y=y_var,
                     # 根据'species'列进行颜色分组，不同物种用不同颜色表示
                     hue='species',
                     markers=markers,
                     # 根据'species'列，设置不同物种的不同标记风格
                     style='species')
plt.xlabel(x_var)
plt.ylabel(y_var)
plt.title('Penguins Scatter Plot')
st.pyplot(fig)

