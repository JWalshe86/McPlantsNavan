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
   
3. Choise of plants
   
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

The UX was explored using a customer journey map. The site then acted successfully on the insights taken from the map. The customer journey map detailed the journey and expected emotions of 3 standard users of the website. Goals and expectations are taken into account. This gave a general view of how to proceed with the project. User stories were then used to break these needs into tasks. The UI involved good use of navigation through anchor links and appropriate sizing for different devices. A toggle dropdown menu was used for smaller screens.

[Customer Journey Map](/static/pdfs/nags-with-notions-customer-jouryney-map.pdf)

#### User Stories 📖<br>

**The number references here proceeded by the hash key refer to the issue number in the github projects.

* As a customer interested in hiring a pizzeria horsebox service, I can request to book the horsebox online so that I can use it for a personal event #3
* As a website user I can see what events have occurred or will be occurring, so I can keep informed.
* As a user I want to be able to see my current bookings displayed on the site.
* As a user I want to only see my own bookings, so my booking information is kept private #171 #154
* As a user I want to quickly see a 'book now' button which brings me to the booking form #163
* As a user I want to be able to create bookings on the site #157
* As a user I want to be able to update bookings on the site #159
* As a user I want to be able to delete bookings on the site #156
* As a user I want to be able to see the prices of all the food items #131 #45
* As a user I want to see the name of each food item underneath its image #44
* As a user I want to be able to see if I'm logged in #99
* As a user I want to access my information once logged in #100
* As a user I want to be able to register an account using a username and password
* As a user I want feedback when my form completion has been successful #93 #94
* As a user I want a dropdown toggle menu for mobile screen sizes #52
* As a user I want a responsive header with interactive links for ease of site navigation #51 #4
* As a user I want to be able to access social media sites from the footer #5


* As an admin I want to be able to upload images related to events #170 #168
* As admin I want to be able to create events but users cannot create events #168
* As admin I want to be able to update events so new information can be added or subtracted #167
* As admin I want to be able to delete events #167
* As admin I want to have my passwords safe #113


### SCOPE 🔭<br>

### STRUCTURE☠<br>

#### Database diagrams

# ORM

* As there is one category to several plants. And there are always several plants to one category.
* The relationship here is a one to many, which involves the use of a foreign key.
* The foreign key field is always placed where the 'many' is - i.e the plants model.

