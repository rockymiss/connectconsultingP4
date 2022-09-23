# Testing

## Validation

### Html Validation

Html validation was done with [https://validator.w3.org/](https://validator.w3.org/). All pages were tested by manually inputting the code into the validator.

There were a few issues in relation to validation

1. I used a python library called Summernote.  The errors came from Summernote and not the code I had created.  

2. By using bootstrap accordion for comments and messages stray tags and duplicate aria-labelled by were generated.  

Despite numerous hours researching these errors unfortunately I was unable to fix the issue for now. 

#### **Home Page**

![Home Page](static/images/readme/validation/index_valid.png)

#### **About Page**

![About Page](static/images/readme/validation/about-valid.png)

#### **User Sign-Up Pages**

![Sign-In Page](static/images/readme/validation/sign-in-validation.png)
![Sign-Out Page](static/images/readme/validation/sign-out-validation.png)
![Sign-Up Page](static/images/readme/validation/sign-up-validation.png)

#### **Blog Pages**

Errors showing are in relation to summernote as mentioned above.

![Blog List Page](static/images/readme/validation/create-blog-validation-errors.png)
![Delete Blog Page](static/images/readme/validation/delete-blog-validation.png)
![Update Blog Page](static/images/readme/validation/update-blog-validation.png)
![Blog-Detail Page](static/images/readme/validation/blog-detail-validation.png)
![Draft-Blog Page](static/images/readme/validation/draft-blog-valid.png)

#### **Comment Pages**
![Review Comments Page](static/images/readme/validation/review-comments-validation.png)
![Approve Commment Page](static/images/readme/validation/approve-comments-valid.png)
![Delete Comment Page](static/images/readme/validation/delete-comment-validation.png)

#### **Testimonial Pages**

Errors showing are in relation to bootstrap errors as mentioned above.

![Create Testimonial Page](static/images/readme/validation/create-testimonial-valid.png)
![Review Testimonial Page](static/images/readme/validation/review-testimonial-validation.png)
![Approve Testimonial Page](static/images/readme/validation/approve-testimonial-validation.png)
![Delete Testimonial Page](static/images/readme/validation/delete-testimonial-valid.png)
![View Testimonial Page](static/images/readme/validation/view-testimonials-valid.png)

#### **Contact pages**

Errors showing are in relation to bootstrap errors as mentioned above. 

![Contact Us Page](static/images/readme/validation/contact-us-valid.png)
![View Messages Page](static/images/readme/validation/view-message-validation.png)
![Delete Messages Page](static/images/readme/validation/delete-message-valid.png)
![Thank You Page](static/images/readme/validation/thank-you-valid.png)

#### **Error Pages**
![403 Error Page](static/images/readme/validation/403-validation.png)
![404 Error Page](static/images/readme/validation/404-validation.png)


### CSS Validation

The stylesheet was validated using [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)

![Stylesheet validation](static/images/readme/misc/css-validation.png)


### Python Validation

Python code was validated using [http://pep8online.com/](http://pep8online.com/).  I also used the GitPod workspace to check for errors as I coded.  I found this useful as there were less errors once I ran the code through the validator. 


### blogcc files

#### admin.py

![pep8 admin.py](static/images/readme/pep8/blogcc-admin.png)

#### apps.py

![pep8 apps.py](static/images/readme/pep8/blogcc-apps.png)

#### forms.py

![pep8 forms.py](static/images/readme/pep8/blogcc-forms.png)

#### models.py

![pep8 models.py](static/images/readme/pep8/blogcc-models.png)

#### urls.py

![pep8 urls.py](static/images/readme/pep8/blogcc-urls.png)

#### views.py

![pep8 views.py](static/images/readme/pep8/blogcc-views.png)

### blogconnect files

#### admin.py

![pep8 admin.py](static/images/readme/pep8/blogconnect-admin.png)

#### apps.py

![pep8 apps.py](static/images/readme/pep8/blogconnect-apps.png)

#### asgi.py

![pep8 asgi.py](static/images/readme/pep8/blogconnect-asgi.png)

#### forms.py

![pep8 forms.py](static/images/readme/pep8/blogconnect-forms.png)

#### models.py

![pep8 models.py](static/images/readme/pep8/blogconnect-models.png)

Errors were noted doing a validation on settings.py however as most of the file is automatically created when installing Django I did not correct them as it made no difference to the workings of the website.

#### settings.py
![pep8 settings.py](static/images/readme/pep8/blogconnect-settings.png)

#### urls.py
![pep8 urls.py](static/images/readme/pep8/blogconnect-urls.png)

#### wsgi.py
![pep8 wsgi.py](static/images/readme/pep8/blogconnect-wsgi.png)

### contact files

#### admin.py

![pep8 admin.py](/workspace/connectconsultingp4/static/images/readme/pep8/contact-admin.png)

#### apps.py

![pep8 apps.py](static/images/readme/pep8/contact-apps.png)

#### forms.py

![pep8 forms.py](static/images/readme/pep8/contact-forms.png)

#### models.py

![pep8 models.py](static/images/readme/pep8/contact-models.png)

#### urls.py

![pep8 urls.py](static/images/readme/pep8/contact-urls.png)

#### views.py

![pep8 views.py](static/images/readme/pep8/contact-views.png)

#### Gitpod Workspace

![Workspace](static/images/readme/pep8/contact-views.png)


## Lighthouse Testing

All pages were checked on lighthouse.  Results were over 90% for performance and best practice and 100% on Accessability and SEO on both mobile and desktop.  On the first test performance was very poor.  This was fixed by applying height and width to an image.


### **First Test**

![Lighthouse Poor Performance](static/images/readme/misc/lighthouse-first-test.png)

### **Lighthouse Picture Performance**

![Lighthouse Picture Performance](static/images/readme/misc/Lighthouse-pictures-width.png)

### **Final Test**

![Final Lighthouse Test](static/images/readme/misc/Lighthouse-fix-test.png)


## Manual Testing

To ensure that all elements of the website were working I carried out a detailed manual test and checked off the list as I went.

| Status | **Navigation Logged Out**
|:-------:|:--------|
| &check; |:Clicking the Connect Consulting Logo brings you to the homepage
| &check; |:The only menus that can be viewed are About, Testimonials, Blogs, Contact Us and Login
| &check; |:On the Testimonials drop down View Testimonials and Create Testimonials can be viewed
| &check; |:On the Login drop down Log-In and Register can only be viewd
| &check; |:The Admin Only drop down cannot be viewed
| &check; |:Clicking About brings you to the about page
| &check; |:Clicking Testimonials opens a dropdown menu showing View Testimonals and Create Testimonials
| &check; |:Clicking View Testimonials brings you to the View Testimonials page
| &check; |:Clicking Create Testimonials brings you to the Sign-In page
| &check; |:Clicking Blogs brings you to the Blog list page
| &check; |:Clicking Contact Us brings you to the Contact page
| &check; |:Clicking Log-In opens a dropdown menu showing Log-in and Register
| &check; |:Clicking Log-In opens a the Sign-In page
| &check; |:Clicking Register opens the Sign-Up page

| Status | **Navigation Logged In - User**
|:-------:|:--------|
| &check; |:Clicking the Connect Consulting Logo brings you to the homepage
| &check; |:The only menus that can be viewed are About, Testimonials, Blogs, Contact Us and Logout
| &check; |:On the Testimonials drop down View Testimonials and Create Testimonials can be viewed
| &check; |:On the Logout drop down Log-Out can only be viewd
| &check; |:The Admin Only drop down cannot be viewed
| &check; |:Clicking About brings you to the about page
| &check; |:Clicking Testimonials opens a dropdown menu showing View Testimonals and Create Testimonials
| &check; |:Clicking View Testimonials brings you to the View Testimonials page
| &check; |:Clicking Create Testimonials brings you to the Create Testimonials page
| &check; |:Clicking Blogs brings you to the Blog list page
| &check; |:Clicking Contact Us brings you to the Contact page
| &check; |:Clicking Log-out opens a dropdown menu showing Log-out
| &check; |:Clicking Log-out opens a the Sign-Out page asking the user if they are sure they want to sign out

| Status | **Home Page**
|:-------:|:--------|
| &check; |: All users should see a Navigation Bar at the top of the page which stays fixed if the user needs to scroll down
| &check; |: All users should see a footer at the bottom of the page
| &check; |: All users should see a white background with some circular yellow shape in it
| &check; |: All users should see a CC logo at the top of the page with the words Hospitality Specialists written over it 
| &check; |: All users should see a Heading with the words 'Who dares wins'
| &check; |: All users should see information about Connect Consulting which clearly sets out what Connect Consulting do


| Status | **About**
|:-------:|:--------|
| &check; |: All users should see a Navigation Bar at the top of the page which stays fixed if the user needs to scroll down
| &check; |: All users should see a footer at the bottom of the page
| &check; |: All users should see a white background with some circular yellow shape in it
| &check; |: All users should see an image of a smiling man wearing glasses leaning up against a wall
| &check; |: All users should see information about that man and what Connect Consulting do and why the user should use their services.


| Status | **View Testimonials**
|:-------:|:--------|
| &check; |: The user should see a Navigation Bar at the top of the page which stays fixed if the user needs to scroll down
| &check; |: The user should see a footer at the bottom of the page
| &check; |: The user should see a white background with some circular yellow shape in it
| &check; |: The user should see testimonials, 3 to a page in cards with a header showing the company name and the content below with the date the Testimonial was created
| &check; |: The header of each card should have a gradient effect
| &check; |: The user should see a button on the bottom of the page with the word 'Next' if there are more than 3 testimonials.
| &check; |: The user should be brought to another page of testimonials if they click the Next button 
| &check; |: The user should see two buttons with the words 'Prev' and 'Next' on the second page or any subsequent page
| &check; |: The user should be brought back to the previous page if they click the 'Prev' button 
| &check; |: The user should only see the button 'Prev' on the last page of testimonials


| Status | **Create Testimonials Logged In-User**
|:-------:|:--------|
| &check; |: The user should see a Navigation Bar at the top of the page which stays fixed if the user needs to scroll down
| &check; |: The user should see a footer at the bottom of the page
| &check; |: The user should see a white background with some circular yellow shape in it
| &check; |: The user should see a form with the heading 'Create your Testimonial'
| &check; |: The user should see input fields for Name, Company Name and Content
| &check; |: The user should see a functional submit button at the bottom of the form
| &check; |: If the user completes the form fully and clicks submit they should see a message at the top of the page telling them the testimonial has been submitted for approval to admin
| &check; |: If the user does not complete the 'Name' field the user will get an error message 
| &check; |: if the user does not complete the 'Company Name' field the user will get an error message
| &check; |: If the user does not complete the 'Content' field the user will get an error message

| Status | **Blogs/Blog List Logged or Not Logged In**
|:-------:|:--------|
| &check; |: The user should see a Navigation Bar at the top of the page which stays fixed if the user needs to scroll down
| &check; |: The user should see a footer at the bottom of the page
| &check; |: The user should see a white background with some circular yellow shape in it
| &check; |: The user should see blogs, 3 to a page in cards with a header showing a picture, The title of the blog, the subtitle, the author and the date created
| &check; |: The user should only see a button 'View Blog'
| &check; |: If the user clicks on 'View Blog' it should direct them to the detailed view of the Blog on it's own
| &check; |: The user should see a button on the bottom of the page with the word 'Next' if there are more than 3 Blogs.
| &check; |: The user should be brought to another page of blogs if they click the Next button 
| &check; |: The user should see two buttons with the words 'Prev' and 'Next' on the second page or any subsequent page
| &check; |: The user should be brought back to the previous page if they click the 'Prev' button 
| &check; |: The user should only see the button 'Prev' on the last page of testimonials

| Status | **Blog/BlogList Logged-In Admin User**
|:-------:|:--------|
| &check; |: The admin user should see a Navigation Bar at the top of the page which stays fixed if the user needs to scroll down
| &check; |: The admin user should see a footer at the bottom of the page
| &check; |: The admin user should see a white background with some circular yellow shape in it
| &check; |: The admin user should see a button called 'draft blogs' and when clicked will bring the admin user to a page of blogs not yet publically posted
| &check; |: The admin user should see blogs, 3 to a page in cards with a header showing a picture, The title of the blog, the subtitle, the author and the date created
| &check; |: The admin user should see three buttons below the blog: 'View Blog', 'Edit' and 'Delete'
| &check; |: If the admin user clicks on 'View Blog' it should direct them to the detailed view of the Blog on it's own
| &check; |: If the admin user clicks on 'Edit' it should direct them to the detailed view of the Blog to edit the blog
| &check; |: If the admin user clicks on 'Delete' it should direct them to page asking them if they are sure they want to delete the blog
| &check; |: The user should see a button on the bottom of the page with the word 'Next' if there are more than 3 Blogs.
| &check; |: The user should be brought to another page of blogs if they click the Next button 
| &check; |: The user should see two buttons with the words 'Prev' and 'Next' on the second page or any subsequent page
| &check; |: The user should be brought back to the previous page if they click the 'Prev' button 
| &check; |: The user should only see the button 'Prev' on the last page of testimonials


| Status | **Contact Us**
|:-------:|:--------|
| &check; |: The user should see a Navigation Bar at the top of the page which stays fixed if the user needs to scroll down
| &check; |: The user should see a footer at the bottom of the page
| &check; |: The user should see a white background with some circular yellow shape in it
| &check; |: The user should see a heading with the message 'Send us a message'
| &check; |: The user should see a form to complete with fields: 'First name', 'Last name', 'Email', and 'Message'
| &check; |: The user should get an error message if they don't complete the form fully
| &check; |: The user should see a default email in the email field (this is for testing purposes so users for now do not have to put in their real email address)
| &check; |: The user should see placeholder text in the message field saying 'We would love to hear from you'
| &check; |: If the user completes the form correctly they should be redirected to a thank you page when they click submit

| Status | **Thank You**
|:-------:|:--------|
| &check; |: The user should see a Navigation Bar at the top of the page which stays fixed if the user needs to scroll down
| &check; |: The user should see a footer at the bottom of the page
| &check; |: The user should see a white background with some circular yellow shape in it
| &check; |: The user should see the CC Connect Consulting logo with the message 'Thank you for your message'

| Status | **Log-out User and Admin**
|:-------:|:--------|
| &check; |: If the user clicks 'Log-Out' on the menu bar they should be directed to a sign-Out Page asking them are they sure they want to sign out. 
| &check; |: The user should see a heading 'Sign Out' and a message saying 'Are you sure you want to sign out'
| &check; |: The user should see a button with the words 'Sign Out' and once clicked will sign the user out. 
| &check; |: The user should be redirected to the homepage and see a message confirming that they have signed out. 
| &check; |: The user should see a Navigation Bar at the top of the page which stays fixed if the user needs to scroll down
| &check; |: The user should see a footer at the bottom of the page
| &check; |: The user should see a white background with some circular yellow shape in it
| &check; |: The user should see the CC Connect Consulting logo with the message 'Thank you for your message'

| Status | **Log-in User and Admin**
|:-------:|:--------|
| &check; |: If the user clicks 'Log-In' on the menu bar they should be directed to a sign-in Page 
| &check; |: The user should see a heading 'Sign In' and a message saying 'You must be signed in to leave a comment or create a testimonial'
| &check; |: The user should see a 'Username' field and 'password field. 
| &check; |: The user should see a small tick box with the words 'Remember me'.  If selected they will be remembered the next time they log in.
| &check; |: The user should see a 'Sign In' button and when clicked will bring the user to the homepage where a message will pop up telling the user they have successfully signed in.
| &check; |: The user should see a Navigation Bar at the top of the page which stays fixed if the user needs to scroll down
| &check; |: The user should see a footer at the bottom of the page
| &check; |: The user should see a white background with some circular yellow shape in it
| &check; |: The user should see the CC Connect Consulting logo with the message 'Thank you for your message'

 Status | **Register**
|:-------:|:--------|
| &check; |: If the user clicks 'Log-In' on the menu bar they should see 'Register' in the dropdown list'  Once clicked it should open the Sign-up page. 
| &check; |: The user should see a heading 'Sign Up' and a message saying if they already have an account then to click the signin click'
| &check; |: The user should be directed to the Sign-In page if they click the sign-in link
| &check; |: The user should see the fields 'Username', 'Email', 'Password' and 'Password Again'. 
| &check; |: The user should see a 'Sign Up' button and when clicked will bring the user to the homepage where a message will pop up telling the user they have successfully signed up.
| &check; |: The user should see a Navigation Bar at the top of the page which stays fixed if the user needs to scroll down
| &check; |: The user should see a footer at the bottom of the page
| &check; |: The user should see a white background with some circular yellow shape in it
| &check; |: The user should see the CC Connect Consulting logo with the message 'Thank you for your message'


| Status | **Blog Detail Logged Out**
|:-------:|:--------|
 &check; |: The user should see a Navigation Bar at the top of the page which stays fixed if the user needs to scroll down
| &check; |: The user should see a footer at the bottom of the page
| &check; |: The user should see a white background with some circular yellow shape in it
| &check; |: The user should see the CC Connect Consulting logo with the message 'Thank you for your 
| &check; |: The user should see the title of the Blog Post and an image
| &check; |: The user should see blog content
| &check; |: Below the blog content the user should see another image 
| &check; |: The user will see a star and how many likes the blog got
| &check; |: The user shoulld see a comments section with comments
| &check; |: The user should see a message saying you must be logged in to leave comments
| &check; |: The user will see a button with the words 'Login' and once clicked will direct them to the login page

| Status | **Blog Detail Logged In**
|:-------:|:--------|
 &check; |: The user should see a Navigation Bar at the top of the page which stays fixed if the user needs to scroll down
| &check; |: The user should see a footer at the bottom of the page
| &check; |: The user should see a white background with some circular yellow shape in it
| &check; |: The user should see the CC Connect Consulting logo with the message 'Thank you for your 
| &check; |: The user should see the title of the Blog Post and an image
| &check; |: The user should see blog content
| &check; |: Below the blog content the user should see another image 
| &check; |: The user will see a star and how many likes the blog got
| &check; |: The user should see a star and once clicked the star will change color and the number will increase beside it
| &check; |: The user should see a comments section with comments
| &check; |: The user should see a message saying 'Leave a comment' and their name underneath it
| &check; |: The user should see a comment body where they can write a comment
| &check; |: The user should see a submit button and once clicked they will get a message saying their comment has been sent to admin for approval.

| Status | **Update Blog Logged-In Admin User**
|:-------:|:--------|
| &check; |: The admin user should see a Navigation Bar at the top of the page which stays fixed if the user needs to scroll down
| &check; |: The admin user should see a footer at the bottom of the page
| &check; |: The admin user should see a white background with some circular yellow shape in it
| &check; |: The admin user should see a fully populated form with the blog information to edit
| &check; |: The admin user should be able to edit any details of the blog including images
| &check; |: The admin user should see a Submit button, once clicked will redirect the admin user back to the blog list message where a message will pop up saying the blog has been updated.

| Status | **Delete Blog Logged-In Admin User**
|:-------:|:--------|
| &check; |: The admin user should see a Navigation Bar at the top of the page which stays fixed if the user needs to scroll down
| &check; |: The admin user should see a footer at the bottom of the page
| &check; |: The admin user should see a button on the blog list with the word 'Delete'
| &check; |: The admin user should be re-directed to a page asking the user if they are sure they want to delete the blog.
| &check; |: The admin user should see two buttons 'Yes' and 'Go Back'
| &check; |: If the admin user clicks on 'Go Back' they will be re-directed to the blog list page. 
| &check; |: If the admin user clicks on 'Yes' they will be re-directed to the blog list page where a message will confirm that the blog has been deleted.




## Bugs

### 



**Fix:**
