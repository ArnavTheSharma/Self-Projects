import java.util.LinkedList;
import java.util.Arrays;
import java.lang.Comparable;

class Data<T extends Comparable<T>> {
    public T data;

    public Data(T d) {
        this.data = d;
    }
    // default constructor
    public Data() {
        this.data = null;
    }

    // @Override
    public int compareTo(Data<T> d) {
        if (this.data.compareTo(d.data) != 0) {
            return this.data.compareTo(d.data);
        } else {
            throw new IllegalArgumentException("Cannot have duplicates in Tree");
        }
    }
    // search, insertion, print (as triplets. Do * if node isn't there )
}


class Node<T extends Comparable<T>> {
    public Data data;
    public Node left;
    public Node right;
    
    public Node(Data d){
        this.data = d;
    }

    // default constructor
    public Node() {
        data = null;
        left = null;
        right = null;
    }

}

public class Tree {
    public Node head;
    public LinkedList<Node> tree;

    public Tree(Node h, LinkedList<Node> t) {
        this.head = h;
        this.tree = t;
    }

    // public add(Node node) {
    //     if ()
    // }
    
    private void insert(Node node) {
        if (this.head == null) {
            head = node;
        } else {
            if (node.data.compareTo(head.left.data) == 1){

            } 
        }
    }

    public static void main(String args[]) {
        LinkedList<Integer> list = new LinkedList<>(Arrays.asList(1.0, 2.0));
        Node node = new Node()
    }


}



// Psuedo-code
