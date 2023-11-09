class Solution {
    public int solution(String[] babbling) {
        String[] words = {"aya", "ye", "woo", "ma"};
        int total = 0;
        // 연속된 같은 단어 X, 단어가 목록에 있어야 함
        for (String b : babbling){
            for (String word : words){
                if (b.indexOf(word+word)!=-1){
                    break;
                }
                b=b.replace(word,"0");
            }
            if (b.matches(".*[a-z].*")){
                continue;
            }
            total+=1;
        }
        return total;
    }
}