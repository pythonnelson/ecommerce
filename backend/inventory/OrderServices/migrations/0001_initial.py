# Generated by Django 4.2.14 on 2024-08-01 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('po_code', models.CharField(max_length=255)),
                ('po_date', models.DateTimeField()),
                ('expected_delivery_date', models.DateTimeField()),
                ('payment_terms', models.CharField(choices=[('CASH', 'CASH'), ('CREDIT', 'CREDIT'), ('ONLINE', 'ONLINE'), ('CHEQUE', 'CHEQUE')], default='CASH', max_length=255)),
                ('payment_status', models.CharField(choices=[('PAID', 'PAID'), ('UNPAID', 'UNPAID'), ('PARTIAL PAID', 'PARTIAL PAID'), ('CANCELLED', 'CANCELLED')], default='UNPAID', max_length=255)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_type', models.CharField(choices=[('PERCENTAGE', 'PERCENTAGE'), ('AMOUNT', 'AMOUNT')], default='PERCENTAGE', max_length=255)),
                ('shipping_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_type', models.CharField(choices=[('FREE', 'FREE'), ('PAID', 'PAID')], default='FREE', max_length=255)),
                ('shipping_tax_percentage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_cancelled_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_cancelled_tax_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('additional_details', models.JSONField()),
                ('status', models.CharField(choices=[('DRAFT', 'DRAFT'), ('SENT', 'SENT'), ('RECEIVED', 'RECEIVED'), ('PARTIAL RECEIVED', 'PARTIAL RECEIVED'), ('CANCELLED', 'CANCELLED'), ('RETURNED', 'RETURNED')], default='DRAFT', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('approved_at', models.DateTimeField()),
                ('cancelled_at', models.DateTimeField()),
                ('cancelled_reason', models.TextField()),
                ('received_at', models.DateTimeField()),
                ('returned_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrderInwardedLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_path', models.TextField()),
                ('invoice_number', models.CharField(max_length=255)),
                ('notes', models.TextField()),
                ('inwarded_at', models.DateTimeField()),
                ('additional_details', models.JSONField()),
                ('status', models.CharField(choices=[('DRAFT', 'DRAFT'), ('SENT', 'SENT'), ('RECEIVED', 'RECEIVED'), ('PARTIAL RECEIVED', 'PARTIAL RECEIVED'), ('CANCELLED', 'CANCELLED'), ('RETURNED', 'RETURNED')], default='DRAFT', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrderItemInwardedLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('inwarded_quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax_percentage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_type', models.CharField(choices=[('PERCENTAGE', 'PERCENTAGE'), ('AMOUNT', 'AMOUNT')], default='PERCENTAGE', max_length=255)),
                ('shipping_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_tax_percentage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('additional_details', models.JSONField()),
                ('status', models.CharField(choices=[('DRAFT', 'DRAFT'), ('SENT', 'SENT'), ('RECEIVED', 'RECEIVED'), ('PARTIAL RECEIVED', 'PARTIAL RECEIVED'), ('CANCELLED', 'CANCELLED'), ('RETURNED', 'RETURNED')], default='DRAFT', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrderItems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity_ordered', models.IntegerField()),
                ('quantity_received', models.IntegerField()),
                ('quantity_cancelled', models.IntegerField()),
                ('quantity_returned', models.IntegerField()),
                ('buying_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_returned', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_cancelled', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_ordered', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax_percentage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_tax_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_cancelled_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_cancelled_tax_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_type', models.CharField(choices=[('PERCENTAGE', 'PERCENTAGE'), ('AMOUNT', 'AMOUNT')], default='PERCENTAGE', max_length=255)),
                ('additional_details', models.JSONField()),
                ('status', models.CharField(choices=[('DRAFT', 'DRAFT'), ('SENT', 'SENT'), ('RECEIVED', 'RECEIVED'), ('PARTIAL RECEIVED', 'PARTIAL RECEIVED'), ('CANCELLED', 'CANCELLED'), ('RETURNED', 'RETURNED'), ('PARITAL RETURNED', 'PARITAL RETURNED')], default='DRAFT', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('approved_at', models.DateTimeField()),
                ('cancelled_at', models.DateTimeField()),
                ('cancelled_reason', models.TextField()),
                ('received_at', models.DateTimeField()),
                ('returned_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrderLogs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('additional_details', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('so_code', models.CharField(max_length=255)),
                ('so_date', models.DateTimeField()),
                ('expected_delivery_date', models.DateTimeField()),
                ('payment_terms', models.CharField(choices=[('CASH', 'CASH'), ('CREDIT', 'CREDIT'), ('ONLINE', 'ONLINE'), ('CHEQUE', 'CHEQUE')], default='CASH', max_length=255)),
                ('payment_status', models.CharField(choices=[('PAID', 'PAID'), ('UNPAID', 'UNPAID'), ('PARTIAL PAID', 'PARTIAL PAID'), ('CANCELLED', 'CANCELLED')], default='UNPAID', max_length=255)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_type', models.CharField(choices=[('PERCENTAGE', 'PERCENTAGE'), ('AMOUNT', 'AMOUNT')], default='PERCENTAGE', max_length=255)),
                ('shipping_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_type', models.CharField(choices=[('FREE', 'FREE'), ('PAID', 'PAID')], default='FREE', max_length=255)),
                ('shipping_tax_percentage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_cancelled_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_cancelled_tax_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('additional_details', models.JSONField()),
                ('status', models.CharField(choices=[('DRAFT', 'DRAFT'), ('SENT', 'SENT'), ('DELIVERED', 'DELIVERED'), ('PARTIAL DELIVERED', 'PARTIAL DELIVERED'), ('CANCELLED', 'CANCELLED'), ('RETURNED', 'RETURNED')], default='DRAFT', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('approved_at', models.DateTimeField()),
                ('cancelled_at', models.DateTimeField()),
                ('cancelled_reason', models.TextField()),
                ('received_at', models.DateTimeField()),
                ('returned_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SalesOrderItemOutwardedLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('outwarded_quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax_percentage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_type', models.CharField(choices=[('PERCENTAGE', 'PERCENTAGE'), ('AMOUNT', 'AMOUNT')], default='PERCENTAGE', max_length=255)),
                ('shipping_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_tax_percentage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('additional_details', models.JSONField()),
                ('status', models.CharField(choices=[('DRAFT', 'DRAFT'), ('SENT', 'SENT'), ('DELIVERED', 'DELIVERED'), ('PARTIAL DELIVERED', 'PARTIAL DELIVERED'), ('CANCELLED', 'CANCELLED'), ('RETURNED', 'RETURNED')], default='DRAFT', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SalesOrderLogs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('additional_details', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SalesOrderOrderItems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity_ordered', models.IntegerField()),
                ('quantity_delivered', models.IntegerField()),
                ('quantity_shipped', models.IntegerField()),
                ('quantity_cancelled', models.IntegerField()),
                ('quantity_returned', models.IntegerField()),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_returned', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_cancelled', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_ordered', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax_percentage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_tax_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_cancelled_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_cancelled_tax_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_type', models.CharField(choices=[('PERCENTAGE', 'PERCENTAGE'), ('AMOUNT', 'AMOUNT')], default='PERCENTAGE', max_length=255)),
                ('additional_details', models.JSONField()),
                ('status', models.CharField(choices=[('DRAFT', 'DRAFT'), ('SENT', 'SENT'), ('DELIVERED', 'DELIVERED'), ('PARTIAL DELIVERED', 'PARTIAL DELIVERED'), ('CANCELLED', 'CANCELLED'), ('RETURNED', 'RETURNED'), ('PARITAL RETURNED', 'PARITAL RETURNED')], default='DRAFT', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('approved_at', models.DateTimeField()),
                ('cancelled_at', models.DateTimeField()),
                ('cancelled_reason', models.TextField()),
                ('shipped_at', models.DateTimeField()),
                ('returned_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SalesOrderOutWardedLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_path', models.TextField()),
                ('invoice_number', models.CharField(max_length=255)),
                ('notes', models.TextField()),
                ('outwared_at', models.DateTimeField()),
                ('additional_details', models.JSONField()),
                ('status', models.CharField(choices=[('DRAFT', 'DRAFT'), ('SENT', 'SENT'), ('DELIVERED', 'DELIVERED'), ('PARTIAL DELIVERED', 'PARTIAL DELIVERED'), ('CANCELLED', 'CANCELLED'), ('RETURNED', 'RETURNED')], default='DRAFT', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
