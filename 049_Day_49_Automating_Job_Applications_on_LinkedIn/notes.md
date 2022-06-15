# Day 49: Automating Job Applications on LinkedIn
Automated Job Applications with Selenium. 

LinkedIn has a section called "Jobs". Click on the EasyApply button and apply!

The resume comes from your settings. You can preupload your resume (so you don't have to do this using your bot). There are only four or five steps to automate to apply for a job.

## Step 1: Setup Your LinkedIn Account
Use LinkedIn's "Easy Apply" function to send applications to all the jobs that meet your criteria (instead of just a single listing).

If you have reservations about sending job applications to the job listings on LinkedIn, alternatively you may "Save" all t he jobs that meet your criteria and follow the company that posted the job instead.


## Step 2: Automatically Login

`https://www.linkedin.com/jobs/search/?currentJobId=3075033946&f_AL=true&f_E=3&f_JT=F&f_WT=2&keywords=python%20developer`

```py
# go to sign in page
time.sleep(1)
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

# fill credentials and sign in
time.sleep(1)
username = driver.find_element(By.NAME, "session_key")
username.send_keys(linkedin_username)
password = driver.find_element(By.NAME, "session_password")
password.send_keys(linkedin_password, Keys.ENTER)
```

## Step 3: Apply for a Job
Skipped this and went straight into the list.

## Step 4: Apply for all the jobs
This code doesn't actually apply for jobs. It instead clicks the **SAVE** and **FOLLOW** buttons.

```py
time.sleep(3)
listings = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")

for listing in listings:
    listing.click()
    time.sleep(2)
    save_button = driver.find_element(By.CSS_SELECTOR, "button.jobs-save-button")
    save_button.click()
    print(f"{save_button.text} Button Clicked!")


    # scroll to the bottom of the right rail
    right_rail = driver.find_element(By.CLASS_NAME, "jobs-search__right-rail")
    right_rail.click()
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.END)
    time.sleep(1)

    # follow button
    try:
        follow_button = driver.find_element(By.CSS_SELECTOR, 'button.follow')
        follow_button.click()
        print(f"{follow_button.text} Button Clicked!")
    except NoSuchElementException:
        continue
```