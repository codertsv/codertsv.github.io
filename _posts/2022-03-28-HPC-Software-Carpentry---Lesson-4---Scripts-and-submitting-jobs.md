---
title:  "HPC Software Carpentry - Lesson 4 - Scripts and submitting jobs"
date:   2022-03-28 15:22:47 +1000
author: Lorenzo Bertola
excerpt_separator: <!--more-->
categories:
# - Meeting
 - Presentation
 - Tutorial
# - Q&A
# - Blog
tags:
 - R
# - Python
# - Statistics
 - HPC
# - Shiny
 - Bash
 - Lorenzo
header:
# image: assets/images/...
---

## Learning Objectives

In this lesson you will learn:

- How to run R on the HPC in 3 different ways (i.e., interactively, via scripts and by submitting jobs)
- How to write an R script with `nano`
- How to write a PBS script and submit a job to the HPC

## Running R on the HPC

I this lesson I use R as most new students that asked me how to use the HPC usually have some knowledge of R and are often already using it for their analyses. So I use this as a hopefully universal example. With time I will expand on this to add a python example and other things.

### R in interactive mode

First of all we will simply start R within the HPC. This will 'switch our language from bash to R'. Think of this as if you opened R Studio and are now writing your code in R. You can enter one line of code at a time and run it. Notice how your command prompt has changed from `[jc000000@ln01:2 ~]%` to simply `>`. 

For this first example we will use one of the many built in datasets. In particular, the USA arrests datasets containing data on crimes and similar.

First, we load the dataset

~~~
data("USArrests")
~~~
{: .language-r}

Now, to plot it let's use `ggplot` cause that's the way to go these days. To use ggplot we will need to load it first. There is no need to install it as it has already been installed as part of the R singularity and been made available to HPC users. A lot of commmonly used packages are already available and should get you started. If you need additional packages the appropriate way is to contact the HPC team and request for the package to be added. The way to do this is through a ServiceNow request. Ggplot is available though so we can simply load it.

~~~
library(ggplot2)
~~~
{: .language-r}

And now let's produce a plot comparing urban population and murders. This is not very informative nor intersting. I will update this with something more relevant at a later stage.

~~~
p1 <- ggplot(USArrests) + geom_point(aes(x=UrbanPop,y=Murder)) + theme_classic()
~~~
{: .language-r}

Finally, let's save this plot as a jpg file

~~~
ggsave(filename="murderVspop.jpg", p1, device = "jpg")
~~~
{: .language-r}

And finally to visualise it transfer it to our computer with an `scp` command. If you need a refresher on how to use those see Lesson 3 of this series on our website.

~~~
scp -P8822 jc274669@zodiac.hpc.jcu.edu.au:~/murderVspop.jpg ~/Desktop
~~~
{: .language-bash}

## R script
This is all fine and dandy. But it can get hard to keep track of your code, making it harder to reproduce it. Say for instance that you receive an update dataset and you want to re-analyse it in the same way. You would have to type all of these commands again one by one. An alternative is to have an R script already with all the steps involved, and you can run the whole script at once.

To do this, we will first exit R with `quit()`. Then, we create an empty text file with `nano`. Note how we put `.R` at the end as an extension.

~~~
nano myRscript.R
~~~
{: .language-bash}

~~~
### load dataset
data("USArrest")

### load packages
library(ggplot2)

### produce plot
p1 <- ggplot(USArrests) + geom_point(aes(x=UrbanPop,y=Murder)) + theme_classic$

### save plot
ggsave(filename="~/murderVspop.jpg", p1, device = "jpg")
~~~
{: .language-bash}

Then exit and save your file. Now, instead of running each line of code one by one, we can run the whole script at once with the below command.

~~~
singularity run $SING/R-4.1.2.sif R -f myRscript.R
~~~
{: .language-bash}

This is much better, we didn't need to type the lines of code that we already used before one by one, and could chat while waiting for the script to finish running. Note how this is a pretty fast running and simple code. These scripts will come even more handy when you are trying to run long functions.

But, what if while your R script is running you want to do other things on the HPC? or what if your internet connection dies and kicks you out of the HPC? Your script would stop running as well.



## PBS Script and submitting your job
