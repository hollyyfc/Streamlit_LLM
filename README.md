# ✨ AI Storyteller 

***—— A Streamlit App Powered by HuggingFace LLM***

Stuck with a severe case of writer's block? Have the setting you envisioned but paralyzed with too many options for continuing the story? Try [AI Storyteller](https://hollyyfc-aistoryteller.streamlit.app/)! Be it a poem, novel or creative essay, we've got your back to help you get over the hump. A little assistance can unleash a lot of creativity.

The web app itself is built with [Streamlit](https://streamlit.io/) and powered by [HuggingFace](https://huggingface.co/distilbert/distilgpt2)'s `distilgpt2` model, an English-language model pre-trained with the supervision of the smallest version of Generative Pre-trained Transformer 2 (GPT-2) for resource and response efficiency. The application invites users to kick-start a story with their own sentences, which the AI then elaborates on, spinning the tale further with imaginative continuity. The UI is crafted with a soothing Morandi color scheme, offering a visually pleasing and user-friendly environment for storytelling enthusiasts and casual users alike. 

## Demo

Ready to get your hands on? Just type the opening line of your tale into the textbox and watch as our clever AI conjures up the next part of your story! Let this genie in your browser do the magic and wait for something fun 🧞‍♂️

![cat](image/cat.png)

![hp](image/hp.png)

*Note: Due to the size of your input and the model computing period, the response time might vary between 4 to 7 seconds. Beware of refresh or multiple hits of the button!*

## Reproducible Steps

If you're interested in replicating the app or building somehting of your own, Streamlit provides a user-friendly environment for production in Python: 

1. Install Streamlit: `pip install streamlit`
2. Install HuggingFace Transformers library: `pip install transformers`
3. Create a directory / folder hosting your project
4. Place `requirements.txt` in your directory. Add necessary library dependencies to the file. (Run `pip install -r requirements.txt` if dependencies were never installed locally before)
5. Create a `<YOUR-APP-NAME>.py` file in your directory and build your app with Python. Feel free to refer to my code and take a look at the Streamlit UI structure and how to utilize imported LLMs
6. Local run and test your app: `streamlit run <YOUR-APP-NAME>.py` 
7. Create a GitHub repo and push both files there
8. Deploy your app on Streamlit: 
    - Go to https://streamlit.io/ and signup for an account (ideally using your GitHub account)
    - Navigate to your profile and create a new app *using existing repository*
    - Choose the GitHub repo you wish to connect and import your files, and correctly fill in the required fields
    - Wait for deployment 

You should get an URL for your final deployed app (either system-generated or self-defined). Make sure to check your developer logs for any deployment issues! 


