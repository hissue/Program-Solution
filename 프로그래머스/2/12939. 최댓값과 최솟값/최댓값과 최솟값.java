class Solution {
    public String solution(String s) {
        String[] arr = s.split(" ");
        int min = Integer.parseInt(arr[0]);
        int max = Integer.parseInt(arr[0]);
        for (int i=1; i<arr.length; i++){
            if (!arr[i].equals(" ")){
                int tmp = Integer.parseInt(arr[i]);
                min = (tmp < min) ? tmp : min;
                max = (tmp > max) ? tmp : max;
            }
            
        }
        return min + " " + max;
    }
}