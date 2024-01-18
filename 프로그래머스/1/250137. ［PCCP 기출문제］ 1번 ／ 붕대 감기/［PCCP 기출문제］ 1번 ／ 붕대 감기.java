// 1초마다 x만큼의 체력 회복, t초 연속으로 붕대 감는데 성공하면 y 체력 추가 회복, 최대 체력보다 커지는 것 불가
class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int time = 0;
        int len = attacks.length-1;
        int i = 0;
        int cur_health = health;
        int count = 0;
        while(time < attacks[len][0] && cur_health > 0){
            time++;
            if(time == attacks[i][0]){
                cur_health -= attacks[i][1];
                i++;
                count=0;
                continue;
            } 
            count++;
            if(count == bandage[0]){
                cur_health += bandage[2];
                count=0;
            }
            
            cur_health += bandage[1];
            cur_health = cur_health > health ? health : cur_health;
        }
        
        return cur_health <= 0 ? -1 : cur_health;
    }
}