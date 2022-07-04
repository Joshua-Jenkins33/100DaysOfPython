- [Day 58: Web Foundation Bootstrap](#day-58-web-foundation-bootstrap)
  - [What is Bootstrap?](#what-is-bootstrap)
  - [Installing Bootstrap](#installing-bootstrap)
  - [Web Design 101 - Wireframing](#web-design-101---wireframing)
    - [Instructor Wireframing Process](#instructor-wireframing-process)
  - [The Bootstrap Navigation Bar](#the-bootstrap-navigation-bar)
  - [What We'll Make: Tindog](#what-well-make-tindog)
  - [Download the Starting Files](#download-the-starting-files)
  - [Setting Up Our New Project](#setting-up-our-new-project)
  - [The Bootstrap Grid Layout System](#the-bootstrap-grid-layout-system)
    - [Handling the Grid](#handling-the-grid)
    - [Using `col-#`](#using-col-)
    - [Challenge](#challenge)
  - [Getting Custom Fonts and Montserrat Black to Work](#getting-custom-fonts-and-montserrat-black-to-work)
  - [Adding Grid Layouts to Our Website](#adding-grid-layouts-to-our-website)
    - [Challenge: Change Section Title Background Color](#challenge-change-section-title-background-color)
    - [Challenge: Grid for the Title Section](#challenge-grid-for-the-title-section)
    - [Challenge: Embed the Fonts Ubuntu and Montserrat](#challenge-embed-the-fonts-ubuntu-and-montserrat)
  - [A Note About CSS Link Order](#a-note-about-css-link-order)
  - [Bootstrap Containers](#bootstrap-containers)
  - [Bootstrap Buttons and Font Awesome](#bootstrap-buttons-and-font-awesome)
    - [Challenge: Add a Dark and Light Button](#challenge-add-a-dark-and-light-button)
  - [Styling Our Website Challenges and Solutions](#styling-our-website-challenges-and-solutions)
  - [Bootstrap Challenge 1](#bootstrap-challenge-1)
  - [Solution to Bootstrap Challenge 1](#solution-to-bootstrap-challenge-1)
  - [The Bootstrap Carousel: Part 1](#the-bootstrap-carousel-part-1)
  - [The Bootstrap Carousel: Part 2](#the-bootstrap-carousel-part-2)
  - [Bootstrap Cards](#bootstrap-cards)
  - [CSS Z-Index and Stacking Order](#css-z-index-and-stacking-order)
  - [Advanced CSS - Media Query Breakpoints](#advanced-css---media-query-breakpoints)
    - [Media Query Structure](#media-query-structure)
  - [Bootstrap Challenge 2](#bootstrap-challenge-2)
  - [Solution to Bootstrap Challenge 2](#solution-to-bootstrap-challenge-2)
    - [CTA Section](#cta-section)
    - [Footer Section](#footer-section)
    - [Update Navbar](#update-navbar)
  - [Code Refactoring](#code-refactoring)
    - [Guiding Principles](#guiding-principles)
  - [Refactoring Our Website: Part 1](#refactoring-our-website-part-1)
  - [Advanced CSS - Combining Selectors](#advanced-css---combining-selectors)
    - [Multiple Selectors:](#multiple-selectors)
    - [Hierarchical Selectors](#hierarchical-selectors)
    - [Combined Selectors](#combined-selectors)
  - [Refactoring Our Website: Part 2](#refactoring-our-website-part-2)
  - [Advanced CSS - Selector Priority](#advanced-css---selector-priority)
  - [Completing the Website](#completing-the-website)
   
# Day 58: Web Foundation Bootstrap

## What is Bootstrap?
The most popular front-end library. Second-most starred repository on Github. It's reponsible/has adaptable layout that changes per device screen-size. Many many pre-styled elements.

Heading over to [codeply](https://www.codeply.com) because this allows you to use Bootstrap libraries.

Effectively, when you have this library implemented, you no longer have to custom-css buttons and other elements. You can simply call a Bootstrap class related to that element and BOOM! It's been prettified with minimal work.

They even have content so you can just copy and paste to have fully fleshed out website ***pages***.

## Installing Bootstrap

**First Way**
The simplest way is to copy the Bootstrap CDN. You place it in a `<link rel='' link=''>` element and, if the user doesn't already have the bootstrap files cached on their machine, it will download these files so the website can be served to every user appropriately.

**CDN.** Content Delivery Network. The internet is delivered through submarine cables. Comes from the idea that having to go to one spot in the world isn't the most effective and time efficient; you can lose a lot of folks if they have to wait longer than a few seconds to load your site. The idea is that you can access the website from a whole bunch of points in the world. The CDN helps you find the shortest route (Bootstrap hosts it on Max CDN).

**Second Way**
You can copy and use their starter HTML template. It includes JavaScript and JQuery which is required for some of the elements utilized by Bootstrap. This is probably the easiest way. 

**Third Way**
Install the html and css files and then link to the relative file; the downside is that the user will have to download all of these files (it won't cache it or take advantage of the caching) which can lead to latency.

## Web Design 101 - Wireframing
The Workflow of a Web Designer:
1. Wireframe
  - Low fidelity representation of your design; pencil and piece of paper
  - Architects don't just build buildings without any plans or buy-in or iterations of the design process
  - Opposite of Mock-Ups (High Fidelity, Dream-state, easy to get bogged down by color / images / etc)
  - Go to [ui-patterns.com](ui-patterns.com) to see examples to see how people have solved web design problems
  - [sneakpeakit.com](sneakpeakit.com) papers you can print out for drawing your wireframes
  - [balsamiq.cloud](balsamiq.com) collaborative / industry-standard way of wireframing (30-day trial)
2. Create a Mock-Up (optional)
3. Create a Prototype
  - Animated version that shows off what it's really going to look like
  - [https://dribble.com](https://dribble.com) fantastic starting point to get inspiration; peoples' portfolios

### Instructor Wireframing Process
She's using balsamiq. Website showing off her app (image of a phone on the right side), link bar on the top right, logo on the top left, big text about the app, android and ios buttons for downloading, three little images that show off features of website and explanatory text, etc.

Wireframe your own little startup website!

## The Bootstrap Navigation Bar
Head over to documentation to the components -> and navbar. Test it out in a CodePly program.

`<nav>` elements are like divs, they're just more semantically correct as they tell the developer what the purpose of this renamed `<div>` is. 

The `navbar-expand-<size>` class will make the navbar horizontal rather than vertical. You can use the `size` section of that to determine when you're find with it collapsing. `navbar-expand-md` will keep the navbar horizontal until it detects a small screen size, in which case it would collapse the navbar into a vertical format.

`ms-auto` will align things to the right. 

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <a class=navbar-brand href="">tindog</a>
    <ul class="navbar-nav ms-auto">
        <li class="nav-item">
            <a class="nav-link">Contact</a>
        </li>
        <li class="nav-item">
            <a class="nav-link">Pricing</a>
        </li>
        <li class="nav-item">
            <a class="nav-link">Download</a>
        </li>
    </ul>
</nav>
```

Now we want to make a dropdown for the navbar if the navbar is squished to vertical.

**Completed Navbar**
```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <a class=navbar-brand href="">tindog</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ms-auto">
            <li class="nav-item">
                <a class="nav-link">Contact</a>
            </li>
            <li class="nav-item">
                <a class="nav-link">Pricing</a>
            </li>
            <li class="nav-item">
                <a class="nav-link">Download</a>
            </li>
        </ul>
    </div>
</nav>

```

## What We'll Make: Tindog
Tinder—but for dogs!

## Download the Starting Files
In the coming lessons, we'll be learning about Bootstrap while we build and design our TinDog website.

I've created a skeleton project with all the graphics and some skeleton HTML for you work with.

1. Download the ZIP file from this lesson's resources

2. Extract the ZIP file and move it to your Desktop.

## Setting Up Our New Project
Downloaded the project and applied the navbar we created earlier to it. Then linked Bootstrap to the html file.

## The Bootstrap Grid Layout System
As the screen gets smaller, we need to be able to dynamically handle the listing width. See [airbnb.com](airbnb.com) as an example. Bootstrap is **responsive** (think screen-size, not lack of latency).

I want the buttons and "Meet New Dogs Nearby" to take up the left half of the screen and the app image to take up the right half.

### Handling the Grid
The below is split into two even columns
```html
<div class="row">
    <div class="col" style="background-color:red; border: 1px solid;">
        col
    </div>
    <div class="col" style="background-color:blue; border: 1px solid;">
        col
    </div>
</div>
```

### Using `col-#`
The total for each row is `12`. The below will only take up the left half of the screen.
```html
<div class="row">
    <div class="col-6" style="background-color:green; border: 1px solid;">
        col
    </div>
</div>
```

---

The above aren't responsive to screen re-sizing, however.

You can solve this with the following below (`col-md-6`). It effectively says "We should have a medium- (6) sized column from any size (med+) but for anything smaller, we will have a single column.
```html
<div class="row">
    <div class="col-md-6" style="background-color:blue; border: 1px solid">
        col-md-6
    </div>
    <div class="col-md-6" style="background-color:blue; border: 1px solid">
        col-md-6
    </div>
</div>
```

What if you want to recreate airbnb? 4 for desktop, 3 for tablet, 2 for phone?
```html
<div class="row">
    <div class="col-lg-3 col-md-4 col-sm-6" style="background-color:blue; border: 1px solid">
        col-lg-3 col-md-4 col-sm-6
    </div>
    <div class="col-lg-3 col-md-4 col-sm-6" style="background-color:blue; border: 1px solid">
        col-lg-3 col-md-4 col-sm-6
    </div>
    <div class="col-lg-3 col-md-4 col-sm-6" style="background-color:blue; border: 1px solid">
        col-lg-3 col-md-4 col-sm-6
    </div>
    <div class="col-lg-3 col-md-4 col-sm-6" style="background-color:blue; border: 1px solid">
        col-lg-3 col-md-4 col-sm-6
    </div>
</div>
```

### Challenge
- [x] Have 6 show up on 1 row for large
- [x] Have 3 show up on 1 row for medium
- [x] Have 1 show up on 1 row for small

```html
<div class="row">
    <div class="col-lg-2 col-md-4 col-sm-12" style="background-color:purple; border: 1px solid">
        col-lg-2 col-md-4 col-sm-12
    </div>
    <div class="col-lg-2 col-md-4 col-sm-12" style="background-color:purple; border: 1px solid">
        col-lg-2 col-md-4 col-sm-12
    </div>
    <div class="col-lg-2 col-md-4 col-sm-12" style="background-color:purple; border: 1px solid">
        col-lg-2 col-md-4 col-sm-12
    </div>
    <div class="col-lg-2 col-md-4 col-sm-12" style="background-color:purple; border: 1px solid">
        col-lg-2 col-md-4 col-sm-12
    </div>
    <div class="col-lg-2 col-md-4 col-sm-12" style="background-color:purple; border: 1px solid">
        col-lg-2 col-md-4 col-sm-12
    </div>
    <div class="col-lg-2 col-md-4 col-sm-12" style="background-color:purple; border: 1px solid">
        col-lg-2 col-md-4 col-sm-12
    </div>
    <div class="col-lg-2 col-md-4 col-sm-12" style="background-color:purple; border: 1px solid">
        col-lg-2 col-md-4 col-sm-12
    </div>
</div>
```

## Getting Custom Fonts and Montserrat Black to Work
Tl;DR If you have problems getting a Montserrat-Black to work check back to this note for the solution.

> Hey guys,
> 
> In the next lesson, I'll be introducing you to Google fonts. Some students have had issues getting the bolder Montserrat black to show up because > Google has updated their website UI. In order to get the different font weights of the Google font, you need to include it when you select it in > > Google fonts.

So when you are on the font page, make sure you select the 100, 400 and 900 font weights, e.g.

Next, look at the right-hand pane and make sure that you have all the desired font weights and then click on the Embed tab.

Now you should be able to copy the stylesheet link for the font and use it in your CSS.

So the final code should look like this:
```html
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@100;300;400;500;900&family=Ubuntu:wght@300;400;700&display=swap" rel="stylesheet">

    h1 {  
    font-family: 'Montserrat, sans-serif';  
    font-size: 3rem;  
    line-height: 1.5;  
    font-weight: 900;
    }
```

## Adding Grid Layouts to Our Website

### Challenge: Change Section Title Background Color
```css
#title {
  background-color: #ff4c68
}
```
```html
<section id="title">
```

### Challenge: Grid for the Title Section
```html
    <!-- Title -->
    <div class="row">
      <div class="col-md-6">
        <h1>Meet new and interesting dogs nearby.</h1>
        <button type="button">Download</button>
        <button type="button">Download</button>
      </div>
      <div class="col-md-6">
        <img src="images/iphone6.png" alt="iphone-mockup">
      </div>
    </div>
```

### Challenge: Embed the Fonts Ubuntu and Montserrat
```css
.logo {
  font-family: 'Ubuntu', sans-serif;
}

.main_heading {
  font-family: 'Montserrat', sans-serif;
  font-size: 3rem;
  line-height: 1.5;
  font-weight: 900;
}
```

## A Note About CSS Link Order
A quick note about the next lecture. If you find that your custom styles are not working, make sure that you change the order of link tags in the header.

CSS styles are applied in the order they are linked in your HTML code.

So if you had two stylesheets e.g. styles1.css and styles2.css which both target the same element

## Bootstrap Containers
Basic building block for a lot of componenets in Bootstrap (required when you use lots of Bootstrap components). It allows you to horizontally center or pad out your content by using a container.

```css
.container-fluid {
  padding: 3% 15%;
}
```

You can use the `container` class to make the whole container responsive to the screen width or you can use `container-fluid` to have it always take up 100% of the viewport.

## Bootstrap Buttons and Font Awesome
These still look out of place!

### Challenge: Add a Dark and Light Button
```html
<button type="button" class="btn btn-dark">Download</button>
<button type="button" class="btn btn-outline-light">Download</button>
```

The nifty icons come from [fontawesome.com](https://fontawesome.com/).

```html
<!-- Font Awesome -->
<script src="https://kit.fontawesome.com/bcee156780.js" crossorigin="anonymous"></script>


<div class="col-md-6">
  <h1 class="main_heading">Meet new and interesting dogs nearby.</h1>
  <button type="button" class="btn btn-dark btn-lg"><i class="fa-brands fa-apple"></i> Download</button>
  <button type="button" class="btn btn-outline-light btn-lg"><i class="fa-brands fa-google-play"></i> Download</button>
</div>
```

## Styling Our Website Challenges and Solutions
Style Navbar
```css
/* Navigation Bar */

  .navbar {
    padding-bottom: 4.5rem;
}

.navbar-brand {
  font-family: 'Ubuntu', sans-serif;
  font-size: 2.5rem;
  font-weight: bold;
}

.nav-link {
  font-size: 1.2rem;
  font-weight: 'Montserrat-Light';
}
```

Buttons and Images
```css
/* Download Buttons */

.download-button {
  margin: 5% 3% 5% 0;
}

/* Title Image */

.title-image {
  width: 60%;
  transform: rotate(25deg);
}
```

## Bootstrap Challenge 1
Now that you are starting to get to grips with Bootstrap and styling our website with Bootstrap classes, it's time for a challenge!


You're going to style the next section on our website by yourself. Here's the specification you should follow, it contains the colours, icons and fonts you should use. Try to get the margins/padding to look the same as the specification, but the exact values won't matter too much.


Step 1 - Add font awesome icons and format the text and icons. The icons to choose from font-awesome are: check-circle, bullseye and heart.
```html
<i class="fa-solid fa-circle-check"></i>
<i class="fa-solid fa-bullseye"></i>
<i class="fa-solid fa-heart"></i>
```

Step 2 - Make sure the layout is responsive, the icons should take up full width on medium sized screens and below e.g. iPad, phone.
```html
  <!-- Features -->

  <section id="features">
    <div class="row">
      <div class="feature-box col-lg-4 col-md-12">
        <i class="fa-solid fa-circle-check font-awesome"></i>
        <h3>Easy to use.</h3>
        <p>So easy to use, even your dog could do it.</p>
      </div>
      <div class="feature-box col-lg-4 col-md-12">
        <i class="fa-solid fa-bullseye font-awesome"></i>
        <h3>Elite Clientele</h3>
        <p>We have all the dogs, the greatest dogs.</p>
      </div>
      <div class="feature-box col-lg-4 col-md-12">
        <i class="fa-solid fa-heart font-awesome"></i>
        <h3>Guaranteed to work.</h3>
        <p>Find the love of your dog's life or your money back.</p>
      </div> 
    </div>
    </section>
```

But on desktop or large screen devices it should take up a 1/3 of the screen width.

Step 3 - Make the icons change colour when you mouse over the icons.
```css
.font-awesome {
  color: #ef8172;
  font-size: 3rem;
  padding-bottom: 1rem;
}

.font-awesome:hover {
  color: #ff4c68;
}
```

## Solution to Bootstrap Challenge 1
Didn't bother; pretty happy with own outcome.

## The Bootstrap Carousel: Part 1
Just did the prep styling for the testimonial and press sections.

```css
/* Testimonial Section */

#testimonials {
  padding: 7% 15%;
  text-align: center;
  background-color: #ef8172;
  color: #fff;
}

.testimonial-image {
  width: 10%;
  border-radius: 100%;
  margin: 20px;
}

#press {
  background-color: #ef8172;
  text-align: center;
  padding-bottom: 3%;
}

.press-logo {
  width: 15%;
  margin: 20px 20px 50px;
}
```

```html
  <!-- Testimonials -->

  <section id="testimonials">

    <h2>I no longer have to sniff other dogs for love. I've found the hottest Corgi on TinDog. Woof.</h2>
    <img class="testimonial-image" src="images/dog-img.jpg" alt="dog-profile">
    <em>Pebbles, New York</em>

    <!-- <h2 class="testimonial-text">My dog used to be so lonely, but with TinDog's help, they've found the love of their life. I think.</h2>
    <img class="testimonial-image" src="images/lady-img.jpg" alt="lady-profile">
    <em>Beverly, Illinois</em> -->

  </section>


  <!-- Press -->

  <section id="press">
    <img class="press-logo" src="images/techcrunch.png" alt="tc-logo">
    <img class="press-logo" src="images/tnw.png" alt="tnw-logo">
    <img class="press-logo" src="images/bizinsider.png" alt="biz-insider-logo">
    <img class="press-logo" src="images/mashable.png" alt="mashable-logo">

  </section>
```

## The Bootstrap Carousel: Part 2

```html
  <!-- Testimonials -->

  <section id="testimonials">

    <div id="testimonial-carousel" class="carousel slide" data-bs-ride="false">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <h2>I no longer have to sniff other dogs for love. I've found the hottest Corgi on TinDog. Woof.</h2>
          <img class="testimonial-image" src="images/dog-img.jpg" alt="dog-profile">
          <em>Pebbles, New York</em>
        </div>
        <div class="carousel-item">
          <h2 class="testimonial-text">My dog used to be so lonely, but with TinDog's help, they've found the love of their life. I think.</h2>
          <img class="testimonial-image" src="images/lady-img.jpg" alt="lady-profile">
          <em>Beverly, Illinois</em>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#testimonial-carousel" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#testimonial-carousel" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </section>
```

```css
.carousel-item {
  padding: 7% 15%;
}
```

## Bootstrap Cards
Bootstrap has a "[Pricing Page](https://getbootstrap.com/docs/5.0/examples/pricing/)" example.

She also recommends heading to [bootsnipp](https://bootsnipp.com) for a bunch of pre-made components.

They are using a bootstrap component to build the pricing page: bootstrap **cards**. That's how you can make sense of what's going on in the code.

```css
/* Pricing Section */

#pricing {
  padding: 100px;
  text-align: center;
}

.pricing-column {
  padding: 3% 2%;
}
```

```html
  <!-- Pricing -->

  <section id="pricing">

    <h2>A Plan for Every Dog's Needs</h2>
    <p>Simple and affordable price plans for your and your dog.</p>

    <div class="row row-cols-1 row-cols-lg-3 row-cols-md-2 g-4">
      <div class="pricing-column col">
        <div class="card h-100">
          <div class="card-header">
            <h3>Chihuahua</h3>
          </div>
          <div class="card-body">
            <h2>Free</h2>
            <p>5 Matches Per Day</p>
            <p>10 Messages Per Day</p>
            <p>Unlimited App Usage</p>
            <button class="w-100 btn btn-lg btn-outline-dark" type="button">Sign Up</button>
          </div>
        </div>
      </div>
      <div class="pricing-column col">
        <div class="card h-100">
          <div class="card-header">
            <h3>Labrador</h3>
          </div>
          <div class="card-body">
            <h2>$49 / mo</h2>
            <p>Unlimited Matches</p>
            <p>Unlimited Messages</p>
            <p>Unlimited App Usage</p>
            <button class="w-100 btn btn-lg btn-dark" type="button">Sign Up</button>
          </div>
        </div>
      </div>
      <div class="pricing-column col col-lg-4 col-md-12">
        <div class="card h-100">
          <div class="card-header">
            <h3>Mastiff</h3>
          </div>
          <div class="card-body">
            <h2>$99 / mo</h2>
            <p>Pirority Listing</p>
            <p>Unlimited Matches</p>
            <p>Unlimited Messages</p>
            <p>Unlimited App Usage</p>
            <button class="w-100 btn btn-lg btn-dark" type="button">Sign Up</button>
          </div>
        </div>
      </div>
    </div>

  </section>
```

## CSS Z-Index and Stacking Order
Out top title section is bigger than it needs to be. We want the phone image to hide behind the bottom section. We can handle this by the **Z-Index** (or position) whether it's more towards you or away from you. This is an advanced CSS element.

Absolute / Relative / Static Positioning.
- Absolute takes HTML elements out of the HTML flow

Z-Order naturally happens from top to bottom of the actual HTML document's text. There are other ways of changing the stacking order. We can use CSS by utilizing the property `z-index`.

Setting the `z-index` to 1 will bring it to the front. -1 will send it to the back. The default `z-index` of elements are 0. If all have the same `z-index`, then stacking order will be maintained by the order in which it is written in the file.

`z-index` only works if it has a position. Static, for example, will make it appear that it is not working.

This was a bit wild.

```css
#features {
  padding: 7% 15%;
  background-color: white;
  position: relative;
}

.title-image {
  width: 20%;
  transform: rotate(25deg);
  position: absolute;
  right: 22%;
}
```

I'm not sure why, but my `.title-image width` had to be adjusted when her's did not need it.

## Advanced CSS - Media Query Breakpoints
Weirdness with image scaling for desktop to mobile. 

Mobile-First! Why can't I just have 1 design have it be looking good on the web? Since 2016 mobile browsers surpassed desktop browsers. 

Google Rankings are affected by whether or not it's mobile-friendly for Google Search Rankings.

I only want my text to be red when they print... Going to use `@media print`
`@speech` and `@screen` are other options.

```html
<h1>Hello World</h1>
```

```css
@media print {
h1 {
  color: red;
}
}
```

### Media Query Structure
`@media <type> <feature>`

Checking to see if something is true or false. If the media is a screen and the feature is that it's minimum width is 900 pixels, then change something.
```css
@media screen (min-width: 900px) {
  //change something
}
```

Continuing Demo:
```html
<h1>Hello World</h1>
```

```css
h1 {
  font-size: 30px;
}

@media (max-width: 900px) {
h1 {
  /* color: red; */
  font-size: 60px;
}
}
```

We created a media query breakpoint at 900 pixels that will override our font size for smaller devices. 

We need the image to be displayed as `static` when it's on a smaller screen and not be rotated. It also needs its width change. Text will need to be center aligned instead of left.

Solution:
```css
@media (max-width: 1028px) {
  #title {
    text-align: center;
  }
  .title-image {
    position: static;
    transform: rotate(0);
    width: 60%;
  }
}
```

## Bootstrap Challenge 2
In this challenge, you are going to complete the layout and design of our TinDog website. Similar to the previous challenge, below is a specification. Use what you have learnt about CSS and Bootstrap to format the appearance of your website's last two sections to look the same as the specification. The fonts and colours have been specified by you should use your judgement and create the margins/padding by eye.

- [x] Font Awesome Button Icons
- [x] Section Background COlor of #ff4c68
- [x] Large Bootstrap Buttons (Dark Themed)
- [x] Montserrat Black Text
- [x] Bottom section background #fff
- [x] Font Awesome: Twitter, Facebook, Instagram, Envelope

## Solution to Bootstrap Challenge 2

### CTA Section

```html
  <!-- Call to Action -->
  
  <section id="cta">
    
    <h3 class="cta-heading">Find the True Love of Your Dog's Life Today.</h3>
    <button type="button" class="btn btn-dark btn-lg download-button"><i class="fa-brands fa-apple"></i> Download</button>
    <button type="button" class="btn btn-outline-light btn-lg download-button"><i class="fa-brands fa-google-play"></i> Download</button>

  </section>
```

```css
/* CTA Section */

#cta {
  background-color: #ff4c68;
  color: #fff;
  padding: 7% 15%;
  text-align: center;
}

.cta-heading {
  font-weight: 900;
  font-size: 3.5rem;
  line-height: 1.5rem;
}
```

### Footer Section

```html
  <!-- Footer -->

  <footer id="footer">

    <i class="social-icon fa-brands fa-twitter footer-icons"></i>
    <i class="social-icon fa-brands fa-facebook-f footer-icons"></i>
    <i class="social-icon fa-brands fa-instagram footer-icons"></i>
    <i class="social-icon fa-solid fa-envelope footer-icons"></i>
    <p>© Copyright 2018 TinDog</p>

  </footer>
```
```css
/* Footer Section */

#footer {
  padding: 7% 15%;
  text-align: center;
}

.social-icon {
  margin: 20px 10px;
}
```

### Update Navbar
```html
      <!-- Nav Bar -->
      <nav class="navbar navbar-expand-lg navbar-dark">
        <a class="navbar-brand" href="">tindog</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link" href="#footer">Contact</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#pricing">Pricing</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#cta">Download</a>
                </li>
            </ul>
        </div>
      </nav>
```

## Code Refactoring
Our `styles.css` is atrocious.

We want to be DRY: Do Not Repeat Yourself

We want to keep it performant and easy to read.

Suitcase packing anecdote. 

### Guiding Principles
1. Readability
2. Modularity
3. Efficiency
4. Length

## Refactoring Our Website: Part 1
We shouldn't be applying styles to things like `<h1>` tags if we aren't planning on using it for *every* tag.

Condensed our CSS and added a few new classes. Adhering to DRY.

## Advanced CSS - Combining Selectors

### Multiple Selectors: 

```css
selector1, selector2 {

}
```

### Hierarchical Selectors
This is a bad example though, because ids are unique. So if you're going to change the css of an id, there's not much reason to select deeper things.
```css
#title .container-fluid {
  padding-top: 3%;
  text-align: left;
}
```

The below is a good example, however.
```css
div .container-fluid {

}
```

You read selectors from right to left.

### Combined Selectors
```css
selector1.selector2 {

}

selector1#selector2 {

}

h1#title {color: red}
```

The following doesn't work (if you don't have that set in your html)
```css
div#title {color: red}
```
```html
<div class="container-fluid">
  <h1 id="title">Hello World</h1>
</div>
```

Combined Selectors don't utilizie spaces, so it's pretty much direct inheritance from the parent. If that path doesn't exist, it won't do anything.

Example:
```html
<div class="container">
  <h1 class="title">Hello World</h1>
</div>
<div class="container-fluid">
  <h1 calss="title">Good Bye World!</h1>
</div>
```

Look for a class of container but also a class of title. This isolates the **Hello World.**
```css
.container .title {
  color: red;
}
```

## Refactoring Our Website: Part 2
After looking at combining selectors, we can continue our refactor.

White Background = Black Text
Red Background = White Text

Going to create classes for **Colored** and **white** sections.

```css
/* Sections */

.colored-section {
  background-color: #ff4c68;
  color: #fff;
}

.white-section {
  background-color: white;
}
```


## Advanced CSS - Selector Priority
in-line styles > `#ids` > `.class` > `raw html elements`

Last definition receives priority.

Prevent conflicting rules; use `ids` sparingly. Just because you have one of something isn't a good enough reason to use an id rather than a class for CSS.

Try using only 1 class.

Avoid in-line styles at all costs.

## Completing the Website

It's all done!