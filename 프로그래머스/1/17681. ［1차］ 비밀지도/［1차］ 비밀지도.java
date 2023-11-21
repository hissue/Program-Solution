import java.util.*;
class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        List<String> answer = new ArrayList<>();
        for(int i=0; i<arr1.length;i++){
          String temp = Integer.toBinaryString(arr1[i]|arr2[i]);
            temp=temp.replace("0"," ");
            answer.add(temp.replace("1","#"));
        }
        String[] result = new String[n];
        for (int i=0; i<answer.size();i++){
            result[i] = answer.get(i).length() == n ? answer.get(i) : " ".repeat(n-answer.get(i).length()) + answer.get(i);
        
        }
        
        
        return result;
    }
}