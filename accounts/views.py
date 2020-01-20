from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, Group
from articles.models import Article
from rest_framework import viewsets
from accounts.serializers import UserSerializer, GroupSerializer, ArticleSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
	#Api endpoint that allows users to be viewed or edited
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class ArticleViewSet(viewsets.ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)#validate
		if form.is_valid():
			user = form.save()
			login(request, user)
			# log the user in
			return redirect('articles:article_list')
	else:
		form = UserCreationForm()

	return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		# print(request.POST)
		if form.is_valid():
			#log in the user
			user = form.get_user()
			login(request, user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:
				return redirect('articles:article_list')
	else:
		form = AuthenticationForm()

	return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('articles:article_list')

