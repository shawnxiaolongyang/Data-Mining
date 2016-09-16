setwd('C:/Users/xyang/Desktop/COURSE/CS412 Datamining/HW/optional/MP6')

sales_fact<-read.csv("transactions.csv", header = TRUE, sep=' ')
#
myfunction <- function(x){
temp = 0
if( is.null(x) )
	return(temp)

temp = sum(x)
return(temp)
}

a = c()
myfunction(a)

#build a data_cube,
revenue_cube <- 
    tapply(sales_fact$amount, 
           sales_fact[,c("prod", "month", "year", "loc","unit")],
           FUN=myfunction)

revenue_cube[is.na(revenue_cube)] <- 0 


#plot 
mmfunc <- function(ff) {

if( length(dim(ff)) < 3 ){
	print("here1")
	barplot(as.matrix(ff), main="Which product has the most popularity (units = 2) in "NZ" during the first six months of the year 2012", ylab = "Numbers", cex.lab = 1.5, cex.main = 1.4, beside=TRUE)

} else if (length(dim(ff)) == 3 ) {
	par(mfrow=c(dim(ff)[1],1))
	for (i in 1:dim(ff)[1]){
		barplot(as.matrix(ff[i,,]), main="My Barchart", ylab = "Numbers", cex.lab = 1.5, cex.main = 1.4, beside=TRUE)
	}
} else if (length(dim(ff)) == 4 ) {
    par(mfrow=c(dim(ff)[1], dim(ff)[2]))
    for (i in 1:dim(ff)[1]){
        for (j in 1:dim(ff)[2]){
            
            barplot(as.matrix(ff[i,j,,]), main="My Barchart", ylab = "Numbers", cex.lab = 1, cex.main = 1, beside=TRUE)
        }
    }
} 

return(0)
}
# Question A
apply(revenue_cube[,,,c("CA"),],c("year","month"),FUN = myfunction)
mmfunc(apply(revenue_cube[,,,c("CA"),],c("year","month"),FUN = myfunction))

# Question B
revenue_cube[, c("1","2","3","4","5","6"),c("2012"),c("NZ"),c("2")]
mmfunc(revenue_cube[, c("1","2","3","4","5","6"),c("2012"),c("NZ"),c("2")])

# Question C
apply(revenue_cube[c("Tablet"),,,,],c("loc"),FUN = myfunction)
mmfunc(apply(revenue_cube[c("Tablet"),,,,],c("loc"),FUN = myfunction))