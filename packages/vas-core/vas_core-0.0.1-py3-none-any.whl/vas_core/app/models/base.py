from django.conf import settings
from django.db import models
from safedelete.models import SafeDeleteModel


class BaseModelAbstract(SafeDeleteModel):
    old_id = models.CharField(null=True, blank=True, max_length=100)
    createdBy = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL,
                                  blank=True, null=True)
    
    deleted = models.BooleanField(default=False)
    deletedById = models.UUIDField(blank=True, null=True)
    
    deletedAt = models.DateTimeField(db_column='deletedAt', blank=True,
                                     null=True)
    createdAt = models.DateTimeField(db_column='createdAt',
                                     auto_now_add=True)
    updatedAt = models.DateTimeField(db_column='updatedAt', auto_now=True)
    
    class Meta:
        abstract = True
        ordering = ('-createdAt', )

    def delete(self, by=None, force_policy=None, **kwargs):
        self.deletedBy = by
        self.deleted = True
        super(BaseModelAbstract, self).delete(force_policy, **kwargs)

    def undelete(self, force_policy=None, **kwargs):
        self.deletedBy = None
        self.deleted = False
        super(BaseModelAbstract, self).undelete(force_policy, **kwargs)

    def to_redis(self) -> str:
        raise NotImplemented()


class LocalizationField(models.JSONField):
    def __init__(
            self,
            verbose_name=None,
            name=None,
            encoder=None,
            decoder=None,
            **kwargs,
    ):
        super(LocalizationField, self).__init__(verbose_name=verbose_name,
                                                name=name, encoder=encoder,
                                                decoder=decoder, null=False,
                                                blank=False)
