# ๐ My Fifth Project ๐

---

##### - Outline : 2022๋ 3์ 11์ผ, ๋ค์ฏ๋ฒ์งธ ๊ดํต ํ๋ก์ ํธ๋ฅผ ์ํํ์๋ค. ์์ ํ๋ก์ ํธ๋ฅผ ๋ง์ด ํ๋ค๋ณด๋, ์ด์ ๋ ๊ทธ๋ ๊ฒ ์ด๋ ต์ง๋ง์ ์๊ณ , ์ด๋์ ๋ ์๊ฐ์ด ๊ฑธ๋ฆด ๊ฒ์์ ๊ฐ์คํ๊ณ  ์ํ๊ฒ ๋๋ ๊ฒ ๊ฐ๋ค. ๊ฒ์ ์ง๋ ค ์์ํ๋ ๊ฒ์ด ์๋๋ผ, ๊ทธ์  ํ๋ฌ๊ฐ๋ ๊ณผ์  ์์์ ์ฑ์ฅํ  ์ ์๋ ์ข์ ๊ธฐํ๋ผ๊ณ  ์๊ฐํ๋ฉฐ ์ฐจ๊ทผ์ฐจ๊ทผ ๋์๊ฐ ์ ์๊ฒ ๋ ๊ฒ ๊ฐ๋ค. ์ด ํ์ผ์์๋ ์ค๋ ๋ด๊ฐ ํด๋น ํ๋ก์ ํธ๋ฅผ ์งํํ๋ฉด์ ๋๊ผ๋ ์ ์ ์ค์ฌ์ผ๋ก ์๊ฐํด ๋ณด๊ณ ์ ํ๋ค.

---

<br>


# **< Title : "ํ๋ ์์ํฌ ๊ธฐ๋ฐ ์น ํ์ด์ง ๊ตฌํ" >**

*(This project was carried out in **Python 3.9.9 and Django 3.2.12 environment .**)*

- *์๊ตฌ์ฌํญ : ์ปค๋ฎค๋ํฐ ์๋น์ค์ ๊ฒ์ํ ๊ธฐ๋ฅ ๊ฐ๋ฐ์ ์ํ ๋จ๊ณ๋ก, ์ํ ๋ฐ์ดํฐ์ ์์ฑ, ์กฐํ, ์์ , ์ญ์  ๊ฐ๋ฅํ ์ดํ๋ฆฌ์ผ์ด์์ ์์ฑ์์ผ์ผ๋ง ํ๋ค. ํด๋น ๊ธฐ๋ฅ์ ํฅํ ์ปค๋ฎค๋ํฐ ์๋น์ค์ ํ์ ๊ธฐ๋ฅ์ผ๋ก ์ฌ์ฉ๋  ์ ์๋ค. ๊ธฐ์ ๋์ด ์๋ ์ฌํญ๋ค์ ๋ํด ํ์์ ์ผ๋ก ๊ตฌํ์์ผ์ผ ํ๋ค.*

---

*(ํ๋ก์ ํธ ํ์ผ์ settings.py, urls.py์ base.html ๋ฑ์ ๊ธฐ๋ณธ ์ค์ ์ ์ ์ธํ๊ณ  , ์ฑ ํ์ผ์ ๊ดํด์๋ง ์์ฑํฉ๋๋ค.)*

<br>

