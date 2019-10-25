package com.piday.tool.data.transfer.clusterlocal.localToHdfs;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

public class HdfsUtil {

    // HDFS_PATH 很重要！是访问连接HDFS的关键
    private static final String HDFS_PATH = "hdfs://192.168.1.103:9000";
    // 必需的FileSystem类
    private static FileSystem fileSystem = null;
    // 配置对象
    private static Configuration configuration = null;

    static{
        configuration = new Configuration();
        // 获取一个fileSystem对象，这就相当于建立连接了
        try {
            fileSystem = FileSystem.get(new URI(HDFS_PATH),configuration,"piday");
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (URISyntaxException e) {
            e.printStackTrace();
        }
    }

    public static boolean isExistPath(String filePath){
        try {
            //return fileSystem.
            return fileSystem.exists(new Path(filePath));
            //return fileSystem.isDirectory(new Path(filePath));
        } catch (IOException e) {
            e.printStackTrace();
        }
        return false;
    }

    public static boolean isDir(String filePath){
        try {
            return fileSystem.isDirectory(new Path(filePath));
            //return fileSystem.isDirectory(new Path(filePath));
        } catch (IOException e) {
            e.printStackTrace();
        }
        return false;
    }

    public static void checkAndCreateAutomatic(String filePath){
        if(!isDir(filePath)){
            try {
                fileSystem.mkdirs(new Path(filePath));
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public static void uploadFileFromLocalFileToHdfs(String localPath, String hdfsPath) {
        try {
            fileSystem.copyFromLocalFile(new Path(localPath),new Path(hdfsPath));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void pullFileFromHdfs(String localPath,String hdfsPath) {
        try {
            fileSystem.copyToLocalFile(new Path(hdfsPath), new Path(localPath));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        checkAndCreateAutomatic("/user/piday/zhili/craw/raw/alisupply");
        checkAndCreateAutomatic("/user/piday/zhili/craw/raw");
    }
}
