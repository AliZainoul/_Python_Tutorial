public class Main {
    public static void main(String[] args) { 
        Person p = new Person("Alice"); 
        System.out.println(p.getName());
        System.out.println(p.name); 
        p.name = "Ali";
    }
}


/*
Main.java:4: error: name has private access in Person
        System.out.println(p.name);
                            ^
Main.java:5: error: name has private access in Person
        p.name = "Ali";
         ^
2 errors
*/