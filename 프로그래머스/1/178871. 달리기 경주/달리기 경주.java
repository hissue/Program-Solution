import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map<String,Integer> map = new HashMap<>();
     
        for (int i=0; i<players.length; i++) {
            map.put(players[i],i);
        }
        
        for (String c : callings){
            int temp = map.get(c); 
            String name = players[temp-1];
            players[temp] = name;
            players[temp-1] = c;
            map.put(c, temp-1);
            map.put(name, temp);
        }
        
        return players;
    }
}