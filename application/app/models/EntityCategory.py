from . import models, BaseClassModel


class EntityCategory(BaseClassModel):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'entity_categories'
        verbose_name = 'EntityCategory'
        verbose_name_plural = 'EntityCategories'

    def __str__(self):
        return self.name
