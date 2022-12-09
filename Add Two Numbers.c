/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
int c=0,j,h,temp,flag=0;
struct ListNode *k,*o,*i;
i=k=(struct ListNode*)malloc(sizeof(struct ListNode));
while(l1!=NULL||l2!=NULL)
{   if(l1==NULL)
    {j=0;}
    else
    {j=l1->val;}
    h=l2==NULL?0:l2->val;
    temp=c+j+h;
    k->next=(struct ListNode*)malloc(sizeof(struct ListNode));
    k=k->next;
    if(flag==0){o=k;flag=1;}
    k->val=temp%10;
    c=temp/10;
    
    l1=(l1==NULL)?NULL:l1->next;
    l2=(l2==NULL)?NULL:l2->next;
}
if(c==1)
{k->next=(struct ListNode*)malloc(sizeof(struct ListNode));
    k=k->next;
   k->val=1;
}
k->next=NULL;
free(i);
return(o);
}

