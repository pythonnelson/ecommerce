ACCOUNT_CHOICES = [
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    ('suspended', 'Suspended'),
]

ROLES = [
    ('admin', 'Admin'),
    ('user', 'User'),
    ('guest', 'Guest'),
]

LANGUAGES = [
    ('en', 'English'),
    ('es', 'Spanish'),
    ('fr', 'French'),
    ('de', 'German'),
    # Add other languages as needed
]

DEPARTMENTS = [
    ('hr', 'Human Resources'),
    ('it', 'IT'),
    ('finance', 'Finance'),
    ('marketing', 'Marketing'),
]

DESIGNATIONS = [
    ('manager', 'Manager'),
    ('developer', 'Developer'),
    ('analyst', 'Analyst'),
    ('designer', 'Designer'),
]

CURRENCIES = [
    ('AED', 'AED'),
    ('AFN', 'AFN'),
    ('ALL', 'ALL'),
    ('AMD', 'AMD'),
    ('ANG', 'ANG'),
    ('AOA', 'AOA'),
    ('ARS', 'ARS'),
    ('AUD', 'AUD'),
    ('AWG', 'AWG'),
    ('AZN', 'AZN'),
    ('BAM', 'BAM'),
    ('BBD', 'BBD'),
    ('BDT', 'BDT'),
    ('BGN', 'BGN'),
    ('BHD', 'BHD'),
    ('BIF', 'BIF'),
    ('BMD', 'BMD'),
    ('BND', 'BND'),
    ('BOB', 'BOB'),
    ('BRL', 'BRL'),
    ('BSD', 'BSD'),
    ('BTN', 'BTN'),
    ('BWP', 'BWP'),
    ('BYN', 'BYN'),
    ('BZD', 'BZD'),
    ('CAD', 'CAD'),
    ('CDF', 'CDF'),
    ('CHF', 'CHF'),
    ('CLP', 'CLP'),
    ('CNY', 'CNY'),
    ('COP', 'COP'),
    ('CRC', 'CRC'),
    ('CUP', 'CUP'),
    ('CVE', 'CVE'),
    ('CZK', 'CZK'),
    ('DJF', 'DJF'),
    ('DKK', 'DKK'),
    ('DOP', 'DOP'),
    ('DZD', 'DZD'),
    ('EGP', 'EGP'),
    ('ERN', 'ERN'),
    ('ETB', 'ETB'),
    ('EUR', 'EUR'),
    ('FJD', 'FJD'),
    ('FKP', 'FKP'),
    ('FOK', 'FOK'),
    ('GBP', 'GBP'),
    ('GEL', 'GEL'),
    ('GGP', 'GGP'),
    ('GHS', 'GHS'),
    ('GIP', 'GIP'),
    ('GMD', 'GMD'),
    ('GNF', 'GNF'),
    ('GTQ', 'GTQ'),
    ('GYD', 'GYD'),
    ('HKD', 'HKD'),
    ('HNL', 'HNL'),
    ('HRK', 'HRK'),
    ('HTG', 'HTG'),
    ('HUF', 'HUF'),
    ('IDR', 'IDR'),
    ('ILS', 'ILS'),
    ('IMP', 'IMP'),
    ('INR', 'INR'),
    ('IQD', 'IQD'),
    ('IRR', 'IRR'),
    ('ISK', 'ISK'),
    ('JEP', 'JEP'),
    ('JMD', 'JMD'),
    ('JOD', 'JOD'),
    ('JPY', 'JPY'),
    ('KES', 'KES'),
    ('KGS', 'KGS'),
    ('KHR', 'KHR'),
    ('KID', 'KID'),
    ('KMF', 'KMF'),
    ('KRW', 'KRW'),
    ('KWD', 'KWD'),
    ('KYD', 'KYD'),
    ('KZT', 'KZT'),
    ('LAK', 'LAK'),
    ('LBP', 'LBP'),
    ('LKR', 'LKR'),
    ('LRD', 'LRD'),
    ('LSL', 'LSL'),
    ('LYD', 'LYD'),
    ('MAD', 'MAD'),
    ('MDL', 'MDL'),
    ('MGA', 'MGA'),
    ('MKD', 'MKD'),
    ('MMK', 'MMK'),
    ('MNT', 'MNT'),
    ('MOP', 'MOP'),
    ('MRU', 'MRU'),
    ('MUR', 'MUR'),
    ('MVR', 'MVR'),
    ('MWK', 'MWK'),
    ('MXN', 'MXN'),
    ('MYR', 'MYR'),
    ('MZN', 'MZN'),
    ('NAD', 'NAD'),
    ('NGN', 'NGN'),
    ('NIO', 'NIO'),
    ('NOK', 'NOK'),
    ('NPR', 'NPR'),
    ('NZD', 'NZD'),
    ('OMR', 'OMR'),
    ('PAB', 'PAB'),
    ('PEN', 'PEN'),
    ('PGK', 'PGK'),
    ('PHP', 'PHP'),
    ('PKR', 'PKR'),
    ('PLN', 'PLN'),
    ('PYG', 'PYG'),
    ('QAR', 'QAR'),
    ('RON', 'RON'),
    ('RSD', 'RSD'),
    ('RUB', 'RUB'),
    ('RWF', 'RWF'),
    ('SAR', 'SAR'),
    ('SBD', 'SBD'),
    ('SCR', 'SCR'),
    ('SDG', 'SDG'),
    ('SEK', 'SEK'),
    ('SGD', 'SGD'),
    ('SHP', 'SHP'),
    ('SLL', 'SLL'),
    ('SOS', 'SOS'),
    ('SRD', 'SRD'),
    ('SSP', 'SSP'),
    ('STN', 'STN'),
    ('SYP', 'SYP'),
    ('SZL', 'SZL'),
    ('THB', 'THB'),
    ('TJS', 'TJS'),
    ('TMT', 'TMT'),
    ('TND', 'TND'),
    ('TOP', 'TOP'),
    ('TRY', 'TRY'),
    ('TTD', 'TTD'),
    ('TVD', 'TVD'),
    ('TWD', 'TWD'),
    ('TZS', 'TZS'),
    ('UAH', 'UAH'),
    ('UGX', 'UGX'),
    ('USD', 'USD'),
    ('UYU', 'UYU'),
    ('UZS', 'UZS'),
    ('VES', 'VES'),
    ('VND', 'VND'),
    ('VUV', 'VUV'),
    ('WST', 'WST'),
    ('XAF', 'XAF'),
    ('XCD', 'XCD'),
    ('XDR', 'XDR'),
    ('XOF', 'XOF'),
    ('XPF', 'XPF'),
    ('YER', 'YER'),
    ('ZAR', 'ZAR'),
    ('ZMW', 'ZMW'),
    ('ZWL', 'ZWL'),
]

