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

But, now you have you key, you don't really want to share it. The allowance that you get with the key is generous (1000 requests per hour) but if lots of people can see, and thus, use your key for their own purposes, that allowance might not last long.

The trick is to use a Streamlit _secret_ which is a named variable that is hidden from the user. When you have deployed your app to the Streamlit Cloud you can set the value of the secret and use the code ``st.secret["variable_name"]`` to access it in your app.

But when you are developing locally that is not an option. So what you need to do is create a special file _secrets.toml_ in a special folder _.streamlit_ which should be located in your root directory.

The contents of the file should look something like this:

````
nasaKey = 'your_key_goes_here'
````

Then in your code you would referr to it like this:

```` Python
myKey = st.secret["nasaKey"]
````

You can, of course, give it a different name.

