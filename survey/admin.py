from django.contrib import admin
from survey.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [('Question Statement', {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pup_date'], 'classes': ['collapse']})]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pup_date')
    list_filter = ['pup_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
