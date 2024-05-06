from django.shortcuts import render
from django.http import request
from .models import Epic
from django.contrib import messages


# Create your views here.
def home(request):


    return render(request,'home.html')


def verify(request,**kwargs):

    epic_no=request.GET['epicstr']
    epic=Epic.objects.filter(epic=epic_no).values('pk', 'epic', 'date', 'manufacturerName', 'manufacturerRegistration','batchNo','monthYear_manufacture')
    print(epic)
    if not epic:

        return render(request, 'error.html', {'result': "Not Found"})
    else:
        return render(request,'result.html',{'epic':epic})


