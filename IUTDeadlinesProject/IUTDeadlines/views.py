from django.shortcuts import render, redirect
from .models import SophomoreDeadlines, SophomoreSubjects, FreshmanSubjects, SeniorSubjects, JuniorSubjects


# Sophomores page
def index(request):
    Days = SophomoreDeadlines.objects.order_by('id')
    Subjects = SophomoreSubjects.objects.order_by('year')
    emptyDays=[]
    for d in Days:
        isDayFull = False
        for s in Subjects:
            if s.year.year == d.year:
                isDayFull = True
        if isDayFull == False:
            emptyDays.append(d.year)
        else:
            emptyDays.append(1)

    allDays = zip(Days, emptyDays)


    context = {'Subjects' : Subjects, 'allDays': allDays}
    return render(request, 'IUTDeadlines/index.html', context)


# Freshman page
def freshman(request):
    Days = SophomoreDeadlines.objects.order_by('id')
    Subjects = FreshmanSubjects.objects.order_by('year')
    emptyDays=[]
    for d in Days:
        isDayFull = False
        for s in Subjects:
            if s.year.year == d.year:
                isDayFull = True
        if isDayFull == False:
            emptyDays.append(d.year)
        else:
            emptyDays.append(1)

    allDays = zip(Days, emptyDays)


    context = {'Subjects' : Subjects, 'allDays': allDays}
    return render(request, 'IUTDeadlines/freshman.html', context)


# Junior page
def junior(request):
    Days = SophomoreDeadlines.objects.order_by('id')
    Subjects = SeniorSubjects.objects.order_by('year')
    emptyDays=[]
    for d in Days:
        isDayFull = False
        for s in Subjects:
            if s.year.year == d.year:
                isDayFull = True
        if isDayFull == False:
            emptyDays.append(d.year)
        else:
            emptyDays.append(1)

    allDays = zip(Days, emptyDays)


    context = {'Subjects' : Subjects, 'allDays': allDays}
    return render(request, 'IUTDeadlines/junior.html', context)


# Senior page
def senior(request):
    Days = SophomoreDeadlines.objects.order_by('id')
    Subjects = SeniorSubjects.objects.order_by('year')
    emptyDays=[]
    for d in Days:
        isDayFull = False
        for s in Subjects:
            if s.year.year == d.year:
                isDayFull = True
        if isDayFull == False:
            emptyDays.append(d.year)
        else:
            emptyDays.append(1)

    allDays = zip(Days, emptyDays)


    context = {'Subjects' : Subjects, 'allDays': allDays}
    return render(request, 'IUTDeadlines/senior.html', context)






