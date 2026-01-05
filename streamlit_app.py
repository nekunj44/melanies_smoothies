# Import python packages
import streamlit as st
import requests
import pandas

# Write directly to the app
st.title(f":balloon: Customize your smoothie :balloon:")
st.write(
  """Choose the fruits you want in your custom Smoothie!
  """
)

from snowflake.snowpark.functions import col, when_matched

cnx = st.connection("snowflake")
session = cnx.session()

name_on_order = st.text_input("Name on Smoothie:")

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'),select(col('SEARCH_ON'))

pd_df = my_dataframe.to_pandas()
st.dataframe(pd_df)
st.stop()
                                                                      

ingredients_list = st.multiselect(
    "Choose up to 5 ingredients:",
    my_dataframe,
    max_selections = 5
)

if ingredients_list:
    ingredients_string = ''
    for var1 in ingredients_list:
        ingredients_string += var1 + " "
        st.subheader(fruit_chosen + ' Nutrition Information')
        smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/" + fruit_chosen)
        sf_df = st.dataframe(data=smoothiefroot_response.json(), use_container_width=True)

    my_insert_stmt = """ insert into 
    smoothies.public.orders(name_on_order, ingredients)
    values('""" + name_on_order + """', 
    '""" + ingredients_string + """')"""

    submit_button = st.button('Submit Order')

    if submit_button:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")

smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
sf_df = st.dataframe(data=smoothiefroot_response.json(), use_container_width=True)
