import streamlit as st

st.title("Discovering Signals - Root Hair Analyzer")
st.divider()

st.text("Select your operating system from below.")
# st.text("Once the Google Drive link has opened, click 'Download', and save your .zip file to a safe location on your system.")

col1, col2 = st.columns(2)

with col1.expander("MacOS", expanded=False):
    st.link_button('Download App', "https://drive.google.com/file/d/1tVgmH87d4CY-BnOdJj9Pd-R6k5LNytjG/view?usp=sharing",
                   type='primary')
    st.text('')
    st.text("1. Click 'Download App'")
    st.text("2. A Google Drive link will open. Click 'Download'")
    st.text("3. Save the .zip file to a safe location")
    st.text("4. Open Finder, navigate to the .zip file, and double click it")
    st.text("5. You should see a file called RootHairAnalyzer open; this is your app. Double click to open")
    st.text("Optional: Move the app to your Applications folder for easier future access")

with col2.expander("Windows", expanded=False):
    st.link_button("Download App", "https://drive.google.com/file/d/1K_IMNXt5vRsRFswknl3AwWMEXXl55iU_/view?usp=sharing",
                   type='primary')     
    st.text('')
    st.text("1. Click 'Download App'")
    st.text("2. A Google Drive link will open. Click 'Download'")
    st.text("3. Save the .zip file to a safe location")
    st.text("4. Open Finder, navigate to the .zip file, and double click it")
    st.text("5. You should see a file called RootHairAnalyzer open; this is your app. Double click to open")
    st.text("Optional: Right click on the app and create a desktop shortcut for easy access later")
st.text(" ")
st.text(' ')
st.text(' ')
st.text(' ')

st.write("For feedback or issues, please email: ***anto2005antony@gmail.com***")
