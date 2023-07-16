import requests
from .import forms
from django.shortcuts import render
from django.conf import settings
from .forms import CommentForm
from .models import Comment
from django.core.paginator import Paginator
url = "https://imdb-top-100-movies.p.rapidapi.com/"

headers = {
	"X-RapidAPI-Key": "565905d3aamsh90e6cfeb00ba7c9p1eb7bejsn9ff323ad2aab",
	"X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
}
def comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CommentForm()

    comments = Comment.objects.order_by('-created_at')
    context={'comments': comments}
    return render(request,'comment.html',context)
def index(request):


    response = requests.get(url, headers=headers)
    movies= response.json()
    movie_data=[]
    for movie in movies:
        movie_data.append({
            'image': movie['image'],
            'title': movie['title'],
            'rank': movie['rank'],
            'rating':movie['rating'],
            'year':movie['year']
        })
      # Paginate the movie data
    paginator = Paginator(movie_data, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass the movie data to the template
    context = {'movies': movie_data,'page_obj': page_obj}
    return render(request, 'index.html', context)
