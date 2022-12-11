/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
int count=0,i=0;
struct ListNode* tp;
struct ListNode *pn;
tp=head;
while(tp!=NULL)
{
    count++;
    tp=tp->next;
}
n=count-n;
if(n==0)
{
    pn=head;
    head=head->next;
    free(pn);
    return head;
}
pn=NULL;
tp=head;
while(i<n&&tp!=NULL)
{   printf("%d",tp->val);
    pn=tp;
    tp=tp->next;
    i++;
}
pn->next=tp->next;
free (tp);
return head;
}
