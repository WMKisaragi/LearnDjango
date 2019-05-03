from django.urls import path

from . import  views

#どのアプリのurlを見るのかを伝える宣言
app_name = 'polls'
urlpatterns = [
    # ex : /polls/
    path('',views.index, name='index'),
    ##section3
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/',views.vote, name='vote')
]
