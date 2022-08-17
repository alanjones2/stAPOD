import streamlit as st
import requests

st.set_page_config(page_title=None, page_icon=None, layout="wide")

st.title("NASA's Astronomy Picture of the day")
 
with st.sidebar:

    st.header("APOD")
    d = st.date_input("Select a date:")
    # 2022-01-25 for example of video
    st.write("""NASA have been producing their Astronomy Picture of the Day since 1995. 
    Sometimes they are images and occasionally they are videos but they are almost invariably spectacular.
    The official APOD can be found at https://apod.nasa.gov/apod/astropix.html and is updated each day. 
    This web page lets you choose a particular date and displays the image, and its description, for that day.    
    """)


params = {'api_key': 'RrVw3lyjiGOTSL3ufkFOGIEaUpkegPuAisOudUyG', 'date':d}
response = requests.get('https://api.nasa.gov/planetary/apod', params=params)

if response:
    #st.json(response.json())
    data = response.json()

    col1, col2 = st.columns(2)
    
    with col1:
        if data['media_type'] == 'video':
            st.video(data['url'])
        else:
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


# st.audio("https://www.nasa.gov/mp3/569462main_eagle_has_landed.mp3")