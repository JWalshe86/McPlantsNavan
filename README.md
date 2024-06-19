# McPlantsNavan

![Responsiveness](/media/readme/landing-page.png)

  - [Overview](#overview)
  - [Business](#business-model)
  - [UX/UI](#uxui)
    - [STRATEGY](#strategy)
      - [Goals<br>](#goals)
      - [User Stories<br>](#user-stories)
    - [SCOPE<br>](#scope)
    - [STRUCTURE<br>](#structure)
    - [FLOWCHARTS<br>](#flowcharts)
    - [SURFACE/DESIGN<br>](#surfacedesign)
    - [EXISTING FEATURES<br>](#existing-features)
    - [FUTURE FEATURES<br>](#future-features)
  - [BUGS OR ERRORS](#bugs-or-errors)
  - [TESTING](#testing)
  - [MODULES IMPORTED](#modules-imported)
  - [DEPLOYMENT](#deployment)
    - [CREATING THE WEBSITE](#creating-the-website)
    - [DEPLOYING ON HEROKU](#deploying-on-heroku)
    - [FORK THE REPOSITORY](#fork-the-repository)
    - [CLONE THE REPOSITORY](#clone-the-repository)
  - [CREDITS](#credits)
  - [TOOLS](#tools)
  - [ACKNOWLEDGEMENTS](#acknowledgements)


# Overview 🚠
Online store for garden center based in Navan, where you can purchase a wide variety of plants Users should be able to access the site and select the plants they'd like to purchase. Users can also view events related to the garden center. Subscribed users can obtain a newsletter. The site mainly uses Django, CSS, Javascript and python. CRUD functionality is found on all models. Stripe is integrated for payments. Emails are sent once users register to the site or newsletter. Admin can access a stock list page. 

# Business_Model

## Incentive

  There is a growing demand for plants and flowers. It's possible Covid 19 re-ignited people's
interest in gardening, and a huge increase in online purchases in general. In 2020 the global online
market size was estimated at $6 billion and it's expected to grow by 10% yearly until 2028. Some argue
people are now more environmentally aware, and the spread of mobiles makes it far easier to purchase online. Online shopping can allow more personalised purchases and there has been an improvement in logistics, so people are more confident their product arrives safely. One only needs to look at the rise of the Green Party in Ireland, to see that the interest in plants is not just a fad. A UK online nursery named Patch has seen it's revenue increase by 500% yearly since its launch in 2016.

## Target Audience, Competitors, and unique Selling Point

1. Target Audience

Those most likely to buy plants include young families who have purchased a new home and those retired.Those living in the suburbs and countryside are more likely to want plants. Additionally, where transport is limited, people may be more incentivised to shop online. Those willing to purchase plants will typically be 'middle earners'. 

2. Competitors
   
   Competitors include other online nurseries, such as Gardens4You.ie or thegardenshop.ie.
   
3. Choice of plants
   
   Plants were chosen that were in the price range of middle earners in Ireland. Research on other websites helped determine which plants were in the highest demand. Plants were also selected by their 
   availability. Local plants were prioritised. Prior to launching the site surveys were sent out to the local population, whereby people selected their favourite plants. A professional photographer was
   used to ensure the plant images were of the highest quality.

4. Promotion of Site
   
   A social media account was created using facebook [FB business page](/media/readme/fb-business-page.png). A robots.txt file was used to improve the sites search engine optimization score. 

5. Customer Loyalty

   A newsletter was created to keep customers informed about the site. There is also an events section whereby customers can come to events and increase footfall at the garden center.

# XML Site Map

* [XML site map verification](/media/readme/xml-verification.png)

* [FB business page](/media/readme/fb-business-page.png)

## UX/UI

### STRATEGY

#### Goals 🥅<br>

The UX focused on ensuring the site was as visual as possible. User stories were used to break perspective clients needs into tasks. The UI involved good use of navigation through anchor links and appropriate sizing for different devices. A toggle dropdown menu was used for smaller screens.

#### User Stories 📖<br>

* As a user interested in buying plants, I can look up plants online and purchase them.
* As a user I can see what events have occurred or will be occurring, so I can keep informed.
* As a user I want to be able to register for a newsletter.
* As a user I want to get an email including my purchased items (invoice).
* As a user I want to be able to see the prices of all the plants
* As a user I want to see the name of each plant with a description underneath
* As a user I want to be able to log in securely and log out
* As a user I want to be able to leave a review and see other reviews
* As a user I want feedback that I've successfully submitted a form
* As a user I want a dropdown toggle menu for mobile screen sizes
* As a user I want a responsive header with interactive links for ease of site navigation
* As a user I want to be able to access social media sites from the footer

<br>

* As staff member I want to be able to see my current stock levels for each plant displayed on the site.
* As a staff member I want to be able to upload images related to events
* As a staff member I want to be able to create, edit and delete newsletters
* As a staff member I want to be able to create events to display online.
* As a staff member I want to be able to update events on the site.
* As a staff member I want to be able to delete events on the site.


### SCOPE 🔭<br>

### STRUCTURE☠<br>

#### Database diagrams

# ORM

* As there is one category to several plants. And there are always several plants to one category.
* The relationship here is a one to many, which involves the use of a foreign key.
* The foreign key field is always placed where the 'many' is - i.e the plants model.

![ORM](https://github.com/JWalshe86/McPlantsNavan/blob/media/databasediagram.png)

# Work Flow

## Issues

Issues were created initially based on the projects user stories. Issues were then added to the repo's issue page as the project progressed. Issues were managed using a kanban board in the repo's projects section. Here issues were given prioritisation, and their status could be reviewed. 

![Issues Example](/static/pdfs/issues.png)

## Agile

![Kanban Board](/media/readme/kanbanboard.png)

#### Sprints

Issues were linked to github milestones. Milestones were used as Agile 'sprints'. 

There were 4 sprints

![Sprints](/static/pdfs/4sprints.png)

* Sprint 1: Involved the initial set up of the project. Getting the template and core models/views.

* Sprint 2: During this sprint the aim is to have the site connected to Stripe and a user can purchase plants online.

* Sprint 3: During sprint 2 much of the project was completed. A priority now was to ensure that I've 3 custom models, as per the requirements. Then I could testing.

* Sprint 4: Top priorities were to ensure that I've met all the requirements: 3 custom models, Get AWS working to store images & connect to Heroku, Test all features, Complete README, Fix css issues on small screen sizes.

### SURFACE/DESIGN<br>

I chose a light green, as I felt this related to the plant theme. I then used Huemint to generate a color pallete from this: #fad3b0, #5cc7f9 and #1275e0.

![Color Palette](/static/pdfs/colorpallet.png)

## FEATURES

### EXISTING FEATURES

* Select multiple plants, add them to a cart and purchase them online
* Subscribe to newsletter
* Receive emails upon sign up to site, sign-up to newsletter and upon a successful purchase
* See upcoming events
* See reviews
* See current stock

### FUTURE FEATURES 🚀

* Dynamic stock takes

## Technologies used 🧑‍💻

* [jsonformatter.org](https://jsonformatter.org/)
* [genmymodel](https://app.genmymodel.com/)
* [huemint](https://huemint.com)


### Django Packages

- [Requirements.txt](./requirements.txt)


Many of the packages here are dependencies of core packages. The main packages used were:
- Django as the framework
- django-allauth for user permissions
- django-crispy forms to make forms look and perform better
- factory-boy to create fake data for automated tests
- pillow to manage images
- python-dotenv to create a virtual python environment and keep dependencies local
- waitress as a subtitute for gunicorn as I was using windows
- whitenoise for static support when deploying to a server

### Infastructural Technologies

- PosterSQL - used as the database
- Heroku - where site was deployed

## Languages used

- Python, Javascript 🐍

## BUGS OR ERRORS 🐛 😵// Issues which take me more than 2 hours to solve

* 95% of the bugs I was able to resolve through using stackoverflow. 

* Stripe Webhook not responding
  For weeks I couldn't figure out why webhooks wouldn't work when I made a payment on Heroku using stripe. If I hard coded the stripe secret key locally and then pushed this to heroku it would work. Eventually I noticed that in my Heroku config variables I had 'STRIPE_WB_KEY' instead of 'STRIPE_WH_KEY'. However even when I fixed this it still wouldn't work. I then added the STRIPE_WB_KEY to heroku through the heroku cli. This time it worked.  
  
* Could not access django
  I changed my 'venv' virtual environment folder from 'venv' to '.venv'. This resulted in my requirements.txt file emptying and I couldn't access django. I had to delete everything in the django db and make migrations from scratch. I also had to re-upload the fixtures. 
  

## Testing

### Feature Testing

### Manual Tests to assess javascript functionality

All tests on functionality were passed.

### Screensize testing

[Mobile Screen Size tests](static/pdfs/screensizetests.md)

#### User Stories Testing<br>

* As a customer interested in purchasing plants, I can look at plants, add them to my cart and purchase them safely online.
Achieved. [Stripe Testing](/static/pdfs/stripe-testing.pdf)

* As a website user I can see what events have occurred or will be occurring, so I can keep informed.
Achieved. See feature testing for more detail. As an admin I can add, edit, delete events.
[Event Testing](static/pdfs/testevents.md)

* As a user I want to be able to register to a newsletter
Achieved. See feature testing for more detail.
[Newsletter Testing](/static/pdfs/newsletter_testing.md)

* As a user I want to be able to register an account using a username and password
Achieved. See feature testing for more detail.
[Registration Testing](/static/pdfs/register-testing.md)

[Authorisation Testing](/static/pdfs/authorisation-testing.md)

* As a user I want to be able to access social media sites from the footer #5
Achieved. See feature testing for more detail.

## 404 Page
* Custom 404 page for incorrect site entries. Users can go back to the home page.
  [custom 404 page](/static/pfds/custom404.png)

## Automated Testing

### HTML Validation
[W3C base2 HTML](/static/pdfs/base.html2.pdf)
[W3C final base HTML](/static/pdfs/finalbase.htmltest.pdf)
[W3C final base HTML](/static/pdfs/plants.pdf)

### CSS Validation
[W3C CSS](/static/pdfs/basecsstest.pdf)

### Lighthouse Testing

[Lighthouse Landing Page](/static/pdfs/landingpagelighthousetest.pdf)
[Lighthouse All Plants Page](/static/pdfs/allplantslighthousetest.pdf)

## MODULES IMPORTED 👽


## DEPLOYMENT 🚀

### CREATING THE WEBSITE

[Mentor Meeting 1 Feedback](/static/pdfs/mentor-meeting1-291123-notes.txt)

### DEPLOYING ON HEROKU

- Install Gspread using pip install Gspread in the terminal
- Ensure the requirement.txt file in the virtual working environment contains Gspread
- Enter [Heroku](https://id.heroku.com/login) and click 'Create new App'.
- Store sensitive data contained in the creds.json file in the config/Environment Vars
- Add both Python and node.js buildpacksClick Deploy and then connect to GitHub
- Search and connect to the GitHub repository name
- Click deploy branch
- When the project has been successfully deployed, click view.

### FORK THE REPOSITORY 🍴

If you would like to contribute to the project. You can:
1. Open the pizza ordering system repository on my account and
press the fork button on the top right of the screen.
2. Click create a new fork.
3. Navigate to your fork of the original repository.
4. Copy the URL for the repository.
5. Type git clone into your terminal and paste the repository.
6. You can then create a pull request which I will review.

### CLONE THE REPOSITORY ©

You can clone the repository to use locally by following these steps:
1. Navigate to the GitHub Repository you want to clone
2. Click on the code drop-down button
3. Click on HTTPS
4. Copy the repository link to the clipboard
5. Open your IDE of choice (git must be installed for the next steps)
6. Type git clone copied-git-URL into the IDE terminal

The project will now be cloned locally for you to use.


## CREDITS 💛

# Credits

* The framework of the site and all it's code is heavily based on Code Institues [Boutique Ado website](https://github.com/code-Institute-Solutions/boutique_ado_v1/)
* [Hero Image downloaded from freepik.com](https://www.freepik.com/free-ai-image/vivid-colours-plants-natural-environment_157431491.htm#query=flower%20fields&position=10&from_view=keyword&track=ais_user&uuid=bc7f256e-e5cd-4281-a0d1-385efb1f6726)
* [Flower Image Dataset from Kaggle.com](https://www.kaggle.com/datasets/aksha05/flower-image-dataset?)
* [postimage to host images](https://postimg.cc/gallery/wJB7W9T)
* [Deploy Django Project With Postgresql DB to Heroku](https://youtu.be/2OHc5EqfX5g?si=aw9Em89nmB460fss)
* [Review Model](https://youtu.be/rnNtbcYhC-o?si=XoHG5_sVqRH2Er7p)
* [Making Newsletter Master Code Online](https://youtu.be/r-V3UJ6D67E?si=lPGILH0XCca_MdBm)
* [Nursery-ecommerce](https://fastercapital.com/content/Nursery-e-commerce-platform--Building-a-Successful-Nursery-E-Commerce-Platform--A-Guide-for-Entrepreneurs.html)
* [Plant Favicon](https://www.plantstore.ie/)


## TOOLS 🧰

## ACKNOWLEDGEMENTS 👏

* I'd like to thank Code Institute Tutor Marco who supported and listend to myself, Abdul and Aongus every Wednesday.
* To my mentor who gave great advice on the project
* To everyone on youtube and stackoverflow who created content
* To my friends, family and colleagues at 2Toucons (Chandeep) for reviewing the site
* To Nags with Notions for giving me images and ideas and reviewing the site
* Code Institute
* [Mimmi](https://github.com/Stockman-Jr) For testing the site and recommending I improve staff/user access permissions.


   











