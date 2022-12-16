
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_project.common.urls')),
    path('profile/', include('web_project.accounts.urls')),
    path('events/', include('web_project.events.urls')),
    path('featured/', include('web_project.techreview.urls'))
    # re_path(),
]

handler404 = 'web_project.common.views.handler404'
handler500 = 'web_project.common.views.handler404'