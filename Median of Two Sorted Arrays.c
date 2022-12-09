double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){
    nums1=realloc(nums1,sizeof(int)*(nums1Size+nums2Size));
    int i,k,j,N,item;
    int* p;
for(i=0;i<nums2Size;i++){
    item=nums2[i];
    p=nums1;
    N=nums1Size;
    for(j=N-1;j>=0&&*(p+j)>item;j--)
      {*(p+j+1)=*(p+j);}
       *(p+j+1)=item;
       nums1Size++;
}
    k=nums1Size;
     for(i=0;i<k;i++)
    {printf("%d\t",*(nums1+i));}
if((k)%2==0)
{
    return((nums1[k/2]+nums1[(k/2)-1])/2.0);
}
else
return(nums1[(k/2)]);
}
