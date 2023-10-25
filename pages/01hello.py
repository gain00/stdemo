import streamlit as st

print(st.__version__)

# 제목위젯
st.title('제목')
st.header('헤더')
st.subheader('소제목')

# 텍스트 위젯
st.text('간단한 텍스트 출력')

# 수식 위젯
st.latex(r''' e^{i\pi} + 1 = 0''')

# 코드 위젯
st.code('for i in range(8) : foo()')

# 버튼 위젯
if st.button('클릭해보세요~'):
    st.write('hello world')
# 버튼 위젯
if st.checkbox("i gree"):
    st.write('약관 동의')

option1 = st.radio("a",["v","c"])
st.write('선택사항:', option1)



option2 = st.multiselect("사고싶은것",["milk","apple"])
st.write('선택사항:', option2)

import time
# Show and update progress bar
# bar = st.progress(0)
# for i in range(0, 100+1, 10):
#     bar.progress(i)
#     time.sleep(1)

# 사이드바 위젯

# Just add it after st.sidebar:
st.sidebar.radio('Choose:',[1,2])

col1, col2 = st.columns(2)
col1.write('Column 1')
col2.write('Column 2')
