# from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from . import forms, models



def login(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        if len(list(models.User.objects.filter(fbook_auth_id = uid))) != 1:
            models.User.objects.create(fbook_auth_id = uid)
        # access = request.POST['access']
        # request.session['access'] = access
        request.session['uid'] = uid
        return redirect('/home')
    else:
        return render(request, 'snap/index.html')


def main(request):
    return render(request, 'snap/mainpage.html')

def display(request):
    current_user = models.User.objects.get(fbook_auth_id=request.session['uid'])
    caughtlist = models.Catch.objects.filter(user=current_user)
    return render(request,'snap/display.html', { 'caughtlist' : caughtlist})

def catch(request):
    current_user = models.User.objects.get(fbook_auth_id=request.session['uid'])
    if request.method == 'POST':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(current_user.name + str(current_user.pk) + myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        species = models.Animal.objects.get(name=request.form['species'])
        
        models.Catch.create(user=current_user, species=species, notes=request.form['notes'])

        
        form = forms.CatchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/catches")
    else:
        catches = models.Catch.objects.filter(user=current_user)
        return render(request, 'snap/catches.html', {'catches': catches})
