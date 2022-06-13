# Generated by Django 4.0.3 on 2022-04-07 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_task_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='pay',
            field=models.CharField(default='SOME STRING', max_length=50, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='task',
            name='image',
            field=models.ImageField(blank=True, upload_to='image/'),
        ),
    ]