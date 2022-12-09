/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int* twoSum(int* nums, int numsSize, int target, int* returnSize)
{   *returnSize=2;
    
    int *k=(int*)malloc(sizeof(int)*2);
    int i,j;
   
   for (int i = 0; i < numsSize-1; i++) {
            for (int j = i + 1; j < numsSize; j++) {
                if (nums[j]+ nums[i] == target ) {
                    k[0]=i;
                    k[1]=j;
                    return(k);
                }
            }
        }
   return(NULL);
}
