class Solution {
    public boolean isAnagram(String s, String t) {
        int s1[] = new int [26];
        int t1[] = new int [26];
        if(s.length()!=t.length())
            return false;
        for(int i=0;i<s.length();i++)
        {
            s1[(int)s.charAt(i)-97]++;
            t1[(int)t.charAt(i)-97]++;
        }
        for(int i=0;i<26;i++)
        {
            if(s1[i]!=t1[i])
                return false;
        }
        return true;
    }
}
