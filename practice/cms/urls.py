from django.conf.urls import url
from cms import views

urlpatterns=[
    url(r'^user/$', views.user_list, name='user_list'),
    url(r'^user/add/$', views.user_edit, name='user_add'),
    url(r'^user/mod/(?P<user_id>\d+)/$', views.user_edit, name='user_mod'),
    url(r'^user/del/(?P<user_id>\d+)/$', views.user_del, name='user_del'),
]