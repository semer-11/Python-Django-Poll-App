
from typing import Tuple
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
import datetime

# Create your models here.




class question(models.Model):
        now=datetime.datetime.now()
        question=models.CharField(max_length=250,blank=False)
        pub_date=models.DateTimeField(default=now)
        owner=models.ForeignKey(User, on_delete=models.CASCADE)
        
        

        def __str__(self):
                
                return "%s " % (self.question)


        


class choice(models.Model):
    choice_text=models.CharField(max_length=200,blank=True)
    vote=models.IntegerField(default=0)
    question_id=models.ForeignKey(question,on_delete=models.CASCADE)
    
    def __str__(self):
                return "%s" % (self.choice_text)
    
    


class voted_to(models.Model):
        user=models.CharField(max_length=50)
        to_question=models.IntegerField()
        choice_selected=models.IntegerField()
        is_voted=models.BooleanField(default=False)
        def __str__(self):
            return "%s" %(self.choice_selected)
        
        

        