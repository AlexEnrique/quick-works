import javax.swing.*;
import java.util.*;
import java.awt.*;


public class Text extends JLabel {
  public Color DEFAULT_TEXT_C = new Color(70, 70, 70);

  public Text() {
    setBackground(DEFAULT_TEXT_C);
    setForeground(DEFAULT_TEXT_C);
    setFont(new Font("Noto Sans", 0, 16));
  }

  public Text(String text) {
    setBackground(DEFAULT_TEXT_C);
    setForeground(DEFAULT_TEXT_C);
    setFont(new Font("Noto Sans", 0, 16));
    setText(text);
  }


}
