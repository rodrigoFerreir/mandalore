from . import models, BaseClassModel, EntityCategory


class Entity(BaseClassModel):
    name = models.CharField(max_length=200)
    cpf_cnpj = models.CharField(max_length=22, unique=True)
    category = models.OneToOneField(EntityCategory, on_delete=models.PROTECT)

    class Meta:
        db_table = 'entities'
        verbose_name = 'Entity'
        verbose_name_plural = 'Entities'

    def __str__(self):
        return self.name
