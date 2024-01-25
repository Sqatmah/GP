ACTIVE = 'active'
DISABLED = 'disabled'

MALE = 'male'
FEMALE = 'female'

APPROVED = 'approved'
REJECT = 'reject'
WAITING = 'waiting'
PAID = 'paid'

INDIVIDUAL = 'individual'
COMPANY = 'company'
FAMILY = 'family'

USER_STATUS = (
    (ACTIVE, 'Active'),
    (DISABLED, 'Disabled'),
)

GENDER = (
    (MALE, 'Male'),
    (FEMALE, 'Female')
)

REQUEST_STATUS = (
    (APPROVED, 'Approved'),
    (REJECT, 'Reject'),
    (WAITING, 'Waiting'),
    (PAID, 'Paid')
)

ROLE_CHOICES = (
    (INDIVIDUAL, 'Individual'),
    (COMPANY, 'Company'),
    (FAMILY, 'Family')
)
