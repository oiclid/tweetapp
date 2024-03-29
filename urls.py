from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    ( r'^resources/(?P<path>.*)$', 
      'django.views.static.serve', 
      { 'document_root': settings.MEDIA_ROOT } ),
    ( r'^twitterPanel/', include( 'twitterPanel.urls' ) ),
)
