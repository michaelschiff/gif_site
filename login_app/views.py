from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):
    if (request.user.is_authenticated()): return HttpResponseRedirect(reverse('gif_app.views.index'))
    return render_to_response('login_app/splash.html')

def login_page(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login_app/login_page.html', c)

def registration(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login_app/registration.html', c)

def login_handler(request):
    alert = "Username and/or Password did not validate."
    user = None
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
    except:
        return render_to_response('login_app/login_page.html', {'msg': alert}, context_instance=RequestContext(request))
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('gif_app.views.index'))
        else:
            return render_to_response('login_app/login_page.html', {'msg': alert}, context_instance=RequestContext(request))
    else:
        return render_to_response('login_app/login_page.html', {'msg': alert}, context_instance=RequestContext(request))

def logout_handler(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_app.views.index'))

def newuser_handler(request):
    try:
        user = User.objects.create_user(username=request.POST['username'],
                                        email="",
                                        password=request.POST['password'])
        user.save()
        return HttpResponseRedirect(reverse('login_app.views.index'))
    except:
        return render_to_response('login_app/registration.html', {'msg': "That Username is already taken. Pick a different one."}, context_instance=RequestContext(request))
