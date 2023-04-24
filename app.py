import streamlit as st
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

@st.cache
def predictScore(abstract):
    model_dir = 'arpachat/model-patent-score'
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForSequenceClassification.from_pretrained(model_dir)

    #abstract = "The present invention relates to passive optical network (PON), and in particular, to an optical network terminal (ONT) in the PON system. In one embodiment, the optical network terminal includes a first interface coupled to a communications network, a second interface coupled to a network client and a processor including a memory coupled to the first interface and to the second interface, wherein the processor is capable of converting optical signals to electric signals, such that the network client can access the communications network."
    inputs = tokenizer.encode_plus(abstract, max_length=512, padding='max_length', truncation=True, return_tensors='pt')

    outputs = model(inputs['input_ids'], attention_mask=inputs['attention_mask'])
    scores = torch.softmax(outputs.logits, dim=1)[0]

    probs = F.softmax(scores, dim=0)
    accept_prob = probs[0].item()
    print(accept_prob)

    return accept_prob



def main():
    df = pd.read_pickle("my_dataframe.pkl")
    df = df.iloc[:50]
    title_list = df['title'].tolist()
    pnumber_list = df['patent_number'].tolist()

    display_list = [f"{a}-{b}" for a, b in zip(pnumber_list, title_list)]

    # Prepopulate the drop-down menu with the default value 'Option 2'
    default_option = display_list[0]

    # Create the drop-down menu with prepopulated default value
    selected_option = st.selectbox('Select a patent number which is displayed along with its title', display_list, index=display_list.index(default_option))
    st.write(selected_option)
    pnumber = selected_option.split("-")[0]
    print(pnumber)
    pclaims = df.loc[df['patent_number'] == str(pnumber), 'claims'].iloc[0]
    pabstract = df.loc[df['patent_number'] == str(pnumber), 'abstract'].iloc[0]
    score = predictScore(pabstract)
    st.write(pclaims)
    st.write(pabstract)

    with st.form("my_form"):
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.write("The patentability score of this patent: ", score)


if __name__ == '__main__':
    main()