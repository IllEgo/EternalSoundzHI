from django.db import models


class LightPackage(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='light_package_images/', default='default_light_package_image.jpg')


class SoundPackage(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='sound_package_images/', default='default_sound_package_image.jpg')


class AddOn(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='addon_package_images/', default='default_addon_package_image.jpg')


class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    event_start = models.DateTimeField(null=True, blank=True)
    event_end = models.DateTimeField(null=True, blank=True)
    event_location = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255)
    sound_package = models.ForeignKey(SoundPackage, on_delete=models.PROTECT)
    light_package = models.ForeignKey(LightPackage, on_delete=models.PROTECT)
    event_details = models.TextField()
    add_ons = models.ManyToManyField(AddOn, blank=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Calculate the total price based on the selected packages and add-ons
        total_price = self.sound_package.price + self.light_package.price
        for add_on in self.add_ons.all():
            total_price += add_on.price
        self.total_price = total_price
        super(Booking, self).save(*args, **kwargs)