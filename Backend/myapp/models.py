from djongo import models


class Image(models.Model):
    _id = models.ObjectIdField()
    imageData = models.CharField(max_length=65535)
    filename = models.CharField(max_length=255)

    class Meta:
        db_table = 'IMAGE'


class Address(models.Model):
    _id = models.ObjectIdField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=20)
    floor = models.IntegerField(null=True, blank=True)


class Property(models.Model):
    ad_type_choices = [
        ('sale', 'Sale'),
        ('rent', 'Rent'),
        ('sold', 'Sold'),
    ]

    type_choices = [
        ('room', 'Room'),
        ('flat', 'Flat'),
        ('house', 'House'),
    ]

    description = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=5, choices=type_choices)
    adType = models.CharField(max_length=5, choices=ad_type_choices)
    userId = models.CharField(max_length=255)
    price = models.IntegerField()
    rooms = models.IntegerField()
    creationDate = models.DateTimeField()
    address = models.EmbeddedField(model_container=Address)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, db_column='imageId')

    class Meta:
        db_table = 'PROPERTY'
