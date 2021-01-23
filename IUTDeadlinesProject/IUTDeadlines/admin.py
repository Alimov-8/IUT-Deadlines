from django.contrib import admin

# Register your models here.
from .models import SophomoreDeadlines, SophomoreSubjects

@admin.register(SophomoreDeadlines)
class SophomoreDeadlinesAdmin(admin.ModelAdmin):
    list_display = ('day', 'year')


@admin.register(SophomoreSubjects)
class SophomoresSubjectsAdmin(admin.ModelAdmin):
    list_display = ('subject', 'deadline', 'location')
