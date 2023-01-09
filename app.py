import streamlit as st
import streamlit.components.v1 as components

st. set_page_config(layout="wide")

st.sidebar.image("https://www.microlog.it/wp-content/uploads/2018/11/icona_soluz_contapersone_col.png", width=100)
st.sidebar.subheader("About Crowd Counting Model")
st.sidebar.markdown("###### An end-to-end trainable deep architecture that combines features obtained using multiple receptive field sizes and learns the importance of each such feature at each image location")
st.sidebar.markdown("###### The approach adaptively encodes the scale of the contextual information required to accurately predict crowd density")
st.sidebar.markdown("###### This yields an algorithm that outperforms state-of-the-art crowd counting methods, especially when perspective effects are strong")

st.sidebar.subheader("Context-Aware Network Model")
st.sidebar.image("model.png")

st.sidebar.subheader("Crowd Density Estimation")
st.sidebar.image("prediction.png")


st.sidebar.caption("How to use the App (Demo Video)- [link](https://aclanthology.org/2021.acl-long.340.pdf)")
st.sidebar.caption("App by </Shahnab>")

st.subheader("Crowd Counting Estimator Engine")
# embed streamlit docs in a streamlit app
st.components.v1.iframe("https://shad0ws-crowdcounting.hf.space", width=1100, height=650, scrolling=True)
