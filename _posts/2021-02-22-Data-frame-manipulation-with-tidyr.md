---
title:  "Data frame manipulation with tidyr"
date:   2021-02-22 15:39:12 +1000
author: Kevin Bairos-Novak
excerpt_separator: <!--more-->
categories:
 - Meeting
# - Presentation
 - Tutorial
# - Q&A
# - Blog
tags:
 - R
 - Kevin
# - Python
# - Statistics
# - HPC
# - Shiny
# - Bash
header:
# image: assets/images/...
---

Here is our introduction to data frame manipulation using tidyr, one of the many useful packages from the tidyverse!

Data manipulation is often required when we inherit data in an excessively long or wide format.

Tidyr lets us change the format of our data between long and wide formats, so it is more useable to us (e.g., better for plotting using ggplot2, more readible, etc.).

This tutorial uses two datasets [gapminder_data](/assets/data/gapminder_data.csv) and [gapminder_wide](/assets/data/gapminder_wide.csv). 


## Set-up
Load the required libraries

```r
# If not previously installed, run the following without '#':
# install.packages("tidyverse")

library(tidyverse)
```

```
## ── Attaching packages ──────────────────────────────────────────────── tidyverse 1.3.0 ──
```

```
## ✓ ggplot2 3.3.3     ✓ purrr   0.3.4
## ✓ tibble  3.0.3     ✓ dplyr   1.0.2
## ✓ tidyr   1.1.2     ✓ stringr 1.4.0
## ✓ readr   1.3.1     ✓ forcats 0.5.0
```

```
## ── Conflicts ─────────────────────────────────────────────────── tidyverse_conflicts() ──
## x dplyr::filter() masks stats::filter()
## x dplyr::lag()    masks stats::lag()
```

```r
library(here)
```

```
## here() starts at /Users/Kribin/Documents/Analytics/R
```

Set the working environment


```r
here::here()
```

```
## [1] "/Users/Kribin/Documents/Analytics/R"
```

Load the datasets (original data and wide format) and look at gap_wide data


```r
gapminder <- read.csv("gapminder_data.csv") # original data
gap_wide <- read.csv("gapminder_wide.csv") # wide format

head(gap_wide)
```

```
##   continent      country gdpPercap_1952 gdpPercap_1957 gdpPercap_1962
## 1    Africa      Algeria      2449.0082      3013.9760      2550.8169
## 2    Africa       Angola      3520.6103      3827.9405      4269.2767
## 3    Africa        Benin      1062.7522       959.6011       949.4991
## 4    Africa     Botswana       851.2411       918.2325       983.6540
## 5    Africa Burkina Faso       543.2552       617.1835       722.5120
## 6    Africa      Burundi       339.2965       379.5646       355.2032
##   gdpPercap_1967 gdpPercap_1972 gdpPercap_1977 gdpPercap_1982 gdpPercap_1987
## 1      3246.9918      4182.6638      4910.4168      5745.1602      5681.3585
## 2      5522.7764      5473.2880      3008.6474      2756.9537      2430.2083
## 3      1035.8314      1085.7969      1029.1613      1277.8976      1225.8560
## 4      1214.7093      2263.6111      3214.8578      4551.1421      6205.8839
## 5       794.8266       854.7360       743.3870       807.1986       912.0631
## 6       412.9775       464.0995       556.1033       559.6032       621.8188
##   gdpPercap_1992 gdpPercap_1997 gdpPercap_2002 gdpPercap_2007 lifeExp_1952
## 1      5023.2166      4797.2951      5288.0404      6223.3675       43.077
## 2      2627.8457      2277.1409      2773.2873      4797.2313       30.015
## 3      1191.2077      1232.9753      1372.8779      1441.2849       38.223
## 4      7954.1116      8647.1423     11003.6051     12569.8518       47.622
## 5       931.7528       946.2950      1037.6452      1217.0330       31.975
## 6       631.6999       463.1151       446.4035       430.0707       39.031
##   lifeExp_1957 lifeExp_1962 lifeExp_1967 lifeExp_1972 lifeExp_1977 lifeExp_1982
## 1       45.685       48.303       51.407       54.518       58.014       61.368
## 2       31.999       34.000       35.985       37.928       39.483       39.942
## 3       40.358       42.618       44.885       47.014       49.190       50.904
## 4       49.618       51.520       53.298       56.024       59.319       61.484
## 5       34.906       37.814       40.697       43.591       46.137       48.122
## 6       40.533       42.045       43.548       44.057       45.910       47.471
##   lifeExp_1987 lifeExp_1992 lifeExp_1997 lifeExp_2002 lifeExp_2007 pop_1952
## 1       65.799       67.744       69.152       70.994       72.301  9279525
## 2       39.906       40.647       40.963       41.003       42.731  4232095
## 3       52.337       53.919       54.777       54.406       56.728  1738315
## 4       63.622       62.745       52.556       46.634       50.728   442308
## 5       49.557       50.260       50.324       50.650       52.295  4469979
## 6       48.211       44.736       45.326       47.360       49.580  2445618
##   pop_1957 pop_1962 pop_1967 pop_1972 pop_1977 pop_1982 pop_1987 pop_1992
## 1 10270856 11000948 12760499 14760787 17152804 20033753 23254956 26298373
## 2  4561361  4826015  5247469  5894858  6162675  7016384  7874230  8735988
## 3  1925173  2151895  2427334  2761407  3168267  3641603  4243788  4981671
## 4   474639   512764   553541   619351   781472   970347  1151184  1342614
## 5  4713416  4919632  5127935  5433886  5889574  6634596  7586551  8878303
## 6  2667518  2961915  3330989  3529983  3834415  4580410  5126023  5809236
##   pop_1997 pop_2002 pop_2007
## 1 29072015 31287142 33333216
## 2  9875024 10866106 12420476
## 3  6066080  7026113  8078314
## 4  1536536  1630347  1639131
## 5 10352843 12251209 14326203
## 6  6121610  7021078  8390505
```
Look at dimensions of each dataset

