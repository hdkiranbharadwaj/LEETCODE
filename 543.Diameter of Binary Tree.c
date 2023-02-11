/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 int Height(struct TreeNode* R,int* k)
{
    if (R == NULL)
    {
        return 0;
    }
    int l=Height(R->left,k);
    int r=Height(R->right,k);
    *k=Max(*k,(l+r));
    return (1 + Max(l,r));
}
int Max(a,b)
{
    return(a>b?a:b);
}
int diameterOfBinaryTree(struct TreeNode* root){
    int k=0;
Height(root,&k);
return (k);
}
