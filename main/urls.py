from django.urls import path
from . import views
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView
                    )

urlpatterns = [
    path("", PostListView.as_view(), name="homepage"),
     path("user/<str:username>", UserPostListView.as_view(), name="userhomepage"),
    path("about", views.about, name="aboutpage"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="detailpage"),
    path("post/new/",PostCreateView.as_view(), name='createpage'),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="updatepage"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="deletepage"),
]