import streamlit as st
from query import generate_response

def main():
    st.title("📚 CourseLens")
    st.write("Ask any question about the free courses available on Analytics Vidhya!")

    # User input
    user_input = st.text_input("Enter your query:", "")

    if st.button("Search"):
        if user_input.strip():
            with st.spinner("Searching for the best courses..."):
                response = generate_response(user_input)
                st.subheader("Search Results:")
                st.write(response)
        else:
            st.warning("Please enter a query to search.")

if __name__ == "__main__":
    main()
