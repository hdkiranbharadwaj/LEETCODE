int reverse(int x){
long flag=0,temp=x;
long rev=0;
if(temp<0)
{
    flag=1;
    temp=temp*(-1);
}
while(temp!=0)
{
   rev=(rev*10)+(temp%10);
   temp=temp/10;
}
if((-2147483648 >= rev) ||(rev>= 2147483648 - 1))
{return 0;
}
else
{if(flag)
    {  
        return(rev*-1);
    }
    else
    {
    return rev;
    }
}



}
