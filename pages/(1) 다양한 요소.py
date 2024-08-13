import streamlit as st  # Streamlit 라이브러리 임포트
from datetime import datetime  # 날짜 및 시간 관련 기능을 위한 datetime 모듈 임포트
import pandas as pd
import numpy as np

# 앱의 제목 설정
st.title("🤹🏻‍♂️ 인터랙티브한 요소 넣기")

# 이미지 섹션의 서브헤더 설정
st.subheader("이미지 넣기")

# 두 개의 열을 생성하여 이미지를 나란히 배치
col1, col2 = st.columns(2)

# 첫 번째 열에 이미지 추가
with col1:
    st.image("https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/5eeea355389655.59822ff824b72.gif")  # 첫 번째 이미지

# 두 번째 열에 이미지 추가
with col2:
    st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTd5NHoyd3FkY2NrMTF4bnF3ZWtsZjJ5bm1nZXJ2ejZvbzI5YW5vaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jUwpNzg9IcyrK/giphy.webp")  # 두 번째 이미지

# 확장 가능한 섹션을 만들어 비디오 추가
with st.expander("expander 안에 내용 입력하기"):
    st.video("https://youtu.be/xo_6_aZMwuE")  # 비디오 링크

# 움직이는 이미지 섹션의 서브헤더 설정
st.subheader("움직이는 이미지 넣기")
# GIPHY 링크로 이동하는 버튼 추가
st.link_button("GIPHY 링크 바로가기", 'https://giphy.com/')

# 데이터 표시를 위한 제목 및 헤더 설정
st.title(":blue[Beautiful] :red[Data] :green[display]")  # 데이터 표시 제목
st.header("제목제목(header)")  # 헤더
st.subheader("부제목부제목(subheader)")  # 서브헤더
st.caption("캡션을 입력해주세요.")  # 캡션

# 코드 블록 표시
st.code("print('hello')# 코드 입력하듯이 입력해주세요")  # 코드 예시
st.code("print('hello')# 코드 입력하듯이 입력해주세요", language='r')  # 코드 예시
st.code('''print("hello")# 코드 입력
print("World")# 여러 줄인 경우''', language='python')  # 코드 블록 표시

# 텍스트 및 쓰기 기능
st.text("hello again_text")  # 텍스트 표시
st.write("hello again_write")  # 쓰기 기능(더 기능이 유연함)

# 수식 표시
st.latex("2+1=3")  # 수식 예시
st.latex(r'''E=mc^2''', help='질량-에너지 등가 원리')  # 질량-에너지 등가 원리 수식

# 구분선 표시
st.divider()  # 구분선 추가
st.write("----")  # 구분선 텍스트(똑같음))

# 메트릭 표시를 위한 두 개의 열 생성
col1, col2 = st.columns(2)
col1.metric("온도", "12.4℃", "1.2℃")  # 첫 번째 열에 메트릭 추가
col2.metric("온도", "12.4℃", "1.2℃")  # 두 번째 열에 메트릭 추가
