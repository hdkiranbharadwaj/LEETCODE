/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head){
struct ListNode *FN,*PN,*TP,*KP,*PPN;
if(head==NULL||head->next==NULL)
{
    return head;
}
struct ListNode* NN=(struct ListNode*)malloc(sizeof(struct ListNode));
NN->next=head;
head=NN;
FN=head->next->next;
PN=head->next;
PPN=head;
while(FN!=NULL)
{
  PPN->next=FN;
  PN->next=FN->next;
  FN->next=PN;
  TP=PN;
  PN=FN;
  FN=TP;
  if(FN->next==NULL)
  {
      break;
  }
  PN=PN->next->next;
  FN=FN->next->next;
  PPN=PPN->next->next;
}
return head->next;
}