- **movies/urls.py**

  ```python
  from django.urls import path
  from . import views
  
  app_name = 'movies'
  
  urlpatterns = [
      path('', views.index, name='index'),
      path('new/', views.new, name='new'),
      path('create/', views.create, name='create'),
      path('<int:movie_pk>/', views.detail, name='detail'),
      path('<int:movie_pk>/delete/', views.delete, name='delete'),
      path('<int:movie_pk>/edit/', views.edit, name='edit'),
      path('<int:movie_pk>/update/', views.update, name='update'),
  ]
  ```

  : ํด๋ผ์ด์ธํธ๋ก๋ถํฐ ์์ฒญ์ด ๋ค์ด์ค๊ฒ ๋๋ค๋ฉด ํด๋นํ๋ ์์์ ๋ณด์ฌ์ค ์ ์๊ฒ๋ ์๋ตํด์ค ์ ์์ด์ผ ํ๋ค. ๋๋ ๊ทธ๋ ๊ฒ ๋ฐฐ์ ๋ค. ๊ทธ๊ฒ์ด ์น ์๋น์ค๋๊น. ๊ทธ๋ ๊ธฐ์ ๊ฐ์ฅ ๋จผ์  url๋ก ๋ค์ด์์๋ ๊ทธ ๋ค์ ๊ณผ์ ์ธ view๊น์ง ์ด์ด์ค ์ ์๋ ๊ฒ์ด urls.py ์ด๋ค.

  ์ด ๊ณผ์ ์์ ์ค๋ฅ๋ฅผ ๊ฐ์ฅ ๋ง์ด ๊ฒช์๋ค. ์๋ํ๋ฉด, ๋๋ urls.py๊ฐ ๊ฐ์ฅ ์ฒ์ ๋จ๊ณ์ธ ์ค ์๋ฉด์๋ ๋ค๋ฅธ ๋ถ๋ถ๋ถํฐ ์์ฑํ๊ฒ ๋์ด ํ์คํธ ํด ๋ณด์๋๋ฐ ์๊พธ ๋์ง ์์๊ธฐ ๋๋ฌธ์ด๋ค. ์ด๊ฒ ์ ๊ฒ ๋ค ๋ง์ ธ๋ณด๋ค๊ฐ ๋์ ํ ๋ด๊ฐ ์๋ชป ํ ๊ฒ์ด ์๋ค๊ณ  ๋จ์ ์ง์ด ๋ฒ๋ฆฌ๋ ค๋ค๊ฐ, ์ฒ์ ๊ณผ์ ๋ถํฐ ๋ค์ ์๊ฐํด ๋ณผ ์ ์๊ฒ ๋์๋ค. ๊ทธ ๊ฒฐ๊ณผ ๋ด๊ฐ ๊ฐ์ฅ ๊ธฐ์ด์ ์ธ ๋ถ๋ถ์ ๋์น๊ณ  ์์๋ ๊ฒ์ด์๋ค.

  ์ปดํจํฐ ํ๋ง ํ๋ค๊ฐ ์ ์ ์ด๊ฒ์ ์๊ฒ ๋์์ ๋ ๋๋ ์ ๋ง ๋ด ์์ ์ด ์ด๋ผํด์ง๊ณ  ํ์ฐธ ๋ฏธ์ํ๋ฉฐ ์์ฑํ๋ค๊ฐ ๊ฒฐ๊ตญ์ ๊ธฐ๋ณธ์ด ์ ์ผ ์ฐ์ ์ด๋ฉฐ ์ ์ผ ์ค์ํ๋ค๋ ๊ฒ์ ๋ค์ ํ๋ฒ ๊นจ๋ซ๊ฒ ๋์๋ค.

<br>

