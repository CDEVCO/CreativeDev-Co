-- disable stripe payment provider
UPDATE payment_provider
   SET kasikorn_bank_username = NULL,
       kasikorn_bank_password = NULL,
