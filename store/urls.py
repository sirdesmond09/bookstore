from django.conf.urls import include, url
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'bookstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name = 'index'),
    url(r'^store/', views.store, name = 'store')
]
