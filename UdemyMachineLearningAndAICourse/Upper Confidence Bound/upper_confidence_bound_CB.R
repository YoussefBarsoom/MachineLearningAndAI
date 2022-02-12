dataset = read.csv('Ads_CTR_Optimisation.csv')
N=10000
d=10
adsSelected = integer(0)
numberOfSelection = integer(d)
sumOfRewards = integer(d)
totalReWard = 0
for (n in 1:N)
{
  maxUB = 0 
  ad=0
  for(i in 1:d)
  {
    if(numberOfSelection[i]>0)
    {
  avergeReward = sumOfRewards[i]/numberOfSelection[i]
  delta_i = sqrt(3/2 * log(n)/numberOfSelection[i])
    upperBound = avergeReward + delta_i
    }
    else
    {
      upperBound = 1e400
    }
    if(upperBound>maxUB)
    {
      maxUB= upperBound
      ad =i 
    }
    
    
  
    
  }
  adsSelected = append(adsSelected ,ad)
  numberOfSelection[ad]=numberOfSelection[ad]+1
  reward = dataset[n,ad]
  sumOfRewards[ad]= sumOfRewards[ad] + reward
  totalReWard = totalReWard + reward
}


hist(adsSelected,col = 'blue', main='Histrogram of ads Selected', xlab = 'Ads',ylab='NUmber of times ad was selected')