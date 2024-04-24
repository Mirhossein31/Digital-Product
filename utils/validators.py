from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

class SKUValidator (RegexValidator):
    regex= '^[a-zA-z0-9\-\_]{6,20}$'
    message= 'SKU must be alphanumbric with 6 to 20 characters.'
    code= 'invalid_sku'

class PhoneNumberValidator(RegexValidator) :
    regex= '^98(9[0-3,9]\d{8}|[1-9]\d{9})$' 
    message= 'Phone number must be valid 12 digits kile 98xxxxxxxxxx'
    code= 'invalid_phone_number' 

validate_sku= SKUValidator() 
validate_phone_number= PhoneNumberValidator()   
