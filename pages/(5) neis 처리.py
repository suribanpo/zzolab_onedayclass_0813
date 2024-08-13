import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title(" NEIS 데이터 처리 앱")
st.info("이 앱은 NEIS 데이터를 처리하여 학생들의 성적 정보를 정리합니다. 엑셀 파일을 업로드하여 데이터를 확인하세요.")

uploaded_file = st.file_uploader("엑셀 파일을 업로드하세요", type=["xlsx"])
sample_data = pd.read_excel("data/neis.xlsx")

@st.cache_data
def load_data(uploaded_file):
    if uploaded_file is not None:
        return pd.read_excel(uploaded_file)  # 업로드한 데이터
    else:
        return sample_data  # 샘플 데이터 파일 경로

data = load_data(uploaded_file)

# 샘플 데이터 보기 체크박스
if st.checkbox("샘플 데이터 보기"):
    st.success("샘플 데이터를 업로드하였습니다. ")
    # st.dataframe(data)  # 샘플 데이터 표시

def process_data(df):
    df = df.dropna(how='all').dropna(axis=1, how='all')
    df = df.iloc[2:, 1:14]
    df.columns = ['학년', '반', '번호', '이름', '중간고사', '기말고사', '문제해결력평가', '독서탐구활동', '포트폴리오', '합계', '원점수', '성취도', '석차등급']
    df = df[df.학년.notna()]

    realfinal1 = df[df.석차등급.notna()]
    realfinal2 = df[df.석차등급.isna()].iloc[:, :5]
    realfinal2.columns = ['학년', '반', '번호', '이름', '석차']

    return pd.merge(realfinal1, realfinal2, how='outer', on=['학년', '반', '번호', '이름'])
# 데이터 처리 및 시각화
processed_data = process_data(data)
st.write("처리된 데이터:")
st.dataframe(processed_data)

# 데이터 다운로드 버튼 생성
csv = processed_data.to_csv(index=False)  # 데이터프레임을 CSV로 변환
st.download_button("데이터 다운로드", csv, "processed_data.csv", "text/csv")  # 다운로드 버튼

import streamlit.components.v1 as components

st.subheader("데이터 탐색을 위한 CODAP!")
st.info("위에서 [데이터 다운로드]한 후, [새 문서] 클릭 > 다운받은 데이터를 CODAP의 비어있는 창으로 드래그앤 드롭해주세요. ")
st.link_button("분석 예시 바로가기", "https://codap.concord.org/app/static/dg/ko/cert/index.html#shared=https%3A%2F%2Fcfm-shared.concord.org%2FYKYIVlWzPKZyAv6ZmMQZ%2Ffile.json")
components.iframe("https://codap.concord.org/app/static/dg/ko/cert/index.html", height=500)

# if processed_data[selected_column].isnull().all():
#     st.error("모든 데이터가 변환되지 않았습니다. 유효한 숫자 데이터를 확인하세요.")  # 오류 메시지 출력
# else:
#     fig, ax = plt.subplots()  # 서브플롯 생성
#     # plt.figure(figsize=(10, 6))  # 그래프 크기 설정
#     sns.histplot(processed_data[selected_column], binwidth = 2, binrange = [0, 30], kde=True, color='skyblue', ax=ax)  # ax에 히스토그램 그리기 및 커널 밀도 추정 추가
#     ax.set_title(f"{selected_column}의 히스토그램", fontsize=16)  # 제목 설정
#     ax.set_xlabel(selected_column, fontsize=14)  # X축 레이블 설정
#     ax.set_ylabel("빈도", fontsize=14)  # Y축 레이블 설정
#     # ax.grid(True)  # 그리드 추가
#     st.pyplot(plt)  # 그래프 출력

