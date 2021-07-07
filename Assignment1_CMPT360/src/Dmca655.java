// Michael Angelo C. Adraincem
// MCA655 11208422
// Assignment 1 Part D
// Dmca655.java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Dmca655 {
    private static void softwareTesting(String filename){
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
        Files.write(Paths.get("Dmca655.txt"), results);
    }

    public static void main(String[] args){
        long startTime = System.nanoTime();
        softwareTesting("software.txt");
        long endTime = System.nanoTime();
        long duration = (endTime - startTime);
        System.out.println("Time: " + duration/1000000000.0000 + "seconds");
    }
}
