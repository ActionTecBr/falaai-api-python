from enum import StrEnum


class EmailEvent(StrEnum):
    AVULSO_COMPLETED = "avulso.completed"
    CREDITS_EXHAUSTED = "credits.exhausted"
    CREDITS_LOW = "credits.low"
    PAYMENT_FAILED = "payment.failed"
    SUBSCRIPTION_CANCELED = "subscription.canceled"
    SUBSCRIPTION_CREATED = "subscription.created"
    SUBSCRIPTION_DOWNGRADED = "subscription.downgraded"
    SUBSCRIPTION_RENEWED = "subscription.renewed"
    SUBSCRIPTION_UPGRADED = "subscription.upgraded"

    def __str__(self) -> str:
        return str(self.value)
