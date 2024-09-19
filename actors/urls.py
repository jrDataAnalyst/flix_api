from django.urls import path
from . import views


urlpatterns = [

    path('actors/', views.ActorCreateListView.as_view(), name='actors-create-list'),
    path('actor/<int:pk>/', views.ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view')

]