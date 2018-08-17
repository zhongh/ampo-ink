setwd("~/Projects/ampo-ink/analysis")
library("lattice")

df <- read.csv("~/Projects/ampo-ink/queries/query_results_question_8.csv", stringsAsFactors=FALSE)
View(df)

df$Droplet_Tail <- as.logical(trimws(df$Droplet_Tail))
df$Droplet_Satellites <- as.logical(trimws(df$Droplet_Satellites))
typeof(df$Droplet_Tail)
cloud(Droplet_Velocity ~ Max_Voltage_Amplitude * Dwell_Time | Ink, groups = (df$Droplet_Tail | df$Droplet_Satellites), data=df)
help(cloud)
