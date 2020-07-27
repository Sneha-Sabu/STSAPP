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
import time
from django.contrib import messages
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa


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
def Region(request, cats):
    region_locations = Entry.objects.filter(region=cats)
    entryFilter = EntryFilter(request.GET, queryset=region_locations)
    region_locations = entryFilter.qs
    context = {'region_locations': region_locations, 'entryFilter': entryFilter}
    return render(request, 'accounts/region.html', context)


@login_required(login_url='login')
def allRegions(request):

    return render(request, 'accounts/allregions.html')


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
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')  # Get username input first
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        BL = BlackList.objects.values_list('username', flat=True)  # Read all data into array

        usercheck = User.objects.values_list('username', flat=True)

        if username not in usercheck:
            messages.info(request,
                          'Username does not exist. Contact admin zhangbowen0101@gmail.com to create your account.')
            return redirect('/login')

        if username in BL:  # Check if the username is in blacklist
            black_list_user = BlackList.objects.get(username=username)
            usertime = black_list_user.trytologintime
            seconds = time.time() - time.mktime(usertime.timetuple())
            if seconds > 21600: # Admin can change cold time for resetting here
                black_list_user.delete()

                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    black_list_user.flag1 = True
                    black_list_user.save()
                    messages.info(request, 'Your username or password is incorrect. Please double-check and try again.')
                    return redirect('/login')

            elif black_list_user.flag3 is True:
                messages.info(request, 'For security reasons, your account has been locked after three incorrect login attempts. Please email the admin at zhangbowen0101@gmail.com to reset your login credentials.')

            elif black_list_user.flag2 is True:
                if user is not None:
                    black_list_user.delete()
                    login(request, user)
                    return redirect('home')
                else:
                    black_list_user.flag3 = True
                    black_list_user.save()
                    messages.info(request, 'For security reasons, your account has been locked after three incorrect login attempts. Please email the admin at zhangbowen0101@gmail.com to reset your login credentials.')
                    return redirect('/login')
            elif black_list_user.flag1 is True and black_list_user.flag2 is False:
                if user is not None:
                    black_list_user.delete()
                    login(request, user)
                    return redirect('home')
                else:
                    black_list_user.flag2 = True
                    black_list_user.save()
                    messages.info(request, 'Your username or password is incorrect. The maximum retry attempts allowed for login are 3. Please try again with the correct details for the last attempt or email the admin at zhangbowen0101@gmail.com to reset your login credentials.')
                    return redirect('/login')
            else:
                if user is not None:
                    black_list_user.delete()
                    login(request, user)
                    return redirect('home')
                else:
                    black_list_user.flag1 = True
                    black_list_user.save()
                    messages.info(request, 'Your username or password is incorrect. Please double-check and try again.')
                    return redirect('/login')
        else:

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                BlackList.objects.create(username=username, flag1=True, flag2=False, flag3=False)
                messages.info(request, 'Your username or password is incorrect. Please double-check and try again.')
                return redirect('/login')

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


@login_required(login_url='login')
@admin_only
def AuditLogsView(request):
    template_name = "auditlogs.html"
    history = Entry.history.all()
    history2 = BlackList.history.all()
    history3 = User.history.all()
    history4 = Group.history.all()
    context = {'history': history, 'history2': history2, 'history3' :history3, 'history4' :history4}
    return render(request, 'accounts/auditlogs.html', context)

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class Download_auditlogsPDF(View):
    def get(self, request, *args, **kwargs):
        history1 = Entry.history.all()
        history2 = BlackList.history.all()
        history3 = User.history.all()
        history4 = Group.history.all()
        context = {'history1': history1, 'history2': history2, 'history3': history3, 'history4': history4}

        pdf = render_to_pdf('accounts/pdf_auditlogs.html', context)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "auditlogs.pdf"
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response

class DownloadviewlocationsPDF(View):
    def get(self, request, pk, *args, **kwargs):
        entry = Entry.objects.get(id=pk)
        context = {'entry': entry}
        pdf = render_to_pdf('accounts/pdf_viewlocations.html',context)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "location.pdf"
        content = "attachment; filename=%s" % (filename)
        response['Content-Disposition'] = content
        return response


