import java.util.*;
class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        int temp = 0;
        for (int i=0; i<10;i++){
            temp+=i;
        }

        for (int i=0;i<numbers.length;i++){
            answer+=numbers[i];}
        return temp - answer;
    }
}