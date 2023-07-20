# Overview 
A Django website that retrievs the top IMDB movies and their details using the RapidAPI. The website includes a comment section that allows users to leave comments about the movies. Here I used testing from django.test import TestCase
from django.test.client import Client

Create your tests here.
class HomeViewTest(TestCase):
def test_index(self):
client= Client()
response = client.get('/')
assert response.status_code == 200

In this project, unit testing has been implemented using the Django TestCase class and the Client class from django.test.client

![photo_2023-07-16 20 05 27](https://github.com/MurotovichSh/Top_movies/assets/124291194/7575c071-fd0b-4e27-8bd3-8371dbe5caa9)

![photo_2023-07-16 20 05 23](https://github.com/MurotovichSh/Top_movies/assets/124291194/902a8b35-eff1-4d08-a406-e3ce1f66007b)
# Features 
Movie listings: The website retrieves the top 100 movies from IMDB using the RapidAPI and displays them on a web page.
Pagination: The website includes pagination buttons that allow users to browse through the list of movies.
Movie detail page: The website includes a detail page for each movie that displays more information about it, including the plot, cast, and ratings.
Comment section: The website includes a comment section that allows users to leave comments about the movies.
Comment form: The comment section includes a form that users can fill out to leave a comment.
Comment display: The comment section displays existing comments in reverse chronological order.
# Acknowledgement
API: The official API and RapidAPI docmentations were used in order to build this website.
