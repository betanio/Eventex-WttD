src/core/models.py


# Custom Managers

##class PhoneContactManager(models.Manager):
##    def get_query_set(self):
##        qs = super(PhoneContactManager, self).get_query_set()
##        qs = qs.filter(kind='P')
##        return qs
##
##class EmailContactManager(models.Manager):
##    def get_query_set(self):
##        qs = super(EmailContactManager, self).get_query_set()
##        qs = qs.filter(kind='E')
##        return qs
##
##class FaxContactManager(models.Manager):
##    def get_query_set(self):
##        qs = super(FaxContactManager, self).get_query_set()
##        qs = qs.filter(kind='F')
##        return qs

class KindContactManager(models.Manager):
    


class Speaker(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    url = models.URLField(verify_exists=False)
    description = models.TextField(blank=True)
    avatar = models.FileField(upload_to='palestrantes',
                              blank=True, null=True)
    
    def __unicode__(self):
        return self.name


class Contact(models.Model):
    KINDS = (
        ('P', _('Telefone')),
        ('E', _('E-­‐mail')),
        ('F', _('Fax')),
    )
    
    speaker = models.ForeignKey('Speaker', verbose_name=_('Palestrante'))
    kind = models.CharField(max_length=1, choices=KINDS)
    value = models.CharField(max_length=255)

    objects = models.Manager()
    phones = PhoneContactManager()
    emails = EmailContactManager()
    faxes = FaxContactManager()