![ORM](https://github.com/JWalshe86/McPlantsNavan/blob/media/databasediagram.png)


### FLOWCHARTS 📈<br>

Reasoning to flowchart: A flowchart was created to present the entire user story visually. The user is initially presented
with a welcoming landing page. The user is informed they can choose to book the pizza box for
personal use or see when other events are on that they could attend and try some pizza. The pizza
menu is displayed. If the user wishes to book they are shown the available dates. To book the user
needs to login. If not already registered the user must sign up. Once the user is logged in they
can select their preferred dates. They then receive a confirmation email regarding their booking. The dates available, personal information and password data is then updated.

[Full Site Flowchart](/static/pdfs/nags-with-notions-flowchart-sprint1.pdf)

# Work Flow

## Agile

* ![Kanban Board](~/projects/McPlantsNavan/media/readme/kanbanboard)

#### Sprints

[Sprint 1](https://github.com/JWalshe86/Nags-With-Notions2.0/milestone/19) * This will be closed but closed issues can be viewed.

Sprint 1 was overdue by one month as the django lms learning material took much longer than expected. The real project has started now and I expect to work through the issues at a quicker pace. Upon reflection, and advice from slack meeting 110124 I should implement story points to get a better grasp on what can be achieved between sprints and what to prioritise. I will also pivot towards putting crud functionality on bookings rather than comments

* Sprint 2

[Sprint 2](https://github.com/JWalshe86/Nags-With-Notions2.0/milestone/20) * This will be closed but closed issues can be viewed.


Sprint 2 saw the completion of 50% of its tasks. Story points were introduced to get a better grasp on the workload, and this may allow one to gain a better understanding of what can be realistically achieved in Sprint 3. Considerable time was put into automatic testing, which is not a requirement for the pass criteria; so in sprint 3 effort will be directed into other areas. During Sprint 2 much of the functional objectives were achieved. In Sprint 3 I hope to divest more energy into testing. 46 open issues were passed forward from Sprint 2 to Sprint 3. 159 story points were completed in Sprint 2. 147 story points have been passed for to Sprint 3, which makes this workload realistically achievable by the end of Sprint 3.

* [Sprint 3](https://github.com/JWalshe86/Nags-With-Notions2.0/milestone/21) * This will be closed but closed issues can be viewed.

The previous sprint was supposed to prioritise testing but during testing I found several bugs. One bug took several days to fix. This involved ensuring that the registered user could only see their own bookings in the view bookings tab. Connecting the user as a foreign key to my booking model and using the booking id as an argument to track whether the booking belonged to a specific user or not was quite challenging to figure out. Thus during this phase only 6 tasks were completed. For the next two weeks I intend to double down on testing: starting with ensuring all the booking functionality is correct and documenting this in the readme. Still several weeks until the Mar 22 deadline so things appear to be on track.


[Sprint 4](https://github.com/JWalshe86/Nags-With-Notions2.0/milestones?state=closed) * This will be closed but closed issues can be viewed.

The 8 days overdue for sprint 4 was a result of extra work in my internship. However, a lot of manual testing was completed which was quite tedious. This testing also highlighted many errors which took time to fix. The main focus now is to complete the testing and the user stories.

[Sprint 5](https://github.com/JWalshe86/Nags-With-Notions2.0/issues)

The final sprint involved doubling down on testing. Python testing was completed. The readme was updated. My site was also tested by friends and work colleagues.

Everything onn Kanban board was completed.

[Kanban Board](/static/images/KanbanBoard.png)

### SURFACE/DESIGN<br>

I chose the 'square' color harmony using Adobe's color wheel. The base color was the color associated with Nags with Notions Logo. However I swapped out #C4C9F5 for aliceblue as I felt #C4C9F5 was a bit too harsh.

![Color Palette](/static/images/colorpalette.png)

#### Wireframes

[Initial Landing Page Wireframe](/static/pdfs/Nags-With-Notions-Wireframe.pdf)


Reasoning for Wireframe structure: As a user, I want to be able to see when the Pizza Horsebox is available for private hire. As the owner, I want customers to know they can hire the horse box and when it's available. Also, I want the user of the website to know that Nags with Notions also sells pizzas at events and when these events are on. The wireframe shows websites snippets where such features have been executed successfully. Having shown this wireframe to Nags With Notions they are happy to proceed.

## FEATURES

### EXISTING FEATURES

### FUTURE FEATURES 🚀

## Technologies used 🧑‍💻

* [jsonformatter.org](https://jsonformatter.org/)
* [genmymodel](https://app.genmymodel.com/)


### Django Packages

- [Requirements.txt1](./static/images/requirements.txt1.png)
- [Requirements.txt2](./static/images/requirements.txt2.png)

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

* CategoryBug

* [CategoryBug](./static/pdfs/categorybug.pdf)

## Testing

### Feature Testing

*If in Markdown: PDF's open in github https://github.com/JWalshe86/Nags-With-Notions2.0?tab=readme-ov-file

[Manual Testing](/static/pdfs/testing/manual-testing.pdf)

### Manual Tests to assess javascript functionality

All tests on functionality were passed.
[Javascript tests on functionality](/static/pdfs/testing/Manual%20Test%20to%20Assess%20Javascript%20Functionality.pdf)

### Model Testing

Use of pytest-cov to see where tests may be required. I prioritised testing my custom code, as Django would have tested it's own code extensively. I installed factory-boy to insert fake data into the database. [First successful use of Pytest](/static/pdfs/testing/first-successful-use-of-pytest.docx). Due to the complexity of this testing, and time constraints I moved onto manual tests.

#### User Stories Testing<br>

* As a customer interested in purchasing plants, I can look at plants, add them to my cart and purchase them safely online.
Achieved. [Stripe Testing](/static/pdfs/stripe-testing.pdf)

* As a website user I can see what events have occurred or will be occurring, so I can keep informed.
Achieved. See feature testing for more detail. As an admin I can add, edit, delete events.
[Event Testing](static/pdfs/testevents.md)

* As a user I want to be able to see my current bookings displayed on the site.
Achieved. See feature testing for more detail.
[Bookings list](/static/images/userstorytesting/canseebookings.png)

* As a user I want to only see my own bookings, so my booking information is kept private #171 #154
Achieved. See feature testing for more detail.
[See own bookings](/static/images/userstorytesting/canseebookings.png)

* As a user I want to quickly see a 'book now' button which brings me to the booking form #163
Achieved. See feature testing for more detail.
[Book Now 1](/static/images/userstorytesting/booknow1.png)
[Book Now 2](/static/images/userstorytesting/booknow2.png)

* As a user I want to be able to create bookings on the site #157
Achieved. See feature testing for more detail.
[Create booking](/static/images/userstorytesting/newbookingcreated.png)

* As a user I want to be able to update bookings on the site #159
Achieved. See feature testing for more detail.
[Update booking 1](/static/images/userstorytesting/update1.png)
[Update booking 2](/static/images/userstorytesting/update2.png)
[Update booking 3](/static/images/userstorytesting/update3.png)

* As a user I want to be able to delete bookings on the site #156
Achieved. See feature testing for more detail.
[Delete booking 1](/static/images/userstorytesting/delete1.png)
[Delete booking 2](/static/images/userstorytesting/delete2.png)
[Delete booking 3](/static/images/userstorytesting/delete3.png)

* As a user I want to be able to see the prices of all the food items #131 #45
Client asked for prices to be removed and ratings used instead.
[See ratings](/static/images/userstorytesting/pizzaratings.png)

* As a user I want to be able to register to a newsletter
Achieved. See feature testing for more detail.
[Newsletter Testing](/static/pdfs/newsletter_testing.md)

* As a user I want to be able to see if I'm logged in #99
Achieved username presents in header.
[Logged in](/static/images/userstorytesting/userloggedin.png)


* As a user I want to access my information once logged in #100
Achieved. Restricted info for users not logged in.
[Limited info](/static/images/userstorytesting/‫limitedinfonotloggedin.png)

* As a user I want to be able to register an account using a username and password
Achieved. See feature testing for more detail.
[Authorisation Testing](/static/pdfs/register-testing.md)


* As a user I want feedback when my form completion has been successful #93 #94
Achieved. See feature testing for more detail.
[success message](/static/images/userstorytesting/newbookingcreated.png)

* As a user I want a dropdown toggle menu for mobile screen sizes #52
Achieved. See feature testing for more detail.
[Toggle Dropdown](/static/images/userstorytesting/toggledropdown.png)

* As a user I want a responsive header with interactive links for ease of site navigation #51 #4
Achieved. See feature testing for more detail.

* As a user I want to be able to access social media sites from the footer #5
Achieved. See feature testing for more detail.

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

* [Hero Image downloaded from freepik.com](https://www.freepik.com/free-ai-image/vivid-colours-plants-natural-environment_157431491.htm#query=flower%20fields&position=10&from_view=keyword&track=ais_user&uuid=bc7f256e-e5cd-4281-a0d1-385efb1f6726)
* [Flower Image Dataset from Kaggle.com](https://www.kaggle.com/datasets/aksha05/flower-image-dataset?)
* [postimage to host images](https://postimg.cc/gallery/wJB7W9T)
* [Deploy Django Project With Postgresql DB to Heroku](https://youtu.be/2OHc5EqfX5g?si=aw9Em89nmB460fss)
* [Review Model](https://youtu.be/rnNtbcYhC-o?si=XoHG5_sVqRH2Er7p)
* [Making Newsletter Master Code Online](https://youtu.be/r-V3UJ6D67E?si=lPGILH0XCca_MdBm)
* [Nursery-ecommerce](https://fastercapital.com/content/Nursery-e-commerce-platform--Building-a-Successful-Nursery-E-Commerce-Platform--A-Guide-for-Entrepreneurs.html)
* [Plant Favicon](https://www.plantstore.ie/)


## TOOLS 🧰

* Icons from [remixicon.com](https://remixicon.com/)
* [Figma](www.figma.com) was used to create the wireframes & user story map
*[tinypng](tinypng.com) was used to compress images


## ACKNOWLEDGEMENTS 👏

* I'd like to thank Code Institute Tutors Iris and Marco who supported and listend to myself, Abdul and Aongus every Wednesday.
* To my mentor who gave great advice on the project
* To everyone on youtube and stackoverflow who created content
* To my friends, family and colleagues at 2Toucons (Chandeep) for reviewing the site
* To Nags with Notions for giving me images and ideas and reviewing the site
* Code Institute


   











