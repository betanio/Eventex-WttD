
from django.conf.urls.defaults import patterns, url

## from views import talks
## from views import talk_detail
## from views import speaker_detail


urlpatterns = patterns('core.views',
    # Examples:
    # url(r'^$', 'src.views.home', name='home'),
    # url(r'^src/', include('src.foo.urls')),

    url(r'^palestras/$', 'talks', name='talks'),
    url(r'^palestras/(\d+)/$', 'talk_detail', name='talk_detail'),
    url(r'^palestrante/([-\w]+)/$', 'speaker_detail', name='speaker_detail'),
)


