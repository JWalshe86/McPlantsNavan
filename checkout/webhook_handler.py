from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request
        print("testing")

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        print("testing")
        return HttpResponse(
            content=f'iiiiiiiiiiiUnhandled webhook received: {event["type"]}',
            status=200,
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        print("testingsuccess")
        return HttpResponse(
            content=f'cccccccWebhook received: {event["type"]}', status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        print("testingfailure")
        return HttpResponse(
            content=f'xxxxxxxxxWebhook received: {event["type"]}', status=200
        )
