# Day 41: Web Foundation: HTML

## How Does the Internet Actually Work?
Some people think of it as a cloud. Hanging around in the sky, super complex, super hard to understand.

That's not it at all. The internet is really simple; it's a long piece of wire. That wire connects different computers together. Computer in Seattle can communicate with and shuffle data to a computer in London.

Some of these computers have a very special job; they have to be online 24/7, ready to serve you all of the data you're actually requesting when you try to access websites. These computers are called **servers**. Computers, like yours that are trying to access this information across the Internet, are called **clients**.

A **webserver**. A giant library that's open 24/7; you can go there at any hour of the day and make a request. It'll be there to serve you at any hour. 

Your browser will send a request/message to your **Internet Service Provider**. The ISP relays that information to a **DNS Server** (souped up Phone Book; looking at the exact IP Address of the website you're looking for). An **IP Address** is like a postal address for your computer. Once the DNS Server finds the IP address, it sends it back to your computer. You then deliver that message to the specific IP address through your Internet Service Provider. The message is delivered via what's called the **Internet Backbone**, which is literally the backbone of the internet. Just go to [www.submarinecablemap.com](https://www.submarinecablemap.com/#/) to see all of the underwater cables that power the internet. The internet is made up of these huge sprawling masses of wires connecting all of the world.

To make a request from London to Seattle, the request travels through the cables that cross the Atlantic Ocean. Once the computer received my request, the server will send that back. 

## How Do Websites Actually Work?

*What does HTML, CSS, JavaScript do?*

You need a **Browser**, which are pieces of software that allow you to look up the IP address of a website and receive data that will render into websites. They are composed of these three types of code files: HTML, CSS, JS. Each of these have different jobs.

**HTML** Is responsible for the structure of your website; if your website is your house, HTML would be the builder. They establish the structure of your house. Adding an image, button, text box, etc.

**CSS** This is responsible for styling your website. Painters, etc, in the house analogy. I want the button to be red, the text to be white, etc.

**JavaScript** Allows your website to do things, to have some kind of behavior. This is like the electrician for your house. Wires so that your lightbulbs actually turn on, or plumbing for your toilet to flush. 

## Introduction to HTML
Create an HTML that has a title that says "Hello" and a body that says "Hello World!".

```html
<head>
    <title>Hello</title>
</head>

<body>
    <h1>Hellow World!</h1>
</body>
```

HTML is the foundation of all websites. You can create a website using only an HTML file, though you can't with CSS or JavaScript.

**HTML Acronym.** HyperText Markup Language

Other Markup Languages
- XML: Extensible Markup Language
- GML: Generalized Markup Language

They're all based on **markup**, where editors would mark up manuscripts and either specify changes to the author or specify structural changes to the publishers. HTML works much the same way. You can specify the structure of your website via tags.

### The Adventures of Sherlock Holmes
[gutenkberg.org](https://www.gutenberg.org/files/1661/1661-h/1661-h.htm)

You can view the file in plain text or in HTML. She uses this an example of what plain text looks like in an HTML file and then what you can do to the structure of that plain text file by using HTML tags.

```html
<h1>THE ADVENTURES OF SHERLOCK HOLMES</h1>

<h3>by</h3>

<h2>SIR ARTHUR CONAN DOYLE</h2>
```

`h6` is the smallest font size for a heading. How do you know? Documentation. Find out how to help yourself. She recommends MDN or w3 schools for HTML and headings. She also likes [devdocs.io](devdocs.io). It's structured in a simple way that's easy to follow.

Now we need to work on spacing:
```html
<h1>THE ADVENTURES OF SHERLOCK HOLMES</h1>
<br>
<h3>by</h3>
<br>
<h2>SIR ARTHUR CONAN DOYLE</h2>
```

`<br>` doesn't need an open or closing tags. It works all by itself.


## The Anatomy of an HTML Tag
`<h1>Hello World!</h1>`

Here we have an opening tag (`<h1>`), the content (`Hello World!`), and a closing tag (`</h1>`).

Self-closing tags: `<br>`. 

How do we find out if something requires opening/closing tags or is self-closing? Go to the documentation and find out. On [devdocs.io](devdocs.io), you can view the **Tag Omission** category.

```html
<hr>
<h1>THE ADVENTURES OF SHERLOCK HOLMES</h1>
<br>
<h3>by</h3>
<br>
<h2>SIR ARTHUR CONAN DOYLE</h2>
<hr>
```

Notice that their (gutenberg's) `<hr>` tags are rendered thicker than ours. Cheat by using the `inspect element` functionality from your browser. There's shows up with additional information: 
- `<hr size="3" noshade> == $0`
- `<hr` -- The HTML element
- `size="3">` -- HTML Attribute (more information to the browser to specify modifications to the website)

Attributes are also contained on the documentation. 

```html
<center>
<hr size="3" noshade>
<h1>THE ADVENTURES OF SHERLOCK HOLMES</h1>
<br>
<h3>by</h3>
<br>
<h2>SIR ARTHUR CONAN DOYLE</h2>
<hr size="3" noshade>
</center>
```

## What we're building -- HTML Personal Site
Going to be building an HTML-only, super-basic website. Justified because big tech name folks have pretty awful person sites.

## What is the HTML Boilerplate?
A template. The word comes from the printer presses that used "boiler plates", and they coined that phrase because their templates of stamping characters looked a lot like the text on actual boiler plates.

```html
<html <!DOCTYPE html> <!-- This tells it to render it in HTML 5-->
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        
    </body>
</html>
```

**HTML Tags**
Everything between these tags is html code.

**Head Tags**
The part of the HTML file that holds information about the web page and tells the browser how it should handle the page. It'll give it a title...
```html
<html <!DOCTYPE html> <!-- This tells it to render it in HTML 5-->
<html>
    <head>
        <meta charset="utf-8">
        <title>My Personal Site</title>
    </head>
    <body>
        
    </body>
</html>
```

You can open your HTML page by pasting the path into a browser.

### Metatags
The *meta* element... These give extra extra meta data or associated data to your HTML document; we're telling the browser that all our text is encoded using the UTF-8 encoding system. This determines what characters will be uploaded correctly. Mojibake—characters that are transformed because it's using the wrong character set for the characters being requested. 

UTF-8 contains all of these characters. It also includes emojis.

Metatags have attributes, as well. `name` allows you to specify which attribute to modify, like any of the following: description, keywords, author, viewport, etc.

## How to Structure Text in HTML
- [x] Add a Level 1 heading that contains your name.

```html
<html <!DOCTYPE html> <!-- This tells it to render it in HTML 5-->
<html>
    <head>
        <meta charset="utf-8">
        <title>Josh's Personal Site</title>
    </head>
    <body>
        <h1>Joshua Jenkins</h1>
    </body>
</html>
```

- [x] Add a paragraph tag that contains your title and italicize it
```html
<html <!DOCTYPE html> <!-- This tells it to render it in HTML 5-->
<html>
    <head>
        <meta charset="utf-8">
        <title>Josh's Personal Site</title>
    </head>
    <body>
        <h1>Joshua Jenkins</h1>
        <br>
        <p><em>Data Engineer at VisitPay</em></p>
    </body>
</html>
```

**The difference between `<i>` and `<em>`...**
`<i>` doesn't emphasize the text (doesn't convey as much information), it just stylizes it.

`<em>` emphasizes italics, `<strong>` emphasizes bolds. You generally want the emphasis.

- [x] Add a new paragraph with a brief bio.

```html
<html <!DOCTYPE html> <!-- This tells it to render it in HTML 5-->
<html>
    <head>
        <meta charset="utf-8">
        <title>Josh's Personal Site</title>
    </head>
    <body>
        <h1>Joshua Jenkins</h1>
        <p><em>Data Engineer at VisitPay</em></p>
        <br>
        <p>I'm a husband, father, member of The Church of Jesus Christ of Latter-day Saints, and Data Engineer. I've got two happy golden retrievers and love to spend my free time working on 100 Days of Code, tackling a mountain peak, visiting family, swimming, playing Dungeons and Dragons, and occasionally hang out in World of Warcraft.</p>
    </body>
</html>
```

- [x] Add a horizontal rule after your bio
```html
<html <!DOCTYPE html> <!-- This tells it to render it in HTML 5-->
<html>
    <head>
        <meta charset="utf-8">
        <title>Josh's Personal Site</title>
    </head>
    <body>
        <h1>Joshua Jenkins</h1>
        <p><em>Data Engineer at VisitPay</em></p>
        <br>
        <p>I'm a husband, father, member of The Church of Jesus Christ of Latter-day Saints, and Data Engineer. I've got two happy golden retrievers and love to spend my free time working on 100 Days of Code, tackling a mountain peak, visiting family, swimming, playing Dungeons and Dragons, and occasionally hang out in World of Warcraft.</p>
        <hr>
    </body>
</html>
```

- [x] Add a level 3 heading underneath the horizontal rule and call it education, listing all the schools you've attended.
```html
<html <!DOCTYPE html> <!-- This tells it to render it in HTML 5-->
<html>
    <head>
        <meta charset="utf-8">
        <title>Josh's Personal Site</title>
    </head>
    <body>
        <h1>Joshua Jenkins</h1>
        <p><em>Data Engineer at VisitPay</em></p>
        <br>
        <p>I'm a husband, father, member of The Church of Jesus Christ of Latter-day Saints, and Data Engineer. I've got two happy golden retrievers and love to spend my free time working on 100 Days of Code, tackling a mountain peak, visiting family, swimming, playing Dungeons and Dragons, and occasionally hang out in World of Warcraft.</p>
        <hr>
        <h3>Education</h3>
        <ul>
            <li>Bachelor's in Information Systems</li>
            <ul>
                <li>BYU Marriott School of Business (2017-2019)</li>
                <li>Brigham Young University (2015-2019)</li>
            </ul>
            <li>Rigby High School (2009-2012)</li>
        </ul>
    </body>
</html>
```
## HTML Lists
- [x] Add a level 3 heading called "Hobbies" and list several hobbies listed using an ordered list
```html
<html <!DOCTYPE html> <!-- This tells it to render it in HTML 5-->
<html>
    <head>
        <meta charset="utf-8">
        <title>Josh's Personal Site</title>
    </head>
    <body>
        <h1>Joshua Jenkins</h1>
        <p><em>Data Engineer at VisitPay</em></p>
        <br>
        <p>I'm a husband, father, member of The Church of Jesus Christ of Latter-day Saints, and Data Engineer. I've got two happy golden retrievers and love to spend my free time working on 100 Days of Code, tackling a mountain peak, visiting family, swimming, playing Dungeons and Dragons, and occasionally hang out in World of Warcraft.</p>
        <hr>
        <h3>Education</h3>
        <ul>
            <li>Bachelor's in Information Systems</li>
            <ul>
                <li>BYU Marriott School of Business (2017-2019)</li>
                <li>Brigham Young University (2015-2019)</li>
            </ul>
            <li>Rigby High School (2009-2012)</li>
        </ul>
        <h3>Hobbies</h3>
        <ol>
            <li>Be a father to my wonderful little boy</li>
            <li>Be a husband to my darling wife</li>
            <li>Expand my technical expertise by working through online courses like 100 Days of Code</li>
            <li>Play and Run Dungeons and Dragons Adventures</li>
            <li>Attend activities through my Church</li>
            <li>Be an active homeowner</li>
            <li>Workout: Swimming</li>
            <li>Summit Mountains with my Pups</li>
            <li>Play RPGs; currently into World of Warcraft</li>
        </ol>
    </body>
</html>
```

## HTML Image Elements
`<img src="angela.png">`

This is another self-closing tag. But just having `<img>` isn't enough. You *have* to have the `src` attribute populated, as this tells the `<img>` tag *what* image is going to be used.

`<src>` can be a url (fetched from an internet), or a path file your website has access to.

`alt=""` attribute
- This is for if a browser cannot render the image, then it will simply display an alternative text to the user to describe what the image was about.

This is used for SEO; Google looks at alt texts. 

To remove our reliance on twitter, we can put the image into our folder.

- [x] Add an image
```html
<html <!DOCTYPE html> <!-- This tells it to render it in HTML 5-->
<html>
    <head>
        <meta charset="utf-8">
        <title>Josh's Personal Site</title>
    </head>
    <body>
        <img src="images\professional_josh_circle.png" alt="Profile picture for Joshua Jenkins">
        <h1>Joshua Jenkins</h1>
        <p><em>Data Engineer at VisitPay</em></p>
        <br>
        <p>I'm a husband, father, member of The Church of Jesus Christ of Latter-day Saints, and Data Engineer. I've got two happy golden retrievers and love to spend my free time working on 100 Days of Code, tackling a mountain peak, visiting family, swimming, playing Dungeons and Dragons, and occasionally hang out in World of Warcraft.</p>
        <hr>
        <h3>Education</h3>
        <ul>
            <li>Bachelor's in Information Systems</li>
            <ul>
                <li>BYU Marriott School of Business (2017-2019)</li>
                <li>Brigham Young University (2015-2019)</li>
            </ul>
            <li>Rigby High School (2009-2012)</li>
        </ul>
        <h3>Hobbies</h3>
        <ol>
            <li>Be a father to my wonderful little boy</li>
            <li>Be a husband to my darling wife</li>
            <li>Expand my technical expertise by working through online courses like 100 Days of Code</li>
            <li>Play and Run Dungeons and Dragons Adventures</li>
            <li>Attend activities through my Church</li>
            <li>Be an active homeowner</li>
            <li>Workout: Swimming</li>
            <li>Summit Mountains with my Pups</li>
            <li>Play RPGs; currently into World of Warcraft</li>
        </ol>
    </body>
</html>
```

## HTML Links and Anchor Tags
`<a href=""</a>`

Hyperlinks to other sources.


```html
<html <!DOCTYPE html> <!-- This tells it to render it in HTML 5-->
<html>
    <head>
        <meta charset="utf-8">
        <title>Josh's Personal Site</title>
    </head>
    <body>
        <img src="images\professional_josh_circle.png" alt="Profile picture for Joshua Jenkins">
        <h1>Joshua Jenkins</h1>
        <p><em>Data Engineer at <a href="https://www.visitpay.com/">VisitPay</a></em></p>
        <br>
        <p>I'm a husband, father, member of The Church of Jesus Christ of Latter-day Saints, and Data Engineer. I've got two happy golden retrievers and love to spend my free time working on 100 Days of Code, tackling a mountain peak, visiting family, swimming, playing Dungeons and Dragons, and occasionally hang out in World of Warcraft.</p>
        <hr>
        <h3>Education</h3>
        <ul>
            <li>Bachelor's in Information Systems</li>
            <ul>
                <li>BYU Marriott School of Business (2017-2019)</li>
                <li>Brigham Young University (2015-2019)</li>
            </ul>
            <li>Rigby High School (2009-2012)</li>
        </ul>
        <h3>Hobbies</h3>
        <ol>
            <li>Be a father to my wonderful little boy</li>
            <li>Be a husband to my darling wife</li>
            <li>Expand my technical expertise by working through online courses like 100 Days of Code</li>
            <li>Play and Run Dungeons and Dragons Adventures</li>
            <li>Attend activities through my Church</li>
            <li>Be an active homeowner</li>
            <li>Workout: Swimming</li>
            <li>Summit Mountains with my Pups</li>
            <li>Play RPGs; currently into World of Warcraft</li>
        </ol>
    </body>
</html>
```

What if I want to store information on a different page?
1. Create a new page in the same directory
2. Say `hobbies.html`
3. In an `<a>` tag on `index.html`, reference `hobbies.html` like so: `<a href="hobbies.html">Hobbies</a>`

### Index Page
```html
<html <!DOCTYPE html> <!-- This tells it to render it in HTML 5-->
<html>
    <head>
        <meta charset="utf-8">
        <title>Josh's Personal Site</title>
    </head>
    <body>
        <img src="images\professional_josh_circle.png" alt="Profile picture for Joshua Jenkins">
        <h1>Joshua Jenkins</h1>
        <p><em>Data Engineer at <a href="https://www.visitpay.com/">VisitPay</a></em></p>
        <br>
        <p>I'm a husband, father, member of The Church of Jesus Christ of Latter-day Saints, and Data Engineer. I've got two happy golden retrievers and love to spend my free time working on 100 Days of Code, tackling a mountain peak, visiting family, swimming, playing Dungeons and Dragons, and occasionally hanging out in World of Warcraft.</p>
        <hr>
        <h3>Education</h3>
        <ul>
            <li>Bachelor's in Information Systems</li>
            <ul>
                <li>BYU Marriott School of Business (2017-2019)</li>
                <li>Brigham Young University (2015-2019)</li>
            </ul>
            <li>Rigby High School (2009-2012)</li>
        </ul>
        <a href="hobbies.html">Hobbies Page</a>
        <a href="contact_me.html">Contact Me</a>
    </body>
</html>
```

### Hobbies Page
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Joshua's Personal Site</title>
</head>
<body>
    <h3>Hobbies</h3>
    <ol>
        <li>Be a father to my wonderful little boy</li>
        <li>Be a husband to my darling wife</li>
        <li>Expand my technical expertise by working through online courses like <a href="https://github.com/Joshua-Jenkins33/100DaysOfPython">100 Days of Code</a></li>
        <li>Play and Run <a href="https://www.dndbeyond.com/">Dungeons and Dragons Adventures</a></li>
        <li>Attend activities through my church, <a href="https://www.churchofjesuschrist.org/?lang=eng">The Church of Jesus Christ of Latter-day Saints</a></li>
        <li>Be an active homeowner</li>
        <li>Workout: Swimming</li>
        <li>Summit Mountains with my Pups</li>
        <li>Play RPGs; currently into <a href="https://worldofwarcraft.com/en-us/">World of Warcraft</a></li>
    </ol>
    <a href="index.html">Main Page</a>
    <a href="contact_me.html">Contact Me</a>
</body>
</html>
```

### Contact Me Page
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Joshua's Personal Site</title>
</head>
<body>
    <h1>My Contact Details</h1>
    <p>My Fictional Address</p>
    <p>Phone Number: 029-392-2098</p>
    <p>myemail@email.com</p>
    <a href="index.html">Main Page</a>
</body>
</html>
```