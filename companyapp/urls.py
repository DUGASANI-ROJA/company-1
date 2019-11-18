from django.conf.urls import url

from .import views


app_name = 'companyapp'
urlpatterns = [
    url(r'^$', views.home_page, name="home_page"),

    url(r'^company_registration/$', views.company_registration, name="company_registration"),
    url(r'^emp_registration/$', views.emp_registration, name="cmp_registration"),
    url(r'^com_login/$', views.com_login, name="com_login"),
    url(r'^count/$', views.count, name="count"),
    url(r'^(?P<company_designation>\w+)/count_list/$', views.count_list, name="count_list"),
    url(r'^details/(?P<company_id>[0-9]+)/$', views.details, name="details"),

]
