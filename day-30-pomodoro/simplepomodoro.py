import streamlit as st
import time

st.title("Simple Pomodoro Timer")

work_min = st.number_input("Work minutes", min_value=1, max_value=60, value=25)
break_min = st.number_input("Break minutes", min_value=1, max_value=30, value=5)

if st.button("Start Pomodoro"):
    placeholder = st.empty()
    st.write(f"Pomodoro started! Work for {work_min} minutes.")
    # Work countdown
    for i in range(work_min * 60, 0, -1):
        mins, secs = divmod(i, 60)
        placeholder.write(f"Time left: {mins:02}:{secs:02}")
        time.sleep(1)
    st.write(f"Work session done! Take a break for {break_min} minutes.")
    # Break countdown
    for i in range(break_min * 60, 0, -1):
        mins, secs = divmod(i, 60)
        placeholder.write(f"Break time left: {mins:02}:{secs:02}")
        time.sleep(1)
    st.write("Pomodoro complete! Well done!")
