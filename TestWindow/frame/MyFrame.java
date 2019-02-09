import javax.swing.*;
import java.util.*;
import java.awt.*;

public class MyFrame {
  public static void main(String[] args) {
    Window frame;
    Text text;

    text = new Text("Olá Mundo");
    frame = new Window(500, 400);

    frame.setTitle("TesteWindow");
    frame.setVisible(true);

    frame.add(text, 100, 100, new Dimension(100, 40)); // write this func
    frame.add(text, 0, 0, new Dimension(100, 40)); // write this func

    frame.pack();
    frame.setLocationRelativeTo(null);
  }
}
