from django.urls import path
from django.conf.urls import include,url
from . import views
urlpatterns=[url(r'api/users^$',views.UserCreate.as_view(),name='account-create'),]
urlpatterns = [path('',views.index,name='index'),]
urlpatterns = [path('receipe/',views.receipe_create_listAll),
	       path('receipe//',views.receipe_modify_user),]
