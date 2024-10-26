import streamlit as st

# Set up the app title and description
st.title("🌡️ Temperature Converter")
st.write("Easily convert temperatures between Celsius and Fahrenheit!")

# Temperature conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Choose conversion type
conversion_type = st.radio("Select the conversion type:", ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))

# Input field and conversion
if conversion_type == "Celsius to Fahrenheit":
    celsius = st.number_input("Enter temperature in Celsius:", format="%.2f")
    if st.button("Convert"):
        fahrenheit = celsius_to_fahrenheit(celsius)
        st.success(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

elif conversion_type == "Fahrenheit to Celsius":
    fahrenheit = st.number_input("Enter temperature in Fahrenheit:", format="%.2f")
    if st.button("Convert"):
        celsius = fahrenheit_to_celsius(fahrenheit)
        st.success(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

# Footer message
st.write("🌞 Stay cool or warm as you like!")