- **movies/views.py**

  ```python
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
  ```

  : ๊ฝค ๊ธด ์ฝ๋์ด๋ค ๋ณด๋ ๊ฐ๊ฐ์ ๋ํ ํด์์ ํ๋ค ์ ์๋๋ฐ, ๊ทธ๋๋ ์์ฑํ๋ฉด์ ๋๊ผ๋ ์ ์ ์ ์ด๋ณด๋๋ก ํ  ๊ฒ์ด๋ค. ์ผ๋จ, ๊ทธ ์ ์ ๋ณต์ตํ  ๋๋ ํผ์ ๊ตฌํํ๊ธฐ๊ฐ ๋ง์ด ํ๋ค์์๋ ๊ฒ์ ๋นํด, ์ฐ์ต์ ๊ฒช๋ค๋ณด๋ ๊ฒฐ๊ตญ ์ด๋ ์ ๋ ์ดํด๋ ํ๋ฉด์ ๊ตฌํํ  ์ ์์๋ ๊ฒ ๊ฐ๋ค. ~~๋ฌผ๋ก , ์์๋ด์ฉ์ ๋ง์ด ์ฐธ๊ณ ํ์๋ค..^^~~ ๊ทธ๋๋ ๋ฐ๋ณตํ๋ค๋ณด๋ ์ฒ์์ ์ ๊ธฐํ๊ฒ๋ง ๋๊ปด์ก์๋๋ฐ, ๊ฐ์๋ก ์น๊ทผํด์ง๋ ๊ฒ ๊ฐ๋ค. ํจ์ ๊ตฌํ์ ์์ด์ redirect์ render๋ฐํ์ ์ฐจ์ด์ ์ ๋ํด์๋ ์๊ฐํด๋ณด๊ณค ํ๋ค. ๋ค์์ ์ด๋ฒ ํ๋ก์ ํธ๋ฅผ ์ํํ๋ฉด์ ์ป์ ์ง์์ด๋ค.

  > ```python
  > return render(request, template_name, context=None, content_type=None, status=None, using=None)
  > ```
  >
  > : ์๋ render์ ํ๋ผ๋ฏธํฐ์ด๋ค. render๋ ๊ณง, ํ๋ฉด์ html ํ์ผ์ ๋์์ผ๋ก์จ ์๋ตํด์ฃผ๋ ๊ฒ์ด๋ผ๊ณ  ์๊ฐํ๋ฉด ๋  ๊ฒ ๊ฐ๋ค. ์ฆ, ํํ๋ฆฟ์ ๋ถ๋ฌ์จ๋ค.
  >
  > ```python
  > return redirect(to, permanent=False, *args, **kwargs)
  > ```
  >
  > : ์๋ redirect์ ํ๋ผ๋ฏธํฐ์ด๋ค. to๋ ์ด๋ URL๋ก ์ด๋ํ  ์ง ์ ์ด์ฃผ๋ฉด ๋๋ค. urls.py์ name์ ์ ์ํ๊ณ  ์ฌ์ฉํ๋ ๋ฐฉ์์ผ๋ก ๊ตฌํํ์๋ค. redirect๋ ๊ณง, URL๋ก ์ด๋ํ๋ค๊ณ  ์๊ฐํ๋ฉด ๋  ๊ฒ ๊ฐ๋ค.

<br>

- **movies/admin.py**

  ```python
  from django.contrib import admin
  from .models import Movie
  
  class MovieAdmin(admin.ModelAdmin):
      list_display = ('pk', 'title', 'audience', 'release_date', 'genre', 'score', 'poster_url', 'description')
  
  admin.site.register(Movie, MovieAdmin)
  ```

  : admin.py๋ ๋นผ๋จน๊ณ  views.py์์ ํจ์๋ฅผ ๋จผ์  ์์ฑํ๋ค๊ณ  ํ๋ค๊ฐ ๊ฒฐ๊ตญ์ ์์์ด ๋ง์ ์ค๋ฅ๊ฐ ๋๋ฅผ ๋ฐ๊ฒจ์ฃผ์๋ค. ํผ์ ๋ง์ด ์๊ฐํด๋ณด๋ค๊ฐ ์ด ๋ํ ๊ฒฐ๊ตญ ํด๊ฒฐํ  ์ ์๊ฒ ๋ ๊ฒ ๊ฐ๋ค. ์ฝ๋๊ฐ ์์ง์ ์ต์ํ์ง ์์์, ์ด์  ์์ ๋ด์ฉ์ ์ฐธ๊ณ ํ์ฌ ์์ฑํ์๋ค.

<br>

