# BRIAN STRITCH P5 - BS_AUTO_PARTS
## Created and developed by Brian Stritch
<hr>

At [**At BS_AUTO_PARTS**](https://brian-stritch-p5-bs-auto-parts.herokuapp.com/) is an e-commerce web application and store based on a fictional auto parts and motorsport parts store. [**BS_AUTO_PARTS**](https://brian-stritch-p5-bs-auto-parts.herokuapp.com/) consists of an online shop that caters for the average motorist as much as the motorsport enthusiast. The application is fully functional and allows a purchase to be made with a test Credit card number to display its functionality.
<br>
<br>
At [**At BS_AUTO_PARTS**](https://brian-stritch-p5-bs-auto-parts.herokuapp.com/) our members can sign-up and login to create a personal profile and can manage their credentials in the user profile page and when signed up can avail of features such as the members forum, where members can discuss topics, have the ability to  comment on existing posts or create their own posts. Users also have the ability to like other users posts and comments.
<br> 

The benefit of this application will allow users to purchase the products they require and also offers the user access to information relating to their vehicles. Should the User wish to discuss any issues they may have they can create a post in the many different Topics and can have other members assistance to help them resolve any issues theymay have.The User has the functionality to edit or delete any posts or comments which they themselves have created.

<hr>

The users on this website can create reviews on their favourite prducts and can like or unlike a review reated by another member, and the user can also create comments on other reviews left by other members. The users can also like and unlike the comments left by other members.

<br>

###### Am_I_RESPONSIVE.COM 
#### HOME PAGE
![Am-i-responsive-image](static/readme_images/am-i-responsive-home.JPG "Example of the Home landing page view")
#### SHOP INDEX PAGE 
![Am-i-responsive-image](static/readme_images/am-i-responsive-index.JPG "Example of the shop Index page view")

<hr>

# View the live site [**here**](https://brian-stritch-p5-bs-auto-parts.herokuapp.com/).

<hr>

## Table of Contents
1. [**UX**](#ux)
    1. [**User Stories**](#user-stories)
        1. [**New Users**](#new-users)
        2. [**Existing Members**](#existing-members)
        3. [**Admin / Staff Users**](#admin-/-staff-users)
    2. [**Wireframes**](#wireframes)
    3. [**Entity Relationship Diagram (ERD)**](#entity-relationship-diagram-(ERD))
2. [**Features**](#features)
    1. [**Existing Features**](#existing-features)
        1. [**Regular Users**](#regular-users)
        2. [**Staff Users**](#staff-users)
    2. [**Future Features**](#future-features)
3. [**Technologies Used**](#technologies-used)
4. [**Database**](#database)
    1. [**Physical database diagram**](#physical-database-diagram)
    2. [**Database models**](#models)
        1. [**User Model**](#user-model)
        2. [**Booking Model**](#booking-model)
        3. [**Review Model**](#review-model)
        4. [**Comment Model**](#comment-model)
5. [**Testing**](#testing)
    1. [**User Credentials**](#user-credentials)
        1. [**Test User**](#test-user)
        2. [**Test User Staff**](#test-user-staff)
    2. [**Manual**](#manual)
    3. [**Validation**](#validation)
        1. [**CSS**](#CSS)
        2. [**HTML**](#HTML)
        3. [**JavaScript**](#javaScript) 
        4. [**Python**](#python)
        5. [**Accessibility**](#accessibility)
    4. [**Automated**](#automated)
        1. [**Django / Coverage**](#django-/-coverage)
            1. [**Test Steps**](#test-steps)
    5. [**Responsiveness**](#responsiveness)
        1. [**Desktop Size**](#desktop-size)
        2. [**Tablet Size Screen Navigation Menu**](#tablet-size-screen-navigation-menu)
        3. [**Mobile Size Home Page**](#mobile-size-home-page)
        4. [**Mobile Size Home Page Navigation**](#mobile-size-home-page-navigation)
        5. [**Tablet Size Bookings Page Navigation Menu**](#tablet-size-bookings-page-navigation-menu)
        6. [**Tablet Size Reviews Page Navigation Menu**](#tablet-size-reviews-page-navigation-menu)
        7. [**Tablet Size Admin Page Navigation Menu**](#tablet-size-admin-page-navigation-menu)        
    6. [**Bugs Found**](#bugs-found)
6. [**Deployment**](#deployment)
    1. [**GitHub**](#GitHub)
        1. [**To commit the code on GitPod to GitHub**](#to-commit-the-code-on-GitPod-to-GitHub)
    2. [**Heroku**](#heroku)
7. [**Credits**](#credits)
    1. [**Content**](#content)
    2. [**Media**](#media)
    3. [**Acknowledgements**](#acknowledgements)

## UX Site users
This project was designed to allow users to, through CRUD functionality, create read update delete , shopping bag orders, product reviews, forum posts, forum post comments, and the ability to sign up to a newsletter and send a message to the site owners via the contact us form via the navigation menu. In particular;

- Allows users to create an account through the signup form
- Allows users to edit their accounts details on their profile page
- Allows users to delete their accounts from their profile page
- Allows users to view previous order history in the profile page

- Allows users to navigate through the shop easily to find the products they wish to buy
- Allows users to add products to the shopping bag
- Allows users to make purchases through the store

- Allows users to create a review through the create review form displayed on the product details page
- Allows users to edit their review through the edit review form displayed on the product details page
- Allows users to delete their review through the delete review link displayed on the product details page

- Allows registered users the ability to navigate to the Members forum easily
- Allows registered users the ability to navigate to the Members forum categories and topic easily
- Allows registered users to create forum posts through the create post form attached to the forum topic page
- Allows registered users to edit their forum posts through the edit forum posts form attached to the forum topic page
- Allows registered users to delete their forum posts through the delete forum posts link attached to the forum topic page
- Allows registered users to create a comment on another users post through the create comment form attached to the post detail page
- Allows registered users to edit their comment through the edit comment form attached to the post detail page
- Allows registered users to delete their comment through the delete comment link attached to the edit post detail page

## UX Administration
This project was designed to create an online ecommerce store where the site owners have the functionality to create read update and delete, products, product categories, manufacturer categories, forum topics, forum categories, forum posts and forum comments. 
To restrict the type of content displayed on this website any comments or posts or reviews created by a site user, will be sent to the administrator for verification prior to being published. Should a user update a post, comment, review, the status is reset and the post, comment or review, is resent to the administrator for a further approval prior to publishment. 

Any actions carried out by a site user or administrator are accompanied with messages to inform the user of the tasks and their status. 

The administrator has a seperate admin panel, which is not visible to regular site users, to carry out their day to day tasks which can be seen in the images below. The administration panel allows the storeowner to easily navigate via stock control, newsletter subscribers, contact us messages and manufacturer and category lists with further crud functionality to allow the siteowner full unrestricted access to the tasks they may require. 


This website is designed for the regular everyday individuals, however it caters for the motorsport enthusiast and due to the forum, would cater for all types of motor enthusiast, and allows the users to interact and share the knowledge they have gained. The forum has a classified section where users can trade used goods and can advertise for vehicles and parts wanted. 

The forum has a seperate forum admin menu which is not visible to regular site users where the siteowners have access to forms to create forum categories and topics. The Administartor also has edit and delete functionality avilable at the forum topic and ategory headings, which is not visible to the regular users.

The Color scheme throughout the website is based on an orange and black color scheme as the colors are very different giving the user clear visiblity throughout the website. We have also opted to use larer images for better visiblilty of the products on offer so the user can visibly see the product clearly prior to selectin to purchase it. 

I feel that this website satisfies the base requirements in that the users can create, read, update and delete data related to items in the database in an easy to use and visually appealing interface. 

There are a range of apps including shopping bag, checkout, contact us, favourites, forum, home, media, newsletter, product reviews, products, profiles and storeowners that all work together seamlessly to provide a beautifully designed and easy to navigate website that has been designed to appeal to a wide range of users. 

A new user who does not have an account will have access to the homepage (index.html) and to the store, and has limited functionality such as the newsletter optin, and the contact us messenger the signup page, and the login page. They will be unable to access the forum or create reviews or comments on the existing reviews, and should the user attempt to navigate to the forum, they will be redirected to the sign in page, which also offers a link to sign up.  

Once logged in, the members will have access to the sites remaining functionality for creating reviews, commenting and liking reviews, the forum topics, categories, posts and comments and will allow the editing and deleting of reviews,comments and editing content on their personal profile. 

In regards to the contact us messenging service, should an unregistered user wish to contact the administrator, a form is displayed with numerous fields such as the users address and personal details which is added to the database for future reference. A registed user has simply a message text box displayed as the users information will already be on file.

<br>

# USERS :
        - There are two main user types,
            - An admin(administrator) user account has been set up with username/password of testuseradmin/testpassword
            - A regular(shopper) user account has been set up with username/password of testuser/testpassword
            - When making a payment as a regular user, a test credit card of 4242424242424242 has been set up for the card number
            - For the expiry date, cvc and postal code please input 0424 242424
 
Once logged in, staff members have access to the same functionality as members and additonal functionality which is not made available to a regular user for testing purposes and to maintain stock control etc. The staff status allows selected users to access the management area where staff can view all products, categories, manufacturers, newsletter subscribers and contact us messages sent by site users to administration, and allows access to the django administration area where the staff member can view all products, orders, newsletter subscribers, forum categories, reviews, comments, users etc and has administration priveledges which allows them to create edit and update reviews, comments, bookings, users etc. The administration area is required in order to publish posts, comments, reviews etc, which have been submitted for approval prior to getting published.

Below is a list of views and descriptions ilustrating the different views and functionality available to the site user depending on thier status, ie, staff, regstered user or unregistered guest users, who all have different levels of access depending on thier status.

# User types - Unregistered and Registered User Access:
<br>

## General site pages
<hr>
<br>

##### Shop page view
![Shop page view](media/readme/site_images/index-page.JPG "Example of the Shop page view")

##### Shop page Products view
![Shop page Products view](media/readme/site_images/products-page.JPG "Example of the Shop page Products view")

##### Shop page Product review view
![Shop page Product review view](media/readme/site_images/product-detail-page.JPG "Example of the Shop page Product review view")

##### Registered User add to favourites toggle button
![Registered User add to favourites toggle button](media/readme/site_images/product-added-to-favourites.JPG "Example of the Registered User add to favourites toggle button view")

##### User shopping bag view
![User shopping bag view](media/readme/site_images/shopping-bag.JPG "Example of the User shopping bag view")

##### User checkout page view
![User checkout page view](media/readme/site_images/checkout.JPG "Example of the User checkout page view")


##### User checkout success page view
![User checkout success page view](media/readme/site_images/checkout_success.JPG "Example of the User checkout success page view")

##### Unregistered User contact us page view
![Un-registered User contact us page view](media/readme/site_images/contact-us-form-anonymous-user.JPG "Example of the Un-registered User contact us page view")

##### Registered User contact us page view
![Registered User contact us page view](media/readme/site_images/contact-us-registered-users.JPG "Example of the Registered User contact us page view")

##### Registered User log-in view
![Registered User log-in view](media/readme/site_images/log-in.JPG "Example of the Registered User log-in view")

##### Registered User log-out view
![Registered User log-out view](media/readme/site_images/log-out.JPG "Example of the Registered User log-out view")

##### User sign-up view
![User sign-up view](media/readme/site_images/sign-up.JPG "Example of the User sign-up view")
<br>

## Registered User forum page views
<hr>
<br>

##### Registered User forum page view
![Registered User forum page view](media/readme/site_images/forum-page.JPG "Example of the Administration forum page view")

##### Registered User forum page navigation
![Registered User forum page view](media/readme/site_images/forum-nav.JPG "Example of the Administration forum page navigation")

##### Registered User forum site navigation links
![Registered User forum create category view](media/readme/site_images/forum-main-page-links.JPG "Example of the Administration forum create category view")

##### Registered User forum topic post list view
![Registered User forum topic list view](media/readme/site_images/forum-topic-page.JPG "Example of the Registered User forum  topic list view")
##### Registered User forum topic post view
![Registered User forum topic post view](media/readme/site_images/forum_post_details.JPG "Example of the Registered User forum topic post view")
##### Registered User create forum topic post view
![Registered User create forum topic post view](media/readme/site_images/create-forum-post-page.JPG "Example of the Registered User create forum topic post view")


# User types - Admin Access:
<hr>

## General site pages
<hr>
<br>

##### Administrators user menu
![Administrators navigation menu](media/readme/site_images/admin-account-nav-menu.JPG "Example of the admin access profile navigation")

##### Administration Store Management view
![Administration Store Management view](media/readme/site_images/store_management.JPG "Example of the admin store management view")

##### Administration stock control view
![Administration stock control view](media/readme/site_images/stock_management.JPG "Example of the admin stock management view")

##### Administration store manufacturers and categories menu list view
![Administration store manufacturers and categories menu list view](media/readme/site_images/store_category_and_manufacturer_list.JPG "Example of the Administration store manufacturers and categories menu list view")

##### Administration contact us list view
![Administration contact us list view](media/readme/site_images//storeowners_contact_us_list.JPG "Example of the Administration contact us list view")

##### Administration add product view
![Administration add product view](media/readme/site_images/add-product-page.JPG "Example of the Administration add product view")

##### Administration add category view
![Administration add category view](media/readme/site_images/admin_shop_add_category.JPG "Example of the Administration add category view")

##### Administration add manufacturer view
![Administration add manufacturer view](media/readme/site_images/admin_shop_add_manufacturer.JPG "Example of the Administration add manufacturer view")

##### Administration product likes button, edit, delete and stock management buttons on product detail view
![Administration product likes button on product detail view](media/readme/site_images/admin-product-details.JPG "Example of the Administration product likes button on product detail view")

##### Close up view of administration product likes button, edit, delete and stock management buttons on product detail view
![Administration product likes button on product detail view](media/readme/site_images/admin-stock-management-button.JPG "Example of the Administration product likes button on product detail view")

##### Admin user profile page view
![User Profile](media/readme/site_images/my-account-user-details.JPG "Example of the users profile")
<br>

## Administrators forum page views
<hr>
<br>

##### Administration forum page view
![Administration forum page view](media/readme/site_images/admin_forum_main.JPG "Example of the Administration forum page view")

##### Administration forum page navigation
![Administration forum page view](media/readme/site_images/forum-admin-menu.JPG "Example of the Administration forum page navigation")

##### Administration forum create category view
![Administration forum create category view](media/readme/site_images/admin_forum_create_category.JPG "Example of the Administration forum create category view")

##### Administration forum create topic view
![Administration forum create topic view](media/readme/site_images/admin_forum_create_topic.JPG "Example of the Administration forum create topic view")

<br>

## User Stories
<hr>
<br>

#### New Users
    - As a new user, I would like to be able to view products in the store 
    - As a new user, I would like to be able to view products in the store and add them to my shopping bag
    - As a new user, I would like to be able to navigate from the products to the shopping bag
    - As a new user, I would like to be able to view the products in the shopping bag easily to check its contents
    - As a new user, I would like to be able to view the ability to easily navigate back to the shop products page from the shopping bag
      in case i wish to purchase more products.
    - As a new user, I would like to be able ammend the quantity of products in my shopping bag in case i wish to purchase more of the
      same  products.
    - As a new user, I would like to be able to navigate from the shopping bag to the checkout page to progress with my purchase.
    - As a new user, I would like to be able to easily enter my shipping details to ensure my order is delivered correctly.
    - As a new user, I would like to be able to easily enter my payment details and confirm my purchase.
    - As a new user, I would like to be able to recieve an order confirmation email which outlines which products i have purchased, their
      prices, the quantity of each item, the cost of each item and the total cost of my order.
    - As a new user, I would like to be able to see reasons why I should create an account so that I can decide if I would like to become
      a member
    - As a new user, I would like to be able to have the ability to register and create an account.  
    - As a new user, I would like to be able to have the ability to sign up for the shop newsletter.
    - As a new user, I would like to be able to have the ability to opt in or out of the newsletter or remove my email from the
      newsletter database should i feel the wish to do so.
    - As a new user, I would like to be able to read reviews on each product so that I can see what other users think of the products on
     offer

#### Existing Members
##### I would like to have all the new users functionality and also:
    - As an existing member, I would like to be able to log into my profile easily so that I can avail of members only attributes of the 
    website such as the forum.
    - As an existing member, I would like to be able to log into my profile easily so that I can review my profile information
    - As an existing member, I would like to be able to edit my personal information on my profile so that I can keep the information up to date on the database
    - As an existing member, I would like to be able to delete my profile should i wish to do so

    - As an existing member, I would like to be able to view my previous orders history 
    - As an existing member, I would like to be able to create reviews on products in the store
    - As an existing member, I would like to be able to edit all of my reviews
    - As an existing member, I would like to be able to delete my reviews

    - As an existing member, I would like to be able to access the members forum and view all the different posts in each topic and the comments on each post. 
    - As an existing member, I would like to be able to create my own forum post
    - As an existing member, I would like to be able to easily view my own forum post
    - As an existing member, I would like to be able to edit all of my forum posts
    - As an existing member, I would like to be able to delete my forum post

    - As an existing member, I would like to be able to view all forum post comments 
    - As an existing member, I would like to be able to create my own forum post comments 
    - As an existing member, I would like to be able to view all my forum post comments 
    - As an existing member, I would like to be able to edit all of my forum post comments
    - As an existing member, I would like to be able to delete my forum post comments

    - As an existing member, I would like to be able to view the number of likes on each post 
    - As an existing member, I would like to be able to view the number of likes on each post comment
    - As an existing member, I would like to be able to view the number of likes on each product review

#### Admin / Staff Users
- As a staff member, I would like to be able to view all the restaurant bookings 
- As a staff member, I would like to be able to view all the pending restaurant bookings 
- As a staff member, I would like to be able to view all the approved restaurant bookings 
- As a staff member, I would like to be able to view all the completed restaurant bookings 
- As a staff member, I would like to be able to manage all the restaurant bookings
- As a staff member, I would like for the application to stop any booking duplications
- As a staff member, I would like for the application to only allow a predefined number of guests per hour

- As a staff member, I would like to be able to view all the reviews
- As a staff member, I would like to be able to edit any of the reviews if required
- As a staff member, I would like to be able to delete a review in the event that it contains any offensive or inappropriate content
- As a staff member, I would like to be able to view all comments on reviews
- As a staff member, I would like to be able to approve or disprove all comments on reviews in the event that they contain any offensive or inappropriate content
- As a staff member, I would like to be able to edit any of the comments on a review if required 


- As a staff member, I would like to be able to view all of the users of the website so that I can manage them
- As a staff member, I would like to be able to edit a users Information should it be required
- As a staff member, I would like to be able to delete a user from the website if required
- As a staff member, I would like to be able to be able to edit a users information if required
- As a staff member, I would like to be able to be able to grant a user staff access or remove if required

### Wireframes
As there are many pages to this project, I have included the wireframes in a separate document.

Please [**click here**](https://github.com/BrianStritch/Brian-Stritch-P4-Fine-Wine-n-Dine/blob/main/wireframes.md) to see the wireframes.md file for the entire collection of wireframes.
 

### Site Map
![Site Map](static/readme_images/wireframe_images/site-map-diagram.JPG "Site Map Diagram showing Layout of the Web application")

## Features
### Existing Features
#### Regular Users 
1. Login - The customers are able to create their own accounts and log into the website with secure details.
2. Sign-Up - New users can sign up to create an account.
3. When creating a profile, it will not allow users to create a profile with the same username as another member
4. User Profile - Each user has their own profile that welcomes them by Username for personalisation.
5. Users can create bookings from the bookings page which is visible to logged in users.
6. Users can view their bookings from the bookings page which is visible to logged in users.
7. Users can select a booking and view , edit or delete the booking from the bookings detail page which is visible to logged in users.
8. Users can view reviews from past guests from the reviews page which is visible to all users.
9. Users can view specific reviews details and comments by clicking the review which redirects to the reviews detail page.
10. Users can edit or delete their own reviews or comments from the reviews detail page where an edit and delete button are visible to logged in users, but only for reviews or comments which were created by that user.
11. Users can view the menu to see what food products are available.
12. Users can view the contact and about us page to understand who the owners of the establishment are and what they are about. 
13. Users can also see the contact information, should they wish to contact the establisment directly.
14. Users can view the opnening hours to see when the establishment is open for business.
15. Users can see a gallery of images populated by images provided by guests from reviews.
16. Users can log out at any time from the site by clicking on the logout button 

#### Staff Users
1. Edit Bookings - Staff users can edit any bookings saved to the database using a simple form.
2. Edit Reviews - Staff users can edit any reviews saved to the database using a simple form.
3. Edit Comments- Staff users can edit any comments saved to the database using a simple form.
4. Delete Bookings - Staff users can delete any bookings saved to the database.
5. Delete Reviews - Staff users can delete any reviews saved to the database.
6. Delete Comments- Staff users can delete any comments saved to the database.
7. Edit Users - Staff users can edit any users saved to the database.
8. Delete Users - Staff users can delete any users saved to the database.

### Future Features
1. An Accomodation booking application will be added in a future update so the guests can stay in our new state of the art rooms.
2. A Menu app will be added in order for the staff / admin users to change the menu with a simple update form.
3. A payment method would be added in a future update so that the user can pre-pay their booking
4. A Merchandise shop will be added so that guests can purchase Nanny's clothing merchandise
5. A simple sign up with social media account will be introduced in a future update as we did not have the timescale to complete in this deployment.
6. A contact link between guests and admin will be established in a future update.
7. A User account details app will be set up in a future update to manage contact information and payment methods etc.

## Technologies Used
- HTML - This site uses HTML to instruct the browser how to interprit the code correctly and arrange the layout.
- CSS - This site uses CSS to aid in the style, and overall theme of the website
- Bootstrap - This site uses Bootstrap elements to help design the framework of the site
- Django - This was the chosen framework for developing the project
- Python - This language was chosen to code the a large amount of the functionality of the site
- JavaScript - this was used to program some of the features on the site, such as the messages timeout
- Balsamiq - This was used to create the wireframes in the design phase
- Heroku - This was chosen to host the website app for deployment.
- Coverage - This reporting tool was installed and used to produce reports showing how much of the apps had been tested
- Cloudinary - Cloudinary storage was set up and used for storing website images
- Postgres - This Relational Datatabase was used to handle the data storage

### Database
- The website is a data-centric one with html, javascript, css used with the bootstrap(version 5) framework as a frontend
- The backend consists of Python built with the Django framework with a database of a Postgres for the deployed Heroku version(production)
- Postgres is a powerful, open source object-relational database system (https://www.postgresql.org/)
- A SQLLite database was used for local development (https://www.sqlite.org/index.html)

#### Physical database diagram
This model contains all fields stored in the database collections with their data type and mimics the structure of what is actually stored in the Postgres database
<br>![Database diagram](static/readme_images/database/database-diagram.png)


#### Models
- The following models were created to represent the database model structure for the website
##### User Model
- The User model contains information about the user. It is part of the Django allauth library
- The model contains the following fields: username, password, first_name, last_name, email, is_staff, is_active, is_superuser, last_login, date_joined

##### Booking Model
- The Booking model contains information about reservations made in the restaurant.
- It contains the User model as a foreign-key.
- The model contains the following fields: booking_Id, primary_guest, Slug, availability, booking_status, dietary_notes, additional_comments, no_of_guests, no_of_tables.

##### Review Model
- The Review model contains a review of the establisment by a user/guest
- It contains the User model as a foreign key.
- The model contains the following fields: reviewId, authorID, title, slug, content, excerpt, status, featured_image, updated_on, created_on.

##### Comment Model
- The Comment model contains a comment on a review
- It contains the User Model as a foreign-key and Review model as a foreign-key.
- The model contains the following fields: commentID, reviewID, name, email, body, created_on, approved.

## Testing
### User Credentials
There are two main uses on this site; a site member and a site staff member. Please use the logins below to access and review both user types:

#### Test User
- Username: testuser
- Password: administration

#### Admin User
- Username: admin
- Password: administration

### Manual
As there are many pages for the fine-wine-n-dine website which had to be manually tested to ensure functionality and UX were correct, they have been included in a separate file to avoid taking up too much space on the README.md documentation.

Please see the manual_testing.md file for the full breakdown of the manual testing done for this site. You can click [**here**](https://github.com/BrianStritch/Brian-Stritch-P4-Fine-Wine-n-Dine/blob/main/manual-testing.md)  to reach the file.

During this process, several issues were discovered which have been since fixed on the site. Some examples of these include;

- The standard UserChangeForm in django did not provide the fields for updating the users first_name and last_name and a custom form was required which inherited from the UserChangeForm but was getting a 404 error on submitting. The fix for this error was add a reverse url in the form model to execute when the form was completed and submitted.

- On creating the booking form, an error was found where the primary_guest id was found to be null and must be an instance of User as the booking model primary_guest field was a foreign key of the User model and the fix for this error was to declare the form.instance.primary_guest = request.user which rectified this issue.

- The edit booking view rendered a form however this raised an error where the primary guest was null and this data could not be obtained from the POST request as it was not part of the data sent by the POST request and was not an inherited value. To rectify this error a primary key value of the user had to be passed with the url in the edit button on the bookings detail page, which in turn passed the value to the edit booking page which was then passed with the POST request and the form was then validated and saved. This same issue was found for the delete booking view, edit review, delete review, edit comment, delete comment, edit user profile and delete user profile where a value was needed to be sent with the url in the button

- When the application was deployed on heroku a 500 internal server error was noted on some of the pages when selected and it was found that {% load static %} was not at the top of all documents as i thought it was only required in the base.html file. By placing the {% load static %} statement on the top of all the required pages this rectified this error.

- When the project was deployed to heroku it was found that if the user registration form, create booking form, edit booking form, create review form, edit review form, create comment form, edit comment forms contained any invalid data that the a 500 internal server error was raised and the application would halt. After revising the vews.py files for the respected form views it was found that an if statement was checking the validity of the form data if the data was valid would then save the data to the database. There was no else statement attached and this meant that the application could not process the data and there was no alternative path. To rectify this issue i added an else statement which redirected the user to the required page where the user could resubmit the data.

- The application is set up to allow a maximum of 60 guests in one hour, and each booking can accomodate up to 10 guests at a table and when a booking is created, the POST request data is checked against two database queries to detemine if the booking can be validated. The first check against the database is to check if the user who is making the booking has already chosen the time and dates submitted and if so will return the user to the booking form page with a message notifying them that they have already created a booking for this date and time and to choose an alternative time or date. The second check against the database checks how many bookings have been created for this specific time and date and if there is an available space will save the booking, and if no space is available, will return the user to the booking form page with a message notifying them that they have already created a booking for this date and time and to choose an alternative time or date. On creating this logic it was found that the standard django updateview allowed the bookings to be edited and did not apply the logic as per the booking creation form. The fix for this issue was to create a custom view with GET and POST requests and apply the same logic to the POST request as the booking creation form to check the validity of the updated data prior to saving to the database.

- During manual testing it was noted that the color schemes were displayed differently between browsers. The tests were carried out on chrome mobile browser and samsung internet browser where differences were noted. please see below images displaying same:

###### Google Chrome mobile browser
![Google Chrome mobile browser](static/readme_images/google-chrome-browser.jpg "Google Chrome mobile browser")

###### Samsung mobile browser
![Samsung mobile browser](static/readme_images/samsung-internet-browser.jpg "Samsung mobile browser")

There are other issues that could not be fixed due to ability / time contraints that have been included in the "Bugs Found" section below. 
<hr>

### Validation

<hr>

#### CSS
The custom.css file code was validated using the The W3C CSS Validation Service and the image below verifies that the code was successfully validated with no errors. Numerous warnings were noted which relate to the bootstrap CSS files inherited with the template, however none of the custom css written for this web application failed or had any warnings present.

![W3C CSS Validation](static/readme_images/w3c_validation/W3C-CSS-validation.JPG "W3C CSS validation")

<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>
     

<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
</p>
       
<hr>

#### HTML

All HTML pages have been checked using the W3C Markup Validation Service. Some Errors were found in the Edit_profile.html page which relate to the fields automaticaly rendered using crispy forms.

Some of the page urls were raising a 500 error when the validator attempted to test the page, however to avoid this, the page source code was used for testing, however the tool pointed to several small issues on some pages that were of no consequence, such as opening p tags not being found for a closing /p tag, when they were present in the code, however these issues only related to the crispy forms mentioned above.

Please see the w3c-validation.md file for the full breakdown of the HTML W3C validation testing done for this site. You can click[**here**](https://github.com/BrianStritch/Brian-Stritch-P4-Fine-Wine-n-Dine/blob/main/w3c-validation.md) to reach the file. 


#### JavaScript
JS Hint was used to ensure that the JavaScript used in the website had no errors.

![JSHint report](static/readme_images/JSHint/JSHint-report.JPG "JSHint report")

### Python
All python code pages have been tested to ensure it meets PEP8 standards and the results of which can be found by clicking [**here**](https://github.com/BrianStritch/Brian-Stritch-P4-Fine-Wine-n-Dine/blob/main/pep8-testing.md) to reach the file. 

### Accessibility
All HTML pages have been tested for accessibility and performance using Chrome Devtools Lighthouse testing platform and the results of which can be found by clicking [**here**](https://github.com/BrianStritch/Brian-Stritch-P4-Fine-Wine-n-Dine/blob/main/accessibility-tests.md) to reach the file. 

### Automated
#### Django / Coverage
Django tests were written and Coverage was used to product detailed reports to ensure the sites apps were tested as much as possible. On testing the applicatin with coverage it was noted that an overall score of 85% was obtained.

1. In the terminal, use: "coverage report"
    - generates a detailed report showing what has/what needs testing

2. In order to product a html report which allows you to inspect in each file, to see in easy to use colour codes the lines of code which have been tested or which have not yet been tested, please use the following command: "coverage html"

##### __Coverage report page 1__
![coverage report page 1](static/readme_images/coverage-report-results/Coverage-report-page-1.JPG "coverage report page 1")
##### __Coverage report page 2__
![coverage report page 2](static/readme_images/coverage-report-results/Coverage-report-page-2.JPG "coverage report page 2")


##### Unittest
In order to run tests on GitPod using unittest (which has been installed to handle testing), please follow the below steps in the terminal on GitPod:

1. In fine-wine-n-dine settings.py the database needs to be switched to the local database as the tests will not run when on the heroku postgres database. The loal database is kept in commented out form to allow switching of the database for testing purposes.

2. Run the following code : "pyhton3 manage.py test"
    - This will run a test on all test.py files in the app and will display in the terminal if all tests are passing, and if it does not it will show the error causing the test to fail.

### Responsiveness
This website has been designed to scale correctly to different screen sizes with no issues on layout. In order to ensure that the view was pleasant to the user, certain divs and items had to be arranged differently or hidden/shown depending on screen size. This was handled using CSS media queries.

##### Desktop Size
![Full Size Menu](static/readme_images/responsive-testing/full-screen-navigation-menus.JPG "An example of how the menu looks on a desktop screen")

##### Tablet Size Screen Navigation Menu
![Small Screen Menu](static//readme_images/responsive-testing/moile-and-tablet-sized-screen-navigation-menus.JPG "An example of how the menu looks on a small/mobile screen")

##### Mobile Size Home Page
![Mobile Screen home page](static//readme_images/responsive-testing/mobile-sized-screen-home.JPG "An example of how the home page looks on a mobile screen")

##### Mobile Size Home Page Navigation 
![Mobile Screen Menu](static//readme_images/responsive-testing/mobile-sized-screen-navigation-menus-.JPG "An example of how the menu looks on a mobile screen")

##### Tablet Size Bookings Page Navigation Menu 
![Small Screen Menu Additional nav for Bookings](static/readme_images/responsive-testing/bookings-additional-nav-small-screen-size.JPG "An example of how the menu looks on a small screen with additional nav for bookings")

##### Tablet Size Reviews Page Navigation Menu 
![Small Screen Menu Additional nav for Reviews](static/readme_images/responsive-testing/reviews-additional-nav-small-screen-size.JPG "An example of how the menu looks on a small screen with additional nav for reviews")

##### Tablet Size Admin Page Navigation Menu 
![Small Screen Menu Additional nav for Admin](static/readme_images/responsive-testing/administration-additional-nav-small-screen-size.JPG "An example of how the menu looks on a small screen with additional nav for admin")

In order to ensure that the navigation bar was as responsive as possible, on Desktop the menu shows accross the top of the page while on mobile screens, the menu reduced to a burger icon wide visible button. When the burger icon is clicked, the menu appears as a dropdown with the links to other pages from the nav bar. 

On the bookings page there is an additional nav bar which contains the link to create a booking which drops down with the navigation menu only on the bookings page. 

On the reviews page there is an additional nav bar which contains the link to create a review which drops down with the navigation menu only on the reviews page. 

On the admin bookings page there is an additional nav bar which contains the links to pending bookings, approved bookings, completed bookings and all bookings which drops down with the navigation menu only on the admin bookings page. 

Each page was altered slightly between mobile and desktop for its layout to ensure that the user is getting the best UX possible, regardless of the screen size they are using. This can be seen in the wireframes section as I have included a wireframe of each page with desktop and mobile view. 

### Bugs Found
- When the application was deployed on heroku a 500 internal server error was noted on some of the pages when selected and it was found that {% load static %} was not at the top of all documents as i thought it was only required in the base.html file. By placing the {% load static %} statement on the top of all the required pages this rectified this error.

- During the manual testing it was found that the user did not know that by clicking the username that it would redirect to the user profile details page. This issue was rectified by renaming the link.

- When the project was deployed to heroku it was found during manual testing that if the user registration form, create booking form, edit booking form, create review form, edit review form, create comment form, edit comment forms contained any invalid data that the a 500 internal server error was raised and the application would halt. After revising the vews.py files for the respected form views it was found that an if statement was checking the validity of the form data if the data was valid would then save the data to the database. There was no else statement attached and this meant that the application could not process the data and there was no alternative path. To rectify this issue i added an else statement which redirected the user to the required page where the user could resubmit the data.

- It was found during manual testing that some of the page urls were raising a 500 error when the user attempted to test the page, this was rectified by including the {% load static %} tag on all required pages.

- During manual testing it was found that the user did not know that by clicking the booking in the bookings view that it would redirect the user to the booking details page where the user could then edit or delete the booking.The booking card in the bookings page was displaying too much information and the user was able to view all the booking details without selecting the booking and being redirected to the booking details page. To fix this error the information displayed was significantly reduced and a message was displayed to the user to "click on a booking to view booking details".

- During manual testing numerous issues with styling and layouts were noted which required modifications to the bootsrap classes to display the content as required in this application.

- During manual testing it was noted that the color schemes were displayed differently between browsers. The tests were carried out on chrome mobile browser and samsung internet browser where differences were noted. please see below images displaying same:

###### Google Chrome mobile browser
![Google Chrome mobile browser](static/readme_images/google-chrome-browser.jpg "Google Chrome mobile browser")

###### Samsung mobile browser
![Samsung mobile browser](static/readme_images/samsung-internet-browser.jpg "Samsung mobile browser")

## Deployment
This project was deployed to Heroku at the address **https://b-stritch-p4-fine-wine-n-dine.herokuapp.com/** using the following steps

### GitHub:
- Create a new project on GitHub
- Click the green Gitpod button to open in Gitpod

#### To commit the code on GitPod to GitHub:
- In the terminal, type "git add ." to add all new changes to the code to staging area
- Next, type "git status" to see which files are ready to be commited
- Commit these by typing "git commit -m" and adding a detailed description of the commit in ""
- Next, push the code commit to GitHub by typing "git push"

### Heroku:
- Create a Heroku account
- Create a new app
- Link the Heroku app with your GitHub repository
- Push changes to git using the terminal and verify that the connection to Heroku is working
- Add environment variables to Heroku settings.
- In Heroku click the deploy tab, click on deploy to deploy the latest branch of your repository
    - You can click on automatic deployment where each new push to github will be deployed to heroku

## Credits
### Content
- Font icons imported from FontAwesome. 
### Media
As there are many images for the reviews in this website, most of which were obtained from Pexels.com, shutterstock.com and some images obtained from the establishment facebook page.

### Acknowledgements
- I would like to acknowledge my mentor Mo Shami for all of his help and advice with this project
- I would like to thank my friends and family for their testing help and advice with this project
- I would like to thanks the establishment management of Nannys for permission to use the images from their facebook site.