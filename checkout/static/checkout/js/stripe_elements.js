var stripe_public_key = $('#id_stripe_public_key').text().slice(1,-1);
var client_secret = $('#id_client_secret').text().slice(1,-1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
      iconColor: '#000',
      color: '#000',
      fontWeight: '500',
      fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
      fontSize: '16px',
      fontSmoothing: 'antialiased',      
      '::placeholder': {
        color: '#87BBFD',
      },
    },
    invalid: {
      iconColor: '#dc3545',
      color: '#dc3545',
    },
}
var card = elements.create('card', {style: style});
card.mount('#card-element');
