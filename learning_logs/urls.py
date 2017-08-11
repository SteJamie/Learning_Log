# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 12:44:39 2017

@author: Manu
"""



"""Defines URL patterns for learning_logs."""

from django.conf.urls import url

from . import views


urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    # Show all topics
    url(r'^topics/$', views.topics, name='topics'),
    # Detail page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # Page for adding a new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # Page for deleting a topic
    url(r'^del_topic/$', views.del_topic, name='del_topic'),
    # Page for adding a new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # Page for editing an entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
        name='edit_entry'),
              ]