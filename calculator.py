import streamlit as st

# Set up the app title
st.title("Simple Calculator")

# Input fields for numbers and operation
st.write("Enter two numbers and select an operation:")

# Input fields for numbers
num1 = st.number_input("First Number", format="%.2f")
num2 = st.number_input("Second Number", format="%.2f")

# Dropdown menu for operations
operation = st.selectbox("Operation", ("Add", "Subtract", "Multiply", "Divide"))

# Calculate the result based on the selected operation
result = None
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Division by zero is not allowed.")
    
    # Display the result
    if result is not None:
        st.success(f"The result is: {result}")

