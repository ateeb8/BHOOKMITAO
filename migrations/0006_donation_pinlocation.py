# Generated by Django 4.1.5 on 2023-07-02 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodwaste', '0005_donationarea_donation_volunteerremark_volunteer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='pinlocation',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
