# Townsville R coders club

We meet every Monday at 11am for an hour to discuss all things R. You can find a calendar of our upcoming events [here](https://calendar.google.com/calendar?cid=dW4wOXFwcnB0NjZoYnR0YzFkZDduaDNiMGdAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ).

Our website is [codertsv.github.io](https://codertsv.github.io)

## Dev

We welcome pull requests (PR), this website is open source! If you want to change something please consider making an issue before submitting a PR. 

To develop this website clone the repo and run `bundle exec jekyll serve` to launch the dev server. You will have to install some gems first.

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

```bash 
git push -u origin master
```

## Add an author 

Author information be found in the `/_data/authors.yml` data file. 

To add an author copy the following test into that file replacing the appropriate variables.

```YAML
Kevin Bairos-Novak:
  name: "Kevin Bairos-Novak"
  bio: "PhD candidate in Sean Connolly's lab"
  avatar: "https://avatars.githubusercontent.com/u/57380212?s=400&u=0b446ce13c62692eeb8f66424299e52edf95c2a3&v=4"
  links:
    - label: "GitHub"
      icon: "fab fa-fw fa-github"
      url: "https://github.com/ecolology"
    - label: "Twitter"
      icon: "fab fa-fw fa-twitter-square"
      url: "https://twitter.com/ecolology"
```

To add an author to a post add the following to the top (front matter) of the post.

```YAML
author: Kevin Bairos-Novak
```

