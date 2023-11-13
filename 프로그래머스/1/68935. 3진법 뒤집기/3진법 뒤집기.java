import java.util.*;
class Solution {
    public int solution(int n) {
        ArrayList<Integer> arr = new ArrayList<>();
        while(n > 0){
            arr.add(n%3);
            n = (int) n/3;
        }
        int answer=0;
        int l = arr.size()-1;
        for (int i=0; i<arr.size(); i++){
            answer +=(int)(Math.pow(3,l-i)*arr.get(i));
        }
        
        return answer;
    }
}