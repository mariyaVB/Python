from django.urls import path, re_path
import movies.views as movies

urlpatterns = [
    path('', movies.first),
    path('<slug:slug_movies>/', movies.info_movies),
]
