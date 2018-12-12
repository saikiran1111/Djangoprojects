

from django.contrib import admin
from django.urls import path,include



from django.views.generic import *
from django.views.generic import *

from django.conf import settings

from django.conf.urls.static import static

from Mysite.website import views


import django.contrib.auth  



urlpatterns = [
	#path('',views.home,name='home'),
	path('',views.home,name='home'),
	
	path('signup/',views.signup,name='signup'),
	path('upload/',views.upload,name='upload'),
	path('accounts/',include('django.contrib.auth.urls')),
	path('oauth/', include('social_django.urls', namespace='social')),  # <--
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
	urlpatterns== static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



