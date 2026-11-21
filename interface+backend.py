import streamlit as st

#open_spots = 

st.title("Welcome!")
st.header("Hello")

st.metric("Open spots", "spot")
# new push


select_floor = st.selectbox("Select Floor:", ["Floor 1", "Floor 2"])
select_space = st.selectbox("Select Parking Space:", range(1,13))


if st.button("Navigate"):
    st.success(f"Success! Navigating to {select_floor} parking space {select_space}")


