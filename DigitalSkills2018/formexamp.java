import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


public class Calc {
    private JPanel panelka;
    private JButton minusButton;
    private JButton plusButton;
    private JTextField textField1;
    private JTextField textField2;
    private JTextField textField3;

    public static boolean isNumeric(String str)
    {
        return str.matches("-?\\d+(\\.\\d+)?");  //match a number with optional '-' and decimal.
    }

    public Calc(){
        minusButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String in1 = textField1.getText();
                String in2 = textField2.getText();
                if (!isNumeric(in1)){
                    textField3.setText("Change first number");
                    return;
                }
                if (!isNumeric(in2)){
                    textField3.setText("Change second number");
                    return;
                }

                int ch1 = Integer.parseInt(in1);
                int ch2 = Integer.parseInt(in2);

                int ch3 = ch1 - ch2;

                StringBuilder sb = new StringBuilder();
                sb.append("");
                sb.append(ch3);

                String fka = sb.toString();

                textField3.setText(fka);

            }
        });
        plusButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String in1 = textField1.getText();
                String in2 = textField2.getText();
                if (!isNumeric(in1)){
                    textField3.setText("Change first number");
                    return;
                }
                if (!isNumeric(in2)){
                    textField3.setText("Change second number");
                    return;
                }

                int ch1 = Integer.parseInt(in1);
                int ch2 = Integer.parseInt(in2);

                int ch3 = ch1 + ch2;

                StringBuilder sb = new StringBuilder();
                sb.append("");
                sb.append(ch3);

                String fka = sb.toString();

                textField3.setText(fka);
            }
        });
    }

    public static void main(String[] args){
        JFrame frame = new JFrame("Calc");
        frame.setContentPane(new Calc().panelka);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }
}
