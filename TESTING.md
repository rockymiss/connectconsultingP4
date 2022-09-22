# Testing

## Validation

### Html Validation

Validation was carried out using 

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
![Create Testimonial Page](static/images/readme/validation/create-testimonial-valid.png)
![Review Testimonial Page](static/images/readme/validation/review-testimonial-validation.png)
![Approve Testimonial Page](static/images/readme/validation/approve-testimonial-validation.png)
![Delete Testimonial Page](static/images/readme/validation/delete-testimonial-valid.png)
![View Testimonial Page](static/images/readme/validation/view-testimonials-valid.png)

#### **Contact pages**
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


#### blogcc

![pep8 admin.py](static/images/readme/pep8/blogcc-admin.png)

![pep8 apps.py](static/images/readme/pep8/blogcc-apps.png)

![pep8 forms.py](static/images/readme/pep8/blogcc-forms.png)

![pep8 models.py](static/images/readme/pep8/blogcc-models.png)

![pep8 urls.py](static/images/readme/pep8/blogcc-urls.png)

![pep8 views.py](static/images/readme/pep8/blogcc-views.png)

#### blogconnect

![pep8 admin.py](static/images/readme/pep8/blogconnect-admin.png)

![pep8 apps.py](static/images/readme/pep8/blogconnect-apps.png)

![pep8 asgi.py](static/images/readme/pep8/blogconnect-asgi.png)

![pep8 froms.py](static/images/readme/pep8/blogconnect-forms.png)

![pep8 models.py](static/images/readme/pep8/blogconnect-models.png)

Errors were noted doing a validation on settings.py however as most of the file is automatically created when installing Django I did not correct them as it made no difference to the workings of the website.  
![pep8 settings.py](static/images/readme/pep8/blogconnect-settings.png)

![pep8 urls.py](static/images/readme/pep8/blogconnect-urls.png)

![pep8 wsgi.py](static/images/readme/pep8/blogconnect-wsgi.png)

#### contact

![pep8 admin.py](/workspace/connectconsultingp4/static/images/readme/pep8/contact-admin.png)

![pep8 apps.py](static/images/readme/pep8/contact-apps.png)

![pep8 forms.py](static/images/readme/pep8/contact-forms.png)

![pep8 models.py](static/images/readme/pep8/contact-models.png)

![pep8 urls.py](static/images/readme/pep8/contact-urls.png)

![pep8 views.py](static/images/readme/pep8/contact-views.png)

#### Gitpod Workspace

![Workspace](static/images/readme/pep8/contact-views.png)


## Lighthouse Testing

All pages were checked on lighthouse.  Results were over 90% for performance and best practice and 100% on Accessability and SEO on both mobile and desktop.  On the first test performance was very poor.  This was fixed by applying height and width to an image.


### **First Test**

![Lighthouse Poor Performance](static/images/readme/misc/lighthouse-first-test.png)

### **Lighthouse Picture Performance**

![Lighthouse Picture Performance](static/images/readme/misc/Lighthouse-fix-test.png)

### **Final Test**

![Final Lighthouse Test](static/images/readme/misc/Lighthouse-fix-test.png)


## Manual Testing

To ensure that all elements of the website were working I carried out a detailed manual test and checked off the list as I went. 


| Status | **Logged Out**
|:-------:|:--------|
| &check; |
| &check; |

| Status | **Logged In**
|:-------:|:--------|
| &check; |
| &check; |


| Status | **Admin Logged In**
| &check; |
| &check; |

| Status | **Nav Logged In**
| &check; |
| &check; |

| Status | **Nav Logged Out**
| &check; |
| &check; |

| Status | **Footer**
| &check; |
| &check; |

| Status | **Home Page**
| &check; |
| &check; |


| Status | **About**
|:-------:|:--------|
| &check; |
| &check; |

| Status | **View Testimonials**
|:-------:|:--------|
| &check; |
| &check; |

| Status | **Create Testimonials**
|:-------:|:--------|
| &check; |
| &check; |

| Status | **Blog List Page User Logged In**
|:-------:|:--------|

| Status | **Blog List Page Admin Logged In**
|:-------:|:--------|

| Status | **Blog List Page Logged Out**
|:-------:|:--------|






## Bugs

### 



**Fix:**
