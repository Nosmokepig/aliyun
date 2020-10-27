
from django.urls import path
from user_app import views
app_name = 'user_app'
urlpatterns = [
    path('user_view/',views.UserView.as_view(),name='user_view'),
    path('user_view/<str:id>/',views.UserView.as_view()),
]
