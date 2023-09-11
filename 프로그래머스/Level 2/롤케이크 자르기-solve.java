import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.HashSet;

class Solution {
    public int solution(int[] toppings) {
        Map<Integer, Integer> toppingsMap = new HashMap<>();
        Set<Integer> toppingsTypes = new HashSet<>();
        int fairWay = 0; 
        
        for (int topping : toppings) {
            if (toppingsMap.containsKey(topping)) {
                toppingsMap.put(topping, toppingsMap.get(topping) + 1);
            } else {
                toppingsMap.put(topping, 1);
            }
        }
        
        for (int topping : toppings) {
            toppingsTypes.add(topping);
            toppingsMap.put(topping, toppingsMap.get(topping) - 1);
            if (toppingsMap.get(topping) == 0) {
                toppingsMap.remove(topping);
            }
            
            if (toppingsTypes.size() == toppingsMap.size()) fairWay++;
        }
        
        
        return fairWay;
    }
}