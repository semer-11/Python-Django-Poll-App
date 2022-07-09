from django.contrib import admin
from .models import question,choice, voted_to

# Register your models here.



class question_admin(admin.ModelAdmin):
        list_display=('id','question','pub_date','owner')


class choice_admin(admin.ModelAdmin):
    list_display=('id','choice_text','vote','question_id')


class voted_list(admin.ModelAdmin):
    list_display=('id','user','to_question','choice_selected','is_voted')



admin.site.register(question,question_admin)
admin.site.register(choice,choice_admin)
admin.site.register(voted_to,voted_list)
