//The solution in java
class Solution {
    public void moveZeroes(int[] nums) {
        int flag=1,g=0;
        for(int i=0;i<nums.length-g-1;i++)
        {
            if(nums[i]==0)
            {
                for(int j=i;j<nums.length-1;j++)
                {
                    nums[j]=nums[j+1];
                    
                    
                }
                if(flag==1)
                {
                    nums[nums.length-1]=0;
                    flag=0;
                }
                g++;
                i--;
            }
        }
    }
}


//The Solution in C
void moveZeroes(int* a, int numsSize){
int i,j,temp,g=0;
for(i=0;i<numsSize-g-1;i++)
{
    if(a[i]==0)
    {
        for(j=i;j<numsSize-1;j++)
        {
            a[j]=a[j+1];

        }
        a[numsSize-1]=0;
        i--;
        g++;
    }
}
}
