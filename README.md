# Patentability Score
<br>
<p><b>Landing Page:</b></p>

https://sites.google.com/view/patent-score-checker/home

<p><b>App Link:</b></p>

[https://huggingface.co/spaces/arpachat/sentiment-analysis](https://huggingface.co/spaces/arpachat/Patentability-Score)<br>

<p><b>Model Link:</b></p>

https://huggingface.co/arpachat/model-patent-score

## Model Description

<p>In this project, we have finetuned the existing and widely popular language model "distilbert-base-cased" to get the patentability score of a patent. We have converted the decision input from the HUPD dataset to be either 0 or 1 if it is "ACCEPTED" or "REJECTED" respectively and this is the label for our new model. The abstract of the patent has been used as the feature which is also fed to the model. We have trained this model with all the patents in the HUPD dataset between 1st January 2016 and 21st January 2016. This trained model has also been uploaded to Hugging Face Models(the link is given above)</p>

## File Descriptions

<p>train_hupd.ipynb -  This file contains the code on how the model has been created and trained, finetuned from the "distilbert-base-cased" model.</p>
<p>hupd_load.ipynb - This file loads the HUPD dataset and then creates a dataframe with all the necessary columns needed by our app, to predict the patentability score. This dataframe is stored in a pickle file, so that we can save the processing time to create the dataframe again. This pickle file is retrieved by the app.py file to populate the patent information in the website app.</p>
<p>app.py - This file uses the Streamlit library to make a website with patents, and we can select a patent to get the abstact and claims of the selected patent. We can also find out how likely that patent application is likely to be accepted.</p>

## Steps to run this app locally

<p>To run this application locally, follow the steps discussed below:-</p>
<ol>
<li>Pull this directory to your local repository.</li><br>
  <p><i>git pull https://github.com/dungarpan/AI-Project-FineTuning-Language-Models.git</i></p><br>
<li>Create a virtual environment and install all the dependencies mentioned inside the requirements.txt file</li><br>
  <p><i>pip install -r requirements.txt</i></p><br>
<li>Note that, the model folder couldn't be uploaded to GitHub as the file size were over GitHub's allowed size. The model folder has been uploaded to HuggingFace Models page(link provided above). This directory should be downloaded and put in the same directory as app.py and named 'model-patent-score'.</li><br>
<li>After this we can run streamlit application app.py using the command:</li><br>
<p><i>streamlit run app.py</i></p><br>
</ol><br>

## Screenshots of the application

<p>I am providing screenshots of the running app below</p>

![Docker SS](p1-ws.jpg)
![Docker SS](p1-s.jpg)
![Docker SS](p2-ws.jpg)
![Docker SS](p2-s.jpg)

