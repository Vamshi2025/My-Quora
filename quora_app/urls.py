from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_login),
    path('home/', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ask/', views.ask_question, name='ask'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('like/<int:answer_id>/', views.like_answer, name='like_answer'),
]
