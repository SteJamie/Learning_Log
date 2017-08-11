# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 22:01:34 2017

@author: Manu
"""



""" Defines URL patterns for users """

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views


urlpatterns = [
                # Login page
                url(r'^login/$', login, {'template_name': 'users/login.html'},
                    name='login'),
                # Logout page
                url(r'^logout/$', views.logout_view, name='logout'),
                # Registration page
                url(r'^register/$', views.register, name='register'),
              ]