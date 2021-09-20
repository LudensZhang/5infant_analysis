library(ggplot2)
library(ggpubr)
plot.data = read.csv('plot-data.csv')

p1 = ggplot(plot.data, aes(x=Env, y=ROC.AUC, fill=mode))+
  geom_boxplot()+
  xlim(c('NB:C', 'NB:V', '4M:C', '4M:V', 
         '12M:C', '12M:V', '3Y:C', '3Y:V', '5Y:C', '5Y:V','M'))+
  theme_bw()+
  xlab('')
p1
