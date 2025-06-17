import streamlit as st

st.title("power calculator")
st.write("enter the number to calculate its squar, cube and fifthpower:")

n = st.number_input("enter the integer ", value=1, step=1)

square = n ** 2
cube = n ** 3
fifth_power = n ** 5

st.write(f"The square of number {n} is: {square}")
st.write(f"The cube of number {n} is: {cube}")
st.write(f"The square of number {n} is: {fifth_power}")