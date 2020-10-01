import re

from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views import View
from .models import Equipment_type, Equipment
from .forms import EquipmentForm


# Create your views here.


def create_reg_exp(mask):
    mask = list(mask)
    N = '\d'
    A = '[A-Z]'
    a = '[a-z]'
    X = '([A-Z]|\d)'
    Z = '(\-|\_|\@)'
    result_regexp = '^'
    for char in mask:
        if char == 'N':
            result_regexp = result_regexp + N
        elif char == 'A':
            result_regexp = result_regexp + A
        elif char == 'a':
            result_regexp = result_regexp + a
        elif char == 'X':
            result_regexp = result_regexp + X
        elif char == 'Z':
            result_regexp = result_regexp + Z
    return result_regexp+'+$'


class form(View):

    def get(self, request):
        form = EquipmentForm(request.POST)
        data = {
            'form': form
        }
        return render(request, 'testtaskbackend/form.html', data)

    def post(self, request):
        form = EquipmentForm(request.POST)
        data = {
            'form': form
        }
        if form.is_valid():
            regexp = create_reg_exp(Equipment_type.objects.get(
                name_of_type=form.cleaned_data["code_of_type"]
            ).mask)
            print(re.search(regexp, form.cleaned_data['serial_number']))
            if re.search(regexp, form.cleaned_data['serial_number']):
                equipment = Equipment(serial_number=form.cleaned_data['serial_number'],
                                      code_of_type=Equipment_type.objects.get(
                                          name_of_type=form.cleaned_data['code_of_type']))
                equipment.save()

            else:
                return redirect('/error')
        else:
            raise ValidationError(message="Incorrect")
        return render(request, 'testtaskbackend/form.html', data)

class InvalidSerialNumber(View):

    def get(self, request):
        return render(request, 'testtaskbackend/invalid_serial_nubmer.html')