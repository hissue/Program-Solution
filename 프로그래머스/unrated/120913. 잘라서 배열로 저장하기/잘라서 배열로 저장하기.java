class Solution {
    public String[] solution(String my_str, int n) {
        int index = (int) Math.ceil((double) my_str.length()/n);
        String[] answer = new String[index];
        int start;
        int end;
       for (int i=0 ;i<index;i++){
            start = n*i;
            if ( start+n > my_str.length()){
                end = my_str.length();
            }else{
                end = start + n;
            }
           answer[i] = my_str.substring(start,end);
       }
        return answer;
    }
}