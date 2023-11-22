class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "";
        int c1=0;
        int c2=0;
        int g=0;
        for (String word: goal){
            if(c1 < cards1.length && cards1[c1].equals(goal[g])){
                c1++;
                g++;
            }else if(c2 < cards2.length && cards2[c2].equals(goal[g])){
                c2++;
                g++;
            }else{
                
               return "No";
            }
        }
        return "Yes";
    }
}