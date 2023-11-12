import java.util.*;
class Solution {
    public String solution(String s) {
        ArrayList<Character> lists = new ArrayList<>();
        String answer ="";
        for(int i=0; i<s.length(); i++){
            lists.add(s.charAt(i));
        } 
        Collections.sort(lists);
        Collections.reverse(lists);
    
        for(int i=0; i<s.length(); i++){
            answer+=lists.get(i);
        } 
        return answer;
    }
}