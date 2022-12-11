/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val){
if(head==NULL)
{
    return NULL;
}
struct ListNode *pn,*tp;
pn=head;
tp=head->next;
while(tp!=NULL)
{
    if(tp->val==val)
    {
        pn->next=tp->next;
        free(tp);
        tp=pn->next;
    }
    else
    {
        pn=tp;
        tp=pn->next;
    }
}
if(head->val==val)
{
    pn=head;
    head=head->next;
    free (pn);
}
return(head);

}
