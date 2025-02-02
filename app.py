import streamlit as st


st.title(" 🤑Ava's story Generator")



character = st.text_input(" enter your  character's name")


place = st.selectbox(" choose your place wisely",["Nigeria 🌍🏃‍♂️", "Australia🌍🏃‍♂️","AFrica 🌍🏃‍♂️ ", "USA 🌍🏃‍♂️ ", " Tallinn 🌍🏃‍♂️"])


action = st.selectbox(" choose your actions wisely",["Run 🏃‍♂️🏃‍♂️", "laugh 🤣🤣","sing 🎤🎤🎤 ", "dance 🕺🏾🕺🏾🕺🏾 ", " travel ✈️🧳✈️"])


story_template = f"""
 
Once upon a time, there was a brave adventurer named {character}.

one day, {character} decided to visit the mystical {place}, where no one 
one had to go.
Upon arriving, {character} encountered a mysterious creature and decided to {action}.
The adventure changed {character}'s life forever, teaching them valuable lessons about courage and friendship.

"""


if st.button(" Generate Story"):
    st.write(story_template)