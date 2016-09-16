library(ggplot2)

truth <- read.csv("../xyang105_assign5_result/truth.csv", header=FALSE)
qplot(data = truth, x = V1, y = V2, color = V3)

step1 <- read.csv("../xyang105_assign5_result/step1.csv", header=FALSE)
qplot(data = step1, x = V1, y = V2, color = V3)

step1 <- read.csv("../xyang105_assign5_result/step1.csv", header=FALSE)
qplot(data = step1, x = V1, y = V2, color = V3)

step2a <- read.csv("../xyang105_assign5_result/step2a.csv", header=FALSE)
qplot(data = step2a, x = V1, y = V2, color = V3)

step2b <- read.csv("../xyang105_assign5_result/step2b.csv", header=FALSE)
qplot(data = step2b, x = V1, y = V2, color = V3)
 