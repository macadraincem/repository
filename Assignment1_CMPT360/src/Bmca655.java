// Michael Angelo C. Adraincem
// MCA655 11208422
// Assignment 1 Part B
// Bmca655.java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;



public class Bmca655 {
    private static void beerTime(String filename   ){
        int temp, exponent, result, remainder, c;
        List<String> input = new ArrayList<String>();
        List<String> output = new ArrayList<String>();

        //Get input from file
        try {
            input = readLine(filename);
        } catch (IOException e) {
            System.out.println(e);
        }

        c = Integer.parseInt(input.get(0))+1;
        //Start beerTime Algorithm
        for(int i=1; i < c; i++) {
            temp = Integer.parseInt(input.get(i));
            if (temp != 1 && temp != 2){
                exponent = Math.getExponent(temp);
                remainder = (int) (temp - Math.pow(2, exponent));
                result = (2 * remainder) + 1;
                output.add(String.valueOf(result)+".");
            }
        }

        //Write result to file
        try {
            writeToTxt(output);
        } catch (IOException e) {
            System.out.println("Error writing to Bmca655");
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
        Files.write(Paths.get("Bmca655.txt"), results);
    }

    public static void main(String[] args){
        long startTime = System.nanoTime();
        beerTime("beer.txt");
        long endTime = System.nanoTime();
        long duration = (endTime - startTime);
        System.out.println("Time: " + duration/1000000000.0000 + "seconds");
    }
}
