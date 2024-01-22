YES = 'yes'
NO = 'no'
EX_SUBSCRIPTION = (
    (YES, 'yes'),
    (NO, 'no')
)

ACTIVE = 'active'
DISABLED = 'disabled'

USER_STATUS = (
    (ACTIVE, 'Active'),
    (DISABLED, 'Disabled'),
)

PAID = 'paid'
UNPAID = 'unpaid'

PAYMENT_STATUS = (
    (PAID, 'Paid'),
    (UNPAID, 'unpaid')
)

APPROVE = 'Approve'
REJECT = 'Reject'
WAIT = 'Wait'
PAID = 'Paid'

REQUEST_STATUS = (
    (APPROVE, 'Approve'),
    (REJECT, 'Reject'),
    (WAIT, 'Wait'),
    (PAID, 'Paid')
)

MEN = 'Man'
FEMALE = 'Female'

GENDERS = (
    (MEN, "Men"),
    (FEMALE, 'Female')
)

GOLD = 'Gold'
SILVER = 'Silver'
Bronze = 'Bronze'

INSURANCE_DEGREE = (
    (GOLD, 'Gold'),
    (SILVER, 'Silver'),
    (Bronze, 'Bronze')
)