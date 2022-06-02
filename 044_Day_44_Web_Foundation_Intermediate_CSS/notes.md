# Day 44: Web Foundation -- Intermediate CSS

## Wha We'll Make -- Stylized Personal Site

We've gotten pretty far in our journey of creating our personal website, but we are done aspiring to be like Computer Science professors.

### Challenge
- Create a new folder called `CSS - My Site`
- Create an `index.html`
- Add the HTML backbone and give your website a title of your name
- Create a css folder and a `styles.css` file
- Link up your html and css and give the background an ugly blue color


## What Are Favicons
"Favorite Icon"

An icon that would show up in your browser bar if you were on a website you favorited. Browsers try to display a favicon whether the site has one or not. 

[www.favicon.cc](www.favicon.cc)

```html
<link rel="icon" href="favicon.ico">
```

## HTML Divs
Divs allow us to structure elements differently. Divs, amongst other things, don't do anything unless you use css with it. It stands for a content-division element. It allows you to split up or divide content into separate containers or boxes so you can affect its layout separately. You can structure and style things separately from other content in your website. It'll have height if you specify it **or** if it has content. 

These have **margins**, **borders**, and **padding**. 

There are default rules for the divs contents, like `<h1>` tags. These have preset margins and can create gaps even when your div has these set to 0.

## The Box Model of Website Styling
Simple div with background color blue, 300px x 300px. If we expand it to 600px, other stuff gets pushed out of the way. We can use pixels or percentages. You can also specify a **border**. The blue area is still 300x300 with a border. The border expands its size.

**Circle shorthand**, clockwise, specifies all four sides starting at the time.

Content in the div/box; let's say it's text. We want there to be space between the text and the border. This is **padding**. 

The **margin** is a buffer zone between the current element and everything else. We can use these to affect the layout and appearance of all of our html elements (which we've learned at this point, all html elements are boxes)!

### Challenge: Make Div Boxes
- 2 Divs
- Called middle-container & bottom-container
- First div a class of top-container
- 200x200px squares
- Each with different background colors

### Challenge: Diagonal Div Boxes
```css
.top-container {
  border: solid 10px;
}

.middle-container {  
  border: solid 20px;
  margin-left: 260px;
}

.bottom-container {
  border: solid 10px;
  margin-left: 500px;
}
```

## CSS Display Property

## CSS Static and Relative Positioning

## Absolute Positioning

## The Dark Art of Centering Elements with CSS

## Font Styling in Our Personal Site

## Adding Content to Our Website

## CSS Sizing

## Font Properties Challenge 1 -- Change the Font Color

## Font Properties Challenge 2 -- Change the Font Weight

## Font Properties Challenge 3 -- Change the Line Height

## CSS Font Property Challene Solutions

## CSS Float and Clear

## CSS Challenge

## Stylized Personal Site Solution Walkthrough

## Get More Practice HTML and CSS
