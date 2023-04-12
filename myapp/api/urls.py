from django.urls import path
from myapp.api.views import MovieListAPI, MovieDetailAPI

urlpatterns = [
    path('', MovieListAPI.as_view()),
    path('<int:pk>', MovieDetailAPI.as_view()),
]

# urlpatterns = [
#     path('', views.movie_list ),
#     path('<int:pk>',views.movie_detail),
# ]
