class Solution {
    public int[] solution(long n) {
        String[] answer = Long.toString(n).split("");
        int index = 0;
        int [] result = new int[answer.length];
        for (int i = answer.length-1; i>=0;i--){
            result[index++] = Integer.parseInt(answer[i]);
        }
        
        return result;
    }
}