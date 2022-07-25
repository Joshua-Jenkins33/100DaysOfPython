# Day 70: Advanced - Deploying Your Web Application with Heroku
Going to be publishing our Flask website onto the internet with:
- Git
- Github
- Heroku
- gunicorn

## Version Control and Git
Already pretty familiar with this. It enables you to rollback to a previous version with Git to makeup for a mistake you made that broke the code. You can go back as far as you'd like as long as you know which version.

`git init` initializes git in the directory.

`git add <filename>`

Commit messages are really important for knowing what was done in which versions.

`git log` to see your commits and hashes.

`HEAD` is the position or current state we are in.

`git checkout <file name>` rolls back to the last committed version.
## What is GitHub?
Basics that I already know.

`origin` is the name of the remote. You can name it whatever you want `git remote add origin`, but people are used to origin and anything else will be confused.

`git push -u origin master`
- push: pushes the branch
- `-u` is the flag command that links your local to remote branches
- origin is the remote
- master is the branch (main is default or main branch of all your commits)

Insights --> Network shows the save points of your files.

**Local Repository**
- `.git` file we have in our story directory

**Remote Repository**
- GitHub

git push keeps the two in sync.

## Step 1 - Upload Your Project to GitHub
So now that you've seen the power of Git and GitHub, it's time to put our blog project under version control. We're going to see how you can do this within PyCharm.

1. You can either use the final version of your blog project, or download a fresh, completed copy here.


## Step 2 - Use gunicorn and Heroku to host your website

## Step 3 - Setup a WSGI server with gunicorn

## Step 4 - Upgrade SQLite Databse to PostgreSQL