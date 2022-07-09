# AWS Amazon Web Services S3 Bucket and IAM setup 
<hr>

1. Create an account at aws.amazon.com

2. Open the S3 application and select the create bucket button to begin creating your bucket.
<br>![AWS S3 bucket setup 1](../media/readme/amazon_web_services_s3_bucket_setup/how_to_create_s3_bucket/a.JPG)

3. Open the S3 application and create an S3 bucket named as per your project name
<br>![AWS S3 bucket setup 1](../media/readme/amazon_web_services_s3_bucket_setup/how_to_create_s3_bucket/b.JPG)

4. Uncheck the "Block All Public access setting"
<br>![AWS S3 bucket setup 3](../media/readme/amazon_web_services_s3_bucket_setup/how_to_create_s3_bucket/c.JPG)

5. Select the acknoledgement allowing public access to your bucket
<br>![AWS S3 bucket setup 4](../media/readme/amazon_web_services_s3_bucket_setup/how_to_create_s3_bucket/d.JPG)

6. Select the Create Bucket button to create your bucket.
<br>![AWS S3 bucket setup 5](../media/readme/amazon_web_services_s3_bucket_setup/how_to_create_s3_bucket/e.JPG)

7. The bucket is created, the next step is to open the IAM application to set up access so navigate to IAM from the main menu. On the Iam Dashboard select identity and access amnegement and select user groups.
<br>![AWS Static](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/create_new_group/user-groups-selector.JPG)

8. On the Iam Dashboard select create user group.
<br>![AWS Static](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/create_new_group//user-groups.JPG)

9. So next is to select create group button.
<br> ![AWS S3 bucket setup 77](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/create_new_group/create-new-groups-button.JPG)


10. Create a new user group named as per your repository or project name.
<br>![AWS S3 bucket setup 8](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/create_new_group/group-name.JPG)

11. Select Create group to finalise and create your group.
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/create_new_group/create-group.JPG)


12. Next we add a user to the group

13. Select the user tab to add a user to the group.
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/user/user-tab.JPG)

14. We then select add users
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/user/add-new-user-button.JPG)

15. We then set the users details
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/user/create-user-form.JPG)

16. We then select add user to group and select checkbox next to your user and select 'Next tags' to continue
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/user/add-user-to-group-page.JPG)

17. Select the next tags button to continue.
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/user/next-tags-button.JPG)

18. We then select the next review button as we do not need to make any additional changes.
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/user/next-review-button.JPG)

19. We then select the create user button to create our user.
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/user/create-user-button.JPG)

20. We should see a success message indicating that our user has been created succesfully.
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/user/success-message-as-new-user-created.JPG)

21. We then have access to our users .csv file which we download as this contains the users access keys. Note the AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID variables, they are used in other parts of this README for local deployment and Heroku setup
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/user/download-csv-file.JPG)

22. We now select the policies selector.
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/policies%20selector.JPG)

23. Next we select the create new policy button to create a new policy
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/create%20new%20policy%20button.JPG)

24. below is the new policy creation form
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/new%20policy%20creation%20form.JPG)

25. Next we select the JSON tab at the top.
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/select%20json%20tab.JPG)

26. Next we select import managed policy.
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/import%20managed%20policy.JPG)

27. Next we select import s3 full access policy. 
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/import%20s3%20full%20access%20policy.JPG)

28. Next we select edit resource and add our own custom script.
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/edit%20resource.JPG)

29. Below is the updated resource.
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/next%20tags%20button.JPG)

30. Next we navigate to the next tags button.
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/name%20and%20description%20of%20policy.JPG)

31. Next we give our policy a name and description.
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/create%20policy%20button.JPG)

32. Next we select the Create new policy button.
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/user%20groups%20permissions%20tab%20to%20attach%20policy.JPG)

33. next we navigate to the user groups and permissions tab to attach the new policy.
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/attach%20policy%20tab.JPG)

34. Next we select the add permissions button
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/add%20permissions%20button.JPG)

35. Next we should see our newly added policy.
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/iam_policy/newly%20added%20policy.JPG)


36. Next we navigate to our workspace and update the settings.py file in the top level of our project.
<br>![AWS S3 iam setup 1](../media/readme/amazon_web_services_s3_bucket_setup/iam_setup/update%20settings.py%20file%20in%20main%20app%20to%20use%20bucket.JPG)

