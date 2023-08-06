# django-soft-atomic

[![GitHub](https://img.shields.io/github/license/maniek2332/django-soft-atomic)](https://github.com/maniek2332/django-soft-atomic/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/django_soft_atomic)](https://pypi.org/project/django_soft_atomic/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django_soft_atomic)](https://pypi.org/project/django_soft_atomic/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/django_soft_atomic)](https://pypi.org/project/django_soft_atomic/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/django_soft_atomic)](https://pypi.org/project/django_soft_atomic/)

A more forgiving variation of `django`'s `atomic`, allowing you to pass some
exceptions through atomic block without rollback.

## Rationale

In big applications you may end up relying on exceptions mechanism to pass information
about failure up the stack. Unfortunately, if your business logic involves operations on
database, there is no easy way to wind up execution through atomic block without
rolling back entire transaction. `django-soft-atomic` tries to solves this problem
by allowing certain exceptions to exit atomic block just like sucessful execution
(still maintaining the raised exception).

## Requirements

 * Python 3.6+
 * Django 3.2+

## Installation

### With PIP

Execute: `pip install django_soft_atomic`

See also: [PyPI Page](https://pypi.org/project/django_soft_atomic/)

### Manual

Copy `django_soft_atomic.py` to your codebase and simply start using it.

## Usage (docs)

This "package" constists of single decorator/context-manager, acting as replacement for django's `atomic`:

`soft_atomic(using=None, savepoint=True, durable=False, *, safe_exceptions=(Exception,))`

 * `using` - database name to use
   ([same as original atomic](https://docs.djangoproject.com/en/4.1/topics/db/transactions/#django.db.transaction.atomic)),
 * `savepoint` - disable usage of savepoints in inner blocks
   ([same as original atomic](https://docs.djangoproject.com/en/4.1/topics/db/transactions/#django.db.transaction.atomic)),
 * `durable` - ensure this is outermost block
   ([same as original atomic](https://docs.djangoproject.com/en/4.1/topics/db/transactions/#django.db.transaction.atomic)),
 * `safe_exceptions` - collection (e.g. `tuple`) of exceptions which are allowed to pass through `soft_atomic` block without rollback. Typical DB errors (like `IntegrityError`) will still throw. Defaults to: `(Exception,)`.

## Example

Let's take a simple example, where we would like to perform payment operation and raise an exception if it fails.
We want to create a database entry for both outcomes.

```python
from django_soft_atomic import soft_atomic

class PaymentProcessingException(Exception):
    pass

class PaymentRequest(models.Model):
    payment_id = models.TextField()
    success = models.BooleanField()

@soft_atomic(safe_exceptions=(PaymentProcessingException,))
def process_payment(payment_details):
    payment_id, success = payment_gateway.process_payment(payment_details)
    PaymentRequest.objects.create(payment_id=payment_id, success=success)
    if not success:
        raise PaymentProcessingException("Payment was not sucessful")

def payment_endpoint(payment_details):
    try:
        process_payment(payment_details)
    except PaymentProcessingException:
        ...  # handle a failure
    else:
        ...  # payment was successful
    # in either case the `PaymentRequest` record was created in the database
```
