import streamlit as st

st.title("Discovering Signals - Root Hair Analyzer")
st.divider()

st.text("Please select a download option from below")

col1, col2 = st.columns(2)

with col1.expander("MacOS", expanded=False):
    st.link_button('Download App', "https://drive.google.com/file/d/1LFbcEDF2atjDAlBoKH3Mw-9CMhirEjDu/view?usp=drive_link")

with col2.expander("Windows", expanded=False):
    st.link_button("Download App", "https://drive.google.com/file/d/1l5KtwsILhIPowhPa26pMESzytDKNlqkC/view?usp=drive_link")     

st.text(" ")

st.text("After clicking 'download', make sure to find the .zip file in your files, double click it, and you " \
"should see an app named 'Root Hair Analyzer'. For convenience, feel free to move that app to your desktop " \
"for easier future access.")