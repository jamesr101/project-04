# WDI-Project4
# General Assembly Project 4 : Tippled - a cocktail app

## Goal: To create a full-stack app with React.js & Python

### Timeframe
9 days

## Technologies used

* Python
* Flask
* SQLAlchemy
* PostgreSQL
* React.js
* JavaScript (ES6) / HTML5 / SCSS
* JWT
* Git / GitHub
* Bulma CSS Framework

## My App - Tippled
<img src="https://user-images.githubusercontent.com/40343797/50253501-4e243a00-03e2-11e9-877d-ab31fa658a51.png" alt="tippled logo" width="300"/>

A hosted version of this app can be found on heroku at [tippled.herokuapp.com](https://tippled.herokuapp.com/)

### Application overview
A cocktail recipe app which allows users to see which drinks can be made using the ingredients they own. This was a group project with one other developer.

### Instructions
1. The Tippled homepage displays an alphabetical list of all available cocktails. At the top of the page is a search bar. Users can search for cocktails by name or ingredient. The list of cocktails is updated as the user types into the search bar. Above the search bar is a panel encouraging the user to Sign In or Register so they can specify the ingredients they own.

![tippled homepage](https://user-images.githubusercontent.com/40343797/50253537-67c58180-03e2-11e9-8f38-45d5b5361d75.png)

2. Users can register from the Register Page, or sign in from the Sign In page. When registering for an account, users must provide a unique email address and matching password/password confirmation. When typing your name into the Name field, a random avatar is created which changes as you type.

![register](https://user-images.githubusercontent.com/40343797/50253589-92afd580-03e2-11e9-852f-c247a029e675.png)

3. Once users have registered or signed in, they will be redirected back to the homepage. Their avatar, name and a list of their ingredients is now shown at the top of the page. Users can add ingredients they own to the 'My ingredients' section. The list of available cocktails is automatically updated so cocktails they have the ingredients for are shown at the top. Cocktails containing one or more of their ingredients is shown with a single tick. If the user has all the ingredients, the cocktail is shown with three ticks.

![tippled homepage signed in](https://user-images.githubusercontent.com/40343797/50253562-7b70e800-03e2-11e9-94a0-7441753aea11.png)

4. Clicking on a cocktail will take you to the cocktail show page. This shows the ingredients needed for the drink and the method for mixing the drink. Signed in users will see a tick next to the ingredients which they own.  

![tippled show page](https://user-images.githubusercontent.com/40343797/50253608-a1968800-03e2-11e9-96d0-ce8547798e51.png)

5. From the user panel on the homepage, signed-in users can follow the link to Edit Profile. From here, users can change their name, email or avatar image. The image will automatically update when a new image URL is entered. The email entered must be unique.

## Process

This was a group project with one other developer, [Caoimhe Clarke](https://github.com/cc-85). We used Trello to manage the project and performed daily stand-ups. Features were prioritised using the MoSCoW method. Features were created on separate git branches before being merged into the development branch.

<img width="1439" alt="Trello Board" src="https://user-images.githubusercontent.com/40343797/50253961-233ae580-03e4-11e9-950f-72aeb976e4ee.png">

We started the project by planning our models and database structure. As we were both relatively new to Python and SQL databases, we worked on this through pair programming.

Once our database was functional, we moved onto fleshing out the models and routes. At this point I began work on the Seeds file. When run, the seeds file makes requests to the [cocktailDB API](https://www.thecocktaildb.com/), saving each cocktail to our cocktail database and saving each new ingredient to our ingredient database.

Once our server-side code was working and had been tested by making API requests with Insomnia, we moved onto creating the frontend using React. I worked on the Sign In page, Login page and Edit Account page, while Caoimhe worked on the Cocktail Show-page, Index Page (homepage) and Navbar.

The layout and design of the application was styled using Bulma and SCSS. We had created wireframes which evolved throughout the process. These were used as roadmaps to focus functionality and design.

### Challenges
This was the first project we made using an SQL database and SQLAlchemy. We found this the most challenging aspect of this project, particularly setting up the relationships between our three models Cocktails, Ingredients and Users.

Our application relied heavily on the cocktaildb API to seed out database with data. I found there were many limits to using an external API such as limits to the length of responses and inconsistencies with data structure which had to be handled with additional data validation.

### Wins
I was really pleased with how well Caoimhe and I worked together,  especially how well we managed the project. This was helped by the consistent use of Trello, daily stand-ups and clear prioritisation of features.

I created a seeds file, which makes multiple requests to the cocktaildb API and fills our database with the responses. I was very pleased with the way I got this to work and enjoyed the challenges that came with working with someone else's API.

I become more familiar with React, I was pleased with handling error messages on the login/register pages and implementing [react-select](https://react-select.com/).

<img width="1129" alt="Seeds file" src="https://user-images.githubusercontent.com/40343797/50379677-b162d600-0647-11e9-98d2-7e95f358915b.png">
The code above is from our seeds file. This makes a request to the cocktaildb API for a list of cocktails. The code transverses this list of cocktails and makes a new request for each cocktail. Each cocktail is saved to our database with its corresponding ingredients.

## Future features
If we had more time, I would like to add testing to our application. For future improvements our site could do with cleaning of out data for the ingredients to minimise duplicate or similar entries as items with/without capital letters or differences in spelling will exist as separate items. We would have liked to allowed users to be friends with other users to see which cocktails they could make together, and allow users to star or favourite cocktails.
