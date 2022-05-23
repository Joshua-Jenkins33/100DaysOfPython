# Day 42: Web Foundation — Intermediate HTML

## HTML Tables
Tables have headers, bodies, and footers. `<thead></thead> | <tbody></tbody> | <tfooter></tfooter>`.

The reason you'd utilize these different headers is to allow for functionality, like keeping the header row static and allowing you to scroll through the body table.

The MDN Developer docs has some examples. It shows a bunch of attributes to change the table appearance. But those are all deprecated.

It's downgraded. People recommend you don't use them because they're no longer supported.

## Using HTML Tables for Layout
We could use divs for this buuuuut... we haven't learned about those yet, so we're going to use a table grid.
```html
<html <!DOCTYPE html> <!-- This tells it to render it in HTML 5-->
<html>
    <head>
        <meta charset="utf-8">
        <title>Josh's Personal Site</title>
    </head>
    <body>
        <table>
            <tr>
                <td><img src="images\professional_josh_circle.png" alt="Profile picture for Joshua Jenkins"></td>
                <td>
                    <h1>Joshua Jenkins</h1>
                    <p><em>Data Engineer at <a href="https://www.visitpay.com/">VisitPay</a></em></p>
                    <p>I'm a husband, father, member of The Church of Jesus Christ of Latter-day Saints, and Data Engineer. I've got two happy golden retrievers and love to spend my free time working on 100 Days of Code, tackling a mountain peak, visiting family, swimming, playing Dungeons and Dragons, and occasionally hanging out in World of Warcraft.</p>
                </td>
            </tr>
        </table>
        <hr>
        <h3>Education</h3>
        ...
```

Taboo—using the table tag attributes for styling...

```html
<table cellspacing="20">
    <tr>
        <td><img src="images\professional_josh_circle.png" alt="Profile picture for Joshua Jenkins"></td>
        <td>
            <h1>Joshua Jenkins</h1>
            <p><em>Data Engineer at <strong><a href="https://www.visitpay.com/">VisitPay</a></strong></em></p>
            <p>I'm a husband, father, member of The Church of Jesus Christ of Latter-day Saints, and Data Engineer. I've got two happy golden retrievers and love to spend my free time working on 100 Days of Code, tackling a mountain peak, visiting family, swimming, playing Dungeons and Dragons, and occasionally hanging out in World of Warcraft.</p>
        </td>
    </tr>
</table>
```

## HTML Tables Code Challenge
Create a table where you have an h3 for a title of Skills. You've got your skill on left and the number of stars (emojis) for how familiar you are with it. Have two columns.

## How to Type Emojis
You can utilize the `WIN+.` shortcut to pull up the emojis keyboard. Wild.

## HTML Tables Solution Walkthrough
Nested tables. Ick. I did it right.

```html
<table>
    <tbody>
        <tr>
            <td>
                <table>
                    <tr>
                        <td>Python</td>
                        <td>⭐⭐⭐⭐</td>
                    </tr>
                </table>
            </td>
            <td>
                <table>
                    <tr>
                        <td>Gimp</td>
                        <td>⭐</td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td>
                <table>
                    <tr>
                        <td>Object-oriented Programming (OOP)</td>
                        <td>⭐⭐⭐</td>
                    </tr>
                </table>
            </td>
            <td>
                <table>
                    <tr>
                        <td>Cartography (Fantasy)</td>
                        <td>⭐⭐</td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td>
                <table>
                    <tr>
                        <td>JavaScript</td>
                        <td>⭐⭐⭐</td>
                    </tr>
                </table>
            </td>
            <td>
                <table>
                    <tr>
                        <td>Databricks</td>
                        <td>⭐⭐⭐⭐</td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td>
                <table>
                    <tr>
                        <td>CRM Automation</td>
                        <td>⭐⭐</td>
                    </tr>
                </table>
            </td>
            <td>
                <table>
                    <tr>
                        <td>React</td>
                        <td>⭐⭐</td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td>
                <table>
                    <tr>
                        <td>Linux</td>
                        <td>⭐⭐</td>
                    </tr>
                </table>
            </td>
            <td>
                <table>
                    <tr>
                        <td>HTML & CSS</td>
                        <td>⭐⭐</td>
                    </tr>
                </table>
            </td>
        </tr>
    </tbody>
</table>
```

## HTML Forms
Forms require an opening and closing `<form>` tag. It has two very important elements:
1. The `<label>` open and closing tags, wrapped around text
2. An `<input>` tag; these have various types

Various types: text, submit, file, date, radio, range, etc

## Forms in Practice - Create a Contact Me Form
```html
<form class="" action="index.html" method="post">
    <label>Your Name:</label>
    <input type="text" name="" value=""><br>
    <label>Your Email:</label>
    <input type="email" name="" value=""><br>
    <label>Your Message:</label><br>
    <textarea name="name" rows="10" cols="30"></textarea>
    <input type="submit" name="">
</form>
```

The form attribute `action` means that, when the `submit` button is clicked, we'll be redirected back to the `index.html` page. 

We're going to change this action to `mailto:<someemailaddress>`

Then we're going to delete the empty class and add an `enctype="text/plain"` (encoding type)

Along with some edits for the names of each label/textarea
```html
<form class="" action="mailto:some_email@email.com" method="post" enctype="text/plain">
    <label>Your Name:</label>
    <input type="text" name="yourName" value=""><br>
    <label>Your Email:</label>
    <input type="email" name="yourEmail" value=""><br>
    <label>Your Message:</label><br>
    <textarea name="yourMessage" rows="10" cols="30"></textarea>
    <input type="submit" name="">
</form>
```

\*Note: some validation is built into these input types!

The above builds out an email body that assigns the names of the inputs to values submitted.

## Coding Exercise 1: HTML Challenge
This is really easy and not super worth my time. 

"Write some HTML in the index.html file below. You are aiming to create a page that looks like: 
1. Level 1 Heading
2. Horizontal Rule
3. Hyperlink to MDN docs
4. A table with two columns and two rows

```html
<h1>Here's my Level 1 Heading</h1>
<hr>
<a href="some_link.com">Link to MDN Documentation</a>
<table>
    <tbody>
        <tr>
            <td>Cell 1</td>
            <td>Cell 2</td>
        </tr>
        <tr>
            <td>Cell 3</td>
            <td>Cell 4</td>
        </tr>
    </tbody>
</table>
```

## Publish Your Website!

There are lots of hosting sites, but we don't want to pay for things (because we're learning!).

GitHub lets you do things like this for free!

1. Create repository
2. Upload your files
3. Give it a commit/version message
4. Go to Settings
5. GitHub Pages
6. Select `main` as your branch
7. This spits out a https url! Save this address.