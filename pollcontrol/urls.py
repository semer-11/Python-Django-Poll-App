from django.urls import path
from . import views




urlpatterns=[

path('addpoll/',views.addpoll),
path('mine/',views.mypolls),
path('<int:pollid>/detail/',views.polldetail),
path('<int:question_id>/modify',views.modify),
path('<int:question_id>/modify/question',views.question_modify),
path('<int:question_id>/modify/delete',views.delete),
path('<int:choice_id>/modify/choice',views.choice_modify),
path('<int:question_id>/modify/addchoice',views.addchoice),
path('<int:choice_id>/modify/deletechoice',views.delete_choice),


]