# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from core.models import Speaker, Talk


def homepage(request):
    context = RequestContext(request) 
    return render_to_response('index.html', context)


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    
    ##context = RequestContext(request, {'speaker' : speaker})
    ##return render_to_response('core/speaker_detail.html', context)

    return direct_to_template(request, 'core/speaker_detail.html',
                              {'speaker' : speaker})


def talks(request):
    return direct_to_template(request, 'core/talks.html',
                              {'morning_talks' : Talk.objects.at_morning(),
                               'afternoon_talks' : Talk.objects.at_afternoon(),
                               })


def talk_detail(request, talk_id):
    talk = get_object_or_404(Talk, id=talk_id)
    
    # Fix-me - type hardcored na view
    return direct_to_template(request, 'core/talk_detail.html', {
                              'talk' : talk,
                              'slides': talk.media_set.filter(type="SL"),
                              'videos': talk.media_set.filter(type="YT"),
                            })


