int maxSatisfaction(int* satisfaction, int satisfactionSize){
    int a[satisfactionSize];
    int k=satisfactionSize;
    int i=0,j=0,temp,sum=0,n;
    for(i=0;i<satisfactionSize-1;i++)
    {
        for(j=0;j<satisfactionSize-i-1;j++)
        {
            if(*(satisfaction+j)<*(satisfaction+j+1))
            {
                temp=*(satisfaction+j+1);
                *(satisfaction+j+1)=*(satisfaction+j);
                *(satisfaction+j)=temp;
            } 
        }
    }
    if(*(satisfaction)<0)
    return 0;
    n=satisfactionSize;
    j=0;
    while(j<k)
    {    
        i=0;
         while(n>0)
         {  
            sum=sum+*(satisfaction+(i))*n;
            i++;
            n--;
         }
         a[j++]=sum;
         
             satisfactionSize--;
             sum=0;
             n=satisfactionSize;
         
    }
    int max=0;
    j=0;
    while(j<k)
    {
        if(a[j]>max)
        max=a[j];
        j++;
    }
    return max;
}
