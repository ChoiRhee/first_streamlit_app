import streamlit
import pandas as pd # pandas 설치 없이 사용 가능 (스트림릿에 포함되어 있음)
import requests
import snowflake.connector
from urllib.error import URLError # 에러 처리

streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# import pandas as pd
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

# fruits_selected 라는 변수에 선택한 과일 목록을 넣고, 해당 과일의 행을 가져오도록 설정
fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# 선택한 과일에 대한 행만 보여주기
streamlit.dataframe(fruits_to_show)

# 함수 - 반복되는 코드 블럭
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get('https://fruityvice.com/api/fruit/' + this_fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

# fruityvice api response로 새로운 섹션 생성
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('Please select a fruit to get information.')
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    
except URLError as e:
  streamlit.error()

# SNOWFLAKE에 원할 때만 데이터를 전송할 수 있도록 STOP 설정
streamlit.stop()

# import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets['snowflake'])
my_cur = my_cnx.cursor()
my_cur.execute('SELECT * FROM FRUIT_LOAD_LIST')
my_data_rows = my_cur.fetchall()
streamlit.header('The fruit load list contains:')
streamlit.dataframe(my_data_rows)

# allow the end user to add a fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like to add?', 'jackfruit')
streamlit.write('Thanks for adding', add_my_fruit)

# 
my_cur.execute('INSERT INTO FRUIT_LOAD_LIST VALUES (\'from streamlit\')')
