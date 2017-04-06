from django.db import models

class Site(models.Model):
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100*4, editable=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               related_name='children', null=True, blank=True)

    def __str__(self):
        return self.full_name

    # build the full_name field recursively
    def _get_full_name(self):
        if self.parent:
            return '%s / %s' % (self.parent, self.name)
        return self.name

    # when saving, update the full_name field on ourself and all children
    def save(self, *args, **kwargs):
        update_children = False
        full_name = self._get_full_name()
        if self.full_name is not full_name:
            update_children = True
            self.full_name = self._get_full_name()
        super(Site, self).save(*args, **kwargs)
        if update_children:
            for child in self.children.all():
                child.save(update_fields=['full_name'])

    class Meta:
        unique_together = ('name', 'parent')
        ordering = ('full_name',)
