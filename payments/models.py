from django.db import models

from django.utils.translation import gettext_lazy as _
from utils.validators import validate_phone_number 
from utils.validators import validate_sku

class Gateway(models.Model):
    title= models.CharField(_('title'), max_length=150)
    sku=models.CharField(_('stock keeping unit'), max_length=20, validators=[validate_sku])
    description= models.TextField(_('description'), blank=True)
    avatar= models.ImageField(_('avatar'), blank=True, upload_to='getways/')
    is_enable= models.BooleanField(_('is enable'), default=True)
    credentials= models.TextField(_('credentials'), blank=True)
    created_time= models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time= models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table= 'gateways'
        verbose_name= _('Gateway')
        verbose_name_plural= _('Gateways')

class Payment (models.Model):
    STATUS_VOID= 0  
    STATUS_PAID= 10 
    STATUS_ERROR= 20
    STATUS_CANCELED= 30
    STATUS_REFUNDED= 31
    STATUS_CHOICES= (
                ( STATUS_VOID, _('Void')  ),
                ( STATUS_PAID, _('Paid')  ), 
                ( STATUS_ERROR, _('Error') ),
                ( STATUS_CANCELED, _('User Canceled') ),
                ( STATUS_REFUNDED, _('Refunded') ),
                  ) 
    STATUS_TRANSLATION = {
                 STATUS_VOID, _('Payment could not be processed.') ,
                 STATUS_PAID, _('Payment Succssesful.') , 
                 STATUS_ERROR, _('Payment has encountered an error.Our technical team will check the') ,
                 STATUS_CANCELED, _('Payment canceled by user.') ,
                 STATUS_REFUNDED, _('This payment has been Refunded.') ,         
                       }   
    user= models.ForeignKey('users.User', verbose_name=_('user'), related_name='%(class)s', on_delete=models.CASCADE)
    package= models.ForeignKey('subscriptions.Package', verbose_name= _('package'), related_name='%(class)s', on_delete=models.CASCADE)
    gateway= models.ForeignKey(Gateway, verbose_name=_('gateway'), related_name='%(class)s', on_delete=models.CASCADE)
    price= models.PositiveIntegerField(_('price'),default=0)
    status= models.PositiveSmallIntegerField(_('status'), choices=STATUS_CHOICES, default=STATUS_VOID, db_index=True)
    device_uuid= models.CharField(_('device uuid'),max_length=40, blank=True)
    token= models.CharField(max_length=100)
    phone_number= models.BigIntegerField(_('phone number'), validators=[validate_phone_number],db_index=True)
    consumed_code= models.PositiveIntegerField(_('consumed refrence code'), null=True, db_index=True)
    created_time= models.DateTimeField(_('created time'), auto_now_add=True, db_index=True)
    update_time= models.DateTimeField(_('update time'), auto_now=True, )

    class Meta:
        db_table= 'payments'
        verbose_name= _('Payment')
        verbose_name_plural= _('Payments')