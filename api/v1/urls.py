from django.urls import path
from .views import *

urlpatterns = [
    path('ctg/', CategoryView.as_view(), name='ctg_list'),
    path('ctg/<slug>/', CategoryView.as_view(), name='ctg_one'),

    path('projects/', ProjectView.as_view(), name='project_list'),
    path('projects/s/<slug>/', ProjectView.as_view(), name='project_list_by_ctg'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_one'),

    path('partner/', PartnerView.as_view(), name='partner_list'),
    path('partner/<int:pk>/', PartnerView.as_view(), name='partner_one'),

    path('services/', ServicesView.as_view(), name='services_list'),
]


