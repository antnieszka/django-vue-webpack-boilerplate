"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
"""
from django.urls import path, include
from django.contrib import admin
from backend.app.views import index


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("backend.app.urls")),
    path("", index, name="home"),
]
