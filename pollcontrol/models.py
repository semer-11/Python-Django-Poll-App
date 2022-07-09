from home.models import question
from django.db import models
from django.contrib.auth.models import User
from home.models import question

# Create your models here.



class PollOwner(models.Model):
    user=models.CharField(max_length=50)
    own_question=models.ForeignKey(question , on_delete=models.CASCADE)
    

    def __str__(self) -> int:
        return "%s own's question %s"% (self.user,self.own_question)