# 📌 My Fifth Project 📋

---

##### - Outline : 2022년 3월 11일, 다섯번째 관통 프로젝트를 수행하였다. 작은 프로젝트를 많이 하다보니, 이제는 그렇게 어렵지만은 않고, 어느정도 시간이 걸릴 것임을 각오하고 임하게 되는 것 같다. 겁에 질려 시작하는 것이 아니라, 그저 흘러가는 과정 속에서 성장할 수 있는 좋은 기회라고 생각하며 차근차근 나아갈 수 있게 된 것 같다. 이 파일에서는 오늘 내가 해당 프로젝트를 진행하면서 느꼈던 점을 중심으로 소개해 보고자 한다.

---

<br>


# **< Title : "프레임워크 기반 웹 페이지 구현" >**

*(This project was carried out in **Python 3.9.9 and Django 3.2.12 environment .**)*

- *요구사항 : 커뮤니티 서비스의 게시판 기능 개발을 위한 단계로, 영화 데이터의 생성, 조회, 수정, 삭제 가능한 어플리케이션을 완성시켜야만 한다. 해당 기능은 향후 커뮤니티 서비스의 필수 기능으로 사용될 수 있다. 기술되어 있는 사항들에 대해 필수적으로 구현시켜야 한다.*

---

*(프로젝트 파일의 settings.py, urls.py와 base.html 등의 기본 설정은 제외하고 , 앱 파일에 관해서만 작성합니다.)*

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

  : 클라이언트로부터 요청이 들어오게 된다면 해당하는 작업을 보여줄 수 있게끔 응답해줄 수 있어야 한다. 나는 그렇게 배웠다. 그것이 웹 서비스니깐. 그렇기에 가장 먼저 url로 들어왔을때 그 다음 과정인 view까지 이어줄 수 있는 것이 urls.py 이다.

  이 과정에서 오류를 가장 많이 겪었다. 왜냐하면, 나는 urls.py가 가장 처음 단계인 줄 알면서도 다른 부분부터 작성하게 되어 테스트 해 보았는데 자꾸 되지 않았기 때문이다. 이것 저것 다 만져보다가 도저히 내가 잘못 한 것이 없다고 단정지어 버리려다가, 처음 과정부터 다시 생각해 볼 수 있게 되었다. 그 결과 내가 가장 기초적인 부분을 놓치고 있었던 것이었다.

  컴퓨터 탓만 하다가 정작 이것을 알게 되었을 때 나는 정말 내 자신이 초라해지고 한참 미워하며 자책하다가 결국엔 기본이 제일 우선이며 제일 중요하다는 것을 다시 한번 깨닫게 되었다.

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

  : 꽤 긴 코드이다 보니 각각에 대한 해석은 힘들 수 있는데, 그래도 작성하면서 느꼈던 점에 적어보도록 할 것이다. 일단, 그 전에 복습할 때는 혼자 구현하기가 많이 힘들었었던 것에 비해, 연습을 겪다보니 결국 어느 정도 이해는 하면서 구현할 수 있었던 것 같다. ~~물론, 수업내용을 많이 참고했었다..^^~~ 그래도 반복하다보니 처음엔 신기하게만 느껴졌었는데, 갈수록 친근해지는 것 같다. 함수 구현에 있어서 redirect와 render반환의 차이점에 대해서도 생각해보곤 했다. 다음은 이번 프로젝트를 수행하면서 얻은 지식이다.

  > ```python
  > return render(request, template_name, context=None, content_type=None, status=None, using=None)
  > ```
  >
  > : 위는 render의 파라미터이다. render란 곧, 화면에 html 파일을 띄움으로써 응답해주는 것이라고 생각하면 될 것 같다. 즉, 템플릿을 불러온다.
  >
  > ```python
  > return redirect(to, permanent=False, *args, **kwargs)
  > ```
  >
  > : 위는 redirect의 파라미터이다. to는 어느 URL로 이동할 지 적어주면 된다. urls.py에 name을 정의하고 사용하는 방식으로 구현하였다. redirect란 곧, URL로 이동한다고 생각하면 될 것 같다.

<br>

- **movies/admin.py**

  ```python
  from django.contrib import admin
  from .models import Movie
  
  class MovieAdmin(admin.ModelAdmin):
      list_display = ('pk', 'title', 'audience', 'release_date', 'genre', 'score', 'poster_url', 'description')
  
  admin.site.register(Movie, MovieAdmin)
  ```

  : admin.py도 빼먹고 views.py에서 함수를 먼저 작성한다고 하다가 결국은 수없이 많은 오류가 나를 반겨주었다. 혼자 많이 생각해보다가 이 또한 결국 해결할 수 있게 된 것 같다. 코드가 아직은 익숙하지 않아서, 이전 수업 내용을 참고하여 작성하였다.

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

  : models.py는 손쉽게 작성하였던 것 같다. 요구하는 것에 맞춰서 작성할 수 있었다.

<br>

---

## ✏After finishing..

>   　　벌써 다섯번째 관통 프로젝트를 진행하고 시간이 많이 흘러갔음을 느낀다. 당연하지만 아직도 배울 것은 널리고 널렸고, 내 것으로 만든 것은 아직 거의 없다고 봐도 무방할 정도이다. 그래도 성장하고 있음은 스스로도 많이 체감하곤 한다. 급하게 하지 않을 수 있고, 더 많이 생각하는 방법을 깨닫고 있는 중이다. 이번 과제를 통해 이 점에 대해 많이 느꼈던 것 같다.
>
>   　​	여전히 웹은 나에게 많이 어렵다. 공식처럼 문법을 외워서 썼던 나에게, 그리고 아직 그 버릇을 고치지 못하는 나에게 많이 어려운 것이다. 다만, 구글링 실력이 곧 개발능력이라는 말이 있듯이, 구글과 함께라면 두렵지 않은 것이 또 웹인 것 같다.
>
>   　​	더 많은 자습이 필요함을 느꼈다. 그리고, 이 모든 것을 다 내 것으로 만들고 싶어졌다. CRUD를 구현하는 것은 정말 기본이라고 한다. 그래, 내가 이겨보자. 할 수 있을 것이다.

