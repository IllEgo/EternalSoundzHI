# Generated by Django 4.2.3 on 2023-07-12 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddOn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('image', models.ImageField(default='default_addon_package_image.jpg', upload_to='addon_package_images/')),
            ],
        ),
        migrations.CreateModel(
            name='LightPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('image', models.ImageField(default='default_light_package_image.jpg', upload_to='light_package_images/')),
            ],
        ),
        migrations.CreateModel(
            name='SoundPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('image', models.ImageField(default='default_sound_package_image.jpg', upload_to='sound_package_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('event_start', models.DateTimeField(blank=True, null=True)),
                ('event_end', models.DateTimeField(blank=True, null=True)),
                ('event_location', models.CharField(max_length=255)),
                ('event_type', models.CharField(max_length=255)),
                ('event_details', models.TextField()),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('add_ons', models.ManyToManyField(blank=True, to='bookings.addon')),
                ('light_package', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookings.lightpackage')),
                ('sound_package', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookings.soundpackage')),
            ],
        ),
    ]
