# Generated by Django 4.1.4 on 2023-01-05 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Referenc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=999, verbose_name='عنوان')),
                ('referenc_page', models.CharField(max_length=999, verbose_name='آدرس منبع')),
            ],
            options={
                'verbose_name': 'Referenc',
                'verbose_name_plural': 'References',
            },
        ),
    ]