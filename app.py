from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import streamlit as st

@st.cache
def sentiment_analysis(inp):

    model_name = 'distilbert-base-uncased-finetuned-sst-2-english'
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    res = classifier(inp)
    return res

def main():
    user_input = st.text_input("Enter text here:")
    st.write("You entered:", user_input)
    res = sentiment_analysis(user_input)
    print(res)
    sentiment = res[0]['label']
    conf = res[0]['score']
    st.write("Sentiment of the input: ", sentiment)
    st.write("Confidence of the predicted sentiment: ", conf)

if __name__ == '__main__':
    main()