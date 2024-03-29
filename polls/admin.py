from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Statement',{'fields':['question_text']}),
        ('Date imformation',{'fields':['pub_date'],'classes':['collapse']})
    ]
    inlines = [ChoiceInline]

    list_filter = ['pub_date']

    search_fields = ['question_text']
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
