from django.db import models
from django.core.mail import EmailMultiAlternatives
from shop.models import Settings
from django.template.loader import render_to_string
from cart.models import Cart
from user.models import User
from checkout.models import City,Departament
from shop.models import Site
from settings import BASE_URL,DOMAIN,PHONES
from django.utils.translation import ugettext_lazy as _

try:
    from settings import EMAIL
except:
    EMAIL = 'info@miracles.digital'

cargo_choices = (
    (0,'Нет'),
    (1,'Да')
)

class Order(models.Model):
    delivery_choices = (
        (1,_('Новая почта')),
        (2,_('Деливери')),
        (3,_('УкрПочта')),
        (4,_('Самовывоз')),
        (5,_('Курьерская Доставка'))
    )
    payment_choices = (
        (1,_('Наличными при получении')),
        (2,_('Приват 24'))
    )
    status_choices = (
        (1,'Новый'),
        (2,'Оплачен'),
        (11,'Liqpay Оплачен'),
        (3,'Отменен'),
        (10,'Ждем товар'),
        (9,'Опл. ждем'),
        (7,'На отправку'),
        (8,'Отправлен'),
        (4,'Нет связи'),
        (5,'Liqpay'),
        (6,'Закрыт')
    )
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Имя",max_length=80,null=True)
    lname = models.CharField(max_length=255,verbose_name='Фамилия',null=True)
    sname = models.CharField(max_length=255,verbose_name='Отчество',null=True)
    email = models.CharField(max_length=50,verbose_name="Email",null=True)
    phone = models.CharField(max_length=16,verbose_name="Телефон",null=True)
    cart = models.ForeignKey(Cart,verbose_name='Корзина', on_delete=models.CASCADE)
    delivery_type = models.PositiveIntegerField(choices=delivery_choices,default=4,verbose_name='Способ доставки')
    city = models.ForeignKey(City,verbose_name='Город',null=True, on_delete=models.SET_NULL)
    departament = models.ForeignKey(Departament,verbose_name='Отделение',null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=255,verbose_name='Адрес',null=True)
    payment_type = models.PositiveIntegerField(choices=payment_choices,verbose_name='Способ оплаты',default=1)
    status = models.PositiveIntegerField(choices=status_choices,verbose_name='Статус заказа',default=1)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата добавления')
    ttn_created_date = models.DateTimeField(null=True,verbose_name='Дата отправки')
    comment = models.CharField(max_length=1000,null=True,verbose_name='Комментарий к заказу')
    link = models.CharField(max_length=255,null=True,blank=True,verbose_name='TTH URL')
    ttn = models.CharField(max_length=255,null=True,blank=True,verbose_name='TTH Number')
    # SpecialCargo = models.BooleanField(choices=cargo_choices,default=0,verbose_name='Спецгруз?')

    @property
    def total(self):
        return self.cart.total

    def dict(self):
        return {'id':self.id,'status':self.status,'total':self.cart.total,
                'items_qty':self.cart.items_qty,
                'images':[ + item.product.image.cart_thumb for item in self.cart.items.all()]}

    def detail(self):
        return {'id':self.id,'total':self.cart.total,
                'items_qty':self.cart.items_qty,'name':self.name,'lname':self.lname,
                'sname':self.sname,'phone':self.phone,'email':self.email,'payment_type':self.payment_type,
                'delivery_type':self.delivery_type,
                'city':self.city.id if self.city else None,
                'departament':self.departament.id if self.departament else None,
                'address':self.address,'ttn':self.ttn,
                'cart':[item.dict() for item in self.cart.items.all()],'discount':self.cart.discount}

    def init_form(self,data):
        fields = ['name','lname','sname','payment_type','delivery_type','city','departament','address']

        for field in fields:
            if data.get(field) is None:
                data[field] = getattr(self,field)

        return data

    @property
    def full_name(self):
        return "%s %s %s" % (self.name or '',self.lname or '',self.sname or '')

    @property
    def db(self):
        return self._state.db

    def __lt__(self,other):
        return self.created_at < other.created_at

    @property
    def status_display(self):
        return dict(self.status_choices)[self.status]

    def items(self):
        return list(self.cart)

    def send_mail(self,language='ua'):
        context = {}
        to = self.email
        email = 'mail@%s' % BASE_URL
        add_email = EMAIL
        subject = _('Информация по заказу №%s') % self.id
        from_email = _("{} Интернет магазин <{}>").format(BASE_URL,email)
        context['logo'] = 'http://%s/static/image/logo.png' % BASE_URL
        context['domain'] = BASE_URL
        context['order'] = self
        context['lang'] = language
        context['PHONES'] = PHONES
        text_content,html_content = render_to_string('checkout/message.txt'),render_to_string('checkout/message.html',context)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to,add_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказ'
        ordering = ['-created_at']

    def __str__(self):
        return "№ "+str(self.id)

class Seat(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='seats')
    weight = models.FloatField(verbose_name="Вес")
    volumetricHeight = models.PositiveIntegerField(verbose_name="Высота")
    volumetricWidth = models.PositiveIntegerField(verbose_name="Ширина")
    volumetricLength = models.PositiveIntegerField(verbose_name="Длина")
    cost = models.FloatField(verbose_name="Оценочная стоимость")
    description = models.CharField(max_length=255,verbose_name="Описание")
    specialCargo = models.BooleanField(choices=cargo_choices,default=1)

    def dict(self):
        return {
            'weight':self.weight,
            'volumetricHeight':self.volumetricHeight,
            'volumetricWidth':self.volumetricWidth,
            'volumetricLength':self.volumetricLength,
            'cost':self.cost,
            'description':self.description,
            'specialCargo':self.specialCargo
        }

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Место'