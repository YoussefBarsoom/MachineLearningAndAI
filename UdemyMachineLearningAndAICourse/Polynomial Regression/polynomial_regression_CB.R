dataset = read.csv("Position_Salaries.csv")
#data needed from main
dataset = dataset[,2:3]

#split teaining and test set
#install.packages('caTools')
#set.seed(123)
#split= sample.split(dataset$Purchased,SplitRatio=0.8)
#training_set = subset(dataset,split==TRUE)
#test_set = subset(dataset,split==FALSE)

#FS
# training_set[,2:3] = scale(training_set[,2:3])
# test_set[,2:3] = scale(test_set[,2:3])

#fit Linear Regression to the dataset

lin_reg = lm(formula = Salary~ Level,data=dataset)
#fit Polynomial Regression to the dataset'
dataset$Level2 = dataset$Level ^2
dataset$Level3 = dataset$Level ^3
dataset$Level4 = dataset$Level ^4
#$Level5 = dataset$Level ^5

poly_reg = lm(formula = Salary~ .,data=dataset)




#Visuals for Linear
ggplot() + geom_point(aes (x=dataset$Level,y=dataset$Salary),colour= 'red')+geom_line( aes (x=dataset$Level,y= predict(lin_reg ,newdata = dataset),colour= 'blue'))  +ggtitle('Linear') +xlab('Level')

#Visuals for Polynomial
ggplot() + geom_point(aes (x=dataset$Level,y=dataset$Salary),colour= 'red')+geom_line( aes (x=dataset$Level,y= predict(poly_reg ,newdata = dataset),colour= 'blue'))  +ggtitle('Linear') +xlab('Level')



predict(lin_reg ,newdata = data.frame(Level = 6.5))
predict(poly_reg ,newdata =  data.frame(Level = 6.5,Level2 = 6.5^2,Level3= 6.5^3,Level4 = 6.5^4))
