/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
float sum=0,sum2=0;
int i=0,j=0,temp,k;
struct ListNode  *l3,*KKK,*NN;
while(l1!=NULL)
{
    sum=sum/10.0+(l1->val);
    i++;
    l1=l1->next;
}
while(l2!=NULL)
{
    sum2=sum2/10.0+(l2->val);
    j++;
    l2=l2->next;
}
sum=sum*pow(10,i)+sum2*pow(10,j);
temp=sum;
temp=temp/10;

KKK=l3=(struct ListNode*)malloc(sizeof(struct ListNode));
l3->val=(temp%10);
temp=temp/10;
while(temp!=0){
l3->next=(struct ListNode*)malloc(sizeof(struct ListNode));
l3=l3->next;
l3->val=(temp%10);
temp=temp/10;
}

l3->next=NULL;
return KKK;
}
