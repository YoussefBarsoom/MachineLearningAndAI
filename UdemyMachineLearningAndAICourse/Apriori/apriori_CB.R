#data preprocessing
dataset = read.csv('Market_Basket_Optimisation.csv',header=FALSE)
#Sparse Matrix
#install.packages('arules')
library(arules)
dataset = read.transactions('Market_Basket_Optimisation.csv',sep=',',rm.duplicates = TRUE)
summary(dataset)

#Frq plot of items
itemFrequencyPlot(dataset,topN=10)

#Training Aprioi on the dataset
#Step 1
rules = apriori(dataset,parameter = list(support= 0.004,confidence =0.2))
summary(rules)

inspect(sort(rules,by = 'lift')[1:10])