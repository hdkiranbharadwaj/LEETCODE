/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 struct node{
     int top;
     int* item;
 };
typedef struct node STK;
 void push(int i,STK *K)
{
       *(K->item+(++K->top))=i;
}

int* inorderTraversal(struct TreeNode* root, int* returnSize){
STK K;
K.top=-1;
K.item=(int*)malloc(sizeof(int)*100);
inod(root,&K);
*returnSize=K.top+1;
return K.item;
}
void inod(struct TreeNode* R,STK *K)
{
    if(R==NULL)
     return;
     
     inod( R->left,K);
     push(R->val,K);
     inod(R->right,K);

}
