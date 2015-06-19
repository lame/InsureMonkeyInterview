from app.models import Address, User
from django import forms
from django.shortcuts import render, redirect
from django.views.generic import View


class MainView(View):

    def get(self, request):
        """
        return a list of all users
        """
        # <view logic>
        user_address_form = UserAddress()
        get_address_form = GetAddressForUser()

        return render(request, 'index.html', {
                        'users': User.objects.all(),
                        'user_address_form': user_address_form,
                        'get_address_form': get_address_form,
                        'addresses': None
                      })

    def options(self, request):
        """
        query a username for all addresses
        """
        user_address_form = UserAddress()
        get_address_form = GetAddressForUser()
        form = GetAddressForUser(request.OPTIONS)
        print('in options')
        if form.is_valid():
            return render(request, 'index.html', {
                          'users': User.objects.all(),
                          'user_address_form': user_address_form,
                          'get_address_form': get_address_form,
                          'addresses': [x.address for x in Address.objects.filter(user__user=form.cleaned_data['user'])],
                          })

    def post(self, request):
        """
        create a new user with addresses
        """
        form = UserAddress(request.POST)
        if form.is_valid():
            try:
                address = Address()
                fk_user = User.objects.get(user=form.cleaned_data['user'])
                address.user = fk_user
                address.address = form.cleaned_data['address']
                address.save()
            except User.DoesNotExist:
                User(user=form.cleaned_data['user']).save()
                address = Address()
                fk_user = User.objects.get(user=form.cleaned_data['user'])
                address.user = fk_user
                address.address = form.cleaned_data['address']
                address.save()

        return redirect('/')


class GetAddressForUser(forms.Form):
    user = forms.CharField(label='Username', max_length=20)


class UserAddress(forms.Form):
    user = forms.CharField(label='Username', max_length=20)
    address = forms.CharField(label='User Address', max_length=80)
