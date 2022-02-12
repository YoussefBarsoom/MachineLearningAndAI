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

#Fit Regression to the dataset
#install.packages('e1071')
regressor = svm(formula = Salary~.,data = dataset,type= 'eps-regression')



#Predict Values
predict(regressor ,newdata =  data.frame(Level = 6.5))

#Visuals for Regression Model results

ggplot() + geom_point(aes (x=dataset$Level,y=dataset$Salary),colour= 'red')+geom_line( aes (x=dataset$Level,y= predict(regressor ,newdata = dataset),colour= 'blue'))  +ggtitle('Regressor Model') +xlab('Level')


#Higher Resolution for Visuals
X_grid = seq(min(dataset$Level),max(dataset$Level),0.1)
ggplot() + geom_point(aes (x=dataset$Level,y=dataset$Salary),colour= 'red')+geom_line( aes (x=X_grid,y= predict(regressor ,newdata = data.frame(Level = X_grid)),colour= 'blue'))  +ggtitle('Regressor Model') +xlab('Level')

