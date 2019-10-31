from django.urls import path
from . import views

# importing all views from review application

urlpatterns = [
    path('', views.index, name='index'), # 127.0.0.1.. will be redirected to views.index, name: url to identify the view
    path('sci_fi', views.sci_fi, name='sci_fi'),
    path('children', views.children, name='children'),
    path('mystery', views.mystery,  name='mystery'),
    path('horror', views.horror,  name='horror'),
    path('new', views.new, name='new'),
    path('browse', views.browse, name='browse'),
    path('<int:pk>/edit', views.rev_edit, name='rev_'),
    path('<int:pk>', views.rev_detail, name='rev_detail'), # used to return a page with review when title clicked
          #  <int:pk> – Django expects an integer value and will transfer it to a view as a variable called pk.
]

# assigning view index to root URL.  This tells Django that the views.index is were to direct anyone that goes to
# 127.0.0.1:8000/
# here is where i would add another webpage/view
# name = 'index' is the name of the URL to identify the view.

