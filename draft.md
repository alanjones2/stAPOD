# NASA Open APIs: The Astronomy Picture of the Day in Streamlit

## Streamlit is not just for Data Science, you can create excellent general-purpose web sites, too. Here we use the ``requests`` package to download data from NASA'a API and produce a new version of APOD

![](https://github.com/alanjones2/stAPOD/raw/main/images/HorseheadIr_HubbleNachman_2691.jpg)

This is a bit of fun, really. The program is not complex but it illustrates how to use __NASA Open APIs__ and __secrets management__ in Streamlit.

NASA have been producing their Astronomy Picture of the Day since 1995. Sometimes they are images and occasionally they are videos but they are almost invariably spectacular. The official APOD can be found at https://apod.nasa.gov/apod/astropix.html and is updated each day. 

![](https://github.com/alanjones2/stAPOD/raw/main/images/Screenshot_APOD_2022-08-18_164058.png)

We are going to build an alternative in Streamlit that lets you choose a particular date and displays the image, or video, and its description, for that day.  

Our version will look like this:

![](https://github.com/alanjones2/stAPOD/raw/main/images/ScreenshotstAPOD.png)


### API Key - keep it a secret

The first thing you need to do is obtain an API key from NASA (there is a demo key but the proper one is free, so you might as well get one). Just go the the [NASA Open APIs web page](https://api.nasa.gov/) and request one. It's simple and free, all you need is to give your name, email address and, optionally, tell them how you are going to use the key.

But, now you have you key, you don't really want to share it. The allowance that you get with the key is generous (1000 requests per hour) but if lots of people can see, and so use your key for their own purposes, that allowance might not last long.

The trick is to use a Streamlit _secret_ which is a named variable that is hidden from the user. When you have deployed your app to the Streamlit Cloud you can set the value of the secret and use ``st.secret("variable_name")`` to access it in you app.