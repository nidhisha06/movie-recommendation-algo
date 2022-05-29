import streamlit as st
import pickle
import pandas as pd
import requests
from streamlit_lottie import st_lottie
from PIL import Image



st.set_page_config(page_title="Binge Watch", page_icon=":tada:", layout="wide")

# Remove whitespace from the top of the page and sidebar
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 1.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

# animation function
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_animation_1 = "https://assets6.lottiefiles.com/packages/lf20_CTaizi.json"
lottie_anime_json = load_lottie_url(lottie_animation_1)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True , key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


col1, col2 = st.columns(2)
with col1:
     st_lottie(lottie_anime_json, key='hello', speed=1, reverse=False, loop=True, quality="low", height=200, width=200)
with col2:
     st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie for recommendation',
    movies['title'].values)



if st.button('Search'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)

    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('top 10.jpg')
        st.image(image, width=50)

    with col2:
        st.header("Top 10 Recommended movies")

    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
    with col1:
        st.image(recommended_movie_posters[0], caption=recommended_movie_names[0], width=100)

    with col2:
        st.image(recommended_movie_posters[1], caption=recommended_movie_names[1], width=100)

    with col3:
        st.image(recommended_movie_posters[2], caption=recommended_movie_names[2], width=100)

    with col4:
        st.image(recommended_movie_posters[3], caption=recommended_movie_names[3], width=100)

    with col5:
        st.image(recommended_movie_posters[4], caption=recommended_movie_names[4], width=100)

    with col6:
        st.image(recommended_movie_posters[5], caption=recommended_movie_names[5], width=100)

    with col7:
        st.image(recommended_movie_posters[6], caption=recommended_movie_names[6], width=100)

    with col8:
        st.image(recommended_movie_posters[7], caption=recommended_movie_names[7], width=100)

    with col9:
        st.image(recommended_movie_posters[8], caption=recommended_movie_names[8], width=100)

    with col10:
        st.image(recommended_movie_posters[9], caption=recommended_movie_names[9], width=100)

