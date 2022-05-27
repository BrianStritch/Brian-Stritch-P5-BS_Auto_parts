from django.http import HttpResponse


class StripeWH_handler:
    """
       class to handle stripe webhooks
    """
    def __init__(self,request):
        self.request = request

    def handle_event(self, event):
        """
        class to handle a generic/unknown/unexpected webhooks
        """
        return HttpResponse(
            content = f'Webhook recieved: {event['type']}',
            status=200,
        )


