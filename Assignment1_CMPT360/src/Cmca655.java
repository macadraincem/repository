// Michael Angelo C. Adraincem
// MCA655 11208422
// Assignment 1 Part C
// Cmca655.java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Cmca655 {
    private static void recursion(String filename){
        //Get input from file
        List<String> input = new ArrayList<String>();
        List<String> output = new ArrayList<String>();
        try {
            input = readLine(filename);
        } catch (IOException e) {
            e.printStackTrace();
        }
        //Get number of lines
        int c = Integer.parseInt(input.get(0))+1;

        //Start algorithm
        for (int i=1; i<c; i++){
            String[] splitString = input.get(i).split(",",2);
            int m = Integer.parseInt(splitString[0]);
            int n = Integer.parseInt(splitString[1]);

            if (m % 2 != 0 && n % 2 == 0)
                m--;
            else if (n % 2 != 0 && m % 2 == 0)
                n--;
            //Get absolute value of difference of m and n
            int difference = Math.abs(m-n);
            //Get summation of m
            int mSum = (m*(m+1))/2;
            //Get summation of n
            int nSum = (n*(n+1))/2;
            //Get summation of the difference of m and n
            int dSum = ((difference)*(difference+1))/2;
            //Get add nSum and mSum and deduct dSum
            int summation = mSum + (nSum - dSum);
            output.add(String.valueOf(summation) + ".");
        }

        //Write output to file
        try {
            writeToTxt(output);
        } catch (IOException e) {
            System.out.println("Error writing to Cmca655");
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
        Files.write(Paths.get("Cmca655.txt"), results);
    }

    public static void main(String[] args){
        long startTime = System.nanoTime();
        recursion("recursion.txt");
        long endTime = System.nanoTime();
        long duration = (endTime - startTime);
        System.out.println("Time: " + duration/1000000000.0000 + "seconds");
    }
}
