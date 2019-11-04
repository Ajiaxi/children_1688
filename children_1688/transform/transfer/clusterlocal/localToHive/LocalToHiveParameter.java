package com.piday.tool.data.transfer.clusterlocal.localToHive;

import java.io.File;
import java.io.FilenameFilter;
import java.util.LinkedHashMap;
import java.util.Map;

/***
 * 可以简单的把本地的数据载入hive数据库
 * */
public class LocalToHiveParameter {

    /**
     * 之后处理的表　全部载入这个数据库下
     */
    public static final String db = "zhili";

    /**
     * 本次处理的本地的所有数据的逻辑根目录
     */
//    public static final String localBoot = "C:\\data\\织里\\むし\\zhili\\gov";
    public static final String localBoot = "/home/chenhang/zhili/craw";

    /**
     * 本次处理的数据需要载入hdfs的位置的根目录，可以保证本地根目录下的所有物理路径与hdfs上的物理路径一致
     */
//    public static final String hdfsBoot = "/user/piday/zhili/gov";
    public static final String hdfsBoot = "/user/piday/zhili/craw";

    /**
     * 本次处理的数据的表头信息文件名字，和数据本身放在同一个路径下
     * <p>
     * 当操作上传到hdfs路径上时候，会自动过滤
     * 当操作要使用header.csv创建sql语句时也会进行自动捕捉，过滤处理
     */
    public static final String header = "header.csv";
    public static final String txtHeader = "header.txt";
    /**
     * 自定义的文件过
     */
    public static final FilenameFilter headerFilter = (a, name) -> a.isFile()&&(header.equals(name) || (txtHeader.equals(name)));

    /**
     * 特别指定某个路径下的数据分隔符为　××
     */
    public static final Map<String, String> splitor = new LinkedHashMap() {
        {
//            put("C:\\data\\织里\\むし\\zhili\\craw\\raw\\alirank\\sale_7", ",");
//            put("C:\\data\\织里\\むし\\zhili\\craw\\raw\\alirank\\sale_30", ",");
//            put("C:\\data\\织里\\むし\\zhili\\craw\\raw\\alirank\\search_7", ",");
//            put("C:\\data\\织里\\むし\\zhili\\craw\\raw\\alirank\\search_30", ",");
//            put("C:\\data\\织里\\むし\\zhili\\craw\\raw\\attributes\\base", ",");
//            put("C:\\data\\织里\\むし\\zhili\\craw\\raw\\attributes\\market", ",");
//            put("C:\\data\\织里\\むし\\zhili\\craw\\raw\\attributes\\price", ",");
//            put("C:\\data\\织里\\むし\\zhili\\craw\\raw\\hydp\\cg\\index\\all", ",");
//            put("C:\\data\\织里\\むし\\zhili\\craw\\raw\\hydp\\cg\\index\\sub", ",");
//            put("C:\\data\\织里\\むし\\zhili\\craw\\raw\\hydp\\cg\\rq", ",");
//            put("C:\\data\\织里\\むし\\zhili\\craw\\raw\\hydp\\gy\\index\\all", ",");
//            put("C:\\data\\织里\\むし\\zhili\\craw\\raw\\hydp\\gy\\index\\sub", ",");
//            put("C:\\data\\织里\\むし\\zhili\\craw\\raw\\hydp\\gy\\rq", ",");
//            put("C:\\data\\织里\\むし\\zhili\\craw\\raw\\purchase\\identify", ",");
        }
    };
}
