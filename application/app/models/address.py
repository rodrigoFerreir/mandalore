from . import models, BaseClassModel, Entity


class Address(BaseClassModel):
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    complement = models.CharField(max_length=255, null=True, blank=True)
    neighborhood = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    entity = models.ForeignKey(Entity, on_delete=models.SET_NULL, null=True, blank=True, related_name='address')

    class Meta:
        db_table = 'adresses'
        verbose_name = 'Adress'
        verbose_name_plural = 'Adresses'

    def __str__(self):
        return f'{self.number}, {self.street}, {self.neighborhood}, {self.city}'
