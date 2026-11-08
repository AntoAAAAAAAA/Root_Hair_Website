import streamlit as st

st.title("Discovering Signals - Root Hair Analyzer")
st.divider()

st.text("Select your operating system from below.")
# st.text("Once the Google Drive link has opened, click 'Download', and save your .zip file to a safe location on your system.")

col1, col2 = st.columns(2)

with col1.expander("MacOS", expanded=False):
    st.link_button('Download App', "https://github.com/AntoAAAAAAAA/Root_Hair_Project/releases/latest/download/RHA_Installer.dmg",
                   type='primary')
    st.text('')
    st.text("1. Download and install installer")
    st.text("2. Follow on-screen instructions to install app")
    st.text("3. Follow instructions in github repo regarding security alerts (this app is not digitally signed)")

with col2.expander("Windows", expanded=False):
    st.link_button("Download App", "https://github.com/AntoAAAAAAAA/Root_Hair_Project/releases/latest/download/RHA_Installer_Windows.exe",
                   type='primary')     
    st.text('')
    st.text("1. Download and install installer")
    st.text("2. Follow on-screen instructions to install app")
    st.text("3. Follow instructions in github repo regarding security alerts (this app is not digitally signed)")

st.text(" ")
st.text(' ')
st.text(' ')
st.text(' ')

st.write("For feedback or issues, please email: ***anto2005antony@gmail.com***")
