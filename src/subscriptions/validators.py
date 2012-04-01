# -*- coding: utf-8 -*-

# Optional: ugettext_lazy
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError

# TODO: validação do dígito verificador
def CpfValidator(value):
    if not value.isdigit():
        raise ValidationError(_(u'O CPF deve conter apenas números'))
    
    if len(value) != 11:
        raise ValidationError(_(u'O CPF deve ter 11 dígitos'))


