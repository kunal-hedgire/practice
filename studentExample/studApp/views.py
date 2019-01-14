from django.shortcuts import render,redirect
from studApp.models import studInfo
from studApp.forms import StudentForm
# Create your views here.

def stud(request):
    if request.method == "POST":
        sform = StudentForm(request.POST)
        #print(sform)
        if sform.is_valid(): #validation
            try:
                sform.save()
                return redirect('/show')
            except:
                raise BaseException
    else:
        sform = StudentForm()
    return render(request,'home.html',{'form':sform})


def show(request):
    studlist = studInfo.objects.all()
    return render(request,"show.html",{'studentlist':studlist})

def showone(request,id):
    studlist=studInfo.objects.get(id=id)
    return render(request,'show.html',{'studentlist':studlist})

def edit(request, id):
    studrecord = studInfo.objects.get(id=id)
    return render(request,'edit.html', {'singleStud':studrecord})


def update(request, id):
    stud = studInfo.objects.get(id=id)
    sform = StudentForm(request.POST, instance = stud)
    print(sform)
    if sform.is_valid():
        sform.save()
        return redirect("/show")
    return render(request, 'edit.html', {'singleStud': stud})

def destroy(request, id):
    stud = studInfo.objects.get(id=id)
    stud.delete()
    return redirect("/show")