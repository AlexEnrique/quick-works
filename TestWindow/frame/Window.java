import javax.swing.*;
import java.util.*;
import java.awt.*;

public class Window extends JFrame {
  private GroupLayout layout;
  private GroupLayout.Group hGroup;
  private GroupLayout.Group vGroup;


  /* Constants */
  private final Color WHITE = new Color(255, 255, 255);
  public int CENTER_X;
  public int CENTER_Y;
  public String CENTERING = "addAtCenter";

  /* Initializers */
  public Window() {
    this.setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

    layout = new GroupLayout(getContentPane());
    getContentPane().setLayout(layout);

    hGroup = layout.createParallelGroup(GroupLayout.Alignment.LEADING);
    vGroup = layout.createParallelGroup(GroupLayout.Alignment.LEADING);

    layout.setHorizontalGroup(hGroup);
    layout.setVerticalGroup(vGroup);

    // this.setBackground(WHITE);
    // this.setUndecorated(true);
  }

  public Window(int width, int height) {
    setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
    size(width, height);

    CENTER_X = width/2;
    CENTER_Y = height/2;

    layout = new GroupLayout(getContentPane());
    getContentPane().setLayout(layout);

    hGroup = layout.createParallelGroup(GroupLayout.Alignment.LEADING);
    vGroup = layout.createParallelGroup(GroupLayout.Alignment.LEADING);

    layout.setHorizontalGroup(hGroup);
    layout.setVerticalGroup(vGroup);

    // this.setBackground(WHITE);
    // this.setUndecorated(true);
  }

  /* Methods */
  public void size(Dimension d) {
    this.setSize(d);
    this.setMinimumSize(d);
    this.setMaximumSize(d);
    this.setPreferredSize(d);

    CENTER_X = d.width/2;
    CENTER_Y = d.height/2;
  }

  public void size(int width, int height) {
    this.setSize(new Dimension(width, height));
    this.setMinimumSize(new Dimension(width, height));
    this.setMaximumSize(new Dimension(width, height));
    this.setPreferredSize(new Dimension(width, height));

    CENTER_X = width/2;
    CENTER_Y = height/2;
  }

  public void size(int widthAndHeight) {
    this.setSize(new Dimension(widthAndHeight, widthAndHeight));
    this.setMinimumSize(new Dimension(widthAndHeight, widthAndHeight));
    this.setMaximumSize(new Dimension(widthAndHeight, widthAndHeight));
    this.setPreferredSize(new Dimension(widthAndHeight, widthAndHeight));

    CENTER_X = widthAndHeight;
    CENTER_Y = widthAndHeight;
  }

  public void add(Component component, int x, int y, Dimension d) {
    hGroup.addGroup(layout.createSequentialGroup()
      .addGap(x)
      .addComponent(component, d.width, d.width, d.width)
    );

    vGroup.addGroup(layout.createSequentialGroup()
      .addGap(y)
      .addComponent(component, d.height, d.height, d.height)
    );
  }

  public void add(Component component, int x, int y, int width, int height) {
    hGroup.addGroup(layout.createSequentialGroup()
      .addGap(x)
      .addComponent(component, width, width, width)
    );

    vGroup.addGroup(layout.createSequentialGroup()
      .addGap(y)
      .addComponent(component, height, height, height)
    );
  }

  public void add(Component component, int x, Dimension d) {
    hGroup.addGroup(layout.createSequentialGroup()
      .addGap(x)
      .addComponent(component, d.width, d.width, d.width)
    );

    vGroup.addGroup(layout.createSequentialGroup()
      .addGap(x)
      .addComponent(component, d.height, d.height, d.height)
    );
  }

  public void add(Component component, int x, int width, int height) {
    hGroup.addGroup(layout.createSequentialGroup()
      .addGap(x)
      .addComponent(component, width, width, width)
    );

    vGroup.addGroup(layout.createSequentialGroup()
      .addGap(x)
      .addComponent(component, height, height, height)
    );
  }

  public void add(Component component, String location, Dimension d) {
    if (location.equals(CENTERING)) {
      int x = CENTER_X - d.width/2;
      int y = CENTER_Y - d.height/2;

      add(component, x, y, d);
    }
  }

  public void add(Component component, String location, int width, int height) {
    if (location.equals(CENTERING)) {
      int x = CENTER_X - width/2;
      int y = CENTER_Y - height/2;

      add(component, x, y, width, height);
    }
  }

  public static void main(String args[]) {
      try {
          for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
              if ("".equals(info.getName())) {
                  javax.swing.UIManager.setLookAndFeel(info.getClassName());
                  break;
              }
          }
      } catch (ClassNotFoundException ex) {
          java.util.logging.Logger.getLogger(Window.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
      } catch (InstantiationException ex) {
          java.util.logging.Logger.getLogger(Window.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
      } catch (IllegalAccessException ex) {
          java.util.logging.Logger.getLogger(Window.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
      } catch (javax.swing.UnsupportedLookAndFeelException ex) {
          java.util.logging.Logger.getLogger(Window.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
      }

      java.awt.EventQueue.invokeLater(() -> {
          new Window().setVisible(true);
      });
    }

}
