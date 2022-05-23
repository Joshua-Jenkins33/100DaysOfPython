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

## How to Type Emojis

## HTML Tables Solution Walkthrough

## HTML Forms

## Forms in Practice - Create a Contact Me Form

## Coding Exercise 1: HTML Challenge

## Publish Your Website!