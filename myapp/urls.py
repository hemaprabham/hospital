from django.urls import path
from . import views

urlpatterns = [
    # List Articles View
    path('homepage/', views.list_articles, name='homepage'),

    # Display Article Detail View
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),

    # User Registration and Authentication Views
    path('', views.register, name='register'),
   
    # Add paths for login and logout views if implemented
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Submit Comments View
    path('article/<int:article_id>/comment/', views.submit_comment, name='submit_comment'),
]
