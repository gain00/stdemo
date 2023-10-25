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
import pickle
import streamlit as st

# pip install scikit-learn

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# 멀티 페이지용 제목
st.set_page_config(page_title='hello machine learning',page_icon='💽')
st.sidebar.header('helllo machine learning!💽')
st.title('데이터분석💽')

# iris 데이터를 이용한 학습 및 모델 생성
with open('./data/rfc_iris.pickle', 'rb') as pk:
    model = pickle.load(pk)

pred = model.predict([[5.1, 3.5, 1.4, 0.2]])
st.info(f'분석후 예측된 품종 : {pred}')



st.subheader('iris 품종분석')
iris = pd.read_csv('./data/iris.csv')

sl_val = st.slider('sepal length',
    iris.sepal_length.min(),iris.sepal_length.max(),value=iris.sepal_length.mean())

sw_val = st.slider('sepal width',
                   iris.sepal_width.min(),iris.sepal_width.max(),value=iris.sepal_width.mean())
pl_val = st.slider('petal length',
                   iris.petal_length.min(),iris.petal_length.max(),value=iris.petal_length.mean())
pw_val = st.slider('petal width',
                   iris.petal_width.min(),iris.petal_width.max(),value=iris.petal_width.mean())



pred2 = model.predict([[sl_val, sw_val, pl_val, pw_val]])
st.info(f'분석후 예측된 품종 : {pred2}')


# st.subheader('iris 중요 변수 분석')
# cols = iris.iloc[:, :4].columns
# fig, ax = plt.subplots()
# ax = sns.barplot(x=model.feature_importance_,y=cols, hue=cols)
#
# plt.xlabel('importance')
# plt.ylabel('feature')
# st.pyplot(fig)


# 변수별 분포 그래프
fig, ax = plt.subplots()
ax = sns.displot(x=iris.sepal_length,kind='kde', hue=iris.species)

st.pyplot(ax)


fig, ax = plt.subplots()
ax = sns.displot(x=iris.sepal_width,kind='kde', hue=iris.species)

st.pyplot(ax)

fig, ax = plt.subplots()
ax = sns.displot(x=iris.petal_length,kind='kde', hue=iris.species)

st.pyplot(ax)


fig, ax = plt.subplots()
ax = sns.displot(x=iris.petal_width,kind='kde', hue=iris.species)

st.pyplot(ax)
# data = iris[['sepal_length','sepal_width','petal_length','petal_width']]
# target = iris['species']


#
#
# st.success(f'랜덤포레스트 분류기로 학습된 모델의 정확도는 {score}입니다')
#

