class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Graph graph = new Graph();
        for (int[] prerequisite: prerequisites) {
            graph.connect(prerequisite[1], prerequisite[0]);
        }
        
        return !graph.containsCycle(); 
    }
}

// edge is not needed in this question
// class Edge {
    
// }

class Status {
    public static final int notVisited = 0;
    public static final int visiting = 1;
    public static final int visited = 2;
}

class Node {
    // int key;
    int status = Status.notVisited;
    List<Node> toNodes = new ArrayList<Node>(); 
}

class Graph {
    private Map<Integer, Node> nodes = new HashMap<Integer, Node>();
    
    Node getOrCreateNode(int key) {
        Node node = nodes.get(key);
        if (node == null) {
            node = new Node();
            // node.key = key;
            nodes.put(key, node);
        }
        return node;
    }
    
    void connect(int from, int to) {
        Node fromNode = this.getOrCreateNode(from);
        Node toNode = this.getOrCreateNode(to);
        fromNode.toNodes.add(toNode);
    } 
    
    boolean containsCycle() {
        try {
           for (Node node: nodes.values()) {
                // if (node.status != Status.notVisited) {
                //     continue;
                // } 
                visit(node);
            } 
        } catch (Exception e) {
            return true;
        } 
        return false;
    }
    
    //dfs
    void visit(Node node) throws Exception {
        if (node.status == Status.visited) {
            return;
        }
        
        // contain cycles 
        if (node.status == Status.visiting) {
            throw new Exception();
        }
        
        node.status = Status.visiting;
        for (Node toNode: node.toNodes) {
            visit(toNode);
        }
        node.status = Status.visited;
    }
}