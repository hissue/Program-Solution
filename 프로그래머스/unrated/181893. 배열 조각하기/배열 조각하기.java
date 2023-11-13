class Solution {
    public int[] solution(int[] arr, int[] query) {
        String temp="";
        for (int i=0; i<arr.length; i++){
            temp+=arr[i];
        }
        
        for (int i=0; i<query.length; i++){
            int l = temp.length();
            if (i%2==0){
                temp = temp.substring(0,query[i]+1);
            }else{
                temp = temp.substring(query[i],l);
            }
        }
        int[] answer = new int[temp.length()];
        for (int i=0; i<temp.length(); i++){
            answer[i] = temp[i];
        }
        
        return null;
    }
}