# Generated by Django 3.1.7 on 2021-02-26 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=100.0, max_digits=20)),
            ],
        ),
    ]
