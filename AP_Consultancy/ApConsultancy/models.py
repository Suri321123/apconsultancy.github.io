from django.db import models

jobCategories = (
    ('Management', 'Management'),
    ('Software', 'Software'),
    ('BPO', 'BPO'),)

class RegisterUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    mobile = models.IntegerField()
    dob = models.DateField()
    job=models.CharField(max_length=25, choices=jobCategories, blank=False, default='Select')

    class Meta:
        unique_together = (('email', 'job'),)

    def __str__(self):
        return self.name
