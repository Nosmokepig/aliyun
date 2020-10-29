from django.urls import path
from book import views
urlpatterns = [
    path('book/',views.BookAPIView.as_view()),
    path('book/<str:id>/',views.BookAPIView.as_view()),
]
