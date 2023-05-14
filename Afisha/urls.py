
from django.contrib import admin
from django.urls import path
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/director/', views.director_api_view),
    path('api/v1/director/<int:id>/', views.director_detail_api_view),
    path('api/v1/movies/', views.movies_api_view),
    path('api/v1/movies/<int:id>/', views.movie_detail_api_view),
    path('api/v1/reviews/', views.reviews_api_view),
    path('api/v1/reviews/<int:id>/', views.review_detail_api_view),

]
