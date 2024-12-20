from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Posts, name='Posts'),
    path('accounts/sign-up/', views.sign_up, name='sign-up'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('post/<int:pk>/', views.Post, name='Post'),
    path('post/<int:pk>/post comment/', views.add_comment, name='Comment'),
    path('post/<int:pk>/edit', views.PostEditView.as_view(), name='Post_edit'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='Post_delete'),
]
