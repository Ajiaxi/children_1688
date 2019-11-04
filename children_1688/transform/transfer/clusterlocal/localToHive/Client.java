package com.piday.tool.data.transfer.clusterlocal.localToHive;

import workspace.xiyao.windows.ConnectHadoopPrepare;

import java.io.File;
import java.util.List;

public class Client {



    public static void main(String[] args) {

        //windows平台兼容
        if (ConnectHadoopPrepare.isWindows()) {
            ConnectHadoopPrepare.loadHadoopPrepareFile();
        }
        //解析某个文件夹下所有的文件，得到
        List<File> headerList = HdfsToHiveUtil.praserToFileList(LocalToHiveParameter.headerFilter, LocalToHiveParameter.localBoot);

        //将header文件转化为表结构定义
        List<TableDefinition> tableDefinitionList = HdfsToHiveUtil.praserHeaderList(headerList);

        //将所有的表结构定义转化为可以执行的sql,sql会插入TableDefinition内，成为一个字段
        HdfsToHiveUtil.explainTableDefinition(tableDefinitionList);

        //将解释完毕的TableDefinition，遍历执行
        HiveConnectionExecutorUtil.loadTableDefinition(tableDefinitionList);
    }
}
