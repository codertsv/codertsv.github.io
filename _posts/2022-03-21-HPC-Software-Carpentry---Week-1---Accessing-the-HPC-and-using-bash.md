---
title:  "HPC Software Carpentry - Week 1 - Accessing the HPC and using bash"
date:   2022-03-21 15:44:26 +1000
author: Lorenzo Bertola 
excerpt_separator: <!--more-->
categories:
# - Meeting
 - Presentation
 - Tutorial
 - HPC Software Carpentry
# - Q&A
# - Blog
tags:
# - R
# - Python
# - Statistics
 - HPC
# - Shiny
 - Bash
 - Lorenzo
header:
# image: assets/images/...
---

## Introducing the JCU HPRC

Hello everyone!

This is the start of our new Software Carpentry series on how to use the JCU HPRC for your research endeavours. But, before we start, let's first understand what the HPRC is, and how it is structured.

HPRC stands for High Performance Research Computing. Leaving aside the '*computing*' part of it, we are left with two keys parts: High Performance and Research. The research term is self explanatory, and it tells us that the JCU HPRC is a resource made available by the University mostly for research purposes. The High Performance term refers to the HPRC being a computer (and technically a set of 'computers') with capability for resource demanding jobs, thus why it's defined as 'High Performance'. To understand what we mean by High Performance and resource demanding, let's first have a more in-depth look at what the JCU HPC is. *P.S. from now on I'll be referring to it simply as 'the HPC' for simplicity*.

### The HPC Structure

The HPC consists of **2** login nodes (nl01, nl02), a server, a scheduler, **6** computing nodes and one GPU node. The schematic below shows how these interact with each other. 

![Fig. 1: Schematic of HPC Structure](https://github.com/codertsv/codertsv.github.io/blob/9e9e7cb31d42f138f7612aab21a0e037a45455f2/assets/images/HPCStructure.png)

We start with your personal laptop or computer on the far left. Using the `ssh` command from your terminal (more on this in a second) you can access one of the **login nodes**. Each one of these nodes can be thought of as a separate computer. In addition, these nodes have multiple *cores*, we can think of as the brains of the computer. The more brains, the more tasks the computer can run simultaneously. Additionally, these nodes have a lot of RAM, or Random Access Memory. Basically RAM is important as it "gives applications a place to store and access data on a short-term basis. It stores the information your computer is actively using so that it can be accessed quickly." (more on RAM [here](https://www.crucial.com/articles/about-memory/support-what-does-computer-memory-do)). Because of the many available brains (i.e., cores) and the high computing memory (i.e., RAM) the HPC nodes are available to conduct Computing tasks much faster and more efficiently than your average laptop. To put things in comparison, most laptops these days have ~8 CPUs and 8GB of RAM, while each of these nodes has 40 CPUs and 383GiB (411 GB) of RAM.

But, the login nodes are not where you should conduct your large long jobs. These are mostly for, as the name suggests, logging in to the HPC, testing your script on a portion of the data, before submitting the actual job to the compute nodes. This is achieved with the `qsub` command, which sends your job request to a server (then to a scheduler), and finally to the compute nodes. We will cover in the detail how to submit jobs next week, so for now accept this simplified explanation.

## How to access the JCU HPC
Access the HPC (on and off campus)

## Interacting with the JCU with BASH

BASH is the Bourne Again SHell. A bit about bash and why we need to learn it.

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



