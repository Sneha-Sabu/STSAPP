from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm
from .models import *
from .filters import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from django.contrib import messages
from .decorators import unauthenticated_user, allowed_users, admin_only


# Create your views here.
@login_required(login_url='login')
@admin_only
def home(request):
    user = User.objects.all()
    locations = Locations.objects.all()
    entry = Entry.objects.all()

    total_users = user.count()
    total_locations = entry.count()

    context = {'user': user, 'locations': locations, 'entry': entry, 'total_users': total_users,
               'total_locations': total_locations}
    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')

def locations(request):
    entry = Entry.objects.all()
    entryFilter = EntryFilter(request.GET, queryset=entry)
    entry = entryFilter.qs
    context = {'entry': entry, 'entryFilter': entryFilter}
    return render(request, 'accounts/locations.html', context)

@login_required(login_url='login')

def viewlocations(request, pk):
    entry = Entry.objects.get(id=pk)
    context = {'entry': entry}
    return render(request, 'accounts/viewlocations.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def users(request):
    user = User.objects.all()
    myFilter = UserFilter(request.GET, queryset=user)
    user = myFilter.qs
    context = {'user': user, 'myFilter': myFilter}
    return render(request, 'accounts/users.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createUsers(request):
    context = {}
    return render(request, 'accounts/users.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createLocations(request):
    context = {}
    return render(request, 'accounts/locations.html', context)


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='users')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)
            return redirect('/login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='login')

def userProfile(request):
    user = User.objects.all()
    context = {'user' :user }
    return render(request, 'accounts/user_profile.html', context)






