---
title:  "HPC Software Carpentry - Week 1 - Lesson 2 - BASH fundamentals"
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

- What is a UNIX command
- Fundamental commands in bash
- How

## Interacting with the JCU HPC

### UNIX and UNIX commands
In Lesson 1 we learnt how to access the JCU HPC via an SSH (Secure SHell) client through the *terminal* on Mac or *Command Prompt* on Windows. We will start this lesson assuming that you have just logged in into the HPC. If so, your terminal window should have the following prompt:

`[jc000000@ln1:1 ~]%`

This states your login name (the jc... part) and the host name (ln1:1). The ln part stands for the login node 1 (remember the JCU HPC has 2 login nodes, as we discussed in the first lesson of this series).

The HPC runs on UNIX, which is a particular Operating System, just like Mac and Windows. The peculiarity of UNIX is that it is **Multi-User** and **Multi-Tasking**, meaning that multiple users can have multiple tasks operating simultaneously. The main way to interact with a UNIX system is through commands. These commands usually follow the below structure:

`[jc000000@ln1:1 ~]% head -n myfile.txt`

Where:

- `[jc000000@ln1:1 ~]%` is the command prompt. In the code below I will simply refer to it as '%' for simplicity.
- `head` is the command we want to run. The UNIX shell will thus try and find a program called 'head' and execute it
- `-n 5` is an option on how to execute the 'head' program with a value, 5, provided to that option. These options are used to alter the default behaviour of the command
- `myfile.txt` is the argument taken as an input for the program. In this case a .txt file

Just like in R, these commands are **case sensitive**!! So `head` and `Head` will mean two different things. Make sure you use the right lower or upper case (this is a more common error than you would think when starting and even later on!).

### BASH language
The default 'shell' (i.e., command/scripting language) for UNIX command is bash, or the Bourne Again SHell. You do not need to understand in detail what a shell is ( I don't :S ). For now simply think of it as the language you will use to interact with the HPC. In the rest of this lesson we will go over some of the main fundamental bash commands used to navigate your folders and files, create folders and files, and conducting other routine tasks within the HPC.

## Bash fundamentals
To start familiarising ourselves with the HPC, we will start with some fundamental commands that you will use on a daily basis. 

First of all, let's start to understand where we are, and let's type the `pwd` command (which stands for print working directory). This returns `/home/jc000000/`, telling us that we are in a folder called `jc000000` (where jc000000 is our JCU id). This is our **home directory**. This is important, remember this for later.

If we want to see what's in our home directory at the moment we can type `ls`, for 'list files'. If you just created your JCU HPC account this will not return anything as you currently have no files.

Now let's gather a bit more information. If we type `hostname` we are presented with either `ln01` or `ln02`, referring to either of the two JCU HPC login nodes. Additionally, we can retrieve our username with `whoami`, which returns our jc000000 ID.

Let's now imagine that we want to start our own project. We then want to create a folder to store all project related files within. To create a folder (i.e., directory) we use the `mkdir` command.

~~~
% mkdir cool_project
~~~
{: .language-bash}

If we run the `ls` command again, this time it will show the folder we just created.

~~~
% ls 
~~~
{: .language-bash}
~~~
cool_project
~~~
{: .output}


The `ls` command can take a number of additional options to modify its default behaviour and thus the output. For instance, I often add the `-lh` options, which stand for long (l) and human readable (h). This time the output will contain more information like permissions in the first column, the file size, the month date and time it was created and more.

~~~
% ls -lh
~~~
{: .language-bash}
~~~
drwxrwxr-x  2 jc274669 jc274669   10 Mar 24 14:40 cool_project
~~~
{: .output}


### Getting help on a command: man and --help
If you are ever curious of what additional options might exist, or how to use a command, there are two ways to go about it. The first is using the command `man`, for manual, which will open the full manual for the command of interest.

~~~
% man ls
~~~
{: .language-bash}


![Fig. 1: Result of running man command for the ls command](assets/images/HPC_ManLS.png)

Alternatively, you can use the `--help` option for a command to get a quick guide on how to use it.

~~~
% ls --help
~~~
{: .language-bash}


![Fig. 2: Result of running ls with the --help option](assets/images/HPC_LsHelp.png)

### Moving between directories
There is one final command that you will need to move between different folders/directories, which is the `cd` command, for 'change directory'. So let's change our directory to our project folder.

~~~
% cd cool_project
~~~
{: .language-bash}

And then make some folder within to organise our different files. For instance we might have a folder for our scripts, one for our raw data and one for figures we produce.

~~~
% mkdir scripts
% mkdir raw_data
% mkdir figures
~~~
{: .language-bash}

We can check that they were creating by listing files in our current directory

~~~
% ls -lh
~~~
{: .language-bash}
~~~
figures raw_data scripts
~~~
{: .output}

And we can check we created these folders in the right directory by checking where we are with `pwd`

~~~
% pwd
~~~
{: .language-bash}
~~~
/home/jc000000/cool_project
~~~
{: .output}

Finally, we might be done working on this project for now, and we decide to move back to our home directory to work on something else. 

We can achieve this in two ways:

By changing directory to our 'parent' (i.e., the folder above, or containing our current directory) using the special symbol `..`.

~~~
% cd ..
~~~
{: .language-bash}

Or by using a special symbol that refers to our home directory regardless of where we are: `~`. This is very useful whenever we want to use absolute paths, as in paths that are the same regardless of where we are running the command from. The usefulness of this will become more apparent once we start writing scripts more.

~~~
% cd ~
~~~
{: .language-bash}

We can check that we are back to our home directory with the `pwd` command. 

~~~
% pwd
~~~
{: .language-bash}
~~~
/home/jc000000
~~~
{: .output}

#### Get files to/from HPC to/from laptop

- FileZilla
- ssh ?

#### Working with files

- cat to read non interactively, or to concatenate
- cp to copy, rename
- mv to move files
- rm, with 2000 warnings about rm and asterisks

- nano to create and edit (easiest option)
- emacs-nw (a lot of configuration options, lots of shortcuts)
- vi and vim (basic and difficult to use)
- VSCode from your local machine (see Wytamma's [post](https://blog.wytamma.com/blog/hcp-vscode/))

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
