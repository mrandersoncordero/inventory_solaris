# Generated by Django 5.0.4 on 2024-05-17 00:50

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
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last updated', verbose_name='updated')),
                ('name', models.CharField(max_length=100)),
                ('laction', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-created', '-updated'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last updated', verbose_name='updated')),
                ('contact', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='El número de teléfono debe introducirse en el formato: +9999999. Hasta 20 dígitos permitidos', regex='\\+?1?\\d{9,15}$')])),
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
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('min_stock', models.PositiveIntegerField(default=0)),
                ('max_stock', models.PositiveIntegerField(default=0)),
                ('unit_measure', models.CharField(default='unit', max_length=50)),
                ('wight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='products.category')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='suppliers', to='products.supplier')),
            ],
            options={
                'ordering': ['-created', '-updated'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=50)),
                ('production_date', models.DateTimeField()),
                ('expiration_date', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batch_products', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last updated', verbose_name='updated')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('notes', models.TextField(blank=True, null=True)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batchs', to='products.batch')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intentories', to='products.inventory')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.product')),
            ],
            options={
                'ordering': ['-created', '-updated'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
