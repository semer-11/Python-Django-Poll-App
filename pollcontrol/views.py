from django.db import router
from pollcontrol.models import PollOwner
from django.shortcuts import redirect, render , get_object_or_404
from django.contrib.auth.decorators import login_required
from home.models import question,choice
from django.db.models import Sum

# Create your views here.

@login_required
def addpoll(request):
    if request.method=='POST':
        qst=request.POST['question']
        qst=question(question=qst,owner=request.user)
        qst.save()
        last=question.objects.last()
        chc1=choice(choice_text=request.POST['choice1'],question_id=last)
        chc2=choice(choice_text=request.POST['choice2'],question_id=last)
       
        
        chc1.save()
        chc2.save()
        user_own=PollOwner(user=request.user.get_username(),own_question=last)
        user_own.save()
        return render(request,'addpoll/sucess.html',{'last':last})
    else:
        return render(request,'addpoll/addpoll.html')


@login_required
def mypolls(request):
    
    allpoll=question.objects.filter(owner=request.user)
    return render(request,'addpoll/mypoll.html',{'poll':allpoll})

@login_required
def polldetail(request,pollid):
    poll=question.objects.get(id=pollid)
    chc=choice.objects.filter(question_id=pollid)
    total=choice.objects.filter(question_id=pollid).aggregate(Sum('vote')).get('vote__sum')
    return render(request,'addpoll/polldetail.html',{'poll':poll,'chc':chc,'total':total})

@login_required
def modify(request,question_id):
    qst=get_object_or_404(question,pk=question_id)
    if request.user==qst.owner:
        chc=choice.objects.filter(question_id=question_id)
        return render(request,'addpoll/modify.html',{'qst':qst,'chc':chc})
    else:
       msg='You are not authorized to modify '
       return  render(request,'404.html',{'msg':msg})

@login_required
def choice_modify(request,choice_id):
    if request.method=='POST':
        chc=choice.objects.get(id=choice_id)
        poll = get_object_or_404(question,pk=chc.question_id.id)
        if request.user== poll.owner:
            print(poll.owner)
            value=request.POST['choice']
            chc.choice_text=value
            chc.save()
            route='/'+str(poll.id)+'/modify'
            return redirect(route,permanent=True)
        else:
            redirect('/')

    if request.method=='GET':
        chc=choice.objects.get(id=choice_id)
        return render(request,'addpoll/modifychoice.html',{'chc':chc})
@login_required
def addchoice(request,question_id):
    poll = get_object_or_404(question,pk=question_id)
    if request.user==poll.owner:
        value=request.POST['choice']
        chc=choice(choice_text=value,question_id=poll)
        chc.save()
        route='/'+str(question_id)+'/modify'
        return redirect(route,permanent=True)
    else:
         msg='You are not authorized to make changes'
         return render(request,'404.html',{'msg':msg})




@login_required
def question_modify(request,question_id):
    if request.method=='POST':
        qst = get_object_or_404(question,pk=question_id)
        route='/'+str(question_id)+'/modify'
        if request.user==qst.owner:
            editvalue=request.POST['question']
            qst.question=editvalue
            qst.save()
            
            return redirect(route,permanent=True)
        else:
            msg='You are not authorized to make changes'
            return render(request,'404.html',{'msg':msg})

@login_required
def delete(request,question_id):
    is_owner = get_object_or_404(question,pk=question_id)
    if request.user==is_owner.owner:
        is_owner.delete()
        return redirect('/mine')
    else:
        msg='You are not authorized to make changes'
        return render(request,'404.html',{'msg':msg})

@login_required
def delete_choice(request,choice_id):
    chc=choice.objects.get(id=choice_id)
    poll = get_object_or_404(question,pk=chc.question_id.id)
    if request.user==poll.owner:
        chc=choice.objects.get(id=choice_id)
        chc.delete()
        route='/'+str(poll.id)+'/modify'
        return redirect(route,permanent=True)
    else:
         msg='You are not authorized to make changes'
         return render(request,'404.html',{'msg':msg})