from django.urls import path
from .views import HabitListCreateView, HabitDetailView

urlpatterns = [
    path('habits/', HabitListCreateView.as_view(), name='habit-list-create'),
    path('habits/<int:pk>/', HabitDetailView.as_view(), name='habit-detail'),
]
