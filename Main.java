import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;
import java.util.stream.Collector;

public class Main {
    public static void main(String[] args) {
        // 1. Create two sample lists
        List<String> listOne = Arrays.asList("Apple", "Banana", "Cherry");
        List<String> listTwo = Arrays.asList("Date", "Elderberry", "Fig");

        System.out.println("List 1: " + listOne);
        System.out.println("List 2: " + listTwo);

        // 2. Merge the lists using Stream.concat()
        List<String> mergedList = Stream.concat(listOne.stream(), listTwo.stream())
                                        .collect(Collector.toList()); // Note: Use .collect(Collectors.toList()) if using Java 15 or older

        // 3. Print the result
        System.out.println("Merged List: " + mergedList);
    }
}
// =====================

class Singleton{
    private static Singleton instance ;

    private Singleton(){

    }

    public static Singleton getInstance(){
        if(instance == null){
            instance = new Singleton();
        }
        return instance;
    }

}

// --------------

