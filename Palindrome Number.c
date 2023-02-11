class Solution {
    public boolean isPalindrome(int x) {
        int a,s;
        s=x;
        a=0;
        if(x<0)
        {
            return false;
        }
        while(s!=0)
        {
            a=a*10+(s%10);
            s=s/10;
        }
        if(a==x)
        {
            return true;
        }
        return false;
    }
}
