from django.shortcuts import render, redirect
from .models import Movie

def index(request):
    # movies = Movie.objects.order_by('-pk')
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')

    movie = Movie(title=title, audience=audience, release_date=release_date, genre=genre, score=score, poster_url=poster_url, description=description)
    movie.save()

    return redirect('movies:detail', movie.pk)

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context={
        'movie':movie,
    }
    return render(request, 'movies/detail.html', context)

def delete(request, movie_pk):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_pk)
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie_pk)

def edit(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context={
        'movie':movie,
    }
    return render(request, 'movies/edit.html', context)

def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')

    movie.title = title
    movie.audience = audience
    movie.release_date = release_date
    movie.genre = genre
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description

    movie.save()

    return redirect('movies:detail', movie.pk)
