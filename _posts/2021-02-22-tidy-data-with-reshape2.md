---
title:  "tidyr vs reshape2"
date:   2021-02-22 12:49:33
excerpt_separator: <!--more-->
categories:
# - Meeting
# - Presentation
 - Tutorial
# - Q&A
 - Blog
tags:
 - R
 - César
# - Python
# - Statistics
# - HPC
# - Shiny
# - Bash
header:
# image: assets/images/...
---

An alternative worklfow to Data frame Manipulation with tidyr
Created by [César Herrera](https://github.com/CexyNature/)

tidyr use can be consulted at: https://swcarpentry.github.io/r-novice-gapminder/14-tidyr/index.html

Here, I present an alternative way to manipulate data frames, transform to wide to long and vice versa, using the package reshape2

## reshape2

Load libraries
```R
library(here)
library(reshape2)
```

Working environment
```R
here::here()
```

Load data
```R
gdata <- read.csv("gapminder_data.csv")
gdata_wide <- read.csv("gapminder_wide.csv")
```

Convert wide data to long data
```R
gdata_long_r2 <- melt(gdata_wide, 
                      variable.name = "variable_year",
                      value.names = "value",
                      id.vars = c("continent", "country"))
```

One column combines the information of variable type and year. We will split these into two columns
```R
columns_long <- colsplit(gdata_long_r2$variable, "_", c("variable", "year"))
```

Adding our new columns (variable, year) to the long format data
```R
gdata_long_r2 <- cbind(gdata_long_r2[,-3], columns_long)
```

Create summaries with reshape2
```R
tidy_summary_r2 <- dcast(gdata_long_r2, continent+country~variable, value.var='value',
                         fun.aggregate = mean, 
                         na.rm = TRUE)
```

## Another alternative: creating summaries with base R and reshape2 pivot

Create summaries using base R
```R
gdata_long_r2_summary <- by(gdata_long_r2, 
                            INDICES = list(gdata_long_r2$continent, 
                                           gdata_long_r2$country,
                                           gdata_long_r2$variable),
                            FUN = function(x){
                              data.frame(continent = unique(x$continent),
                                         country = unique(x$country),
                                         variable = unique(x$variable),
                                         mean = mean(x$value))
                            })
```

Then combine the results into a data frame
```R
gdata_long_r2_summary <- do.call(rbind, gdata_long_r2_summary)
```

Pivot from the long format to thw wide format
```R
tidy_summary <- dcast(gdata_long_r2_summary, continent+country~variable, value.var='mean')
```


