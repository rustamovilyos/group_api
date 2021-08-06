from django.urls import path
from . import views


urlpatterns = [
    path('group/', views.GroupListView.as_view()),
    path('group/<int:pk>', views.GroupDetailView.as_view()),
    path('person/', views.PersonListView.as_view()),
    path('person/<int:pk>', views.PersonDetailView.as_view())
]
