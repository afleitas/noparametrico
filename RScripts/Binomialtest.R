limi<-vector(mode="numeric",1000) 
lims<-vector(mode="numeric",1000) 
a<-seq(0,1,0.001) 
length(a)
alfa<-(1-0.95)/2 
x<-7 
nn<-20 



for (i in 1:1001)
{ 
  limi[i]<-pbinom(x-1,nn,a[i]) 
  lims[i]<-pbinom(x,nn,a[i]) 
} 


for (i in 2:1001) 
{ 
  if (limi[i]<=(1-alfa) && limi[i-1]>(1-alfa)) low<-a[i-1] 
  if (lims[i]<=alfa && lims[i-1]>alfa) lup<-a[i-1] 
  
}


mean(limi)
min(limi)
max(limi)

low
lup


binom.test(x= 7,n=20,p=0.4,alternative = "less")


{{s  }}