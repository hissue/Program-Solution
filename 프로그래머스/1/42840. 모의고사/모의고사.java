import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        int[] nums1 = {1, 2, 3, 4, 5};
        int[] nums2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] nums3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] total = {0,0,0};
        for (int i=0; i<nums1.length; i++){
            for (int j=i; j < answers.length; j+=nums1.length){
                if (answers[j]==nums1[i]){
                    total[0]++;
                }
            }
        }
        for (int i=0; i<nums2.length; i++){
            for (int j=i; j < answers.length; j+=nums2.length){
                if (answers[j]==nums2[i]){
                    total[1]++;
                }
            }
        }
        for (int i=0; i<nums3.length; i++){
            for (int j=i; j < answers.length; j+=nums3.length){
                if (answers[j]==nums3[i]){
                    total[2]++;
                }
            }
        }
        int maxTotal = Math.max(total[0],total[1]);
        maxTotal = Math.max(maxTotal,total[2]);
        
        ArrayList<Integer> temp = new ArrayList<Integer>();
        for (int i=0; i<total.length;i++){
            if (maxTotal == total[i]){
                temp.add(i+1);
            }
        }
        
        int[] answer = new int[temp.size()];
        for (int i=0; i<temp.size();i++){
            answer[i] = temp.get(i);
        }
       
        return answer;
    }
}