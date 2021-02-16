---
title:  "How to plot phylogenetic trees in R"
date:   2020-05-25 15:35:13
excerpt_separator: <!--more-->
categories:
 - Meeting
# - Presentation
 - Tutorial
# - Q&A
# - Blog
tags:
 - R
 - Phylogenetics
 - Pete
# - Python
# - Statistics
# - HPC
# - Shiny
# - Bash
header:
# image: assets/images/...
---

Pete (@pete_cowman) gave an intro and demonstrated how to plot phylogenetic trees in R with the package ggtree. After intro he had fun plotting a phylogeny of butterfly fishes. To view Pete's materials on *ggtree* see [his repository here](https://github.com/PeteCowman/ggtree_demo).


```R
# Lets have fun with a tree
# load libraries
library(tidyverse)
library(ape)
library(ggtree)
library(treeio)
library(tidytree)


# read in a BEAST format tree (the one in exmaple folder)

tr <- read.beast("example_data/Chaetodontidae.tre")
tr@phylo
tr@data %>% glimpse()

# plot with ape to get a few node numbers

plot(tr@phylo, cex = 0.3)
nodelabels()

# plot with ggtree
ggtree(tr, ladderize = T, right = T)
ggtree(tr, layout = "circular")
ggtree(tr, layout = "fan")
ggtree(tr, layout = "slanted")
ggtree(tr, layout = "radial")

# since it is calibrated to time I will reverse the node ages to be time before present
p <- ggtree(tr)
p + theme_tree2()

p1 <- revts(p)
p1 + theme_tree2()
# now lets sort outt he tip labels
p1 + geom_tiplab()

# need to add space for labels
p1 + geom_tiplab(size = 2) + xlim(NA,30)

# we can also change the labels to be displayed to save some space.
tr@phylo$tip.label <- gsub("_", " ", tr@phylo$tip.label)

p1 + geom_tiplab(size = 2, fontface = "italic") + xlim(NA,30)

tibble(label = tr@phylo$tip.label) %>% mutate(newlabel = gsub("Chaetodon ", "C. ", label)) %>% arrange(label) -> d
d %>% data.frame(d)

p1 %<+% d + geom_tiplab(aes(label = newlabel), size = 2, fontface = "italic") + xlim(NA,30) -> p2


# lets label some clades

getMRCA(tr@phylo, tip = grep("Chaetodon", tr@phylo$tip.label, value = T))

p2 + geom_nodelab(aes(label = node), geom = "label")
# 112, 136, 205, 182, 165, 141
p2 + 
  geom_cladelabel(node = 112, label  = "Bannerfishes",offset = 20, offset.text = 1, color='black', barsize = 2) + 
  geom_cladelabel(node = 136, label  = "Prognathodes", offset = 20,offset.text = 1, color='grey', barsize = 2) + 
  geom_cladelabel(node = 205, label  = "Clade 1", offset = 20,offset.text = 1, color='black', barsize = 2) + 
  geom_cladelabel(node = 182, label  = "Clade 2", offset = 20,offset.text = 1, color='grey', barsize = 2) + 
  geom_cladelabel(node = 165, label  = "Clade 3", offset = 20,offset.text = 1, color='black', barsize = 2)

# view a clade
viewClade(p2, node = 112)
```


