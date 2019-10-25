package com.piday.tool.data.transfer.clusterlocal.localToCluster;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class SqlProduce {

    public static String table = "##table##";
    public static String defineMark = "##define##";
    public static String splitMark = "##split##";

    public static String handleType_override = "override";
    public static String createTableSql(String tableName, String hanleType, String split, Map<String,String> define){
        String sql = "create table ##table##(##define##)row FORMAT DELIMITED FIELDS TERMINATED BY '##split##' STORED AS TextFile";
        List<String> defineList = new ArrayList<>();
        for(String key:define.keySet()){
            defineList.add(key+" "+define.get(key));
        }
        String defines = String.join(",",defineList);
        sql = sql.replace(table,tableName);
        sql = sql.replace(defineMark,defines);
        sql = sql.replace(splitMark,split);
        return sql;
    }

    public static String createTableSql(String tableName, Map<String,String> define){
        return createTableSql(tableName,handleType_override,SchemaInitial.defult_split,define);
    }

    public static String loadDataIntoTable(String bodyFile,String tableName){
        String sql = "LOAD DATA LOCAL INPATH '"+bodyFile+"' INTO TABLE "+tableName+"";
        return sql;
    }

    public static String dropTable(String tableName){
        return "drop table if exists "+ tableName;
    }

    public static String createTableSql(String tableName, List<HeaderInfo> define){
        String sql = "create table ##table##(##define##)row FORMAT DELIMITED FIELDS TERMINATED BY '##split##' STORED AS TextFile";
        List<String> defineList = new ArrayList<>();
        for(HeaderInfo headerInfo:define){
            defineList.add(headerInfo.getColumnName()+" "+headerInfo.getFieldType()+" comment '"+headerInfo.getComments()+"'");
        }
        String defines = String.join(",",defineList);
        sql = sql.replace(table,tableName);
        sql = sql.replace(defineMark,defines);
        sql = sql.replace(splitMark,",");
        return sql;
    }

}
