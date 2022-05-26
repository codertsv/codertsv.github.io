## LINEAR MIXED EFFECT MODELS

**Disclaimer**: I wrote down these notes while trying to keep up with the conversation being had. They might not be 100% accurate. So please use them as a general guide to remember what we discussed, and figure out where to look for further, detailed, and accurate information of the topic of interest to you.
_Cheers, Lorenzo._

#### RANDOM OR FIXED EFFECT

Using the dragon example from this tutorial https://ourcodingclub.github.io/tutorials/mixed-models/, we started a discussion on the differences between random and mixed effects. See notes from previous meeting for more phylosophical interpretations/points of view. They can be found [here](https://codertsv.github.io/LMMs).

In general, putting your variable as a random instead of fixed effect has the advantage of 'saving' you degrees of freedom, by reducing the number of parameters that have to be estimated.

In our case, this is making an assumption about the distribution of the estimated values across the mountain ranges, as each has its own mean and variance being estimated (" _each mountain range is its own unique snowflake_ ". Cooke, 2020). At this point you should ask yourself, is this actually the case?

#### MIXED EFFECT MODELLING - by Sonja 

Sonja presented her work on measuring fetal renal parenchymal thickness (RPT) during pregnancy (thus longitudinal data).

She measured fetal RPT at 20,24,28,32,36 weeks. Not always able to keep to schedule (e.g., patient misses a scan, birth at < 36 weeks)

_Response variable_: renal parenchymal thickness (RPT)
_Fixed effects_:
- Gestational age
- GDM, no or yes
- Kidney side - Rt of Lt
- Kidney part - Ant or Post
- Sex - M or F

_Package_: 'nlme'

Showed how looking at (fitted) residuals, and applying a stepwise approach to adding interactions and random/mixed effects can guide your choice of what variables to include in the final model. 

Contact Sonja directly for example code or further discussion on this. (**Disclaimer #2** sorry for not summarising this more thoroughly, I was trying to follow her presentation and not being too familiar with this area I had to focus.)

#### MODEL SELECTION

At this point we started a brief discussion on whether all members use a similar step-wise approach for model selection

**Eric N**: agrees on model selection in a stepwise approach, either by hand or using packages that automate the selection of effects and interactions

**Ira C**: highlighted the issue with automated approach. If possible, it is good to keep an exploratory approach, trying to minimise the size of the model and knowing your data (e.g., residuals).

The two (automated and manual) could be used conjunctly to assess whether the same 'best' model is obtained. The same could be down with a bottom-up vs top-down approach (i.e., start once from the simplest model, and once from the most complex model, and compare the obtained best models. If you obtain the same best model, this should give you a hint your result is robust)

#### PACKAGE 'SELECTION'

Bethan asked how to choose ideal package (nlme, lme4, etc).

**Sonja**: it is a matter of output differences and workflow. Outputs between the packages differ and your choice depends on the workflow you are following, what output you can understand and process more easily, etc.

**Kevin**: lme4 and lmerTest work together (the latter provides p-value output for lme4 models, I think?), but lme4 and nlme are just two different packages for doing the same things (but random effects are specified differently), and also have slightly different outputs and capabilities for more complex models

**Lorenzo**
Here two links I looked at to better understand differences. Feel free to add more. For newer git and github users like me this can be a good way to learn about pull request, branching, etc.

Link for further reading: https://rpubs.com/DKCH2020/578881

Conversation on stack exchange (although a bit old, might not be considering updates):
https://stats.stackexchange.com/questions/5344/how-to-choose-nlme-or-lme4-r-library-for-mixed-effects-models

