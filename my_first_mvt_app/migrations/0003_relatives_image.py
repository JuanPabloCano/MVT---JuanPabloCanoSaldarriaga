# Generated by Django 4.0.4 on 2022-05-02 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_mvt_app', '0002_relatives_family_relationship'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatives',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]