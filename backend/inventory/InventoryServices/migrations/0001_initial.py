# Generated by Django 4.2.14 on 2024-08-01 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('mrp', models.CharField(blank=True, max_length=255, null=True)),
                ('batch_number', models.CharField(blank=True, max_length=255, null=True)),
                ('discount_type', models.CharField(choices=[('AMOUNT', 'AMOUNT'), ('PERCENTAGE', 'PERCENTAGE')], default='FLAT', max_length=255)),
                ('discount_amout', models.FloatField()),
                ('sr_no', models.CharField(blank=True, max_length=255, null=True)),
                ('mfg_date', models.DateTimeField(blank=True, null=True)),
                ('uom', models.CharField(max_length=255)),
                ('ptr', models.CharField(blank=True, max_length=255, null=True)),
                ('received_date', models.DateTimeField(blank=True, null=True)),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
                ('quantity_inwarded', models.IntegerField()),
                ('buy_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sell_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax_percentage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock_status', models.CharField(choices=[('IN_STOCK', 'IN_STOCK'), ('OUT_OF_STOCK', 'OUT_OF_STOCK'), ('DAMAGED', 'DAMAGED'), ('LOST', 'LOST')], default='IN_STOCK', max_length=255)),
                ('inward_type', models.CharField(choices=[('PURCHASE', 'PURCHASE'), ('RETURN', 'RETURN'), ('REPLACEMENT', 'REPLACEMENT'), ('WARHOUSE TRANSFER', 'WARHOUSE TRANSFER')], default='PURCHASE', max_length=255)),
                ('additional_details', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('INWARD', 'INWARD'), ('OUTWARD', 'OUTWARD'), ('DAMAGED', 'DAMAGED'), ('LOST', 'LOST'), ('EXPIRED', 'EXPIRED'), ('RETURNED', 'RETURNED'), ('ADJUSTMENT', 'ADJUSTMENT'), ('WAREHOUSE TRANSFER', 'WAREHOUSE TRANSFER')], default='IN_STOCK', max_length=255)),
                ('additional_details', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RackAndShelvesAndFloor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('rack', models.CharField(blank=True, max_length=255, null=True)),
                ('shelf', models.CharField(blank=True, max_length=255, null=True)),
                ('floor', models.CharField(blank=True, max_length=255, null=True)),
                ('additional_details', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='ACTIVE', max_length=255)),
                ('size', models.CharField(choices=[('SMALL', 'SMALL'), ('MEDIUM', 'MEDIUM'), ('LARGE', 'LARGE')], default='SMALL', max_length=255)),
                ('capacity', models.CharField(choices=[('LOW', 'LOW'), ('MEDIUM', 'MEDIUM'), ('HIGH', 'HIGH')], default='LOW', max_length=255)),
                ('warehouse_type', models.CharField(choices=[('OWNED', 'OWNED'), ('LEASED', 'LEASED')], default='OWNED', max_length=255)),
                ('additional_details', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
