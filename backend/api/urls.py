from django.urls import path
from .views import CreatePost, PostDetail, GetPostList

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('', GetPostList.as_view()),
    path('post/', CreatePost.as_view()),
]