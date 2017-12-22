from django.conf.urls import url, include
from django.contrib import admin

from .views import Home, Base, Team, Landingpage
from videos.views import VideoListView
from videos.views import (
    VideoDetailView ,
    VideoCreateView ,
    VideoUpdateView ,
    VideoDeleteView ,
)

from .views import UsercreateView , UserCreateDoneView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UsercreateView.as_view(), name='register'),
    url(r'^accounts/register/done', UserCreateDoneView.as_view(), name='register_done' ),
    url(r'^$', Home.as_view()),
    url(r'^base/$', Base.as_view()),
    url(r'^team/$', Team.as_view()),
    url(r'^videos/$', VideoListView.as_view(), name='videos'),
    url(r'^videos/(?P<pk>\d+)/$', VideoDetailView.as_view(), name='video-detail'),
    url(r'^videos/create/$', VideoCreateView.as_view(), name='video-create'),
    url(r'^videos/(?P<pk>\d+)/update/$', VideoUpdateView.as_view(), name='video-update'),
    url(r'^videos/(?P<pk>\d+)/delete/$', VideoDeleteView.as_view(), name='video-delete'),
    url(r'^index/$', Landingpage.as_view(), name='Landingpage'),
    url(r'^photo/', include('photo.urls', namespace='photo')),
]