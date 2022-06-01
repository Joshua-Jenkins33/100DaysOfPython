# Day 43: Web Foundation CSS

## Introduction to CSS
Cascading Style Sheets!

You can't get super pretty with just HTML. HTML is really wordy to handle page layout. You have to use tables. Yuck.
Tables are easy to make syntax errors. It's also difficult to debug. Embedding tables within tables is a horrible mess.

CCS can't really do anything by itself. They're pretty much just for styling and making things look nice.

## Inline CSS
Change the background! 

Inject CSS into the tag we want to affect. To change the background, we'll modify the `<body>` tag.

The `style=""` attribute injects CSS into the HTML file.

```html
<body style="background-color: blue;">
</body>
```

Go to [colorhunt.co](colorhunt.co) for sweet colors.

```html
<body style="background-color: #F1EEE9;">
</body>
```

## Internal CSS
Go to [devdocs.io](devdocs.io) for lots of documentation.

How to implement CSS code across the entire web page so we won't have to copy and paste the style attribute each time we want to change a particular element. 

In the `<head>` section of the HTML page, we're going to create open and closing `<style>` tags.

```html
<style>
    body {
        background-color: #F1EEE9;
    }
</style>
```

Now we can delete the in-line style CSS.

Now I want to make the `hr` white.

```html
<style>
    body {
        background-color: #F1EEE9;
    }
    hr {
        background-color: white;
    }
</style>
```

But this changes nothing... Browser is setting some CSS by default!

Change the border-style to none!
```html
<style>
    body {
        background-color: #F1EEE9;
    }
    hr {
        background-color: white;
        border-style: none;
        height: 2px;
    }
</style>
```

She likes to use a chrome plug-in called [Pesticide](https://chrome.google.com/webstore/detail/pesticide-for-chrome/bakpbgckdnepkmkeaiomhmfcnejndkbi). Her company developed it!

You can use percentages (good for x-device styling) or pixels.

### Challenge: Make a dotted line 10% of the screen
```html
<style>
hr {
    width: 10%;
    border-style: dotted none none;
    border-width: 5px;
    border-color: #15133C;
}
</style>
```

The downside of this is... you have to change it in every single place. Easier than doing in-line styling, but repetitive nonetheless.

## External CSS
Going to change our personal site to use internal CSS and migrate to external CSS.

1. Create a new folder called `css`. In the newly created folder, create a file called `styles.css`
2. Cut out everything in your `<style>` tags and remove the tags
3. Paste the values in `styles.css`
4. Create a link in your pages to the css folder: `<link rel="stylesheet" href="css/styles.css">`

### Challenge: Modify the `<h1>` and `<h3>` tags to be a different color
```css
h1 {
    color: #15133C;
}

h3 {
    color: #15133C;
}
```

## How to Debug CSS Code
TLDR; Use the browser dev tools to see granular details and remove/add things.

### Debugging Problem 1
`<link rel="stylesheet" href="/css/styles.css">`

The forward slash needed to be removed.

### Debugging Problem 2
`<body style="background-color: white">`

Our style overrode our css file.

## The Anatomy of CSS Syntax

Keep all of your properties in alphabetical order.

Anatomy:
- Who (tag)
- What (properties)
    - How do you know what keywords and attributes you can use? [developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/CSS)

## CSS Selectors

If we wanted to add a broccoli image with a different background color, then we can't just used tag selectors. We'll need to use **class** selectors.

```html
  <img class="" src="https://emojipedia-us.s3.amazonaws.com/thumbs/240/apple/118/bacon_1f953.png" alt="bacon-img">
  <img class="" src="https://emojipedia-us.s3.amazonaws.com/thumbs/240/apple/118/broccoli_1f966.png" alt="broccoli-img">
```

```css
/*****************************TAG SELECTORS*****************************/

h1 {
    color: red;
    font-size: 200px;
}

/*
img {
    background-color: red;
}
*/

/*****************************CLASS SELECTORS*****************************/

.bacon {
    background-color: green;
}

.broccoli {
    background-color: red;
}
```

It's rare you'll want to style paragraphs and images exactly the same way. Classes enable you to do that!

## Classes vs. Ids

The `id` selector is different but similar. 

```html
<h1 id="heading">I Love Bacone</h1>
```

```css
/*****************************TAG SELECTORS*****************************/

h1 {
    color: red;
    font-size: 200px;
}

/*
img {
    background-color: red;
}
*/

/*****************************CLASS SELECTORS*****************************/

.bacon {
    background-color: green;
}

.broccoli {
    background-color: red;
}

/*****************************ID SELECTORS*****************************/
#heading {
    color: blue;
}
```

`id`s are more specific than class selectors, so it'll override the values!

`class`es are more specific than tag selectors.

### When Should You Use Classes / IDs?

You can only have a single instance of one particular id name inside a single page. I can't go into another paragraph `<p>` tag and give it the same `id` as the `<p>` tag above it. You *can* use classes for all of the different `<p>` tags, though. A group of related items. Name versus passport!

You can't have more than 1 ID per element.

### Pseudo Class

These have `:` (colons) in front of them. I can get the state to change if I hover over an image. `a:hover{}`.

```css
/*****************************TAG SELECTORS*****************************/

h1 {
    color: red;
    font-size: 200px;
}


img:hover {
    background-color: gold;
}

/*****************************CLASS SELECTORS*****************************/

.bacon {
    background-color: green;
}

.broccoli {
    background-color: red;
}

/*****************************ID SELECTORS*****************************/
#heading {
    color: blue;
}
```

## Quiz 16: CSS Quiz

1. What is the correct HTML for referring to an external CSS stylesheet?
`<link rel="stylesheet" type="text/css" href="mystles.css">`

2. Where in an HTML document is the correct place to refer to an internal style sheet?
`In the <head> section`

3. Which HTML attribute is used to define inline styles?
``style`

4. Which HTML tag is used to define an internal style sheet?
`<style>`

5. Which is the correct CSS syntax?
`body {color:black;}`

6. Which is more specific as a selector?
`id`

