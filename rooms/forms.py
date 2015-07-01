from django import forms

import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.forms import MultiWidget
from django.forms import extras





SEX_CHOICES = (
    ('girl', 'girl only'),
    ('boy', 'boy only'),
    ('mixed', 'boy/girl'),
)


ROOMTYPE_CHOICES = (
    ('living', 'living room'),
    ('bedroom_1', 'master bedroom'),
    ('bedroom_2',  'bedroom'),
    ('bedroom_3',  'small bedroom'),
)

BUILDINGNAME_CHOICES=(
    ('monaco', 'Monaco'),
    ('avelon', 'Avelon Cove'),
    ('mabella', 'Mabella'),
)



class SearchForm_Newport(forms.Form):
    required_css_class = 'required'
    query = forms.CharField(label='test', widget=forms.TextInput(attrs={'size':32}))
    #
    room_type = forms.MultipleChoiceField(
                        choices=ROOMTYPE_CHOICES,
                        required=True,
                        widget=forms.CheckboxSelectMultiple
    )

    building_name = forms.MultipleChoiceField(
                        choices=BUILDINGNAME_CHOICES,
                        required=True,
                        widget=forms.CheckboxSelectMultiple
    )

    start_date = forms.DateField(
                        required=True,
                        widget=forms.extras.SelectDateWidget()
    )

    end_date = forms.DateField(
                        required=False,
                        widget=forms.extras.SelectDateWidget()
    )

    rent = forms.FloatField(min_value=0., max_value=10000.)
    security_deposit = forms.FloatField(min_value=0, max_value=10000.)

    gender = forms.ChoiceField(
                        choices=SEX_CHOICES,
                        required=True,
                        widget=forms.Select
    )


    # _location = 'Newport'
    # def get_location(self):
    #     return self._location
