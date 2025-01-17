from django.urls import path
from . import views


urlpatterns=[
    path('genres/', views.GenreCreateListView.as_view(), name='genres-create-list'),
    path('genre/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view')
]





