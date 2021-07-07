
import java.io.*;
import java.util.StringTokenizer;  
//****************
//START: READ ONLY
//****************
public class Quantum {
//****************
//END: READ ONLY
//****************

// YOU CAN DEFINE YOUR OWN FUNCTIONS HERE IF YOU REALLY NEED ONE

//****************
//START: READ ONLY
//****************
		
	
    /**     
	 * @param n : The number of buses
     * @return The cost of minimum crossing configuration with X buses
     */
    public static int cost(int X) {
//****************
//END: READ ONLY
//****************

		//WRITE YOUR NSID: MCA655
		
		//start: edit and write your code here 
		int totalPairs = 0;
		int result = 1;
		totalPairs = (X*(X-1))/2;
		if (X <= 4)
		    return 0;
		else{
		    for (int i = 4; i < X; i++){
		            result+=2;
            }
            return result;
        }
        //end: write your code here 
	 
		 
		
    }
//****************
//START: READ ONLY
//****************
    /**
     * Main Function.
     */
    public static void main(String[] args) {

        BufferedReader reader;
        File file = new File("output.txt");
		int X = 0; 
		String line;
        try {
            reader = new BufferedReader(new FileReader("src/Quantum.txt"));
            BufferedWriter writer = new BufferedWriter(new FileWriter(file));            
            while(true){ 
				line = reader.readLine();
				if(line == null) break;				
				X = Integer.parseInt(line); 
                writer.write(cost(X) + "\n");
				writer.flush();
            } 

            reader.close();
            writer.close();
        } catch (FileNotFoundException e) {
            System.out.println("Could not locate input file.");
        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }

}
