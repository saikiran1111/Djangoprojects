from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate

from Mysite.website.forms import SignUpForm
 
from django.contrib import messages

from django.contrib.contenttypes.fields import GenericRelation







from django.core.files.storage import FileSystemStorage

"""@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was updated successfully!')  # <-
            return redirect('settings:password')
        else:
            messages.warning(request, 'Please correct the error below.')  # <-
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'profiles/change_password.html', {'form': form})
"""# Create your views here.

def home(request):
	return render(request,'home.html')


def signup(request):	
	if request.method=='POST':
		form=SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)	
			return redirect('home')
	else:
			form=SignUpForm()
	return render(request,'registration/signup.html',{
		'form':form
		})

def upload(request):
	context={}
	if request.method=='POST':
		upload_file=request.FILES['document']
		fs=FileSystemStorage()
		name=fs.save(upload_file.name,upload_file)
		context['url']=fs.url(name)
	return render(request,'upload.html',context)
	
    



