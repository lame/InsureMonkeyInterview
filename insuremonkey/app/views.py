from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


class MainView(View):

    def get(self, request):
        """
        return a list of all users
        """
        # <view logic>
        return HttpResponse('Get World')

    def options(self, request):
        """
        query a username for all addresses
        """

        return HttpResponse('Options World')

    def post(self, request):
        """
        create a new user with addresses
        """

        return HttpResponse('Post World')
