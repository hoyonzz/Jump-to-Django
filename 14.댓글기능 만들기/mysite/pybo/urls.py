from django.urls import path
from pybo import views



app_name = 'pybo'



urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:question_id>/', views.detail, name = 'detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name = 'answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
    path('commnet/create/question/<int:question_id>/', views.comment_create_question, name='comment_create_question'),
    path('commnet/modify/question/<int:comment_id>/', views.comment_modify_question, name='comment_modify_question'),
    path('commnet/delete/question/<int:comment_id>/', views.comment_delete_question, name='comment_delete_question'),
    path('commnet/create/answer/<int:answer_id>/', views.comment_create_answer, name='comment_create_answer'),
    path('commnet/modify/answer/<int:comment_id>/', views.comment_modify_answer, name='comment_modify_answer'),
    path('commnet/delete/answer/<int:comment_id>/', views.comment_delete_answer, name='comment_delete_answer'),
]
