# DEPLOYMENT TO HEROKU

## Deployment steps:

#### Step 1: Select Create a New Heroku Account
![Step 1:](../media/readme/heroku_deployment_procedure/1.JPG "Heroku deployment steps: Step 1")

#### Step 2: Add your Credentials to create an account
![Step 2:](../media/readme/heroku_deployment_procedure/2.JPG "Heroku deployment steps: Step 2")

#### Step 3: Once an account is created go to the dashboard 
![Step 3:](../media/readme/heroku_deployment_procedure/3.JPG "Heroku deployment steps: Step 3")

#### Step 4: Select New to create a new app
![Step 4:](../media/readme/heroku_deployment_procedure/4.JPG "Heroku deployment steps: Step 4")

#### Step 5: Add your app name and select the region you are closest to
![Step 5:](../media/readme/heroku_deployment_procedure/5.JPG "Heroku deployment steps: Step 5")

#### Step 6: In the example below we have created our app name and selected Europe as our region
![Step 6:](../media/readme/heroku_deployment_procedure/6.JPG "Heroku deployment steps: Step 6")

#### Step 7: Once your app is created you will be returned to the dashboard of your new app
![Step 7:](../media/readme/heroku_deployment_procedure/7.JPG "Heroku deployment steps: Step 7")

#### Step 8: Select the Deploy tab from the top menu
![Step 8:](../media/readme/heroku_deployment_procedure/8.JPG "Heroku deployment steps: Step 8")

#### Step 9: Add a pipeline to deploy from or connect to a github account
![Step 9:](../media/readme/heroku_deployment_procedure/9.JPG "Heroku deployment steps: Step 9")

#### Step 10: You can select a github account and repository to connect to.
![Step 10:](../media/readme/heroku_deployment_procedure/10.JPG "Heroku deployment steps: Step 10")

#### Step 11: In the example below we can see the github account and selected repository to connect to.
![Step 11:](../media/readme/heroku_deployment_procedure/11.JPG "Heroku deployment steps: Step 11")

#### Step 12: Next we enabled Automatic Deploys and Deployed a branch to begin the process
![Step 12:](../media/readme/heroku_deployment_procedure/12.JPG "Heroku deployment steps: Step 12")

#### Step 13: The Automatic deploys have been activated and the tab is now toggled to disable automatic deployment indicating that it was succesful.
![Step 13:](../media/readme/heroku_deployment_procedure/13.JPG "Heroku deployment steps: Step 13")

#### Step 14: Next we navigate to the Settings tab
![Step 14:](../media/readme/heroku_deployment_procedure/14.JPG "Heroku deployment steps: Step 14")

#### Step 15: In the settings section we select REVEAL CONFIG VARS
![Step 15:](../media/readme/heroku_deployment_procedure/15.JPG "Heroku deployment steps: Step 15")

#### Step 16: Select Reveal config vars in order to set the configuration variables
![Step 16:](../media/readme/heroku_deployment_procedure/16.JPG "Heroku deployment steps: Step 16")

#### Step 17: Once selected the relevant Key Value pairs can be input and saved
![Step 17:](../media/readme/heroku_deployment_procedure/17.JPG "Heroku deployment steps: Step 17")

#### Step 18: Below is an image of the required config vars for this project to deploy correctly on heroku.
![Step 18:](../media/readme/heroku_deployment_procedure/18.JPG "Heroku deployment steps: Step 18")

#### Step 19: Next we navigate to the top level of our application in our workspace.
![Step 19:](../media/readme/heroku_deployment_procedure/19.JPG "Heroku deployment steps: Step 19")

#### Step 20: In the Allowed hosts we now include our herokuapp url to allow our workspace access from heroku.
![Step 20:](../media/readme/heroku_deployment_procedure/20.JPG "Heroku deployment steps: Step 20")


## Installation of heroku in Gitpod and login

#### Step 1: Installation of Heroku in the Workspace Terminal.

    - To Install heroku we used the following commands in the terminal:
         - npm i -g heroku 
         - pip install heroku3

#### Step 2: Login to heroku via the workspace terminal

     - To Login to heroku via the workspace terminal we used the following command:
         - heroku login -i 

## We have now completed our Heroku Deployment
