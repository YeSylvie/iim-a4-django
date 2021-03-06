# Generated by Django 3.1.7 on 2021-03-11 09:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadCvFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv_name', models.CharField(blank=True, max_length=255)),
                ('cv_file', models.FileField(upload_to='documents/cv/')),
                ('uploaded_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
