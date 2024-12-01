import random
import time

import streamlit as st
from constants import DATA_PATH, THRESHOLD
import pandas as pd


st.title("Ask for Help")

df = pd.read_csv(DATA_PATH)
last_water_usage = df.iloc[-1]['User Water Usage (liters)']
if last_water_usage > THRESHOLD:
    st.warning(f"Water usage ({last_water_usage} liters) exceeded the threshold "
               f"({THRESHOLD} liters). Ask me for suggestions.")

responses = [
    # Response 1: Welcome
    "Hello there! How can I assist you today? I'm here to help you with water-saving tips.",

    # Response 2: How to reduce water consumption (based on appliances)
    "To reduce water consumption, here are some tips based on the appliances you use: "
    "1. **Shower**: Consider installing a low-flow showerhead to save water. Taking shorter showers can also make a big difference. "
    "2. **Washing Machine**: Always run your washing machine with a full load to maximize efficiency. Using cold water can also reduce water use and energy costs. "
    "3. **Bathtub**: Instead of filling up the bathtub, try taking shorter baths or showers. You can also consider installing a water-saving device for the tub. "
    "4. **Dishwasher**: Make sure to run your dishwasher only when it's fully loaded. You can also skip the pre-rinse cycle and use eco-settings to save water.",

    # Response 3: Thanking the user and offering further help
    "Thank you for using the water-saving tips! If you need more advice or help, feel free to ask. I'm here to assist you anytime."
]


if "response_index" not in st.session_state:
    st.session_state.response_index = 0


def response_generator():
    response = responses[st.session_state.response_index]
    for word in response.split():
        yield word + " "
        time.sleep(0.1)


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = response_generator()
        response = st.write_stream(stream)

    st.session_state.response_index += 1

    # Reset to the first response if we've gone through all responses
    if st.session_state.response_index >= len(responses):
        st.session_state.response_index = 0

    st.session_state.messages.append({"role": "assistant", "content": response})
