#   https://stackoverflow.com/questions/47479522/how-to-create-a-grouped-boxplot-in-r
# two way anova  http://www.sthda.com/english/wiki/two-way-anova-test-in-r
# color  http://www.sthda.com/english/wiki/colors-in-r



A1 <- c(100,40,100,100,80,100,50)
A2 <- c(100,100,100,100,90,100,100)

B1 <- c(0,10,100,0,50,60,20)
B2 <- c(60,100,100,100,90,100,100)

C1 <- c(50,20,90,30,70,100,0)
C2 <- c(100,100,100,100,100,100,100)

D1 <- c(0,0,0,0,0,0,0)
D2 <- c(80,100,100,100,100,100,90)

E1 <- c(50,100,20,100,90,100,100)
E2 <- c(30,50,0,0,40,0,0)



DF2 <- data.frame(
  x = c(c(A1, A2), c(B1, B2),c(C1, C2), c(D1, D2),c(E1, E2)),
  #y = rep(c("PIP->DIP", "DIP->PIP", "PIP=DIP", "0->DIP", "PIP->0"), each = 14),
  y = rep(c("A", "B", "C", "D", "E"), each = 14),
  z = rep(rep(1:2, each=7), 5),
  stringsAsFactors = FALSE
)
str(DF2)
#'data.frame':   70 obs. of  3 variables:
# $ x: num  100 40 100 100 80 100 50 100 100 100 ...
# $ y: chr  "PIP->DIP" "PIP->DIP" "PIP->DIP" "PIP->DIP" ...
# $ z: int  1 1 1 1 1 1 1 2 2 2 ...

# save
write.csv(DF2, file = "C:\\Users\\huaju\\Documents\\GitHub\\personal\\thermal_illusion\\psychometric\\data_exp1.csv")


cols <- c("#FFCCFF","#99CCFF")


boxplot(x ~  z + y, data = DF2,
        at = c(1:2, 4:5, 7:8, 10:11, 13:14), col = cols,
        names = c("PIP->DIP", "", "DIP->PIP", "","PIP=DIP", "","0->DIP", "","PIP->0", ""), xaxs = FALSE, 
        xlab = "Touch Pattern", ylab = "% Hot Judgement",
        boxlwd = 1,cex.lab=1.8,cex.main=1.5, cex.sub=1.5)


# 枠外への描画を許可
par(xpd=T)
# 凡例を表示
legend(5,120, fill = cols, legend = c("DIP=C, PIP=H","DIP=H, PIP=C"), horiz = F)


# conduct two-way ANOVA with interaction effect
res.aov3 <- aov(x ~ y * z, data = DF2)
res.aov3 <- aov(x ~ y + z + y:z, data = DF2)
summary(res.aov3)
#            Df Sum Sq Mean Sq F value   Pr(>F)    
#y            4  18277    4569   8.652 1.40e-05 ***
#z            1  17286   17286  32.732 3.57e-07 ***
#y:z          4  49900   12475  23.623 9.21e-12 ***
#Residuals   60  31686     528
#---
#Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1


# conduct Multiple pairwise-comparison between the means of groups
TukeyHSD(res.aov3, which = "y")
#  Tukey multiple comparisons of means
#    95% family-wise confidence level
#
#Fit: aov(formula = x ~ y + z + y:z, data = DF2)
#
#$y
#           diff       lwr        upr     p adj
#B-A -26.4285714 -50.85688  -2.000265 0.0276304
#C-A -14.2857143 -38.71402  10.142593 0.4754471
#D-A -42.1428571 -66.57116 -17.714550 0.0000865
#E-A -41.4285714 -65.85688 -17.000265 0.0001160
#C-B  12.1428571 -12.28545  36.571164 0.6313063
#D-B -15.7142857 -40.14259   8.714021 0.3779628
#E-B -15.0000000 -39.42831   9.428307 0.4255991
#D-C -27.8571429 -52.28545  -3.428836 0.0176535
#E-C -27.1428571 -51.57116  -2.714550 0.0221393
#E-D   0.7142857 -23.71402  25.142593 0.9999893


# We don’t need to perform the test for the “z” variable because it has only two levels, which have been already proven to be significantly different by ANOVA test. Therefore, the Tukey HSD test will be done only for the factor variable “y”.


