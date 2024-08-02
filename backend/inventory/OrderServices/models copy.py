from django.db import models
from InventoryServices.models import Warehouse
from UserServices.models import Users
from ProductServices.models import *


class PurchaseOrder(models.Model):
    PAYMENT_ORDER_METHODS = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Online', 'Online'),
        ('Paypal', 'Paypal'),
    )
    PAYMENT_STATUS = (
        ('Unpaid', 'Unpaid'),
        ('Partially Paid', 'Partially Paid'),
        ('Fully Paid', 'Fully Paid'),
        ('Cancelled', 'Cancelled'),
    )
    PURCHASE_ORDER_STATUS = (
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Returned', 'Returned'),
    )

    DISCOUNT_TYPE = (
        ('Percentage', 'Percentage'),
        ('Amount', 'Amount'),
    )

    SHIPPING_TYPE = (
        ('Free', 'Free'),
        ('Standard', 'Standard'),
        ('Express', 'Express'),
        ('Priority', 'Priority'),
    )

    id = models.AutoField(primary_key=True)
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE, blank=True, null=True, related_name='warehouse_purchase_order')
    supplier_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name="supplier_purchase_order")
    last_updated_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name="last_updated_by_user_purchase_order")
    purchase_order_code = models.CharField(max_length=255)
    purchase_order_date = models.DateTimeField()
    expected_delivery_order_date = models.DateTimeField()
    payment_method = models.CharField(max_length=255, blank=True, null=True, choices=PAYMENT_ORDER_METHODS, default='Cash')
    payment_status = models.CharField(max_length=255, blank=True, null=True, choices=PAYMENT_STATUS, default='Unpaid')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    balance_due = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, blank=True, null=True, choices=PURCHASE_ORDER_STATUS, default='Pending')
    discount_type = models.CharField(max_length=50, blank=True, null=True, choices=DISCOUNT_TYPE, default="Amount")
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_type = models.CharField(max_length=255, blank=True, null=True, choices=SHIPPING_TYPE, default="Free")
    shipping_tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cancelled = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cancelled_tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    additional_details = models.JSONField()
    created_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='created_by_user_id_purchase_order')
    updated_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='updated_by_user_purchase_order')
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='domain_user_id_purchase_order')
    approved_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='approved_by_user_id_purchase_order')
    approved_at = models.DateTimeField()
    cancelled_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='cancelled_by_user_id_purchase_order')
    cancelled_at = models.DateTimeField()
    cancelled_reason = models.TextField()
    shipped_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='shipped_by_user_id_purchase_order')
    shipped_at = models.DateTimeField()
    returned_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='returned_by_user_id_purchase_order')
    returned_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class PurchaseOrderItem(models.Model):
    DISCOUNT_TYPE = (
        ('Percentage', 'Percentage'),
        ('Amount', 'Amount'),
    )
    PURCHASE_ORDER_ITEM_STATUS = (
        ('Pending', 'Pending'),
        ('Purchased', 'Purchased'),
        ('Returned', 'Returned'),
    )
    id = models.AutoField(primary_key=True)
    purchase_order_id = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='purchase_order_item')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_order_item')
    quantity_ordered = models.IntegerField()
    quantity_received = models.IntegerField()
    quantity_cancelled = models.IntegerField()
    quantity_returned = models.IntegerField()
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_type = models.CharField(max_length=100, choices=DISCOUNT_TYPE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    amount_returned = models.DecimalField(max_digits=10, decimal_places=2)
    amount_cancelled = models.DecimalField(max_digits=10, decimal_places=2)
    amount_ordered = models.DecimalField(max_digits=10, decimal_places=2)
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cancelled_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cancelled_tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    additional_details = models.JSONField()
    status = models.CharField(max_length=100, choices=PURCHASE_ORDER_ITEM_STATUS)
    created_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='created_by_user_purchase_order_item')
    updated_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='updated_by_user_purchase_order_item')
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='domain_user_id_purchase_order_items')
    approved_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='approved_by_user_id')
    approved_at = models.DateTimeField()
    cancelled_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='cancelled_by_user_id')
    cancelled_at = models.DateTimeField()
    cancelled_reason = models.TextField()
    received_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='received_by_user_id')
    received_at = models.DateTimeField()
    returned_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='returned_by_user_id')
    returned_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PurchaseOrderInwardedLog(models.Model):
    PURCHASE_ORDER_OUTWARDED_STATUS = (
        ('Pending', 'Pending'),
        ('Purchase', 'Purchase'),
        ('Returned', 'Returned'),
    )
    id = models.AutoField(primary_key=True)
    purchase_order_id = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='purchase_order_item_inwarded_log')
    invoice_path = models.TextField()
    invoice_number = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    inwarded_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='inwarded_by_user_inwarded_log')
    inwarded_at = models.DateTimeField()
    status = models.CharField(max_length=100, choices=PURCHASE_ORDER_OUTWARDED_STATUS, default='Pending')
    additional_details = models.TextField()
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='domain_user_id_purchase_inwarded_log')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PurchaseOrderItemInwardedLog(models.Model):
    DISCOUNT_TYPE = (
        ('Percentage', 'Percentage'),
        ('Amount', 'Amount'),
    )
    STATUS = (
        ('Draft', 'Draft'),
        ('Pending', 'Pending'),
        ('Sent', 'Sent'),
        ('Received', 'Received'),
        ('Returned', 'Returned'),
        ('Cancelled', 'Cancelled'),
    )
    id = models.AutoField(primary_key=True)
    purchase_order_item_id = models.ForeignKey(PurchaseOrderItem, on_delete=models.CASCADE, related_name='purchase_order_item_id')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_type = models.CharField(max_length=100, choices=DISCOUNT_TYPE)
    shipping_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    additional_details = models.JSONField()
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='domain_user_id_purchase_item_inwarded_log')
    status = models.CharField(max_length=100, choices=STATUS, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PurchaseOrderLog(models.Model):
    STATUS = (
        ('Draft', 'Draft'),
        ('Pending', 'Pending'),
        ('Purchased', 'Purchased'),
        ('Returned', 'Returned'),
    )
    id = models.AutoField(primary_key=True)
    purchase_order_id = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='purchase_order_log')
    comment = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS)
    created_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='created_by_user_purchase_order_log')
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='domain_user_id_purchase_order_logs')
    additional_details = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# ========== SALES ==========
