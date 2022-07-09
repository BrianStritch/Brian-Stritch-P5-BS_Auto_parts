# Stripe setup


## Stripe
1. Register for an account at stripe.com

2. Click on the Developers section of your account once logged in
<br>![Stripe dashboard](../media/readme/stripe_setup/stripe_dashboard.JPG)
<br>![developer tab](../media/readme/stripe_setup/developers-button.JPG)

3. Under Developers, click on the API keys section
<br>![developer menu](../media/readme/stripe_setup/developer-menu-webhook-apikey.JPG)

4. Note the values for the publishable and secret keys
<br>![API keys](../media/readme/stripe_setup/api-keys.JPG)

5. In your local environment(env.py) and heroku, create environment variables STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY with the publishable and secret key values
<br><code>os.environ.setdefault('STRIPE_PUBLIC_KEY', 'your new public key')</code>
<br><code>os.environ.setdefault('STRIPE_SECRET_KEY', 'your new secret key')</code>

6. Back in the Developers section of your stripe account click on Webhooks
<br>![developer menu](../media/readme/stripe_setup/developer-menu-webhook-apikey.JPG)

7. Create a webhook with the url of your website <url>/checkout/wh/, for example: "https://brian-stritch-p5-bs-auto-parts.herokuapp.com/.herokuapp.com/checkout/wh/"

8. Select the payment_intent.payment_failed and payment_intent.succeeded as events to send
<br>![Webhook event listener](../media/readme/stripe_setup/select-all-listener-events.JPG)
9. Note the key created for this webhook
10. In your local environment(env.py) and heroku, create environment variable STRIPE_WH_SECRET with the secret values
<code>os.environ.setdefault('STRIPE_WH_SECRET', 'your new secret webhook key')</code>
