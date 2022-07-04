    # def test_add_review_to_product_failure(self):
    #     """
    #     This test tests add review to product as a failed case and verifies
    #     """
    #     self.client.login(username='test_user', password='test_password')
    #     product = Product.objects.get()
    #     response = self.client.post(f'/products/add_review/{product.id}/')
    #     messages = list(get_messages(response.wsgi_request))
    #     self.assertEqual(str(messages[0]), "Failed to add product review")

    # def test_add_review_to_product(self):
    #     """
    #     This test tests add review to product as a success case and verifies
    #     """
    #     test_user = User.objects.create_user(
    #         username='test_user1', password='test_password')
    #     self.client.login(username='test_user', password='test_password')
    #     product = Product.objects.get()

    #     Review.objects.create(
    #         user=test_user,
    #         product=product,
    #         product_rating='5',
    #         review_text='Test Review Text',
    #     )
    #     response = self.client.post(f'/products/add_review/{product.id}/',
    #                                 {'product_rating': '5',
    #                                  'review_text': 'Test Review Text'})
    #     messages = list(get_messages(response.wsgi_request))
    #     self.assertEqual(str(messages[0]), "Successfully added a review!")

    # def test_add_two_review_one_user_to_product(self):
    #     """
    #     This test tests add two reviews to a product, failure case and verifies
    #     """
    #     test_user2 = User.objects.create_user(
    #         username='test_user2', password='test_password')
    #     self.client.login(username='test_user', password='test_password')
    #     product = Product.objects.get()

    #     Review.objects.create(
    #         user=test_user2,
    #         product=product,
    #         product_rating='5',
    #         review_text='Test Review Text',
    #     )
    #     self.client.post(f'/products/add_review/{product.id}/',
    #                      {'product_rating': '4',
    #                       'review_text': 'Test Review Text1'})
    #     response = self.client.post(f'/products/add_review/{product.id}/',
    #                                 {'product_rating': '3',
    #                                  'review_text': 'Test Review Text2'})
    #     messages = list(get_messages(response.wsgi_request))
    #     self.assertEqual(str(messages[0]), "Successfully added a review!")
    #     self.assertEqual(str(messages[1]), "You have already reviewed "
    #                                        "this product!")

    # def test_delete_review_from_product(self):
    #     """
    #     This test tests delete review from a product and verifies
    #     """
    #     test_user2 = User.objects.create_user(
    #         username='test_user4', password='test_password')
    #     self.client.login(username='test_user4', password='test_password')
    #     product = Product.objects.get()

    #     Review.objects.create(
    #         user=test_user2,
    #         product=product,
    #         product_rating='5',
    #         review_text='Test Review Text',
    #     )
    #     response = self.client.post(
    #         f'/products/delete_review/{product.id}/{test_user2.username}/')
    #     messages = list(get_messages(response.wsgi_request))
    #     self.assertEqual(str(messages[0]), "Your review was deleted")

    # def test_delete_review_from_product_no_permission(self):
    #     """
    #     This test tests delete review from a product and verifies
    #     """
    #     test_user2 = User.objects.create_user(
    #         username='test_user2', password='test_password')
    #     self.client.login(username='test_user', password='test_password')
    #     product = Product.objects.get()

    #     Review.objects.create(
    #         user=test_user2,
    #         product=product,
    #         product_rating='5',
    #         review_text='Test Review Text',
    #     )
    #     self.client.post(f'/products/add_review/{product.id}/',
    #                      {'product_rating': '4',
    #                       'review_text': 'Test Review Text1'})
    #     response = self.client.post(
    #         f'/products/delete_review/{product.id}/{test_user2.username}/')
    #     messages = list(get_messages(response.wsgi_request))
    #     self.assertEqual(str(messages[0]), "Successfully added a review!")
    #     self.assertEqual(str(messages[1]), "Sorry, you don't have permission "
    #                                        "to do that.")

    # def test_get_average_rating_two_reviews(self):
    #     """
    #     This test tests delete review from a product and verifies
    #     """
    #     product = Product.objects.get()
    #     test_user3 = User.objects.create_user(
    #         username='test_user3', password='test_password')
    #     self.client.login(username='test_user3', password='test_password')
    #     review1 = Review.objects.create(
    #         user=test_user3,
    #         product=product,
    #         product_rating='5',
    #         review_text='Test Review Text',
    #     )
    #     test_user4 = User.objects.create_user(
    #         username='test_user4', password='test_password')
    #     self.client.login(username='test_user4', password='test_password')
    #     review2 = Review.objects.create(
    #         user=test_user4,
    #         product=product,
    #         product_rating='4',
    #         review_text='Test Review Text 2',
    #     )
    #     reviews = Review.objects.filter(product=product)
    #     average_rating = get_average_rating(reviews)
    #     self.assertEqual(average_rating, 4.5)

    # def test_get_average_rating_no_reviews(self):
    #     """
    #     This test tests delete review from a product and verifies
    #     """
    #     product = Product.objects.get()
    #     reviews = Review.objects.filter(product=product)
    #     average_rating = get_average_rating(reviews)
    #     self.assertEqual(average_rating, 0)

 # def test_edit_product_page(self):
    #     """
    #     This test tests edit product page(post) as a superuser and verifies
    #     """
        
    #     product = Product.objects.get()
    #     response = self.client.post(f'/products/edit/{product.id}/', {            
    #         'stock_no' : 'test_stock_no',
    #         'name':'Test Name',
    #         'price':'99.99',
    #         'description':'Test Description', 
    #         'suits' : 'universal',
    #         'stock_qty' : '1',
    #         'on_sale' : 'True',
    #         'has_sizes' : 'False',            
    #         'rating' : '4.8',
    #         'image_url' : 'test_url',
    #         'image' : 'test_image.jpg',
    #     })
    #     updated_product = Product.objects.get()
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'products/edit_product.html')
    #     self.assertEqual(updated_product.name, 'Test Name Update')
    #     self.assertEqual(updated_product.description, 'Test Description Update')
