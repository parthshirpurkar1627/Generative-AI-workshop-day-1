import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title (":streamlit: Your Personal Carbon Calculator")
st.write(" :smile: hello")

name = st.text_input("Enter your name:")
if st.button("Greet"):
    st.success(f"Hello, {name}! Welcome to Your Personal Carbon Calculator.")

df = pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])

st.line_chart(df)
st.bar_chart(df)

st.sidebar.title("Sidebar")
st.image("https://tse3.mm.bing.net/th/id/OIP.-1zyzIMDHKcU_-sXth6ZiQHaFP?cb=defcachec2&rs=1&pid=ImgDetMain&o=7&rm=3", caption="Goku Image")
st.video("https://www.youtube.com/watch?v=c92tUshrZ9g&list=RDc92tUshrZ9g&start_radio=1")

st.title("🌍 Carbon Footprint Dashboard")

upload_csv = st.file_uploader("Upload your activity data (CSV)", type="csv")

if upload_csv:
    df = pd.read_csv(upload_csv)
    st.dataframe(df)

st.header("Your Carbon Footprint")
st.subheader("Total Emissions")

st.markdown("**Total Carbon Emissions:** 2.5 tons CO2e/year [Link](http://streamlit.io)") 
st.code("for i  in range(5): print(i)" , language="python")

st.text_input("enter your name ")
st.text_area("enter your address")
st.number_input("enter your age", min_value=0, max_value=120, value=25)
st.slider("select your footprint", 0, 20000, 50)
st.selectbox("select your transportation mode", ["Car", "Public Transport", "Bicycle", "Walking"])
st.multiselect("select your energy sources", ["Electricity", "Natural Gas", "Renewables"])
st.radio("Do you want to receive personalized tips?", ["Yes", "No"])
st.checkbox("I agree to the terms and conditions")

fig,ax = plt.subplots()
ax.plot([1,2,3,4], [10,20,25,30])
st.pyplot(fig)