- **movies/models.py**

  ```python
  from django.db import models
  
  class Movie(models.Model):
      title = models.CharField(max_length=20)
      audience = models.IntegerField()
      release_date = models.DateField()
      genre = models.CharField(max_length=30)
      score = models.FloatField()
      poster_url = models.TextField()
      description = models.TextField()
  ```

  : models.py๋ ์์ฝ๊ฒ ์์ฑํ์๋ ๊ฒ ๊ฐ๋ค. ์๊ตฌํ๋ ๊ฒ์ ๋ง์ถฐ์ ์์ฑํ  ์ ์์๋ค.

<br>

---

## โAfter finishing..

>   ใใ๋ฒ์จ ๋ค์ฏ๋ฒ์งธ ๊ดํต ํ๋ก์ ํธ๋ฅผ ์งํํ๊ณ  ์๊ฐ์ด ๋ง์ด ํ๋ฌ๊ฐ์์ ๋๋๋ค. ๋น์ฐํ์ง๋ง ์์ง๋ ๋ฐฐ์ธ ๊ฒ์ ๋๋ฆฌ๊ณ  ๋๋ ธ๊ณ , ๋ด ๊ฒ์ผ๋ก ๋ง๋  ๊ฒ์ ์์ง ๊ฑฐ์ ์๋ค๊ณ  ๋ด๋ ๋ฌด๋ฐฉํ  ์ ๋์ด๋ค. ๊ทธ๋๋ ์ฑ์ฅํ๊ณ  ์์์ ์ค์ค๋ก๋ ๋ง์ด ์ฒด๊ฐํ๊ณค ํ๋ค. ๊ธํ๊ฒ ํ์ง ์์ ์ ์๊ณ , ๋ ๋ง์ด ์๊ฐํ๋ ๋ฐฉ๋ฒ์ ๊นจ๋ซ๊ณ  ์๋ ์ค์ด๋ค. ์ด๋ฒ ๊ณผ์ ๋ฅผ ํตํด ์ด ์ ์ ๋ํด ๋ง์ด ๋๊ผ๋ ๊ฒ ๊ฐ๋ค.
>
>   ใโ	์ฌ์ ํ ์น์ ๋์๊ฒ ๋ง์ด ์ด๋ ต๋ค. ๊ณต์์ฒ๋ผ ๋ฌธ๋ฒ์ ์ธ์์ ์ผ๋ ๋์๊ฒ, ๊ทธ๋ฆฌ๊ณ  ์์ง ๊ทธ ๋ฒ๋ฆ์ ๊ณ ์น์ง ๋ชปํ๋ ๋์๊ฒ ๋ง์ด ์ด๋ ค์ด ๊ฒ์ด๋ค. ๋ค๋ง, ๊ตฌ๊ธ๋ง ์ค๋ ฅ์ด ๊ณง ๊ฐ๋ฐ๋ฅ๋ ฅ์ด๋ผ๋ ๋ง์ด ์๋ฏ์ด, ๊ตฌ๊ธ๊ณผ ํจ๊ป๋ผ๋ฉด ๋๋ ต์ง ์์ ๊ฒ์ด ๋ ์น์ธ ๊ฒ ๊ฐ๋ค.
>
>   ใโ	๋ ๋ง์ ์์ต์ด ํ์ํจ์ ๋๊ผ๋ค. ๊ทธ๋ฆฌ๊ณ , ์ด ๋ชจ๋  ๊ฒ์ ๋ค ๋ด ๊ฒ์ผ๋ก ๋ง๋ค๊ณ  ์ถ์ด์ก๋ค. CRUD๋ฅผ ๊ตฌํํ๋ ๊ฒ์ ์ ๋ง ๊ธฐ๋ณธ์ด๋ผ๊ณ  ํ๋ค. ๊ทธ๋, ๋ด๊ฐ ์ด๊ฒจ๋ณด์. ํ  ์ ์์ ๊ฒ์ด๋ค.