```r
dim(gapminder)
```

```
## [1] 1704    6
```

```r
dim(gap_wide)
```

```
## [1] 142  38
```

Take a look at the wide format gapminder dataset. Often, we receive data in odd formats such as data with a lot of columns, that we would like to convert to a more useable format, such as a long format or long/intermediate format. 

To do so, we will first convert this dataset into an entirely long-format dataset, that is more useable.

## Pivot wide to long format

Think about which column names you want to 'pivot' into a column of column names. In this case, we will be pivotting every column starting with gdpPercap, lifeExp, and pop into a column of column names and a column of values for each. 

To do so, we start out by making a vector that selects the columns that we want (using the `starts_with()` function to make our lives easier), and then set the new column names we are creating to "obstype_year" and "obs_values" for the name and value column names.


```r
gap_wide %>%
  pivot_longer(cols = c(starts_with("gdpPercap"), 
                        starts_with("lifeExp"), 
                        starts_with("pop")),
               names_to = "obstype_year", values_to = "obs_values")
```

```
## # A tibble: 5,112 x 4
##    continent country obstype_year   obs_values
##    <chr>     <chr>   <chr>               <dbl>
##  1 Africa    Algeria gdpPercap_1952      2449.
##  2 Africa    Algeria gdpPercap_1957      3014.
##  3 Africa    Algeria gdpPercap_1962      2551.
##  4 Africa    Algeria gdpPercap_1967      3247.
##  5 Africa    Algeria gdpPercap_1972      4183.
##  6 Africa    Algeria gdpPercap_1977      4910.
##  7 Africa    Algeria gdpPercap_1982      5745.
##  8 Africa    Algeria gdpPercap_1987      5681.
##  9 Africa    Algeria gdpPercap_1992      5023.
## 10 Africa    Algeria gdpPercap_1997      4797.
## # … with 5,102 more rows
```

Another way of doing the same thing would be to select every column except for country and continent. The following returns the same long-format dataset as above:

```r
gap_wide %>%
  pivot_longer(cols = c(-continent, -country),
               names_to = "obstype_year", values_to = "obs_values")
```

```
## # A tibble: 5,112 x 4
##    continent country obstype_year   obs_values
##    <chr>     <chr>   <chr>               <dbl>
##  1 Africa    Algeria gdpPercap_1952      2449.
##  2 Africa    Algeria gdpPercap_1957      3014.
##  3 Africa    Algeria gdpPercap_1962      2551.
##  4 Africa    Algeria gdpPercap_1967      3247.
##  5 Africa    Algeria gdpPercap_1972      4183.
##  6 Africa    Algeria gdpPercap_1977      4910.
##  7 Africa    Algeria gdpPercap_1982      5745.
##  8 Africa    Algeria gdpPercap_1987      5681.
##  9 Africa    Algeria gdpPercap_1992      5023.
## 10 Africa    Algeria gdpPercap_1997      4797.
## # … with 5,102 more rows
```

Finally, we currently have a composite variable of `obstype_year`, which is the combined name of the observation type (i.e. gdpPercap, lifeExp, pop) and the year (i.e. 1952, 1957, etc.). To separate the two, we can use the `separate()` function.


```r
gap_wide %>%
  pivot_longer(cols = c(starts_with("gdpPercap"), 
                        starts_with("lifeExp"), 
                        starts_with("pop")),
               names_to = "obstype_year", values_to = "obs_values") %>%
	separate(obstype_year, into = c("obs_type", "year"), sep = "_")
```

