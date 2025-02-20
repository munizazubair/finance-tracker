import streamlit as st

st.title("🔢 Unit Converter")

option = st.selectbox("Select Conversion", ["Meters to Feet", "Kg to Pounds", "Celsius to Fahrenheit"])
value = st.number_input("Enter Value:")

if st.button("Convert"):
    if option == "Meters to Feet":
        st.write(f"Result: {value * 3.28084} feet")
    elif option == "Kg to Pounds":
        st.write(f"Result: {value * 2.20462} lbs")
    elif option == "Celsius to Fahrenheit":
        st.write(f"Result: {(value * 9/5) + 32} °F")
