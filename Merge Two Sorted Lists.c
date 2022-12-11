/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
   struct ListNode *NN,*TP,*PN;
while(list2!= NULL)
{   
    NN=(struct ListNode *)malloc(sizeof(struct ListNode));
    NN->val=list2->val;
    TP=list1; PN=NULL;
	while(TP!=NULL && TP->val<NN->val)
	  {
	   PN=TP;
	   TP=TP->next;
	  }
	  if(PN==NULL)
	     {
	      NN->next=TP;
          list1= NN;
	     }
     else{
	     NN->next=TP;
	    PN->next=NN;
        }
    list2=list2->next;
}
return list1;
}
