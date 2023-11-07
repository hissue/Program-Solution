import java.util.*;
class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        List<Integer> arrayList = new ArrayList<>();

        for (int a : arr){
            arrayList.add(a);
        }

        for (int d : delete_list) {
            arrayList.remove((Integer) d);
        }

        int[] answer = new int[arrayList.size()];
        for (int i=0;i< arrayList.size();i++){
            answer[i] = arrayList.get(i).intValue();
        }
        return answer;
    }
}