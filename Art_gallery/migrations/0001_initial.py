# Generated by Django 4.0.6 on 2022-10-15 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='artgallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(default=None, max_length=500, null=True, upload_to='art_gallery/')),
                ('info', models.CharField(max_length=100)),
            ],
        ),
    ]
