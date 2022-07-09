from django.urls import path
from . import views



urlpatterns=[
path('',views.index),
path('register',views.user.register), 
path('accounts/login',views.user.login_query),
path('logout',views.user.log_out),
path('polls',views.polls.poll),
path('polls/all',views.polls.allpolls),
path('<int:question_id>/',views.vote),
path('<int:question_id>/addvote',views.addvote),
path('<int:question_id>/retract',views.retract),

]