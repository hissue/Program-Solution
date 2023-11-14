import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length]; 
        for (int c=0;c<commands.length;c++){
            int[] arr = Arrays.copyOfRange(array, commands[c][0]-1,commands[c][1]);
            Arrays.sort(arr);
            answer[c] = arr[(commands[c][2]-1)];
        }
        return answer;
    }
}