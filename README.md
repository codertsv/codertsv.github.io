# Townsville R coders club

We meet every Monday at 11am for an hour to discuss all things R. You can find a calendar of our upcoming events [here](https://calendar.google.com/calendar?cid=dW4wOXFwcnB0NjZoYnR0YzFkZDduaDNiMGdAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ).

Our website is [codertsv.github.io](https://codertsv.github.io)

## Add a post to the website

Clone the repo from Github. 

```
git clone https://github.com/codertsv/codertsv.github.io.git
```

Use the `createpost.py` script to make a new post.

```
python createpost.py the title of the post
```

This will create a new post in `_posts`. Edit the new post file and and content in Markdown. Add the appropriate tags and categories and commit the changes.

```bash 
git add .
git commit -m "Added new post [title]" 
```

Push the changes to github or create a new RP so they can be reviewed before going live. 

## Dev

We welcome pull requests (PR), this website is open source! If you want to change something please consider making an issue before submitting a PR. 

To develop this website clone the repo and run `bundle exec jekyll serve` to launch the dev server. You will have to install some gems first.



