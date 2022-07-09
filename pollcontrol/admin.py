from django.contrib import admin
from .models import PollOwner

# Register your models here.


class PollList(admin.ModelAdmin):
    list_display=('id','user','own_question')



admin.site.register(PollOwner,PollList)