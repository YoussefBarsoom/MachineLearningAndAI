dataset = read.csv('Ads_CTR_Optimisation.csv')
N=10000
d=10
adsSelected = integer(0)
numberOfSelection_1 = integer(d)
numberOfSelection_0 = integer(d)
totalReWard = 0
for (n in 1:N)
{
  maxRandom = 0 
  ad=0
  for(i in 1:d)
  {
    randomBeta = rbeta(n=1,shape1 = numberOfSelection_1[i] + 1,shape2 = numberOfSelection_0[i] +1)
    
    if(randomBeta>maxRandom)
    {
      maxRandom= randomBeta
      ad =i 
    }
  
  }
  adsSelected = append(adsSelected ,ad)
  reward = dataset[n,ad]
  if (reward ==1)
  {
  numberOfSelection_1[ad]=numberOfSelection_1[ad]+1
  }
  else
    { 
      numberOfSelection_0[ad]=numberOfSelection_0[ad]+1
    }
  totalReWard = totalReWard + reward
}


hist(adsSelected,col = 'blue', main='Histrogram of ads Selected', xlab = 'Ads',ylab='NUmber of times ad was selected')