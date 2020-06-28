public class Solution {
    // DO NOT MODIFY THE LIST. IT IS READ ONLY
    public int strStr(final String A, final String B) {
        int hayLen=A.length();
        int needleLen=B.length();
        if(B.isEmpty())
        return -1;
        if(A.isEmpty()&&B.isEmpty())
        return -1;
        if(A.length()<B.length())
        return -1;
        for(int i=0;i<hayLen-needleLen+1;i++){
            if(A.substring(i,i+needleLen).equals(B)){
                return i;
            }
        }
        return -1;
    }
}