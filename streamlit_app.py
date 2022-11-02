import streamlit

streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# pandas 설치 없이 사용 가능 (스트림릿에 포함되어 있음)
import pandas as pd
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

# fruits_selected 라는 변수에 선택한 과일 목록을 넣고, 해당 과일의 행을 가져오도록 설정
fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# 선택한 과일에 대한 행만 보여주기
streamlit.dataframe(fruits_to_show)

# fruityvice api response로 새로운 섹션 생성
streamlit.header('Fruityvice Fruit Advice')
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)

import requests
fruityvice_response = requests.get('https://fruityvice.com/api/fruit/' + fruit_choice)
# json normalization
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# 테이블 형태로 보여주기
streamlit.dataframe(fruityvice_normalized)
