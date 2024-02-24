from django.contrib import admin
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):  # Это позволит добавлять и редактировать ответы прямо на странице вопроса
    model = Choice
    extra = 3  # Количество пустых полей для вариантов ответов

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

