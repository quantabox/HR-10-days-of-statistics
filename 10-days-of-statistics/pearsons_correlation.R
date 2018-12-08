# R 


f<-file('stdin')
open(f)
feed <- read.table(f,header=FALSE, skip=1)
close(f)
feed <- t(feed)
correlation<-cor.test(feed[,1], feed[,2], method="spearman")
cat(round(correlation$estimate, digits=3),"\n")
