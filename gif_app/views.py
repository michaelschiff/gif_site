from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from django.conf import settings
from gif_app.models import Gif, GifForm
import datetime


def index(request):
    if not request.user.is_authenticated(): return HttpResponseRedirect(reverse('login_app.views.index'))
    gif_list = Gif.objects.all().order_by('-pub_date')
    return render_to_response('gif_app/index.html', {'gif_list': gif_list, 'form': GifForm(), 'user': request.user}, context_instance=RequestContext(request))

def newgif(request):
    if request.method == 'POST':
        request.FILES['file_path'].name = str(len(Gif.objects.all())+1)
        request.POST['user'] = str(request.user.id)
        request.POST['pub_date'] = datetime.datetime.now()
        form = GifForm(request.POST, request.FILES)
        form.save()
    return HttpResponseRedirect(reverse('gif_app.views.index'))