TIME_ZONES = [
    ('UTC-12:00', 'UTC-12:00'),
    ('UTC-11:00', 'UTC-11:00'),
    ('UTC-10:00', 'UTC-10:00'),
    ('UTC-09:30', 'UTC-09:30'),
    ('UTC-09:00', 'UTC-09:00'),
    ('UTC-08:00', 'UTC-08:00'),
    ('UTC-07:00', 'UTC-07:00'),
    ('UTC-06:00', 'UTC-06:00'),
    ('UTC-05:00', 'UTC-05:00'),
    ('UTC-04:00', 'UTC-04:00'),
    ('UTC-03:30', 'UTC-03:30'),
    ('UTC-03:00', 'UTC-03:00'),
    ('UTC-02:00', 'UTC-02:00'),
    ('UTC-01:00', 'UTC-01:00'),
    ('UTC+00:00', 'UTC+00:00'),
    ('UTC+01:00', 'UTC+01:00'),
    ('UTC+02:00', 'UTC+02:00'),
    ('UTC+03:00', 'UTC+03:00'),
    ('UTC+03:30', 'UTC+03:30'),
    ('UTC+04:00', 'UTC+04:00'),
    ('UTC+04:30', 'UTC+04:30'),
    ('UTC+05:00', 'UTC+05:00'),
    ('UTC+05:30', 'UTC+05:30'),
    ('UTC+05:45', 'UTC+05:45'),
    ('UTC+06:00', 'UTC+06:00'),
    ('UTC+06:30', 'UTC+06:30'),
    ('UTC+07:00', 'UTC+07:00'),
    ('UTC+08:00', 'UTC+08:00'),
    ('UTC+08:45', 'UTC+08:45'),
    ('UTC+09:00', 'UTC+09:00'),
    ('UTC+09:30', 'UTC+09:30'),
    ('UTC+10:00', 'UTC+10:00'),
    ('UTC+10:30', 'UTC+10:30'),
    ('UTC+11:00', 'UTC+11:00'),
    ('UTC+12:00', 'UTC+12:00'),
    ('UTC+12:45', 'UTC+12:45'),
    ('UTC+13:00', 'UTC+13:00'),
    ('UTC+14:00', 'UTC+14:00')
]

DISCOUNT_TYPE = [
    ('Percentage', 'Percentage'),
    ('Amount', 'Amount'),
]

