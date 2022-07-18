from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm //remove the since i now use the UserRegisterForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			# messages.success(request, f'Account created for {username}!')
			messages.success(request, f'Your account has been created with username {username}!, You can now login')
			# return redirect('blog-home') //User get redirected to homepage, but it modified so the user gets login to verify
			return redirect('login')


	else:
		form = UserRegisterForm()

	return render(request, 'users/register.html', {'form': form})


