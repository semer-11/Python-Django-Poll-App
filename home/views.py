from django import http
from django.core import exceptions
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import choice, question,voted_to
from django.db.models import Sum
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def index(request):
         return render(request,'home.html')

class user:
     def login_query(request):
          if request.method=='GET':
               return render(request,'login.html')
          elif request.method=='POST':
               username=request.POST['username']
               password=request.POST['password']
               user=authenticate(request,username=username,password=password)
               if user is not None: 
                    login(request,user)
                    
                    return redirect('/',{'user':user})
               else:
                    return HttpResponse('unauthorized user')
          
     def log_out(request):
          
          logout(request)
          return redirect('/')

     def register(request):
          if request.method=='GET':

               return render(request,'register.html')
          if request.method=='POST':
               firstname=request.POST['firstname']
               lastname=request.POST['lastname']
               username=request.POST['username']
               password1=request.POST['password1']
               password2=request.POST['password2']
               if password1==password2:
                    user=User.objects.create_user(username=username,email='email@gmail.com',password=password1)
                    user.first_name=request.POST['firstname']
                    user.last_name=request.POST['lastname']
                    user.save()
                    authenticate(username=username,password=password1)
                    if user is not None:
                         login(request,user)
                         return redirect('/')
               else:
                    return HttpResponse('Error while creating an acoount')

@login_required


class polls:

     def poll(request):
         # byfarvote=voted_to.objects.filter(user=request.user.get_username()).values('to_question')
          qst=question.objects.all().order_by('-pub_date')[:5]
          return render(request,'polls.html',{'qst':qst})
     def allpolls(request):

          qst=question.objects.all().order_by('-pub_date')
          return render(request,'polls.html',{'qst':qst})



@login_required
def vote(request,question_id):
     if request.method=='GET':
          qst=question.objects.get(id=question_id)
          chc=choice.objects.filter(question_id=question_id)
          return render(request,'vote.html',{'qst':qst,'chc':chc} )
          
          
@login_required
def addvote(request,question_id):
     try:
               
               
          selected_choice=choice.objects.get(pk=request.POST['choice_set'])
          selected_choice.vote +=1 
          selected_choice.save()
          user=voted_to(user=request.user.get_username(),to_question=question_id,choice_selected=request.POST['choice_set'])
          user.save()
          each_vote=choice.objects.filter(question_id=question_id)
          total=choice.objects.filter(question_id=question_id).aggregate(Sum('vote')).get('vote__sum')
          the_question=question.objects.get(id=question_id)
          return render(request,'result.html',{'single_vote':each_vote,'total':total,'qst':the_question})
              
     except Exception as e:
          # most often this exception handles  form resubmission 
          each_vote=choice.objects.filter(question_id=question_id)
          total=choice.objects.filter(question_id=question_id).aggregate(Sum('vote')).get('vote__sum')
          
          the_question=question.objects.get(id=question_id) 
          return render(request,'result.html',{'single_vote':each_vote,'total':total,'qst':the_question})


@login_required
def retract(request,question_id):
     
          try:
               qst=voted_to.objects.get(user=request.user.get_username(),to_question=question_id)
               chc=choice.objects.get(id=qst.choice_selected)
               chc.vote -=1
               chc.save()
               qst.delete() # after we retract the vote we need to delete the object.the user doesn't voted for that specific question anymore
               #return the updated value to the voter
               each_vote=choice.objects.filter(question_id=question_id) 
               total=choice.objects.filter(question_id=question_id).aggregate(Sum('vote')).get('vote__sum')
               the_question=question.objects.get(id=question_id)
               return render(request,'result.html',{'single_vote':each_vote,'total':total,'qst':the_question})

          except ObjectDoesNotExist:
               qst=question.objects.get(id=question_id)
               return render(request,'exceptions.html',{'qst':qst})
    
          except Exception as e:
               return HttpResponse('Internal server Error We are Working on it')
     


    
     
    











 