
dataset = read.csv("50_Startups.csv")
#data needed from main
#dataset = dataset[,2:3]

#Catergorical Data
dataset$State = factor(dataset$State , levels = c('New York','California','Florida'),labels = c(1,2,3))


#split teaining and test set
#install.packages('caTools')
set.seed(123)
split= sample.split(dataset$Profit,SplitRatio=0.8)
training_set = subset(dataset,split==TRUE)
test_set = subset(dataset,split==FALSE)

#FS
# training_set[,2:3] = scale(training_set[,2:3])
# test_set[,2:3] = scale(test_set[,2:3])

#Fit Multiple Linear Regression to training set
#regressor = lm(formula = Profit ~ .)
regressor = lm(formula = Profit ~ R.D.Spend+ Administration + Marketing.Spend+State,data = training_set)

#Predict test val
y_pred = predict(regressor,newdata = test_set)

#Backward elimination
regressor = lm(formula = Profit ~ R.D.Spend+ Administration + Marketing.Spend+State,data = training_set)
summary(regressor)
regressor = lm(formula = Profit ~ R.D.Spend ,data = training_set)
summary(regressor)

y_pred = predict(regressor,newdata = test_set)
