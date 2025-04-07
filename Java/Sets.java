import java.util.LinkedList;
import java.util.List;
import java.util.Set;
import java.util.HashSet;

public class Sets<E> {
    public LinkedList<E> deduplicate1(LinkedList<E> l) {
        Set<E> set = new HashSet<>();
        for (E i : l) {
            set.add(i);
        }
        LinkedList<E> result = new LinkedList<>();
        for (E i : set) {
            result.add(i);
        }
        
        return result;
    }


    public LinkedList<E> deduplicate2(LinkedList<E> l) {
        Set<E> set = new HashSet<>();
        LinkedList<E> returnList = new LinkedList<>();
        for (E i : l) {
            if (!set.contains(i)) {
                set.add(i);
                returnList.add(i);
            }
        }
        return returnList;
    }

    public static void main(String[] args) {
        LinkedList<Integer> list = new LinkedList<>();
        list.add(1);
        list.add(2);
        list.add(2);
        list.add(3);
        list.add(4);
        list.add(4);

        Sets<Integer> sets = new Sets<>();
        
        System.out.println(sets.deduplicate2(list));
    }
}
