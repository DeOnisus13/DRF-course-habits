from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateAPIView, HabitRetrieveUpdateDestroyAPIView, MyHabitListAPIView,
                          PublicHabitListAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', HabitRetrieveUpdateDestroyAPIView.as_view(), name='habit'),
    path('list/', MyHabitListAPIView.as_view(), name='list'),
    path('public/', PublicHabitListAPIView.as_view(), name='public'),
]
