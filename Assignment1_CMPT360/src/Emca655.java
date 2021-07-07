// Michael Angelo C. Adraincem
// MCA655 11208422
// Assignment 1 Part E
// Emca655.java
import java.awt.*;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Emca655 {
    private static void sequence(String filename) {
        //Get input from file
        List<String> input = new ArrayList<String>();
        List<String> output = new ArrayList<String>();
        try {
            input = readLine(filename);
        } catch (IOException e) {
            e.printStackTrace();
        }

        //Get number of lines
        int c = Integer.parseInt(input.get(0)) + 1;
        int ctr = 1;
        for (int i = 1; i < c; i++) {
            int n = Integer.parseInt(input.get(i));
            while (n > 1) {
                if (n == 1) {
                    n = 1;
                    ctr++;
                } else if (n % 2 != 0) {
                    n = (3 * n) + 1;
                    ctr++;
                } else {
                    n = n / 2;
                    ctr++;
                }
            }
            output.add(String.valueOf(ctr) + ".");
            ctr = 1;
        }

        //Write output to file
        try {
            writeToTxt(output);
        } catch (IOException e) {
            System.out.println("Error writing to Emca655");
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
        Files.write(Paths.get("Emca655.txt"),  results);
    }

    public static void main(String[] args){
        long startTime = System.nanoTime();
        sequence("sequence.txt");
        long endTime = System.nanoTime();
        long duration = (endTime - startTime);
        System.out.println("Time: " + duration/1000000000.0000 + "seconds");
    }
}
