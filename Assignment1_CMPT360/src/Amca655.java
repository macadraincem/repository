// Michael Angelo C. Adraincem
// MCA655 11208422
// Assignment 1 Part A
// Amca655.java
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;


public class Amca655 {
    private static void palindrome(String filename){

        //Get input from file
        List<String> input = new ArrayList<String>();
        int c;
        try {
            input = readLine(filename);
        } catch (IOException e) {
            System.out.println(e);
        }

        c = Integer.valueOf(input.get(0)) + 1;
        //Start palindrome algorithm
        List<String> output = new ArrayList<String>();
        String temp1, temp2;
        char trailing;

        for(int i=1; i < c; i++){
            if(input.get(i).length() != 1){
                StringBuffer tempBuffer = new StringBuffer(input.get(i));
                temp1 = tempBuffer.toString();
                temp2 = tempBuffer.reverse().toString();
                trailing = temp1.charAt(temp1.length()-1);
                final char t = temp1.charAt(0);
                if(temp1.chars().filter(ch -> ch == t).count() == temp1.length()){
                    output.add(temp1.concat(temp2.replace(Character.toString(trailing), "") + "."));
                }
                else if (temp1.contentEquals(temp2)){
                    output.add(temp1.concat(temp2.replaceFirst(Character.toString(trailing),""))+".");
                }
                else {
                    output.add(temp1.concat(temp2.replace(Character.toString(trailing), "") + "."));
                }
            }
        }

        //Start Writing results to file
        try {
            writeToTxt(output);
        } catch (IOException e) {
            System.out.println("Error writing to Amca655");
        }
    }

    private static List<String> readLine(String filename) throws IOException {
        //File IO code from Piazza discussion
        List<String> lines = Files.readAllLines(Paths.get(filename));
        for(int i=0; i < lines.size(); i++) {
            lines.set(i,lines.get(i).replaceAll(".$", ""));
        }
        return lines;
    }

    private static void writeToTxt(List<String> results) throws IOException {
        //File IO code from Piazza discussion
        Files.write(Paths.get("Amca655.txt"), results);
    }

    public static void main(String[] args){
        long startTime = System.nanoTime();
        palindrome("palindrome.txt");
        long endTime = System.nanoTime();
        long duration = (endTime - startTime);
        System.out.println("Time: " + duration/1000000000.0000 + "seconds");
    }

}
