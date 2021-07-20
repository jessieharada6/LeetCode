import java.util.HashMap;
// Time Complexity: O(m * n)
class Solution {
    public int minDistance(String word1, String word2) {
        this.word1 = word1;
        this.word2 = word2;
        return min(word1.length(), word2.length());
    }
    
    String word1;
    String word2;
    
    HashMap<String, Integer> memo = new HashMap<>();
    
    int min(int size1, int size2) {
        // base case
        // from right to left, so base case can be 0
        if (size1 == 0 && size2 == 0) {
            return 0;
        } else if (size1 == 0) {
            return size2;
        } else if (size2 == 0) {
            return size1;
        }
        
        //size1 > 0 and size2 > 0;
        String key = size1 + "." + size2;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }
        
        int solution = 0;
        char c1 = word1.charAt(size1 - 1);
        char c2 = word2.charAt(size2 - 1);
        if (c1 == c2) {
            solution = min(size1 - 1, size2 - 1);
            // the values are brought up
            System.out.println("solution");
            System.out.println(solution);
        } else {
            int option1 = min(size1 - 1, size2) + 1;
            int option2 = min(size1, size2 - 1)  + 1;
            solution = Math.min(option1, option2);
            // print out size1 and size2
            // the values are brought up
            System.out.println("o1");
            System.out.println(option1);
            System.out.println("o2");
            System.out.println(option2);
            System.out.println("sol");
            System.out.println(solution);
        }
        
        memo.put(key, solution);
        return solution;
    }
}