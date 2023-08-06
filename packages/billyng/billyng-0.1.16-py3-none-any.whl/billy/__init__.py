"""
Copyright (c) 2022 Philipp Scheer
"""


import traceback
from typing import Union
import requests



class BillyError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def decorateAll(decorator):
    def decorate(cls):
        for attr in cls.__dict__: # there's propably a better way to do this
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate


def checkUrlIsSet(func):
    global host
    def wrapper(*args, **kwargs):
        global host
        if not isinstance(host, str) or host.strip() == "":
            raise RuntimeError("billy host is not set")
        return func(*args, **kwargs)
    return wrapper


def billyError(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise BillyError(f"{e}")
    return wrapper



def _handle(response):
    if response.status_code != 200:
        # raise RuntimeError(f"{response.status_code}: {response.text}")
        print(f"BILLY ERROR: {response.status_code}: {response.text}")
        raise RuntimeError(f"Internal error")
    else:
        response = response.json()
        if not response["success"]:
            raise RuntimeError(f"{response['result']}")
        else:
            return response["result"]


@billyError
def _post(url, *args, **kwargs):
    return _handle(requests.post(f"{proto}://{host}:{port}{url}", *args, **kwargs))


@billyError
def _delete(url, *args, **kwargs):
    return _handle(requests.delete(f"{proto}://{host}:{port}{url}", *args, **kwargs))


@billyError
def _get(url, *args, **kwargs):
    return _handle(requests.get(f"{proto}://{host}:{port}{url}", *args, **kwargs))


proto: str = "http"
host: str = None
port: int = 28018


class Customer:
    @staticmethod
    @checkUrlIsSet
    def create(email: str, address: dict = None, description: str = None, metadata: dict = {}, name: str = None, phone: str = None, initialCredits: int = 0):
        """Create a new stripe customer with given email, address description and other data.
        `initialCredits` controls the initial API credits of the customer.
        Returns the new customer ID or raises error"""
        return _post("/customer", json={ k:v for k,v in {
            "email": email, 
            "address": address, 
            "description": description,
            "metadata": metadata, 
            "name": name, 
            "phone": phone, 
            "initialCredits": initialCredits
        }.items() if v is not None})

    @staticmethod
    @checkUrlIsSet
    def delete(customerId: str):
        """Delete a stripe customer by ID"""
        assert isinstance(customerId, str) and customerId.startswith("cus_"), "invalid customer id"
        return _delete(f"/customer/{customerId}")

    @staticmethod
    @checkUrlIsSet
    def getSubscription(customerId: str):
        """Get the subscription of a stripe customer by ID"""
        assert isinstance(customerId, str) and customerId.startswith("cus_"), "invalid customer id"
        return _get(f"/customer/{customerId}/subscription")

    @staticmethod
    @checkUrlIsSet
    def getPaymentMethods(customerId: str, paymentMethodTypes: list = ["card"]):
        """Get the payment methods of a stripe customer by ID"""
        assert isinstance(customerId, str) and customerId.startswith("cus_"), "invalid customer id"
        return _get(f"/customer/{customerId}/paymentMethods?paymentMethodTypes={','.join(paymentMethodTypes)}")

    @staticmethod
    @checkUrlIsSet
    def getInvoices(customerId: str, before: int = None, after: int = None):
        """Setup a payment method in a web session. Creates a stripe SetupIntent and returns the client secret."""
        assert isinstance(customerId, str) and customerId.startswith("cus_"), "invalid customer id"
        qry = []
        if before:
            qry.append(f"before={int(before)}")
        if after:
            qry.append(f"after={int(after)}")
        return _get(f"/customer/{customerId}/invoices?{'&'.join(qry)}")

    @staticmethod
    @checkUrlIsSet
    def removePaymentMethod(paymentMethodId: str):
        """Get the payment methods of a stripe customer by ID"""
        assert isinstance(paymentMethodId, str) and paymentMethodId.startswith("pm_"), "invalid payment method id"
        return _delete(f"/paymentMethod/{paymentMethodId}")

    @staticmethod
    @checkUrlIsSet
    def isAuthorized(customerId: str, credits: int = 0):
        """Check if a customer has enough credits to cover any additional requests"""
        assert isinstance(customerId, str) and customerId.startswith("cus_"), "invalid customer id"
        return _post("/authorized", json={ "customerId": customerId, "credits": credits })

    @staticmethod
    @checkUrlIsSet
    def recordUsage(customerId: str, credits: int = 1, now: bool = False):
        """Record usage data for a customer. Charge the customer for `credits` credits."""
        assert isinstance(customerId, str) and customerId.startswith("cus_"), "invalid customer id"
        return _post("/usage", json={ "customerId": customerId, "credits": credits, "now": now })

    @staticmethod
    @checkUrlIsSet
    def creditTo(customerId: str, credits: int = 1, fixed: bool = True):
        """Credit a customer with `credits` credits. If `fixed` is True, the credits will not be gone after the billing period."""
        assert isinstance(customerId, str) and customerId.startswith("cus_"), "invalid customer id"
        return _post("/credit", json={ "customerId": customerId, "credits": credits, "fixed": fixed })

    @staticmethod
    @checkUrlIsSet
    def setupPaymentMethd(customerId: str, description: str = None, metadata: dict = {}, paymentMethodTypes: list = ["card"]):
        """Setup a payment method in a web session. Creates a stripe SetupIntent and returns the client secret."""
        assert isinstance(customerId, str) and customerId.startswith("cus_"), "invalid customer id"
        return _post("/setupPaymentMethod", json={ k:v for k,v in {
            "customerId": customerId, 
            "description": description, 
            "metadata": metadata, 
            "paymentMethodTypes": paymentMethodTypes
        }.items() if v is not None})

    @staticmethod
    @checkUrlIsSet
    def setDefaultPaymentMethod(customerId: str, paymentMethodId: str):
        """Set default payment method for customer"""
        assert isinstance(customerId, str) and customerId.startswith("cus_"), "invalid customer id"
        return _post(f"/customer/{customerId}/defaultPaymentMethod", json={ "paymentMethodId": paymentMethodId })

    @staticmethod
    @checkUrlIsSet
    def charge(customerId: str, paymentMethodId: str, amount: float, currency: str, description: str = None, descriptor: str = None, offSession: bool = False):
        """Set default payment method for customer"""
        assert isinstance(customerId, str) and customerId.startswith("cus_"), "invalid customer id"
        assert isinstance(paymentMethodId, str) and paymentMethodId.startswith("pm_"), "invalid payment method id"
        assert isinstance(amount, float) or isinstance(amount, int), "invalid amount data type"
        assert isinstance(currency, str), "invalid currency data type"
        return _post(f"/customer/{customerId}/charge", json={ "paymentMethodId": paymentMethodId, "amount": amount, "currency": currency, "description": description, "descriptor": descriptor, "offSession": offSession })





class Subscription:
    @staticmethod
    @checkUrlIsSet
    def create(customerId: str, productId: str, option: Union[str,int] = "base", cancelExistingSubscriptions: bool = True, invoiceNow: bool = True, prorate: bool = True, cancelAtPeriodEnd: bool = False, trialUntil: int = None, paymentMethodTimeout: int = 1, paymentMethodTypes: str = "card", paymentMethodId: str = None):
        """Create a subscription with customerId (obtained by `createCustomer`) and productId (obtained by `listSubscriptions`).
        For `option`, either use "base" or the index of a product option.
        """
        assert isinstance(customerId, str) and customerId.startswith("cus_"), "invalid customer id"
        assert isinstance(productId, str) and productId.startswith("prod_"), "invalid customer id"
        assert isinstance(paymentMethodTimeout, int) and paymentMethodTimeout > 0, "invalid paymentMethodTimeout (must be int and > 0)"
        return _post("/subscription", json={ k:v for k,v in {
            "customerId": customerId, 
            "productId": productId, 
            "option": option, 
            "cancelExistingSubscriptions": cancelExistingSubscriptions, 
            "invoiceNow": invoiceNow, 
            "prorate": prorate, 
            "cancelAtPeriodEnd": cancelAtPeriodEnd, 
            "trialUntil": trialUntil,
            "paymentMethodTimeout": paymentMethodTimeout,
            "paymentMethodId": paymentMethodId,
            "paymentMethodTypes": ",".join(paymentMethodTypes) if isinstance(paymentMethodTypes, list) else paymentMethodTypes,
        }.items() if v is not None})

    @staticmethod
    @checkUrlIsSet
    def cancel(customerId: str, productId: str, invoiceNow: bool = True, prorate: bool = True):
        """Cancel a subscription by specifying the `customerId` and `productId`"""
        assert isinstance(customerId, str) and customerId.startswith("cus_"), "invalid customer id"
        assert isinstance(productId, str) and productId.startswith("prod_"), "invalid customer id"
        return _delete("/subscription/cancel", json={ k:v for k,v in {
            "customerId": customerId, 
            "productId": productId, 
            "invoiceNow": invoiceNow, 
            "prorate": prorate
        }.items() if v is not None})

    @staticmethod
    @checkUrlIsSet
    def list():
        """List all available subscription options"""
        return _get("/subscriptions")


@checkUrlIsSet
def ping():
    """Ping the service"""
    return _get("/ping")

