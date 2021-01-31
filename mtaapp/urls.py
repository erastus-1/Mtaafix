from django.conf.urls import url,include
from . import views



urlpatterns = [
        url('^$',views.home,name='home'),
        url('hoods', views.all_hoods, name='hoods'),
        url('business/view',views.display_business,name = 'viewbiz'),
        url('business/',views.create_business,name = 'business'),
        url('accounts/', include('registration.backends.simple.urls')),
        url('profile/create/',views.create_profile,name = 'profile'),
        url('showprofile/(?P<id>\d+)', views.display_profile, name='showprofile'),
        url('new/post$', views.new_post, name='newpost'),
        url('join/(\d+)', views.join, name='joinHood'),
        url('createHood/$', views.createHood, name='createHood'),
        url('comment/(?P<post_id>\d+)', views.comment, name='comment'),
        url('search/$', views.search, name='search'),

]