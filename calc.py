import streamlit as st

st.title("Calculator")
x = float(st.text_input("first value: "))
y = float(st.text_input("second value: "))



if(st.button("add")):
    st.write(x + y)
if(st.button("subtract")):
    st.write(x-y)
if(st.button("divide")):
    st.write(x/y)
if(st.button("multiply")):
    st.write(x*y)
