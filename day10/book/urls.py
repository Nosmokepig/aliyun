from django.urls import path

from book import views
urlpatterns = [
    path("book/",views.BookGenericAPIView.as_view()),
    path("book/<str:id>",views.BookGenericAPIView.as_view()),

    path("set/login/", views.UserViewSetView.as_view({"post": "user_login"})),
    path("set/register/", views.UserViewSetView.as_view({"post": "register"})),

]

