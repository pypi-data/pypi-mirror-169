SLICKPAY_API_URL = ""


# Request Parameters
fname = "fname"
lname = "lname"
address = "address"
amount = "amount"
rib = "rib"
BACK_URL = "back_url"
WEBHOOK_URL = "webhook_url"
MODE = "mode"
COMMENT = "comment"


# PAYMENT mode
CIB = "CIB"
EDAHABIA = "EDAHABIA"


#
REQUIRED_PARAMTERS = {
    fname,
    lname,
    address,
    amount,
    rib,
    WEBHOOK_URL,
    BACK_URL,
}


PAYMENT_EXPIRED = "expired"
PAYMENT_PAID = "paid"
PAYMENT_FAILED = "failed"
PAYMENT_CANCELED = "canceled"
PAYMENT_IN_PROGRESS = "progress"