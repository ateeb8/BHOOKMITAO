# Generated by Django 4.1.5 on 2023-05-02 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foodwaste', '0004_donation_donationcontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaname', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=300, null=True)),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='donation',
            name='volunteerremark',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=300, null=True)),
                ('userpic', models.FileField(null=True, upload_to='')),
                ('idpic', models.FileField(null=True, upload_to='')),
                ('aboutme', models.CharField(max_length=300, null=True)),
                ('status', models.CharField(max_length=50, null=True)),
                ('regdate', models.DateTimeField(auto_now_add=True)),
                ('adminremark', models.CharField(max_length=300, null=True)),
                ('updationdate', models.DateField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='donation',
            name='donationarea',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodwaste.donationarea'),
        ),
        migrations.AddField(
            model_name='donation',
            name='volunteer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodwaste.volunteer'),
        ),
    ]