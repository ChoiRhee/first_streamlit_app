import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# pandas 설치 없이 사용 가능 (스트림릿에 포함되어 있음)
import pandas as pd
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
#streamlit.dataframe(my_fruit_list)

# 사용자가 상호작용을 할 수 있도록 다중 선택이라는 사용자 대화형 위젯 추가
streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index))

# 페이지에 table 보여주기
streamlit.dataframe(my_fruit_list)
