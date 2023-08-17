from . import models, BaseClassModel, Entity


class Contact(BaseClassModel):
    email = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=255)
    entity = models.ForeignKey(Entity, on_delete=models.SET_NULL, null=True, blank=True, related_name="contact")

    class Meta:
        db_table = 'contacts'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.email
