import streamlit as st
import requests

# Set the page to a wide layout
st.set_page_config(layout="wide")

# Title
st.title("NASA's Astronomy Picture of the Day")
 
# Set up the side bar with a date input widget and some introductory text
with st.sidebar:

    st.header("APOD")
    d = st.date_input("Select a date:")
    # 2022-01-25 for example of video
    st.write("""NASA have been producing their Astronomy Picture of the Day since 1995. 
    Sometimes they are images and occasionally they are videos but they are almost invariably spectacular.""")

    st.write("""The official APOD can be found at https://apod.nasa.gov/apod/astropix.html and is updated each day. 
    This web page lets you choose a particular date and displays the image, and its description, for that day.    
    """)

# Set the parameters for a requests call and get the data from the API
params = {'api_key': st.secrets['nasaKey'], 'date':d}
response = requests.get('https://api.nasa.gov/planetary/apod', params=params)

# If there is a response extract the data as JSON
# and write the fields in the two columns
if response:
    # Uncomment to see the actual data
    #st.json(response.json())
    data = response.json()

    col1, col2 = st.columns(2, gap="small")
    
    with col1:
        # Check the data type and display accordingly
        if data['media_type'] == 'video':
            st.video(data['url'])
        else:
            st.image(data['hdurl'])
        
        # If there is a copyright message then display it
        if 'copyright' in data:
            st.caption(f'Copyright: {data["copyright"]}')
        # Otherwise here is a default caption
        else:
            st.caption("Public domain image courtesy of NASA")
        

    with col2:
        # Write the text fields in column 2
        st.title(data['title'])
        st.write(data['date'])
        st.write(data['explanation'])
        
# If the response is bad just print it out
else:
    st.write(response.text)
