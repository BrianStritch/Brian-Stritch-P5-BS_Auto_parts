# DATABASE MODELS

#### Models
- The following models were created to represent the database model structure for the website
##### User Model
- The User model contains information about the user. It is part of the Django allauth library
- The model contains the following fields: username, password, first_name, last_name, email, is_staff, is_active, is_superuser, last_login, date_joined

##### UserProfile Model
- The UserProfile model has a one-to-one relationship with User
- The model contains the following fields: default_phone_number, default_street_address1, default_street_address2
default_town_or_city, default_county, default_postcode, default_county and default_country

##### Order Model
- The Order model contains information about orders made on the website.
- It contains UserProfile as a foreign-key.
- The model contains the following fields: order_number, user_profile, full_name, email, phone_number, country, postcode, town_or_city, street_address1
, street_address2, county, date, delivery_cost, order_total, grand_total, original_bag, stripe_pid

##### OrderLineItem Model
- The OrderLineItem model contains information about an entry in an order, for orders made on the website.
- It contains Order and Product as foreign-keys.
- The model contains the following fields: order, product, product_size, quantity, lineitem_total

##### Favourites Model
- The Favourites model contains a users favourite products
- It contains Products as one-to-one field, and User as a one-to-one relationship
- The model contains the following fields: products, username

##### Product Model
- The Product Model represents a product and its details
- It contains Category as a foreign-key
- The model contains the following fields: category, stock_no, name, description, suits, stock_qty, on_sale, has_sizes, price, rating,  image_url, image
- The image field contains the product image
- The image_url field contains the url to where the image file is physically stored, for example AWS S3 bucket

##### Category Model
- The Category model contains a product category
- The model contains the following fields: name, friendly_name

##### Manufacturer Model
- The Category model contains a manufacturer category, to be used in relation to the seach by manufacturer field in the store.
- The model contains the following fields: name, friendly_name

##### Newsletter Model
- The Newsletter model contains an email address and subscription ststus for newsletter subscribers
- The model contains the following fields: email, opt-in status

##### Product Review Model
- The product review model represents a review made on a specific product
- It contains product, and review comment as a foreign-key
- The model contains the following fields: product, title, slug, author, updated_on, content, summary, created_on, status, likes

##### Product Review Comments Model
- The News model contains a comment on a new story
- It contains product review as a foreign-key
- The model contains the following fields: product_review, name, email, body, created_on, approved

##### Forum Category Model
- The Forum Category model contains a Forum Category
- The model contains the following fields: name, slug, friendly_name

##### Forum topics Model
- The Forum topic model contains a Forum Topic
- It contains Forum Category as a foreign key
- The model contains the following fields: name, slug, friendly_name

##### Forum post Model
- The Forum post model contains a post in a specific forum category.
- It contains Forum Topic as a foreign-key
- The model contains the following fields: title, slug, author, topic, updated_on, content, summary, created_on, status, likes

##### Forum post comments Model
- The Forum post comments model contains a comments of a forum post by a user
- It contains forum post as a foreign-key.
- The model contains the following fields: user, product, product_rating, review_text, create_date

##### site Users Contact Details Model
- The site Users Contact Details model contains a message from a site user who wishes to contact admin.
- The model contains the following fields: name, surname , email, message, status,  created_on, phone_number, street_address1, street_address2, town_or_city, county, country, postcode

##### Existing Users Contact Details Model
- The Existing Users Contact Details model contains a message from a registered site user who wishes to contact admin.
- It contains forum User as a foreign-key.
- The model contains the following fields: user, message, status, created_on 
