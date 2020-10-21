#  http://www.sthda.com/english/wiki/ggplot2-quick-correlation-matrix-heatmap-r-software-and-data-visualization
#  axis  http://www.sthda.com/english/wiki/ggplot2-title-main-axis-and-legend-titles

A1 <- c(100)
B1 <- c(90)
C1 <- c(40)
D1 <- c(0)

A2 <- c(90)
B2 <- c(60)
C2 <- c(30)
D2 <- c(0)

A3 <- c(60)
B3 <- c(50)
C3 <- c(30)
D3 <- c(0)

A4 <- c(10)
B4 <- c(20)
C4 <- c(30)
D4 <- c(0)

DF <- data.frame(
  hot_judgement = c(c(A1, B1,C1,D1), c(A2, B2,C2,D2), c(A3, B3,C3,D3), c(A4, B4,C4,D4)),
  #var_hot = rep(c("A", "B", "C", "D"), each = 4),
  var_hot = rep(c("43", "40", "37", "32"), each = 4),
  #var_cold = c(1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4),
  var_cold = c("15","18","21","32","15","18","21","32","15","18","21","32","15","18","21","32"),
  stringsAsFactors = FALSE
)

# save
write.csv(DF, file = "C:\\Users\\huaju\\Documents\\GitHub\\personal\\thermal_illusion\\psychometric\\data_exp3.csv")

library(ggplot2)
library(scales)
#library(grid)
#library(reshape2)

p <- ggplot(data = DF, aes(x=var_hot, y=var_cold, fill=hot_judgement)) + 
  geom_tile()  +
  xlab("Hot Stimulus") + ylab("Cold Stimulus") +
  scale_fill_gradient2(low="#99CCFF", mid="#FFCCCC", high="#FF3333", 
                       midpoint=50)

plot(p)

q <- p + theme_light() + theme_minimal() + theme(
axis.title.x = element_text(color="black", size=16),
axis.title.y = element_text(color="black", size=16),
legend.key.height = unit(1,"inch")
) +
labs( fill = "")

plot(q)




  