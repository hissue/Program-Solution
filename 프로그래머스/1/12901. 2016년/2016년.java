class Solution {
    public String solution(int a, int b) {
        int answer = 0;
        int[] months = new int[]{0,31,29,31,30,31,30,31,31,30,31,30,31};
        String[] week = new String[]{"THU","FRI","SAT","SUN","MON","TUE","WED"};
        for (int i=1; i<a; i++){
            answer += months[i];
        }
        return week[(answer+b)%7];
    }
}