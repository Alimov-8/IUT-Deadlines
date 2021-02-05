from django.contrib import admin

# Register your models here.
from .models import SophomoreDeadlines, SophomoreSubjects, FreshmanSubjects, JuniorSubjects, SeniorSubjects

@admin.register(SophomoreDeadlines)
class SophomoreDeadlinesAdmin(admin.ModelAdmin):
    list_display = ('day', 'year')


@admin.register(SophomoreSubjects)
class SophomoresSubjectsAdmin(admin.ModelAdmin):
    list_display = ('subject', 'deadline', 'location')

@admin.register(FreshmanSubjects)
class FreshmanSubjectsAdmin(admin.ModelAdmin):
    list_display = ('subject', 'deadline', 'location')

@admin.register(JuniorSubjects)
class JuniorSubjectsAdmin(admin.ModelAdmin):
    list_display = ('subject', 'deadline', 'location')

@admin.register(SeniorSubjects)
class SeniorSubjectsAdmin(admin.ModelAdmin):
    list_display = ('subject', 'deadline', 'location')
