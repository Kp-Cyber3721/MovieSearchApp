import streamlit as st
import requests

API_KEY = "YOUR_API_KEY"
API_URL = "https://www.omdbapi.com/?apikey=" + API_KEY

st.title("🎬 Movie Search App")

search_term = st.text_input("Enter a movie title")

if st.button("Search"):
    if search_term:
        response = requests.get(f"{API_URL}&s={search_term}")
        data = response.json()
        
        if data.get("Search"):
            for movie in data["Search"]:
                st.image(movie["Poster"], width=150)
                st.write(f"**{movie['Title']} ({movie['Year']})**")
                details_button = st.button(f"Details: {movie['imdbID']}", key=movie['imdbID'])
                
                if details_button:
                    movie_details = requests.get(f"{API_URL}&i={movie['imdbID']}").json()
                    st.write(f"**Plot:** {movie_details.get('Plot', 'N/A')}")
                    st.write(f"**Actors:** {movie_details.get('Actors', 'N/A')}")
        else:
            st.error("No movies found. Try a different title.")
    else:
        st.warning("Please enter a movie title.")
