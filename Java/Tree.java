// Sorting alg

import java.util.LinkedList;
import java.util.Arrays;
import java.lang.Comparable;
import java.lang.StringBuilder;

// class Data<T extends Comparable<T>> {
//     public T data;

//     public Data(T d) {
//         this.data = d;
//     }
//     // default constructor
//     public Data() {
//         this.data = null;
//     }

//     // @Override
//     public int compareTo(Data<T> d) {
//         if (this.data.compareTo(d.data) != 0) {
//             return this.data.compareTo(d.data);
//         } else {
//             throw new IllegalArgumentException("Cannot have duplicates in Tree");
//         }
//     }
// }


class Node<T extends Comparable<T>> implements Comparable<Node<T>> {
    public T data;
    public Node<T> left;
    public Node<T> right;
    
    public Node(T d){
        this.data = d;
    }

    // default constructor
    public Node() {
        data = null;
        left = null;
        right = null;
    }

    @Override
    public int compareTo(Node<T> node) {
        int res = this.data.compareTo(node.data);
        if (res == 0) {
            throw new IllegalArgumentException("Cannot have duplicate Nodes");
        } else {
            return res;
        }
    }
    

}

public class Tree<T extends Comparable<T>> {
    public Node<T> head;
    public LinkedList<Node<T>> tree;

    public Tree(Node<T> h, LinkedList<Node<T>> t) {
        this.head = h;
        this.tree = t;
    }

    // default constructor
    public Tree() {
        this.head = null;
        this.tree = null;
    }

    private boolean search(Node<T> node) {
        if (this.head == null) {
            return false;
        } else {
            Node<T> current = this.head;
            while (current != null) {  
                int res = node.data.compareTo(current.data);
                if (res == 0) { // If 2 values are equal
                    return true;
                } else if (res > 0){ // If node you're inserting is greater than current
                    current = current.right;
                } else {
                    current = current.left;
                }
            }
            return false;
 
        }
    }
    
    private void insert(Node<T> node) {
        if (this.head == null) {
            this.head = node;
        } else {
            Node<T> current = this.head;
            while (true) {  
                if (node.compareTo(current) > 0){ // If node you're inserting is greater than current
                    if (current.right == null) {
                        current.right = node;
                        break;
                    } else {
                        current = current.right;
                    }
                } else {
                    if (current.left == null) {
                        current.left = node;
                        break;
                    } else {
                        current = current.left;
                    }
                }
            }
        }
        
    }


    // recursively find depth: each of the nodes will have 2 fields: max depth if going left and max depth if going right. Each of those child nodes will recursively store the same and if node.left = null then return 0 for depth
    public int getDepth(Node<T> node) {
        int leftDepth = 0;
        int rightDepth = 0;

        if (node == null){
            return 0;
        }             
        // if (node.left == null){
        //     return 0;
        // }             
        // if (node.right == null) {
        //     return 0;
        // }

        leftDepth = 1 + getDepth(node.left);
        rightDepth = 1 + getDepth(node.right);

        return (leftDepth > rightDepth) ? leftDepth : rightDepth;

    }

    @Override
    public String toString() {
        return(printTree(this.head));
    }
    
    // each node has it's own depth level, just print the data + 
    public String printTree(Node<T> node) {
        // if (node == null) {
        //     return "*";
        // } else {
        //     // Doesn't account for if node.left or node.right are null
        //     StringBuilder str = new StringBuilder();
        //     str.append(" ".repeat(4) + node.data );
        //     str.append("\n" + " ".repeat(2) + node.left.data + " ".repeat(2) + node.right.data);
        //     return str.toString();
        // }
        if (node == null) {
            return "*";
        } else {
            StringBuilder str = new StringBuilder();
            str.append("depth: " + getDepth(node) + " data: " + node.data);
            if (node.left == null) {
                str.append("  *");
            } else {
                str.append("\n" + printTree(node.left));
                // str.append("\ndepth: " + getDepth(node.left) + " data: " + node.left.data);
            }
            if (node.right == null) {
                str.append("  *");               
            } else {
                str.append("\n" + printTree(node.right));
                // str.append("\ndepth: " + getDepth(node.right) + " data: " + node.right.data);
            }

            return str.toString();
        }
    }


    public static void main(String args[]) {
        LinkedList<Node<Integer>> list = new LinkedList<>();
        Node<Integer> node1 = new Node<>(1);
        Node<Integer> node2 = new Node<>(2);
        Node<Integer> node3 = new Node<>(3);
        Node<Integer> node4 = new Node<>(4);
        Node<Integer> node5 = new Node<>(5);
        Node<Integer> node6 = new Node<>(6);
        
        Tree<Integer> t = new Tree<>(node1, list);
        t.insert(node3);
        t.insert(node5);
        t.insert(node6);
        t.insert(node2);
        t.insert(node4);

        System.out.println(t.printTree(t.head));
        System.out.println(t.getDepth(t.head));
        
        // int j =10;
        // int i = 10;
        // System.out.println(++i  +  i++);
        // System.out.println(++i  +  ++i);


        //  if (!(obj instanceof List))
        //      true if the object is an instance of the specified type, 
        //      object instanceof Type


    }


}
