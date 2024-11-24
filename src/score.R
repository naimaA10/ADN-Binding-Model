data<-read.delim("bs_score", sep = "")
min_score = min(data$DOPE)
data[which(data$DOPE == min_score), ]
#DOPE :energie plus basse