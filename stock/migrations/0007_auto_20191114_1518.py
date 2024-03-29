# Generated by Django 2.2.7 on 2019-11-14 08:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_datetimetemplate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datetimetemplate',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 14, 15, 18, 22, 698654)),
        ),
        migrations.AlterField(
            model_name='datetimetemplate',
            name='time',
            field=models.TimeField(default=datetime.datetime(2019, 11, 14, 15, 18, 22, 698654)),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.PositiveIntegerField()),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('create_user', models.TextField()),
                ('edit_time', models.DateTimeField()),
                ('edit_user', models.TextField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Item')),
            ],
        ),
    ]
