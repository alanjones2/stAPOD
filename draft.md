# NASA Open APIs: The Astronomy Picture of the Day in Streamlit

## Streamlit is not just for Data Science, you can create excellent general-purpose web sites, too. Here we use the  NASA Open API and show how to keep your API key a secret.

![](https://github.com/alanjones2/stAPOD/raw/main/images/HorseheadIr_HubbleNachman_2691.jpg)

_The Horsehead Nebula in Infrared from Hubble. Can you see a horse's head? To me it looks more like something from Sesame Street. Public domain image courtesy of NASA_

This is a bit of fun, really, but it illustrates how easy it is to construct a general purpose web site in Streamlit and how to keep environment variables away from prying eyes. 

The program is not complex but we'll see how to use __NASA Open APIs__ and __secrets management__ in Streamlit.

NASA have been producing their Astronomy Picture of the Day since 1995. Sometimes they are images and occasionally they are videos but they are almost invariably spectacular.

The official APOD can be found at https://apod.nasa.gov/apod/astropix.html and is updated each day. 

![](https://github.com/alanjones2/stAPOD/raw/main/images/Screenshot_APOD_2022-08-18_164058.png)

We are going to build an alternative in Streamlit that lets you choose a particular date and displays the image, or video, and its description, for that day.  

Our version adds a bit to the original by leveraging the Streamlit sidebar to allow the user to choose a date for the image that they want to display - the default is the one for the current date. It also has a more pleasing layout with the description at the side of the image and sans serif fonts.

An advantage of Streamlit is that you can expand any image for a closer look.

It will look like this:

![](https://github.com/alanjones2/stAPOD/raw/main/images/ScreenshotstAPOD.png)


### API Key - keep it a secret

To build the web page, the first thing you need to do is get an API key from NASA (there is a demo key but the proper one is free, so you might as well get one). Just go the the [NASA Open APIs web page](https://api.nasa.gov/) and request one. It's simple and free, all you need is to give your name, email address and, optionally, tell them how you are going to use the key.

But, now you have you key, you don't really want to share it. The allowance that you get with the key is reasonably generous (1000 requests per hour) but if lots of people can see, and thus use, your key for their own purposes, that allowance might not last long.

The trick is to use a Streamlit _secret_ which is a named variable that is hidden from the user. When you have deployed your app to the Streamlit Cloud you can set the value of the secret and use the code ``st.secret["variable_name"]`` to access it in your app.

But when you are developing locally that is not an option. So what you need to do is create a special file _secrets.toml_ in a special folder _.streamlit_ which should be located in your root directory.

The contents of the file should look something like this:

````
nasaKey = "your_key_goes_here"
````

Then in your code you would referr to it like this:

```` Python
myKey = st.secret["nasaKey"]
````

You can, of course, give it a different name.

### Accessing the API

We use the _requests_ package to access the NASA API, so we first need to set up the parameters and then make the actual request. One of the parameters is, of course, our secret API key. The other is the date that is either today or the one set from the side bar (we'll see that later).
 
```` Python
params = {'api_key': st.secrets['nasaKey'], 'date':d}
response = requests.get('https://api.nasa.gov/planetary/apod', params=params)

````

The message that is returned in in JSON format and has various fields, such as _url_ (of the image), _title_, _description_, etc.

These are written into the one of two columns. The only slight complication is that we need to know whether we are dealing with an image or a video because we need to use the appropriate Streamlit function to display it.

I won't go through the entire code as it is very staightforward. A full listing is given in a Gist, below which contains explanatory comments.

If you want to deploy to the Streamlit Cloud you will need a  _requirements.txt_ file for the required libraries which are ``streamlit`` and ``requests``.

You can find out how to deploy to the cloud in my article [Publish Your Streamlit Apps in the Cloud
](https://towardsdatascience.com/publish-your-streamlit-apps-in-the-cloud-3ac5a5fe3d51).



```` Python
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

````

_gist address https://gist.github.com/2ad757525c6da806d688f6f847465e05.git_