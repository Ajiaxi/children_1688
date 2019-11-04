package com.piday.tool.data.transfer.clusterlocal.localToCluster;

import com.piday.tool.common.old.classes.spark.SparkContextLoaderLocalConfig;
import org.apache.spark.sql.SQLContext;

import java.util.List;

public class Client {
    public static void main(String[] args) {
        //配置，获得spark的执行单元
        SparkContextLoaderLocalConfig loader = SparkContextLoaderLocalConfig.getInstance("spark://192.168.1.103:7077","a");
        SQLContext sqlContext = loader.getSqlContext();

        //SQLContext sqlContext = SparkFactory.getSparkDefaultInstant("spark://192.168.1.103:7077","a").getSqlContext();


        String headerFile = "/home/zifang/data/fastfish/receipt/receipt_header.csv";//receipt.csv
        String bodyFile = "/home/zifang/data/fastfish/receipt/receipt.csv";
        String table = "fastfish.receipt";


        //包裹头信息，得到包含header信息的map
        List<HeaderInfo> header = SchemaInitial.getHeaderInfoList(headerFile);

        //获得相应的三个sql语句
        String createTable = SqlProduce.createTableSql(table,header);
        String load = SqlProduce.loadDataIntoTable(bodyFile,table);
        String dropTable = SqlProduce.dropTable(table);

        //执行三个语句
        sqlContext.sql(dropTable);
        sqlContext.sql(createTable);
        sqlContext.sql(load);

    }
}
