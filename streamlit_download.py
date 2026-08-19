import streamlit as st

st.title("Discovering Signals - Root Hair Analyzer")
st.divider()

st.text("Select your operating system from below.")

st.text("Once the Google Drive link has opened, click 'Download', and save your .zip file to a safe location on your system.")

col1, col2 = st.columns(2)

with col1.expander("MacOS", expanded=False):
    st.link_button('Download App', "https://drive.google.com/file/d/1LFbcEDF2atjDAlBoKH3Mw-9CMhirEjDu/view?usp=drive_link")
    st.text("Click 'Download App', and Google Drive link should open in a new tab.")
with col2.expander("Windows", expanded=False):
    st.link_button("Download App", "https://drive.google.com/file/d/1l5KtwsILhIPowhPa26pMESzytDKNlqkC/view?usp=drive_link")     

st.text(" ")

st.text("Find the .zip file in your files, double click it, and you " \
"should see an app named 'Root Hair Analyzer' show up nearby. For convenience, feel free to move this app to your desktop " \
"for easier future access. Double-clicking this app will open the analyzer.")