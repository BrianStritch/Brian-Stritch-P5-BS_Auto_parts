# Setting up gmail to send messages

## Google emails
To set up the project to send emails using a Google account the following steps are required
1. Create an email account at google.com, login, navigate to Settings in your gmail account and then click on Other Google Account Settings
    <br>![Setting up gmail account ](../media/readme/email_account_setup_for_sending_emails_from_django/1.JPG)
    <br>![Setting up gmail account ](../media/readme/email_account_setup_for_sending_emails_from_django/2.JPG)
    <br>![Setting up gmail account ](../media/readme/email_account_setup_for_sending_emails_from_django/3.JPG)
    <br>![Setting up gmail account ](../media/readme/email_account_setup_for_sending_emails_from_django/4.JPG)
    <br>![Setting up gmail account ](../media/readme/email_account_setup_for_sending_emails_from_django/5.JPG)
    <br>![Setting up gmail account ](../media/readme/email_account_setup_for_sending_emails_from_django/6.JPG)


2. Turn on 2-step verification and follow the steps to enable
    <br>![Setting up gmail account two step verification](../media/readme/email_account_setup_for_sending_emails_from_django/7.JPG)

    <br>![Setting up gmail account two step verification ](../media/readme/email_account_setup_for_sending_emails_from_django/8.JPG)

    <br>![Setting up gmail account two step verification](../media/readme/email_account_setup_for_sending_emails_from_django/9.JPG)

    <br>![Setting up gmail account two step verification ](../media/readme/email_account_setup_for_sending_emails_from_django/10.JPG)

    <br>![Setting up gmail account two step verification ](../media/readme/email_account_setup_for_sending_emails_from_django/11.JPG)

    <br>![Setting up gmail account two step verification ](../media/readme/email_account_setup_for_sending_emails_from_django/12.JPG)
    <br>![Setting up gmail account two step verification ](../media/readme/email_account_setup_for_sending_emails_from_django/13.JPG)

    <br>![Setting up gmail account two step verification ](../media/readme/email_account_setup_for_sending_emails_from_django/14.JPG)

3. Click on app passwords, select Other as the app and give the password a name, for example Django

    <br>![Setting up gmail account app password](../media/readme/email_account_setup_for_sending_emails_from_django/15.JPG)

    <br>![Setting up gmail account app password](../media/readme/email_account_setup_for_sending_emails_from_django/16.JPG)

    <br>![Setting up gmail account app password](../media/readme/email_account_setup_for_sending_emails_from_django/17.JPG)

    <br>![Setting up gmail account app password](../media/readme/email_account_setup_for_sending_emails_from_django/18.JPG)

    <br>![Setting up gmail account app password](../media/readme/email_account_setup_for_sending_emails_from_django/19.JPG)

    <br>![Setting up gmail account app password](../media/readme/email_account_setup_for_sending_emails_from_django/20.JPG)



4. Click create and a 16 digit password will be generated, note the password down
    <br>![Setting up gmail account app password ](../media/readme/email_account_setup_for_sending_emails_from_django/password_generated.jpg)

5. In the Heroku navigate to the settings tab and reveal config vars
    <br>![Setting up gmail account app password ](../media/readme/email_account_setup_for_sending_emails_from_django/21.JPG)

5. In the Heroku config vars create an environment variable called EMAIL_HOST_PASS with the 16 
   digit password
    <br>![Setting up gmail account app password ](../media/readme/email_account_setup_for_sending_emails_from_django/22.JPG)

6. In the Heroku config vars create an environment variable called EMAIL_HOST_USER with the email address of the gmail account
    <br>![Setting up gmail account app password ](../media/readme/email_account_setup_for_sending_emails_from_django/23.JPG)



7. In your workspace navigate to the top level settings.py file to update the email settings
    <br>![Setting up gmail account app password ](../media/readme/email_account_setup_for_sending_emails_from_django/24.JPG)

8. Set and confirm the following values in the settings.py file to successfully send emails
    <br>![Setting up gmail account app password ](../media/readme/email_account_setup_for_sending_emails_from_django/25.JPG)

