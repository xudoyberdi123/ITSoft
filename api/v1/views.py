from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.exceptions import NotFound

from sayt.models import Category, Project, Services, Partner

from .services import *


class CategoryView(GenericAPIView):
    permission_classes = (AllowAny, )

    def get(self, requests, *args, **kwargs):
        if 'slug' in kwargs and kwargs['slug']:
            response = get_one(type='category', key="slug", value=kwargs['slug'])
        else:
            response = get_list(requests, 'category')
        return Response(response, status=HTTP_200_OK)


class ProjectView(GenericAPIView):
    def get(self, requests, *args, **kwargs):
        if 'pk' in kwargs and kwargs['pk']:
            response = get_one(type='project', key="id", value=kwargs['pk'])
        elif 'slug' in kwargs and kwargs['slug']:
            response = get_list(requests, 'project')
        else:
            response = get_list(requests, 'project')

        return Response(response, status=HTTP_200_OK)


class PartnerView(GenericAPIView):
    def get(self, requests, *args, **kwargs):
        if 'pk' in kwargs and kwargs['pk']:
            response = get_one(type='partner', key="id", value=kwargs['pk'])
        else:
            response = get_list(requests, 'partner')

        return Response(response, status=HTTP_200_OK)


class ServicesView(GenericAPIView):
    def get(self, requests, *args, **kwargs):
        response = get_services(requests)

        return Response(response, status=HTTP_200_OK)
