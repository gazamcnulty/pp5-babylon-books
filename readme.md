# Babylon Books - Read me

![Image](static/images/readme_images/mockup.JPG)

**Link to live site deployed on Heroku**
[Link](https://github.com/gazamcnulty/pp5-babylon-books/tree/main)

**Link to project repository on Github**
[Link](https://pp5-babylon-books-760a9235289e.herokuapp.com/)


## About

Babylon Books is a website built to create a new space for book lovers and new readers. It is a store that sells books that are curated and chosen by the founders of the site, they are chosen deliberately based on their likelihood to foster stimulating conversation and debate with the users. The ethos is to spread the love of reading to new readers while providing a space for existing bookworms. It provides a place where users can buy books from a curated selection, view their info and order-history, comment on the book, submit blog posts, like posts. It uses a sleek yet simple design aesthetic to look appealing, welcoming but non-overwhelming. Superusers / admin have access to update the store items in front facing environment, they can create, review, update and delete store items while on the website. Other more specific aspects are available in the django admin backend. Standard users can create profiles, submit payment info via stripe, save their profile info, create comments, blog posts and like posts. These features allow the website to self sustaining without expert assistance.


## Contents

- Introduction
- About
- Contents
- Preparation : Research
- Preparation : Intent
- Preparation: User Stories / Agile methodologies
- Preparation: Marketing / Business
- Features
- Visual Design - colour aesthetic & wireframes
- Validation and testing
- Creation and deployment
- Technologies used
- Known bugs and issues
- Future updates / places to improve
- Sources
- acknowledgements


## Preparation : Research

In preparation for this project, I thought about what kind of site could utilise CRUD functionality for users, but also superusers who are selling a service and require payment via an online facility.  I wanted a website that meets the requirements of the pp5 full stack e-commerce project that could also be used in the real world. The range of websites that would need to request payment is vast, I didn’t want it to be too complex and decided to look at something that would request payment for a static product, without too much variation. This meant moving away from variable services , courses, clothes with different sizes. I decided the most elegant yet simple business would be a noble online bookshop, since a book can be a single entity without variations and books/reading in general is a hobby of mine.

This is also a good idea because while books are not exactly a niche interest, reading books is less popular than it used to be so there is always a desire from smaller communities for dedicated spaces to discuss and buy books that interest them. While smaller communities like this means a smaller user base, I think this makes more sense as it is easier to stand out in a smaller crowd. In this way my site would be competing with dedicated online bookshops, instead of larger stores that sell everything including books. And since I was intending to add on extra features that these dedicated online bookstores don’t provide, its another opportunity for the website to stand out from the others and fill a gap in the market, provided there is a unique selling point.

With this in mind, I conducted research on existing online bookstores, specifically those that are focused mainly on selling books ( excluding stores that sell all kinds of items like Amazon / Argos etc )

- Waterstones 
[Link](https://www.waterstones.com/)

- Blackwells 
[Link](https://blackwells.co.uk/bookshop/home)

- The Works
[Link](https://www.theworks.co.uk/)

- Foyles
[Link](https://www.foyles.co.uk/)

- Wordery
[Link](https://wordery.com/)


After researching these sites, I discovered they had very similar designs, content and features. They all looked mostly bright or white, with very clear legible features, nothing too ambitious in terms of design aesthetic. It seems to be aimed at making the navigation to purchase a book as simple and un-confusing as possible. They don’t look to be aimed at a particular demographic like young people or women , or working professionals - it seems to be blanket approach to try and appear welcoming to everyone. While this is evidently a solid approach that focuses on making the sale of the books as painless as possible, its not quite the approach I want to take. I don’t want Babylon Books to be in and out , quick and painless - I want it to be an interesting , cool site that book lovers want to return to and spend more time on. So I decided to go in a completely different direction with my aesthetic - if Babylon Books is to stand out from its peers I want it to look and feel totally different. Instead of bright friendly colours and aesthetics, it should have a dark, classy look. Insead of looking like a glass of milk sitting on a window sill, it should look like a glass of whiskey sitting on a table in a shadowy reading room. Thats the kind of feel I want to emphasise. 

In terms of the features, the sites all had similar offerings : look at books, at book to shopping bag, proceed to purchase, submit payment via stripe / paypal / etc, receive order confirmation, email, create profile with passwords, reset password, update delivery info, add to wishlist, submit reviews etc. I was aiming to implement most of these already , but I feel that these are all missing the community features that I am looking for. As I said I don’t want it to just be a store where you buy books and you’re done - I want it to be a community of like-minded individuals who like the website because of its cool design, curated booklist, social features and community engagement. With this in mind I decided to implement additional features that were directed at user engagement and community interaction - people should be able to submit comments / reviews of the books in the store, they should be able to submit general blogposts on a separate blog page , they should be able to ‘like’ posts and it should display how many people have liked it. This way its as much about the business end of the store as it is about the space for the book-reading community. The combination of business e-commerce focus, along with social user interactions and content creation will allow my website to stand out.


## Preparation : Intent

Based on above conclusions and conducted research I decided to make a website that offers a cool ‘alternative’ personality and vibe, to the prospective consumer. It offers books for sale, but its not every book under the sun. Its a curated list of only the best most interesting books , which the site runners and users are currently discussion - like a book club. The site runners curate the books on sale, they will look at offering extra benefits to users in future (like podcast / streaming content) while the users who interact with the site also provide content, through book reviews and blog posts. This way its a cool meeting of demographics, everyone has a voice. The design aesthetic will need to go a long way to cultivating the type of personality I want the website to have . I also want the website to be a safespace and feel welcoming to all types of users, so it will be important to have welcoming / encouraging dialogue all over the site, particularly on the homepage and in the about section. This is my chance to communicate directly with potential users and convince them to create an account, make a purchase etc.
In line with the alternative vibe of the site , I also don’t want it too far in the social media direction either. If it had all the bells and whistles of facebook or instagram, it would instantly lose its appeal and overwhelm the users. I want it to be a cool site they can go to, to buy new books , talk about books they are reading, and maybe have meaningful interactions with other users. I don’t want them putting in effort into user profiles or doom scrolling a feed.


## Preparation : User stories / Agile

The ultimate goal of Babylon Books is to provide a unique combination of e-commerce front facing business in the form of an online book shop, with social user interaction/ user generated content. Its not competing directly with online book stores, or social media sites, Babylon Books is trying to carve out a path of its own. With this in mind, I resolved to conduct careful planning both from an agile perspective, but also from business / marketing mindset.

The first step in the agile journey is coming up with a list of user stories : these are hypothetical goals / tasks, that users would want to be able to do when visiting the site. It helps me categorise loose ideas into specific tasks to complete. I made a list of all the features I believed the site ought to have , then considered it from a hypothetical user point of view. This allowed me to create a dynamic list of user stories that would hope to accomplish all of my website goals.
Once I had a list of user stories, I assigned them priority labels from the MOSCOW perspective. This categorises them by must have, should have, could have and wont have . It allows me to prioritise and focus on the most important tasks first, and possibly look at implementing other desirable features later if time permits.
Then , these MOSCOW labelled user stories can be divided up further into iteration projects. These segment the user stories into chunks so they can be tackled together, using a ‘board’ view so that the team can see which has been started, which is currently being worked on , and which has been completed.
Furthermore, a key feature of agile methodology is the inherent flexibility. Although all of the prior features seem essential, its important to remember that agile users are constantly re-assessing the goals, features, user stories, work load as time goes on with the project. This is important because what seems a good idea now, may turn out to be a bad idea later. And, the more work we do on the project, the more experience and info we have to help us determine what should and shouldn’t go into it. With this in mind, i would look at every project iteration while completing the project and see if all of the user stories still made sense as time went on. Sometimes I would change a story to a new goal, or just decide not to complete a user story if it didn’t fit with the overall vision, or if time was an issue. This allows me to focus on the big picture of getting the website completed instead of being bogged down in inflexible tasks.


**Example of a user story from Babylon Books**

![Image](static/images/readme_images/user_story.JPG)


**projects / iterations for Babylon Books**

![Image](static/images/readme_images/iterations.JPG)


**Project board**

![Image](static/images/readme_images/project.JPG)



**pp5 Babylon Books issues list** 
[Link](https://github.com/gazamcnulty/pp5-babylon-books/issues?q=is%3Aissue+is%3Aclosed)



**pp5 Babylon Books projects / iterations list**
[Link](https://github.com/gazamcnulty?query=is%3Aclosed&tab=projects)



## Preparation: E-Commerce Business Model + Marketing


As I said in the above section Prep : Research , I looked at a number of successful e-commerce sites that sell books online. This allowed me to see what features they offered, how they marketed the business, what type of goals they appeared to have. This in turn helped me with my own preparation by considering what type of business Babylon Books should be, what types of items / services are being sold, what type of payment we will want and what kind of database tables will facilitate this. All of this also leads into marketing considerations also.



The first thing to consider is what type of E-commerce application would suit Babylon Books. As described above, I am aiming towards individual users rather than large groups / businesses. And the curated books are carefully selected with only a few books on offer at any time, as opposed to having a vast library. As a result, its safe to say that Babylon Books would not be **B2B** (business to business) it would be B2C (business to customer)
This makes more sense as it targets impulse buyers and gives them the freedom to choose for themselves, as opposed to a B2B in which a purchase would be far more considered and laborious.
The slight disadvantage of a B2C business vs B2B is that you would tend to have smaller transactions ( a business is likely to buy a large supply of items, the individual customer will just want one ) . Based on the ethos of Babylon Books it is clear that B2C is the most suitable.

We can also consider what is being sold, to help make business/ marketing and design choices. We are not selling digital items, or a service , we are selling tangible objects : books. So , it is important to have an image of the book cover, information about the author, a search function, price info and maybe a link to wikipedia for more info on the book itself or the author.

The next thing to consider is what type of payment we will want. Although it could make sense in theory, to have a subscription type service that grants exclusive access to community features on the website (like Patreon) its not quite the vibe I want for the website. I think the type of person who will find Babylon Books interesting is not someone who wants to pay a monthly subscription, they are more likely to just buy a book once and be happy with their purchase. Regardless, selling individual items to individual customers means it makes more sense to consider the single payment option. It would be different if we were selling something that required regular replenishment like ink cartridges etc. As we are selling curated books, a once off purchase would be the best choice.

We should also consider what kind of data tables / models would be required in the website, to enable the features that are needed for the desired E-commerce application. We want to sell individual books, to individual users, via stripe. Books have prices, authors, genres. We also want the users to have other features not directly related to the business / E-commerce side, like reviews / blog posts. With this in mind, I know I will need models for Book (fields: title, description, author, genre, price, date_added,) Author  (fields: name, info, external link, image, books_written), Genre(field: name) just for the main books contents. I will also need models for BlogPost and Review, for user CRUD. I can use existing Django models such as User, to help define user profile details. Per the Code Institute tutorials, I will also need Order and OrderLineItem models when designing the checkout . I may need other models than these, but this shows how considering the E-commerce business implications can directly affect the database considerations and how the website will function.


Finally for **marketing** the E-commerce application, I followed the suggested guideline from the Code Institute tutorials and created a **separate facebook business page**. This a page external to the main website thats purpose is to have some extra marketing , advertising and engagement with users away from the main app. Our website can be designed flawlessly, but if prospective customers don’t know about it, its all for nothing. This is where the facebook page comes in. Facebook has a litany of user-friendly business features which we can use to advertise. We can make posts, share images, stream video, pay for direct marketing and advertising to other facebook users. We can select the type of group / demographic who might be interested in our website and use this when making decisions about the facebook advertising. For the purpose of this project, I created a live facebook page for Babylon books , that has a link to the deployed Babylon Books page. In turn, there is a social media link in the footer of Babylon Books that links to the facebook page. So we are increasing the likelihood all the time that we will reach a potential customer with our marketing info, this in turn increases the chance of the E-commerce application succeeding as a real business.


**Screenshots of the Facebook page for Babylon Books**

![Image](static/images/readme_images/facebook1.JPG)

![Image](static/images/readme_images/facebook2.JPG)

![Image](static/images/readme_images/facebook3.JPG)

![Image](static/images/readme_images/facebook4.JPG)



## Stucture / Features

Screenshots of various pages on the website

* Homepage (index.html)


* Books.html


* Book_detail.html


* About.html


* Checkout.html


* Bag.html


* Blog.html


* add_author.html


* add_product.html


* profile.html
