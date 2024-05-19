/* logic & css from stripe.com */

var stripe_public_key = $('#id_stripe_public_key').text.slice(1, -1);
var client_secret = $('#id_client_secret').text.slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var card = elements.create('card');
var style = {{
    base: {
      color: '#fff',
      fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
      fontSmoothing: 'antialiased',
      fontSize: '16px',
      '::placeholder:: {
        color: '#fce883',
      }
    },
    invalid: {
      iconColor: '#FFC7EE',
      color: '#FFC7EE',
    },
  };
card.mount('#card-element', {style:style});


