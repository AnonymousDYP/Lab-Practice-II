import java.util.Scanner;

public class Chatbot {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Hello! How can I assist you today?");
        String userInput;

        while (true) {
            userInput = scanner.nextLine();

            if (userInput.equalsIgnoreCase("hello")) {
                System.out.println("Hi there!");
            } else if (userInput.equalsIgnoreCase("how are you?")) {
                System.out.println("I'm doing well, thank you!");
            } else if (userInput.equalsIgnoreCase("what's your name?")) {
                System.out.println("You can call me Chatbot.");
            } else if (userInput.equalsIgnoreCase("bye")) {
                System.out.println("Goodbye! Have a great day!");
                break;
            } else {
                System.out.println("I'm sorry, I didn't understand. Could you please rephrase?");
            }
        }

        scanner.close();
    }
}
