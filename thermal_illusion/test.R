library(ggplot2)
library(readxl)
library(tidyverse)
# Loading
file <- "C:/Users/saku_/OneDrive - Maeda Laboratory/thermal_illusion/experiment/20200109.xlsx"
sheets <- excel_sheets(file)
dat <- 
  sheets %>% 
  map_dfr( ~ read_excel(file, skip = 2, sheet = .x) %>% 
             mutate(sheet = .x)) 
result <- read_excel(file, skip = 0, sheet = "figure") 


#ggplot(data=result, aes(x=TD, y=sub1)) + geom_point(color="blue") 

ggplot()+geom_line(data = result,aes(x = TD,y = sub1,colour = "sub1"),size=1)+
  geom_point(data = result,aes(x = TD,y = sub1,colour = "sub1"),size=3)+
  ylim(0,100)+
  geom_line(data = result,aes(x = TD,y = sub2,colour ="sub2"),size=1) + 
  geom_point(data = result,aes(x = TD,y = sub2,colour = "sub2"),size=3)+

  geom_line(data = result,aes(x = TD,y = sub3,colour ="sub3"),size=1) + 
  geom_point(data = result,aes(x = TD,y = sub3,colour = "sub3"),size=3)+

  geom_line(data = result,aes(x = TD,y = sub4,colour ="sub4"),size=1) + 
  geom_point(data = result,aes(x = TD,y = sub4,colour = "sub4"),size=3)+

  geom_line(data = result,aes(x = TD,y = expected,colour ="expected"),size=3,linetype="dotted") + 
  #geom_point(data = result,aes(x = TD,y = expected,colour = "expected"),size=3)+

  scale_colour_manual("",values = c("sub1" = "blue","sub2" = "orange","sub3" = "gray","sub4" = "yellow","expected" = "red"))+
  xlab("Temperature difference(°C)")+ylab("Possibility(%)")+
  theme(text=element_text(size=13, family="Comic Sans MS"))+
  labs(title = "Possibility to choose device with larger spatial frequency 
  under temperature difference conditions")

