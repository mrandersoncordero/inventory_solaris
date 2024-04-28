# Generated by Django 5.0.4 on 2024-04-28 14:14

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fabrict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last updated', verbose_name='updated')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='El número de teléfono debe introducirse en el formato: +9999999. Hasta 15 dígitos permitidos', regex='\\+?1?\\d{9,15}$')])),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['-created', '-updated'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last updated', verbose_name='updated')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('color', models.CharField(max_length=50)),
                ('size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL')], default='S', max_length=4)),
                ('gender', models.CharField(choices=[('M', 'Maculino'), ('F', 'Femenino')], default='Maculino', max_length=1)),
                ('quantity', models.BigIntegerField()),
                ('unit_price', models.FloatField()),
                ('price_sale_dolar', models.FloatField()),
                ('price_sale_bs', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='products.category')),
                ('fabric', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='products.fabrict')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='products.provider')),
            ],
            options={
                'ordering': ['-created', '-updated'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
