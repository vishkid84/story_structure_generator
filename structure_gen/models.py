from django.db import models

class Story(models.Model):

    class Meta:
        verbose_name_plural = 'Stories'

    name = models.CharField(max_length=254)
    overview = models.TextField(null=True, blank=True,)
    structure_one = models.TextField(null=True, blank=True)
    structure_two = models.TextField(null=True, blank=True)
    structure_three = models.TextField(null=True, blank=True)
    structure_four = models.TextField(null=True, blank=True,)
    structure_five = models.TextField(null=True, blank=True)
    structure_five = models.TextField(null=True, blank=True)
    example_one = models.TextField(null=True, blank=True)
    example_two = models.TextField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
