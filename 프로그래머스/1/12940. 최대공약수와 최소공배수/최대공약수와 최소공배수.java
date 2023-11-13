class Solution {
    public int[] solution(int n, int m) {
        int originN = n;
        int originM = m ;
        
       for(;;){
        int r = n%m;
        if(r==0) break;
        n = m;
        m = r;
    }
        return new int[]{m,(originN*originM)/m};
    }
}