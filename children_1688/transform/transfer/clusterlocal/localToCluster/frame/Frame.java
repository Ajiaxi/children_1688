package com.piday.tool.data.transfer.clusterlocal.localToCluster.frame;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;

public class Frame extends JFrame implements ActionListener {

    //窗口
    JFrame jf = new JFrame("本地文件直接插入大数据平台");
    //画板
    JPanel jp = new JPanel();
    //布局卡选项
    JTabbedPane tabPane=new JTabbedPane();
    //布局1
    Container con=new Container();

    //标签
    JLabel jl1_1 = new JLabel("选择body文件");
    JLabel jl1_2 = new JLabel("选择header文件");

    JLabel jl2 = new JLabel("填入表名");
    //按钮
    JButton jb1_1 = new JButton("打开");
    JButton jb1_2 = new JButton("打开");
    JButton jb4 = new JButton("启动程序");
    //文本
    JTextArea jt1_1 = new JTextArea();
    JTextArea jt1_2 = new JTextArea();
    //文件选择器
    JFileChooser chooser = new JFileChooser();

    public Frame(){
//将画板加到窗口上
        jf.add(jp);
//布局，将布局卡加到面板上
        jf.setContentPane(tabPane);
//设置标签，按钮，文本框的位置及大小，x,y,width,height
        jl1_1.setBounds(20,50, 100, 20);
        jb1_1.setBounds(640,20,50,20);
        jt1_1.setBounds(120,20,500,20);

        jl1_2.setBounds(20,50, 100, 20);
        jt1_2.setBounds(120,50,500,20);
        jb1_2.setBounds(640,50,50,20);

        jb4.setBounds(300,140,100,30);
//设置按钮事件处理   this代表本身这个对象，意思是监听这个对象，所里该类必须实现ActionListener
        jb1_1.addActionListener(this);
        jb1_2.addActionListener(this);
        jb4.addActionListener(this);
//将按钮加到布局1上
        con.add(jt1_1);
        con.add(jb1_1);
        con.add(jl1_2);
        con.add(jt1_2);
        con.add(jb1_2);
        con.add(jb4);
//将布局加到布局卡内，并设置该布局的名称
        tabPane.add("写入数据库",con);
//设置窗口属性---------------------
//窗口可见
        jf.setVisible(true);
//窗口大小
        jf.setSize(800, 400);
//关闭窗口时关闭程序
        jf.setDefaultCloseOperation(EXIT_ON_CLOSE);
//设置窗口位置
        jf.setLocation(400, 150);
    }


    public static void main(String[] args) {
//创建该对象则调用构造方法，对象实现ActionListener则自动调用actionPerformed（）方法
        Frame f = new Frame();
    }



    //事件处理，所有事件处理必须写在该方法，该方法重写自ActionListener
    @Override
    public void actionPerformed(ActionEvent e) {
//点击按钮后，判断是哪一个按钮
        if(e.getSource() == jb1_1){
//设置文件选择器只能选择0（文件），1（文件夹）
            chooser.setFileSelectionMode(0);
//打开文件浏览器，点击取消则返回1
            int status = chooser.showOpenDialog(null);
            if(status == 1){
                return;
            }else{
//读取选择器选择到的文件
                File file = chooser.getSelectedFile();
//获取文件绝对路径并写入到文本框内
                jt1_1.setText(file.getAbsolutePath());
            }
        }
        if(e.getSource() == jb1_2){
            chooser.setFileSelectionMode(0);
            int status = chooser.showOpenDialog(null);
            if(status == 1){
                return;
            }else{
                File file = chooser.getSelectedFile();
                jt1_2.setText(file.getAbsolutePath());
            }
        }

//        if(e.getSource() == jb4){
//            Main m = new Main();
//            try {
//                m.start();
//            } catch (Exception e1) {
////准备添加错误日志报告写入文件
//                e1.printStackTrace();
//            }
//        }
    }
}
