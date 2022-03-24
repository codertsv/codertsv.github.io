---
title:  "HPC-Software-Carpentry---Week-1---Lesson-2---BASH-fundamentals"
date:   2022-03-22 10:23:50 +1000
author: 
excerpt_separator: <!--more-->
categories:
# - Meeting
 - Presentation
 - Tutorial
# - Q&A
# - Blog
tags:
# - R
# - Python
# - Statistics
 - HPC
# - Shiny
 - Bash
header:
# image: assets/images/...
---

This is a work in progress. Ready by Monday 28th of March, 2022

## Learning Objectives

In this lesson you will learn:

- The
- How
- How

## Interacting with the JCU with BASH

BASH is the Bourne Again SHell. A bit about bash and why we need to learn it.

`[jc000000@ln1:1 ~]%`

#### Navigating the HPC

- cd
- mkdir
- ..
- .
- pwd
- ls

#### Get files to/from HPC to/from laptop

- FileZilla
- ssh ?

#### Working with files

- nano to create, read
- cat to read non interactively, or to concatenate
- cp to copy, rename
- mv to move files
- rm, with 2000 warnings about rm and asterisks

#### Variables

Should I introduce variables within this lecture?

## A list of useful commands (feel free to add onto it through our github)

### File commands
- `ls`
- `ls -lh`
- `cd`
- `pwd`
- `mkdir`
- `rm`
- `cp`
- `mv`
- `touch`: create or update file
- `nano`: create or update file
- `cat file`: print all contents of file
- `head -n file`: output the first n lines
- `tail -n file`: output the last n lines
- `chmod u+rw,g-rwx,o-rwx file` set read (r), write (w) and execute permissions for file
- `find pattern`: find files matching the pattern

### paths special characters
- `.` stands for current directory
- `..` stands for parent directory. So if I am in the folder `username/working folder` and type `cd ..` it will change the current working directory to `username`.
- `~` stands for home directory. On the JCU HPC this refers to your jc00000 directory. This character is useful for specifying absolute paths in your scripts.

### Environmental variables and aliases
- `export VAR='value'` set a variable
- `echo $VAR` print a variable
- `alias ls='ls -lh'` set an alias command (e.g., now every time i type `ls` it will be interpreted as `ls -lh`)

### Searching
- `grep pattern file`

### Other useful tools
- `man command` show the manual for command
- `command --help` get quick help on command

### Compression
- `gzip file` compress file
- `gunzip file` uncompress file

### Server info
- `whoami`
- `hostname`
