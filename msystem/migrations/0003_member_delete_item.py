# Generated by Django 4.0.4 on 2022-05-16 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msystem', '0002_rename_text_item_address_item_age_item_dswd_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(default='')),
                ('Address', models.TextField(default='')),
                ('Age', models.TextField(default='')),
                ('Dswd', models.TextField(default='')),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
