from django.urls import path
from django.contrib import admin
from curdapp import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'curdpro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('admin/', admin.site.urls),
    path('',views.main_page),
    path('insert',views.inserting_view),
    path('retrieve',views.retrieving_view),
    path('update',views.update_view),
    path('delete',views.delete_view)

]
