# Frisa Booking

![image of site](link to image) - use an image from AmIResponsive that shows the site on multiple devices

## Introduction
The project is to build a website where you as a user can book a workshop to upcycle old things. If the user doesn't visit the website with the goal to book a workshop right away, the website should work as an inspiration.

## Table of Contents
[[_TOC_]]

## User Experience
### User Stories
- User Goals
- Site Owner Goals

## Design
The design is set to be modern but easy to read. It should draw the attention to the images which will enhance the chance to get the users to get inspired. The design should feel welcoming and like you're visiting a friends place. 

### Color Scheme
The color scheme is set to feel modern and harmonize with the hero image. Any bright colors in the scheme were avoided due to not draw any attention from the images at the website. The colors are reused on all pages to make every page feel familiar and to enhance the feeling that the website is an unity. 

### Typography
The typography were chosen to have a modern touch. They were chosen to feel easygoing and fun, but at the same time easy to read. The text was designed to incorporate some spacing, ensuring it doesn't appear as a dense block of text upon opening a page. The written communication across the website adopts a playful tone to foster a friendly atmosphere. Emojis was added to make the tone more playful and friendly.  

### Imagery
All the images are chosen to inspire the website users. The images should give a warm feeling with the help of the content and a warm tone in them. The images have been designed with a playful and dynamic excerpt to encourage user engagement and increase sign-ups for the workshop. The objects on the images are things that has been made by the leader of the workshops. In other words, they are objects that you can do at the workshops!

### Wireframes

#### Index page
![Wireframe of index page](doc/wireframe-index.webp)

#### About page
![Wireframe of about page](doc/wireframe-about.webp)

#### Booking page
![Wireframe of booking page](doc/wireframe-booking.webp)

#### My bookings page
![Wireframe of my bookings page](doc/wireframe-my-bookings.webp)

#### Success page
![Wireframe of success page](doc/wireframe-success.webp)

#### Edit booking page
![Wireframe of edit booking page](doc/wireframe-edit-booking.webp)

#### Sign up page
![Wireframe of sign up page](doc/wireframe-sign-up.webp)

#### Sign in page
![Wireframe of sign in page](doc/wireframe-sign-in.webp)

#### Sign out page
![Wireframe of sign out page](doc/wireframe-sign-out.webp)

### Entity Relationship Diagram - ERD

Three different models were used in the website.

![ERD of Booking Model](doc/erd-booking.webp)

![ERD of Course Model](doc/erd-course.webp)

![ERD of CourseSession Model](doc/erd-coursesession.webp)

## Features

### Header

#### Navigation bar

![Navigation bar as a not logged in user](doc/navbar-not-logged-in.webp)

The navigation bar makes it easy for the user to navigate at the site. It takes the user directly to the home page, about page, booking page, sign in page and sign up page. This helps the user to get a overview of the website.

#### Navigation bar (as a logged in user)

![Navigation bar as a logged in user](doc/navbar-logged-in.webp)

The navigation bar for a logged in user is almost the same as the not logged in user. The main difference is that the sign in and sign up links are replaced with the users username and sign out links. The users username is linking to the page where the user can see their bookings. 

### Index page

#### Hero image

![Hero image at index page](doc/hero-image.webp)

The hero image is an eyecatching image selected to get the user to feel "wow, I want to do that aswell". It's selected to get the user to feel the inspiration flow. The warm tones in the images are there to get a warm and welcoming feeling.

#### Welcome text

![Welcome text at index page](doc/welcome-text.webp)

At the hero image, the welcome text is presented. The text has a darker background which makes it easier for the user to read. The text is there to welcome the user and present a short description of what they can expect of the website. After the text, a button which links to the booking page, is present. It has a lighter color which makes it pop from the background. This presents and directs the user to the main purpose of the website.

#### Carousel

![Carousel of images](doc/carousel.webp)

At the bottom of the index page, a carousel with images are located. This carousel is there to present several more objects that can me done at the workshops. Their goal is to inspire users and increase their interest in registering for the workshops.

### About page

#### Profile image

![Profile image at the about page](doc/profile-img.webp)

The profile image presents the founder and owner of Frisa. To show who it is makes the user to feel closer and get a more friendly feeling when they may fill out the contact form or sign up to a workshop. 

