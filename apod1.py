import streamlit as st
import requests

st.set_page_config(page_title=None, page_icon=None, layout="wide")

#with st.sidebar:

#st.write('sidebar')
st.header("NASA's Astronomical Picture of the day")
d = st.date_input("Select date:")


params = {'api_key': 'DEMO_KEY', 'date':d}
response = requests.get('https://api.nasa.gov/planetary/apod', params=params)

if response:
    #st.json(response.json())
    data = response.json()

    col1, col2 = st.columns([4,4])
    
    with col1:
        st.image(data['url'])
        if 'copyright' in data:
            st.caption(f'Copyright: {data["copyright"]}')
        else:
            st.caption("Public domain image")

    with col2:
        st.title(data['title'])
        st.write(data['date'])
        st.write(data['explanation'])

else:
    st.write(response.text)