import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("구글시트에 있는 문제와 정답으로 즉각 피드백하는 앱 만들기")
url = ""

conn = st.connection("gsheets", type=GSheetsConnection)
data = conn.read(spreadsheet=url, usecols=[0, 1, 2])

# 정답 보이기(아래 줄은 주석처리하기!)
# st.dataframe(data)
if st.button("데이터 새로고침하기"):
    st.cache_data.clear()
for index, row in data.iterrows():
    st.markdown("## ✏️문제"+str(index+1)+". "+str(row["문제"]))
    user_answer = st.text_input("정답을 입력하세요.",key=index)
    if user_answer == "":
        continue
    elif user_answer == row["정답"]:
        st.success("맞았습니다!")
    else:
        st.warning("다시 풀어보세요.")
    # 사용자가 입력한 답안을 구글 시트에 추가
