from django.db import models

class Slide(models.Model):
    title = models.CharField(max_length=140)
    description = models.CharField(blank=True, max_length=140)
    link = models.URLField(blank=False, default='#')
    call_to_action = models.CharField(blank=False, default='View more',max_length=50)
    image = models.ImageField(upload_to='slides', max_length=500, blank=True,null=True)
    published_at = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title