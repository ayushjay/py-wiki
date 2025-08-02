from django.urls import path

from . import views

urlpatterns = [path("", views.index, name="index"),
               path("wiki/<str:title>/", views.entry_page, name="entry_page"),

               
               path("trial/<str:name>", views.trial_page,name="trial_mine"),
               
]