INWARD_TYPE = [
    ('Purchased', 'Purchased'),
    ('Transferred', 'Transferred'),
    ('Returned', 'Returned'),
    ('Replacement', 'Replacement'),
]

# Plan Type Choices
PLAN_TYPES = [
    ('free', 'Free'),
    ('basic', 'Basic'),
    ('premium', 'Premium'),
]

# Address Type Choices
ADDRESS_TYPES = [
    ('home', 'Home'),
    ('office', 'Office'),
    ('billing', 'Billing'),
]

# Product Availability Status Choices
PRODUCT_AVAILABILITY = [
    ('available', 'Available'),
    ('out_of_stock', 'Out of Stock'),
    ('discontinued', 'Discontinued'),
]

# Product Question Status Choices
PRODUCT_QUESTION_STATUS = [
    ('open', 'Open'),
    ('answered', 'Answered'),
    ('closed', 'Closed'),
]

# Product Review Status Choices
PRODUCT_REVIEWS_STATUS = [
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
]

# Paid/Unpaid Status Choices
PAID_UNPAID = [
    ('paid', 'Paid'),
    ('unpaid', 'Unpaid'),
]

# Order Status Choices
ORDER_STATUS = [
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
]

# Payment Type Choices
PAYMENT_CHOICES = [
    ('credit_card', 'Credit Card'),
    ('debit_card', 'Debit Card'),
    ('paypal', 'PayPal'),
    ('bank_transfer', 'Bank Transfer'),
]

# Return Status Choices
RETURN_STATUS = [
    ('initiated', 'Initiated'),
    ('in_process', 'In Process'),
    ('completed', 'Completed'),
    ('rejected', 'Rejected'),
]

# INVENTORY_LOG_STATUS = (
#     ('Inwarded', 'Inwarded'),
#     ('Outwarded', 'Outwarded'),
#     ('Damaged', 'Damaged'),
#     ('Lost', 'Lost'),
#     ('Returned', 'Returned'),
#     ('Discontinued', 'Discontinued'),
#     ('Expired', 'Expired'),
#     ('Adjustment', 'Adjustment'),
#     ('Warehouse Transfer', 'Warehouse Transfer'),
# )

# PAYMENT_ORDER_METHODS = (
#     ('Cash', 'Cash'),
#     ('Cheque', 'Cheque'),
#     ('Online', 'Online'),
#     ('Paypal', 'Paypal'),
# )

# PAYMENT_STATUS = (
#     ('Unpaid', 'Unpaid'),
#     ('Partially Paid', 'Partially Paid'),
#     ('Fully Paid', 'Fully Paid'),
#     ('Cancelled', 'Cancelled'),
# )

# PURCHASE_ORDER_STATUS = (
#     ('Pending', 'Pending'),
#     ('Shipped', 'Shipped'),
#     ('Delivered', 'Delivered'),
#     ('Returned', 'Returned'),
# )

# SHIPPING_TYPE = (
#     ('Free', 'Free'),
#     ('Standard', 'Standard'),
#     ('Express', 'Express'),
#     ('Priority', 'Priority'),
# )

# STATUS = (
#     ('Draft', 'Draft'),
#     ('Pending', 'Pending'),
#     ('Purchased', 'Purchased'),
#     ('Returned', 'Returned'),
# )

# PRODUCT_AVAILABILITY = (
#     ('Available', 'Available'),
#     ('Out of Stock', 'Out of Stock'),
#     ('Coming Soon', 'Coming Soon'),
# )

# PRODUCT_QUESTION_STATUS = (
#     ('Active', 'Active'),
#     ('Inactive', 'Inactive'),
# )

# PRODUCT_REVIEWS_STATUS = (
#     ('Active', 'Active'),
#     ('Inactive', 'Inactive'),
# )

# ADDRESS_TYPES = (
#     ('HOME', 'Home'),
#     ('Office', 'Office'),
#     ('OTHER', 'Other'),
# )

# ACCOUNT_CHOICES = (
#     ('Active', 'Active'),
#     ('Inactive', 'Inactive'),
#     ('Banned', 'Banned'),
# )
# ROLES = (
#     ('Admin', 'Admin'),
#     ('User', 'User'),
#     ('Supplier', 'Supplier'),
#     ('Customer', 'Customer'),
#     ('Staff', 'Staff'),
#     ('Manager', 'Manager'),
# )


# PLAN_TYPES = (
#     ('Basic', 'Basic'),
#     ('Premium', 'Premium'),
#     ('Premium Plus', 'Premium Plus'),
#     ('Enterprise', 'Enterprise'),
# )