```
## # A tibble: 5,112 x 5
##    continent country obs_type  year  obs_values
##    <chr>     <chr>   <chr>     <chr>      <dbl>
##  1 Africa    Algeria gdpPercap 1952       2449.
##  2 Africa    Algeria gdpPercap 1957       3014.
##  3 Africa    Algeria gdpPercap 1962       2551.
##  4 Africa    Algeria gdpPercap 1967       3247.
##  5 Africa    Algeria gdpPercap 1972       4183.
##  6 Africa    Algeria gdpPercap 1977       4910.
##  7 Africa    Algeria gdpPercap 1982       5745.
##  8 Africa    Algeria gdpPercap 1987       5681.
##  9 Africa    Algeria gdpPercap 1992       5023.
## 10 Africa    Algeria gdpPercap 1997       4797.
## # … with 5,102 more rows
```

The separate function takes the `obstype_year` column and separates it based on the underscore character (via the `sep = "_"` argument), and finally, we choose the resulting new column names using the `into` argument. Awesome! Now let's save a new object called gap_long using the above.


```r
gap_long <- gap_wide %>%
  pivot_longer(cols = c(starts_with("gdpPercap"), 
                        starts_with("lifeExp"), 
                        starts_with("pop")),
               names_to = "obstype_year", values_to = "obs_values") %>%
	separate(obstype_year, into = c("obs_type", "year"), sep = "_")
```

Here, we can calculate summary statistics, such as the means for life expectancy, population, and gdpPercap for each continent by using the `group_by()` and `summarise()` functions seen in the previous lesson on package `dplyr`.


```r
gap_long %>%
  group_by(continent, obs_type) %>%
  summarise(means = mean(obs_values))
```

```
## `summarise()` regrouping output by 'continent' (override with `.groups` argument)
```

```
## # A tibble: 15 x 3
## # Groups:   continent [5]
##    continent obs_type       means
##    <chr>     <chr>          <dbl>
##  1 Africa    gdpPercap     2194. 
##  2 Africa    lifeExp         48.9
##  3 Africa    pop        9916003. 
##  4 Americas  gdpPercap     7136. 
##  5 Americas  lifeExp         64.7
##  6 Americas  pop       24504795. 
##  7 Asia      gdpPercap     7902. 
##  8 Asia      lifeExp         60.1
##  9 Asia      pop       77038722. 
## 10 Europe    gdpPercap    14469. 
## 11 Europe    lifeExp         71.9
## 12 Europe    pop       17169765. 
## 13 Oceania   gdpPercap    18622. 
## 14 Oceania   lifeExp         74.3
## 15 Oceania   pop        8874672.
```

This output looks a bit odd, because the data are in a very long format. Ideally, we would have gdpPercap, lifeExp, and pop be separate columns and values. To get to this intermediate format data, we can `pivot_wider()` by obs_type!

## Pivot long to intermediate format

To get to a wider format, we need two things at minimum: a column of column names that will become the new headers on the new columns we create (`names_from` argument), and a column of the associated values (`values_from` argument). 


We will get the new column names from the obs_type column, and the values to fil in from the obs_values column. That's all we need to `pivot_wider()`, tidyr does the rest!

We will save this new data frame as `gap_intermediate`.


```r
gap_intermediate <- gap_long %>%
  pivot_wider(names_from = obs_type, values_from = obs_values)
```

Comparing this to the original dataset, we see it is now exactly the same size

```r
dim(gap_intermediate)
```

```
## [1] 1704    6
```

```r
dim(gapminder) # original gapminder data
```

```
## [1] 1704    6
```

And the same column names

```r
names(gap_intermediate) %in% names(gapminder)
```

```
## [1] TRUE TRUE TRUE TRUE TRUE TRUE
```

## Reordering columns

Currently, the columns are in a different order...


```r
names(gap_intermediate)
```

```
## [1] "continent" "country"   "year"      "gdpPercap" "lifeExp"   "pop"
```

```r
names(gapminder)
```

```
## [1] "country"   "year"      "pop"       "continent" "lifeExp"   "gdpPercap"
```

```r
# all.equal(gap_intermediate, gapminder) # another way of comparing, not run
```

We need to change the column order using `relocate()` (but can also use `select()` insead)


```r
gap_intermediate2 <- gap_intermediate %>%
  relocate(names(gapminder))
names(gap_intermediate2)
```

```
## [1] "country"   "year"      "pop"       "continent" "lifeExp"   "gdpPercap"
```

This creates the same order of column names as the original gapminder dataset. 

# Reordering rows

Another difference is that the original dataset has the rows sorted by country, rather than continent first!


```r
head(gap_intermediate2, 3) 
```

