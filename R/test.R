library(readr)
library(ggplot2)

var <- 5*10
monster_jobs_clean <- read.csv("monster_jobs_clean.csv")
View(monster_jobs_clean)

qplot(data=monster_jobs_clean,x=job_id,y=salary_min,color=job_type)
