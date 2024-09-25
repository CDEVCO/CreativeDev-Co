-- disable stripe payment provider
UPDATE payment_provider
   SET promptpay_username = NULL,
       promptpay_password = NULL,
