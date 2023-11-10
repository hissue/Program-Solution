import java.io.*;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static BufferedReader bf;
    static BufferedWriter bw;
    static int num;
    static Queue<String> queue = new LinkedList<>();

    public static void main(String[] args) throws Exception {
        bf = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));   //할당된 버퍼에 값 넣어주기
        num = Integer.parseInt(bf.readLine());
        for (int i = 0; i < num; i++) {
            String[] cmd = bf.readLine().split(" ");
            switch (cmd[0]) {
                case "push":
                    queue.add(cmd[1]);
                    break;
                case "pop":
                    if (queue.isEmpty()) {
                        bw.write(-1 + "\n");
                    } else {
                        bw.write(queue.poll() + "\n");
                    }
                    break;
                case "size":
                    bw.write(queue.size() + "\n");
                    break;
                case "empty":
                    bw.write((queue.isEmpty() ? 1 : 0) + "\n");
                    break;
                case "front":
                    if (queue.isEmpty()) {
                        bw.write(-1 + "\n");
                    } else {
                        bw.write(queue.peek() + "\n");
                    }
                    break;
                case "back":
                    if (queue.isEmpty()) {
                        bw.write(-1 + "\n");
                    } else {
                        bw.write(queue instanceof LinkedList ?
                            ((LinkedList<String>) queue).get(queue.size() - 1) + "\n" :
                            getLastElement(queue) + "\n");
                    }
                    break;
            }
        }
        bw.flush();
    }

    // Method to get the last element from a Queue if not a LinkedList
    static String getLastElement(Queue<String> queue) {
        String lastElement = "";
        for (String element : queue) {
            lastElement = element;
        }
        return lastElement;
    }
}