class SaleOrder(models.Model):
    PAYMENT_ORDER_METHODS = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Online', 'Online'),
        ('Paypal', 'Paypal'),
    )
    PAYMENT_STATUS = (
        ('Unpaid', 'Unpaid'),
        ('Partially Paid', 'Partially Paid'),
        ('Fully Paid', 'Fully Paid'),
        ('Cancelled', 'Cancelled'),
    )
    SALES_ORDER_STATUS = (
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Returned', 'Returned'),
    )

    DISCOUNT_TYPE = (
        ('Percentage', 'Percentage'),
        ('Amount', 'Amount'),
    )

    SHIPPING_TYPE = (
        ('Free', 'Free'),
        ('Standard', 'Standard'),
        ('Express', 'Express'),
        ('Priority', 'Priority'),
    )

    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name="customer_id")
    last_updated_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name="last_updated_by_user_sales_order")
    sales_order_code = models.CharField(max_length=255)
    sales_order_date = models.DateTimeField()
    expected_delivery_order_date = models.DateTimeField()
    payment_method = models.CharField(max_length=255, blank=True, null=True, choices=PAYMENT_ORDER_METHODS, default='Cash')
    payment_status = models.CharField(max_length=255, blank=True, null=True, choices=PAYMENT_STATUS, default='Unpaid')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    balance_due = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, blank=True, null=True, choices=SALES_ORDER_STATUS, default='Pending')
    discount_type = models.CharField(max_length=50, blank=True, null=True, choices=DISCOUNT_TYPE, default="Amount")
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_type = models.CharField(max_length=255, blank=True, null=True, choices=SHIPPING_TYPE, default="Free")
    shipping_tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cancelled = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cancelled_tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    additional_details = models.JSONField()
    created_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='created_by_user_sales_order')
    updated_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='updated_by_user_sales_order')
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='domain_user_id_sales_order')
    approved_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='approved_by_user_sales_order')
    approved_at = models.DateTimeField()
    cancelled_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='cancelled_by_user_sales_order')
    cancelled_at = models.DateTimeField()
    cancelled_reason = models.TextField()
    received_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='received_by_user_sales_order')
    received_at = models.DateTimeField()
    returned_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='returned_by_user_sales_order')
    returned_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class SalesOrderItem(models.Model):
    DISCOUNT_TYPE = (
        ('Percentage', 'Percentage'),
        ('Amount', 'Amount'),
    )
    SALES_ORDER_ITEM_STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Returned', 'Returned'),
    )
    id = models.AutoField(primary_key=True)
    sales_order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE, related_name='sales_order_item')
    sales_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales_product_item')
    quantity_ordered = models.IntegerField()
    quantity_delievered = models.IntegerField()
    quantity_shipped = models.IntegerField()
    quantity_cancelled = models.IntegerField()
    quantity_returned = models.IntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_type = models.CharField(max_length=100, choices=DISCOUNT_TYPE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    amount_returned = models.DecimalField(max_digits=10, decimal_places=2)
    amount_cancelled = models.DecimalField(max_digits=10, decimal_places=2)
    amount_ordered = models.DecimalField(max_digits=10, decimal_places=2)
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cancelled_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cancelled_tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    additional_details = models.JSONField()
    status = models.CharField(max_length=100, choices=SALES_ORDER_ITEM_STATUS)
    created_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='created_by_user_sales_order_item')
    updated_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='updated_by_user_sales_order_item')
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='domain_user_id_sales_order_items')
    approved_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='approved_by_user_sales_order_item')
    approved_at = models.DateTimeField()
    cancelled_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='cancelled_by_user_sales_order_item')
    cancelled_at = models.DateTimeField()
    cancelled_reason = models.TextField()
    received_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='received_by_user_sales_order_item')
    received_at = models.DateTimeField()
    returned_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='returned_by_user_sales_order_item')
    returned_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SalesOrderOutwardedLog(models.Model):
    SALES_ORDER_OUTWARDED_STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('In Route', 'In Route'),
        ('Returned', 'Returned'),
    )
    id = models.AutoField(primary_key=True)
    sales_order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE, related_name='sales_order_outwarded_log')
    invoice_path = models.TextField()
    invoice_number = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    outwarded_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='outwarded_by_user_id')
    outwarded_at = models.DateTimeField()
    status = models.CharField(max_length=100, choices=SALES_ORDER_OUTWARDED_STATUS, default='Pending')
    additional_details = models.TextField()
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='domain_user_id_outwarded_log')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SalesOrderItemOutwardedLog(models.Model):
    DISCOUNT_TYPE = (
        ('Percentage', 'Percentage'),
        ('Amount', 'Amount'),
    )
    STATUS = (
        ('Draft', 'Draft'),
        ('Pending', 'Pending'),
        ('Sent', 'Sent'),
        ('Delivered', 'Delivered'),
        ('Returned', 'Returned'),
        ('Cancelled', 'Cancelled'),
    )
    id = models.AutoField(primary_key=True)
    sales_order_item_id = models.ForeignKey(SalesOrderItem, on_delete=models.CASCADE, related_name='sales_order_item_id')
    outwarded_quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_type = models.CharField(max_length=100, choices=DISCOUNT_TYPE)
    shipping_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    additional_details = models.JSONField()
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='domain_user_id_sales_order_outwarded_log')
    status = models.CharField(max_length=100, choices=STATUS, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SalesOrderLog(models.Model):
    STATUS = (
        ('Draft', 'Draft'),
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Returned', 'Returned'),
    )
    id = models.AutoField(primary_key=True)
    sales_order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE, related_name='sales_order_log')
    comment = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS)
    created_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='created_by_user_sales_order_log')
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='domain_user_id_sales_order_logs')
    additional_details = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)