```
## # A tibble: 3 x 6
##   country year       pop continent lifeExp gdpPercap
##   <chr>   <chr>    <dbl> <chr>       <dbl>     <dbl>
## 1 Algeria 1952   9279525 Africa       43.1     2449.
## 2 Algeria 1957  10270856 Africa       45.7     3014.
## 3 Algeria 1962  11000948 Africa       48.3     2551.
```

```r
head(gapminder, 3)
```

```
##       country year      pop continent lifeExp gdpPercap
## 1 Afghanistan 1952  8425333      Asia  28.801  779.4453
## 2 Afghanistan 1957  9240934      Asia  30.332  820.8530
## 3 Afghanistan 1962 10267083      Asia  31.997  853.1007
```
We can fix this using the `arrange()` function to arrange by country, then by continent.


```r
gap_intermediate3 <- gap_intermediate2 %>%
	arrange(country, continent)

head(gap_intermediate3, 3) 
```

```
## # A tibble: 3 x 6
##   country     year       pop continent lifeExp gdpPercap
##   <chr>       <chr>    <dbl> <chr>       <dbl>     <dbl>
## 1 Afghanistan 1952   8425333 Asia         28.8      779.
## 2 Afghanistan 1957   9240934 Asia         30.3      821.
## 3 Afghanistan 1962  10267083 Asia         32.0      853.
```

```r
head(gapminder, 3)
```

```
##       country year      pop continent lifeExp gdpPercap
## 1 Afghanistan 1952  8425333      Asia  28.801  779.4453
## 2 Afghanistan 1957  9240934      Asia  30.332  820.8530
## 3 Afghanistan 1962 10267083      Asia  31.997  853.1007
```

# Changing column class

Finally, if we try comparing our two datasets now using the `all.equal()` function:

```r
all.equal(gap_intermediate3, gapminder)
```

```
## [1] "Attributes: < Component \"class\": Lengths (3, 1) differ (string compare on first 1) >"
## [2] "Attributes: < Component \"class\": 1 string mismatch >"                                
## [3] "Component \"year\": Modes: character, numeric"                                         
## [4] "Component \"year\": target is character, current is numeric"
```
We see that there is one last difference. The year in our dataset is a numeric, rather than an integer. This can be easily changed using the `mutate()` function seen previously. Additionally, the original gapminder dataset is not a tibble, so we will revert back to a data frame only using the `as.data.frame()` function.


```r
gap_intermediate4 <- gap_intermediate3 %>%
	mutate(year = as.integer(year)) %>%
	as.data.frame()

all.equal(gap_intermediate4, gapminder)
```

```
## [1] TRUE
```

Now, (finally!) the data are exactly the same as the original!

## Combining all steps together to reduce code

Finally, once we have each step working coherently, we can reduce our code into a single, long pipe that we can run. This will get the data to the exact format we want it to be, that can then be saved for later as a processed dataset, keeping our original, raw, and unprocessed dataset unchanged but easily workable!

First, we gather all code where we re-saved the data frame as a new object:

```r
gap_long <- gap_wide %>%
  pivot_longer(cols = c(starts_with("gdpPercap"), 
                        starts_with("lifeExp"), 
                        starts_with("pop")),
               names_to = "obstype_year", values_to = "obs_values") %>%
	separate(obstype_year, into = c("obs_type", "year"), sep = "_")

gap_intermediate <- gap_long %>%
  pivot_wider(names_from = obs_type, values_from = obs_values)

gap_intermediate2 <- gap_intermediate %>%
  relocate(names(gapminder))

gap_intermediate3 <- gap_intermediate2 %>%
	arrange(country, continent)

gap_intermediate4 <- gap_intermediate3 %>%
	mutate(year = as.integer(year)) %>%
	as.data.frame()
```

Ensure that this all runs smoothly, from start to finish before proceeding. If it does, we can now combine all steps into a single pipeline, to efficiently manipulate our data frame to match the original. Let's name this new data frame `gap_final`.


```r
gap_final <- gap_wide %>%
  pivot_longer(cols = c(starts_with("gdpPercap"), 
                        starts_with("lifeExp"), 
                        starts_with("pop")),
               names_to = "obstype_year", values_to = "obs_values") %>%
	separate(obstype_year, into = c("obs_type", "year"), sep = "_") %>%
  pivot_wider(names_from = obs_type, values_from = obs_values) %>%
  relocate(names(gapminder)) %>%
	arrange(country, continent) %>%
	mutate(year = as.integer(year)) %>%
	as.data.frame()
all.equal(gap_final, gapminder)
```

```
## [1] TRUE
```

And now, we have a concise bit of code that gets the raw data to the perfect format to work with. 

Try it yourself on your own wide or long data, by getting it first to a long format, then moving it towards an intermediate format! Just have a good think about which column names you want where, and you should be able to adapt this code for yourself!




