from django.shortcuts import render, redirect
from .models import SophomoreDeadlines, SophomoreSubjects

def index(request):
    Days = SophomoreDeadlines.objects.order_by('id') 
    Subjects = SophomoreSubjects.objects.order_by('day')
    emptyDays=[]
    for d in Days:
        isDayFull = False
        for s in Subjects:
            if s.day.day == d.day:
                isDayFull = True
        if isDayFull == False:
            emptyDays.append(d.day)
        else:
            emptyDays.append(1) 

    allDays = zip(Days, emptyDays)
                 
    
    context = {'Subjects' : Subjects, 'allDays': allDays}
    return render(request, 'IUTDeadlines/index.html', context)


