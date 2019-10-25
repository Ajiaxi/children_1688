package com.piday.tool.data.transfer.clusterlocal.localToCluster.frame;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;

public class JGUI extends JFrame implements ActionListener {
    public void initial(){
        this.setSize(500,500);
        this.setLocation(500,300);
        this.setLayout(new FlowLayout(FlowLayout.CENTER,10,0));

        JPanel jPanel1 = new JPanel();
        jPanel1.add(new JLabel("选取body文件"));
        jPanel1.add(new JTextField(30));
        jPanel1.add(new JButton("选取"));

        JPanel jPanel2 = new JPanel();
        jPanel2.add(new JLabel("选取head文件"));
        jPanel2.add(new JTextField(30));
        jPanel2.add(new JButton("选取"));

        JPanel jPanel3 = new JPanel();
        jPanel3.add(new JLabel(" 填 入 表 名 "));
        jPanel3.add(new JTextField(30));
        jPanel3.add(new JButton("摆设"));

        this.add(jPanel1);
        this.add(jPanel2);
        this.add(jPanel3);
        this.setVisible(true);
    }

    public static void main(String[] args) {
        JGUI jgui = new JGUI();
        jgui.initial();

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        JFileChooser chooser = new JFileChooser();
            chooser.setFileSelectionMode(0);
//打开文件浏览器，点击取消则返回1
            int status = chooser.showOpenDialog(null);
            if(status == 1){
                return;
            }else{
                File file = chooser.getSelectedFile();
                //jt1_1.setText(file.getAbsolutePath());
            }
        }

}
