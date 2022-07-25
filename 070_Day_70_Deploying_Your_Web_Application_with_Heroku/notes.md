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

[Here's my project!](https://github.com/Joshua-Jenkins33/blog_site)

So now that you've seen the power of Git and GitHub, it's time to put our blog project under version control. We're going to see how you can do this within PyCharm.

1. You can either use the final version of your blog project, or download a fresh, completed copy here.

- [x] Using yesterday's project

2. Open the project in Pycharm and run it to make sure that everything is working as expected. If you downloaded my version from above, then make sure you install all the required packages.

[Her version](https://repl.it/@appbrewery/blog-with-users-end.zip) doesn't exist. 404 error. 

~~Admin account email: angela@email.com~~

~~Admin account password: 123456~~

### Local Version Control with PyCharm
3. Let's put our project under version control. We can do this in PyCharm by simply going to VCS -> Enable Version Control Integration.

This is the same as what we did before with

`git init`

Make sure that you select Git when asked which version control system to use:

If successful, you should now have a new Git Pane where you can see the Git Console and Git Logs.

All the files in our project will turn red because they are not yet added to the staging area to be tracked by git.

4. Add all the files in the project to the staging area by selecting the parent folder and going to VSC -> Git -> Add

All the files should now turn green.

5. Make your initial commit by going to VCS ->  Commit
Type the commit message in the commit pane:

If you see a popup about TODOs, just simply click on Commit.

If successful, you should now be able to see your first commit in the Git Log pane:

### Push to Git Remote on GitHub
6. Sign up for a GitHub account if you haven't already and have your login details handy.

Before we upload our code to GitHub, we should be careful that we are not uploading any secret information. e.g. personal emails or API keys.

It's quite painful to review all the code for these things, so by convention, developers tend to put the top-secret information in an environment .env file.

NOTE: Make sure that you don't have any sensitive information in your project, if you do, create a .env file and store them there. We covered environment variables on Day 35.

Then we can add a .gitignore file to tell our version control system to ignore those files when pushing to a remote.

7. Go to [gitignore.io](https://gitignore.io/) and search for a Flask gitignore template. Copy all the text in the resulting page and create a new file at the top level of your project with the name `.gitignore` notice the dot at the beginning of the name, this is important, it makes it a hidden file. Paste everything from the gitignore page to this file. See the walkthrough below if you're unsure:

8. Add your GitHub details to PyCharm by going to the Version Control settings.

Windows: File -> Settings -> Version Control -> GitHub

Mac: PyCharm -> Preferences -> Version Control -> GitHub

Then click on the "+" button and select Login via GitHub:

Note: in Windows the "+" button is on the top right.

It should now take you to log in to GitHub, if successful, you should see your account added:

9. Next, create a new GitHub repo by going to VCS -> Import into Version Control -> Share Project on GitHub

In the pop-up, fill in the details for your new Github repository, e.g.

Now, PyCharm will create a new remote repository on GitHub in your account and push all the local commits to the remote.

If successful, you should see a popup with a link to your new repository. But you can also go to your GitHub account and find the new repository:

That's it, you've now added version control to your project and pushed it to GitHub. 

## Step 2 - Use gunicorn and Heroku to host your website

## Step 3 - Setup a WSGI server with gunicorn

## Step 4 - Upgrade SQLite Databse to PostgreSQL