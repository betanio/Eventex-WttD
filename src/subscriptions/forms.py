# -*- coding: utf-8 -*-

from django import forms
from subscriptions.models import Subscription

from django.utils.translation import ugettext_lazy as _

from django.core.validators import EMPTY_VALUES
from subscriptions.validators import CpfValidator


class PhoneWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (
            forms.TextInput(attrs={'size':'2','maxlength':'2'}),
            forms.TextInput(attrs={'size':'15','maxlength':'9'}))
        super(PhoneWidget, self).__init__(widgets, attrs)
        
    def decompress(self, value):
        if not value:
            return [None, None]
        
        return value.split('-')


class PhoneField(forms.MultiValueField):
    widget = PhoneWidget
    
    def __init__(self, *args, **kwargs):
        fields = (
            forms.IntegerField(),
            forms.IntegerField())
        super(PhoneField, self).__init__(fields, *args, **kwargs)
        
    def compress(self, data_list):
        if not data_list:
            return None
        if data_list[0] in EMPTY_VALUES:
            raise forms.ValidationError(u'DDD Inválido.')
        if data_list[1] in EMPTY_VALUES:
            raise forms.ValidationError(u'Número Inválido.')
        
        return '%s-%s' % tuple(data_list)


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        exclude = ('created_at', 'paid',)

    name = forms.CharField(label=_('Nome')),
    cpf = forms.CharField(label=_('CPF'), validators=[CpfValidator])
    email = forms.EmailField(label=_('E-mail'), required=False)
    phone = PhoneField(label=_('Telefone'), required=False)
    
        

    # private method (convention: starts with _ )
    def _unique_check(self, fieldname, error_message):
        param = { fieldname: self.cleaned_data[fieldname] }
        try:
            s = Subscription.objects.get(**param)
        except Subscription.DoesNotExist:
            return self.cleaned_data[fieldname]
        raise forms.ValidationError(error_message)

    def clean_cpf(self):
        return self._unique_check('cpf', _(u'CPF já inscrito.'))

    def clean_email(self):
        return self._unique_check('email', _(u'E-mail já inscrito.'))

    # check -- Fields phone or email
    def clean(self):
        super(SubscriptionForm, self).clean()
        
        if not self.cleaned_data.get('email') and \
           not self.cleaned_data.get('phone'):
            raise forms.ValidationError(
                _(u'Informe seu e-mail ou telefone.'))
            
        return self.cleaned_data



