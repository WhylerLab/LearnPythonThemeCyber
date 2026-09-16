public class test {
    public static void main(String[] args) {
    try {
        int result = 12 / 0;    
        System.out.println(result);
    } catch (Exception exception) {    
        System.out.println(exception.getMessage());
    }
    }
}
