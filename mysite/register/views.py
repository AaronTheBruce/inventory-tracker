from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
def sign_up(_res):
  if(_res.method == 'POST'):
    form = RegisterForm(response.POST)
    if form.is_valid():
      form.save()

    return redirect('/home')
  else:
    form = RegisterForm()
  return render(_res, 'register/register.html', {'form': form})
