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

## Bootstrap Cards

## CSS Z-Index and Stacking Order

## Advanced CSS - Media Query Breakpoints

## Bootstrap Challenge 2

## Solution to Bootstrap Challenge 2

## Code Refactoring

## Refactoring Our Website: Part 1

## Advanced CSS - Combining Selectors

## Refactoring Our Website: Part 2

## Advanced CSS - Selector Priority

## Completing the Website