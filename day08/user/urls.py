from django.urls import path
from user import views
urlpatterns = [
    path('teacher/',views.TeacherAPIView.as_view()),
    path('teacher/<str:id>/',views.TeacherAPIView.as_view()),
]

