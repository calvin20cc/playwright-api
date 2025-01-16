import streamlit as st
import requests

# Streamlit app title
st.title("Playwright API - Extracted Text Viewer")

# Input for URL
url = st.text_input("Enter the URL to scrape:", "")

# Button to trigger API call
if st.button("Get Extracted Text"):
    if url.strip():  # Check if URL is not empty
        try:
            # Call the Playwright API
            api_url = "https://playwright-api-439390593547.us-central1.run.app/scrape/"
            params = {"url": url}
            response = requests.get(api_url, params=params, timeout=30)

            # Check the response
            if response.status_code == 200:
                result = response.json()
                extracted_text = result.get("extracted_text", "No text found.")
                
                # Display the extracted text
                st.subheader("Extracted Text:")
                st.text_area("", extracted_text, height=300)
            else:
                st.error(f"API returned an error: {response.status_code}")
                st.text(response.text)
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to call API: {e}")
    else:
        st.warning("Please enter a valid URL.")
