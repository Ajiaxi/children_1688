package com.piday.tool.data.transfer.clusterlocal.localToHdfs;

import workspace.xiyao.windows.ConnectHadoopPrepare;

import java.io.File;
import java.io.FilenameFilter;
import java.util.Map;
import java.util.HashMap;

/**
 * 操作执行器
 * 将本地的数据传输到hdfs的指定的位置上
 */
public class Executor {

//    public static final String localBoot = "C:\\data\\织里\\むし\\zhili\\gov";
    public static final String localBoot = "/home/chenhang/zhili/craw";
    public static final String hdfsBoot = "/user/piday/zhili/craw";
    public static final String header = "header.csv";
    public static final FilenameFilter headerFilter = new FilenameFilter() {
        @Override
        public boolean accept(File dir, String name) {
            return !("header.csv".equals(name) || ("header.txt".equals(name)));
        }
    };

    public static void transferToHdfs(File localPath) {
        if (localPath.isDirectory()) {
            for (File subPath : localPath.listFiles(headerFilter)) {
                //子目录继续递归操作
                transferToHdfs(subPath);
            }
        } else {
            //
            if (!localPath.getName().equals(header)) {
                //当　当前目录不是文件夹的时候，将执行上传到hdfs的操作
                String absoluteLocalPath = localPath.getAbsolutePath();
                String hdfsPath = hdfsBoot + absoluteLocalPath.replace(localBoot, "");
                String hdfsPathDir = hdfsPath.substring(0, hdfsPath.lastIndexOf("/"));
                HdfsUtil.checkAndCreateAutomatic(hdfsPathDir);
                HdfsUtil.uploadFileFromLocalFileToHdfs(absoluteLocalPath, hdfsPath);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        if (ConnectHadoopPrepare.isWindows()) {
            ConnectHadoopPrepare.loadHadoopPrepareFile();
        }
        transferToHdfs(new File(localBoot));
    }
}
