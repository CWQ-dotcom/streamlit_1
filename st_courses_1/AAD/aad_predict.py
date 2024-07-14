import streamlit as st

st.title('***主动脉夹层(AAD)风险预测***')

# 用户身份验证
def authenticate():
    st.subheader('请输入密码，密码为：123456')
    password = st.text_input("", type="password",  placeholder="请输入密码")
    if password == "123456":
        return True
    else:
        st.warning("密码错误，请重新输入。")
        return False

# 主动脉夹层风险预测函数
def predict_aortic_dissection_risk(inputs):
    # 在这里进行主动脉夹层风险预测的逻辑
    # 这里简化为直接返回一个预测结果
    return "高风险"

# 主程序
def main():
    # 身份验证
    authenticated = authenticate()
    if not authenticated:
        return

    # 输入患者信息
    st.header("输入患者信息")
    gender = st.selectbox("选择患者性别", ["男性", "女性"])
    age = st.number_input("输入患者年龄", min_value=0, max_value=150, step=1)

    # 输入预测指标
    st.header("输入预测指标")
    chest_pain = st.selectbox("胸痛", ["有", "无"])
    hypertension_history = st.selectbox("高血压病史", ["有", "无"])
    back_pain = st.selectbox("背痛", ["有", "无"])
    chest_tightness = st.selectbox("胸闷", ["有", "无"])
    sweating = st.selectbox("大汗", ["有", "无"])
    shortness_of_breath = st.selectbox("呼吸困难", ["有", "无"])
    pain_type = st.selectbox("疼痛性质", ["突发性疼痛", "持续性疼痛", "剧烈疼痛", "疼痛扩散"])
    sudden_pain = st.selectbox("是否突发", ["是", "否"])
    have_pain = st.selectbox("有无疼痛", ["是", "否"])
    systolic_bp = st.number_input("输入收缩压", min_value=0, max_value=300, step=1)
    diastolic_bp = st.number_input("输入收张压", min_value=0, max_value=200, step=1)

    # 预测按钮
    st.header("开始预测风险")
    if st.button("开始预测"):
        inputs = {
            "gender": gender,
            "age": age,
            "chest_pain": chest_pain,
            "hypertension_history": hypertension_history,
            "back_pain": back_pain,
            "chest_tightness": chest_tightness,
            "sweating": sweating,
            "shortness_of_breath": shortness_of_breath,
            "pain_type": pain_type,
            "sudden_pain": sudden_pain,
            "have_pain": have_pain,
            "systolic_bp": systolic_bp,
            "diastolic_bp": diastolic_bp,
        }
        prediction = predict_aortic_dissection_risk(inputs)
        st.success(f"预测结果为：{prediction}")

# 主程序入口
if __name__ == "__main__":
    main()
