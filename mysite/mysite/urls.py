"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import hello, current_datetime, hours_ahead,display_meta, contact
from books import views as book_views
from profiles import views as profile_views
from accounts import views as account_views
from links_everywhere.views import get_my_saved_links, get_all_tags_for_url, get_urls_for_tag

urlpatterns = [
    url(r'^$', profile_views.HomePage.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^date/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^meta/$', display_meta),
    url(r'^search/$', book_views.search),
    url(r'^contact/$', contact),
    url(r'^getmyurl/$', get_my_saved_links),
    url(r'^getmytags/$', get_all_tags_for_url),
    url(r'^getrelatedurl/$', get_urls_for_tag),
    url(r'^me$', profile_views.ShowProfile.as_view(), name='show_self'),
    url(r'^me/edit$', profile_views.EditProfile.as_view(), name='edit_self'),
    url(r'^(?P<slug>[\w\-]+)$', profile_views.ShowProfile.as_view(),
        name='show'),
    url(r'^login/$', account_views.LoginView.as_view(), name="login"),
    url(r'^logout/$', account_views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$', account_views.SignUpView.as_view(), name='signup'),
    url(r'^password-change/$', account_views.PasswordChangeView.as_view(),
        name='password-change'),
    url(r'^password-reset/$', account_views.PasswordResetView.as_view(),
        name='password-reset'),
    url(r'^password-reset-done/$', account_views.PasswordResetDoneView.as_view(),
        name='password-reset-done'),
    url(r'^password-reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$$', account_views.PasswordResetConfirmView.as_view(),  # NOQA
        name='password-reset-confirm'),


]
