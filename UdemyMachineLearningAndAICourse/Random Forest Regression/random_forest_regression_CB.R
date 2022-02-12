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

#Fit Random Forest Regression  to the dataset
#install.packages('randomForest')
set.seed(1234)
regressor =  randomForest(x= dataset[1] ,y= dataset$Salary, ntree= 500)


#Predict Values
predict(regressor ,newdata =  data.frame(Level = 6.5))




#Higher Resolution for Visuals
X_grid = seq(min(dataset$Level),max(dataset$Level),0.01)
ggplot() + geom_point(aes (x=dataset$Level,y=dataset$Salary),colour= 'red')+geom_line( aes (x=X_grid,y= predict(regressor ,newdata = data.frame(Level = X_grid)),colour= 'blue'))  +ggtitle('Random Forest Regression  Model') +xlab('Level')