#### About text

![A text about the owner and founder of Frisa](doc/about-text.webp)

The text is a compliment to the profile image to present the founder and owner of Frisa. It will help to enhance the friendly feeling. This will also help the user to know what to expect from the webpage.

#### Contact form

![The contact form at the about page](doc/contact-form.webp)

The contact form is a channel for the user to get in contact if they have any questions. The text on top of the contact form encourage the user to reach out to the site owner.

### Booking page

#### Workshop presentation

![The three different workshops are presented](doc/workshop-presentation.webp)

The three different workshops are presented with a informative text. Each presentation has a read more button so the user can read more if they are interested. The read more button is also there to avoid that the user is met by a wall of text when they are visiting the booking page.

#### Workshop booking

![The booking section where the user can select which session they are interested in](doc/workshop-booking.webp)

The booking section of the page presents the availible workshop sessions. Each session is presented with the name of the workshop, date, time and how many availible spots that are left. Each session is represented as a button where the user can click on the button to book the section.

#### Confirm booking modal

![Confirmation modal after a booking button in pressed](doc/confirm-booking.webp)

A confirmation modal is triggered when the user has pressed a booking button. The confirmation modal gives the opportunity to the user to confirm the booking or cancel the confirmation modal without making any booking. The confirm button is green and cancel button is red to enhance the meaning of the buttons.

#### Double booked modal

![Modal to show that the user already has a booking at the chosen workshop](doc/double-booked.webp)

A double booking modal is triggered when the user tries to book a workshop session that they already has a booking at. This is to avoid that the user books the workshop session several times.

### Success page

#### Confirmation text

#### Navigation buttons

### My bookings page

#### No bookings - text

#### No bookings - button

#### Active bookings - text

#### Active bookings - booked workshops

#### Confirm cancellation modal

### Edit booking page

#### Availible workshops

#### Confirm workshop change modal

### Sign up page

### Sign in page

### Sign out page


Screenshot of implemented feature
Description of the value this feature has for the users


## Features to be Added
Describe some additional features you could potentially add to the project that would increase user value - could be things linked to technologies not yet covered by the course but would be a benefit to the user for example, the ability to save an article, or add an article to the site, leave a review.


## Testing

### Validation of Code
Insert screenshots of HTML, CSS and any other code files being tested in the relevant code validator - CSS validator might not validate newer CSS syntax - be careful to read and fully understand why it is giving you an error.

### Lighthouse
You can perform a test of your website for performance, accessibility, best practices and SEO through the google chrome lighthouse test - it is in your Dev tools. Bear in mind that your internet connection speed plays a part in the performance figures obtained. Where it scores low, it will give you suggestions on how to improve the site - read the suggestions and think about how to implement them - it could be a good idea.
Do this for both Desktop and Mobile.

### Wave Webaim - accessibility testing
You can test your site for accessibility through the wave.webaim site - it needs to be deployed in order for it to test it. Fix any errors that it gives

### Manual Testing

You need to perform, and document everything you did to manually test your site.
At a minimum - you need to check every link on every page works as intended.
So that is check every link in the nav bar (do this on every single page because its a link in a different file) and any other links that appear on your site.
Test the responsiveness of the site - you can do this in the dev tools in responsive mode.
You should also load the site once deployed on as many devices you have access to. What is different from one device to the next? why is it different?

Test the user stories that you created earlier in the readme - did you satisfy the goal, how?

To write up the tests you can use a table,
| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| enter details here | enter details here | enter details here | enter details here | enter details here |

You should have tests for every section of every page.. individually.

## Technologies Used

Detail what technologies you used. So what code languages, what frameworks, libraries, what software did you use to develop the site - Balsamic for your wireframes, Figma for a mockup?

## Deployment

Detail how to clone the repository, how to fork the repository - how to run the site locally and how to deploy it.


## Credits

You need to credit where you got anything for your site from.. where are the images from, are they all from the same site? where did you get the content from, if you wrote it yourself, did you fact check anywhere? did you get code from anywhere? if so, it needs to be clearly marked in both the code and the readme.

## Acknowledgements
Any special acknowledgements you'd like to leave

Back to top link to return to the top of the readme.