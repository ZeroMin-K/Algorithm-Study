class Solution {
    public int solution(String binomial) {
        String[] expressions = binomial.split(" ");
        int x = Integer.parseInt(expressions[0]);
        int y = Integer.parseInt(expressions[2]);
        String op = expressions[1];
        
        if (op.equals("+")) {
            x += y;
        } else if (op.equals("-")) {
            x -= y;
        } else if (op.equals("*")) {
            x *= y;
        } else {
            x /= y;
        }
        
        return x;
    }
}