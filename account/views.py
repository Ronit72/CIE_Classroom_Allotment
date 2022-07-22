from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def login(request):
    if request.method =='POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            return redirect('adminland')
    else:
            form = AuthenticationForm()
    return render(request,'login.html',{'form': form})
