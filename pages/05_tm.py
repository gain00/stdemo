import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import plotly.graph_objects as go
import json
import streamlit as st
import altair as alt
import plotly.express as px
import seaborn as sns
from bokeh.plotting import figure

#pip install konlpy WordCloud

from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud


# 멀티페이지
st.set_page_config(page_title='hello textminig',page_icon='📃')
st.sidebar.header('helllo geo!📃')
st.title('텍스트마이닝 시각화📃')

# 폰트 및 형태소 분석기 초기화
fontpath = 'c:/Windows/Fonts/malgun.ttf'
twitter = Okt()

option1 = st.selectbox('연설문', ['잡스','도럼프'])
optcols = 'pop' if option1 == '잡스' else 'forepop'




with open('./data/trump_ko.txt', encoding='utf-8') as f:
    docs1 = f.read()
with open('./data/trump_ko.txt', encoding='utf-8') as f:
    docs2 = f.read()

st.write(docs[:300])

# 워드 클라우드 시각화 1
tokens = twitter.nouns(docs)
words = [t for t in tokens if len(t) >1 ]


with st.spinner('워드클라우드 생성중'):
    wc = Counter(words)
    wc = dict(wc.most_common())

    wcimg = WordCloud(font_path=fontpath, background_color='white',
                      width=640, height=480).generate_from_frequencies(wc)

    fig = plt.figure()
    ax = plt.imshow(wcimg, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(fig)

