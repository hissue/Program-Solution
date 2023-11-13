class Solution {
    public String solution(String s) {
        String answer = "";
        int index = 0;
        for (int i=0; i<s.length(); i++){
            if (s.substring(i,i+1).equals(" ")) { 
                index = 0;
                answer += " ";
                continue;
            }
            answer += index%2 == 1 ? s.substring(i,i+1).toLowerCase() : s.substring(i,i+1).toUpperCase();
            index++;
        }
        return answer;
    }
}