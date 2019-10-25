package com.piday.tool.data.transfer.clusterlocal.localToHive;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class HdfsToHiveUtil {


    public static List<File> praserToFileList(FilenameFilter headerFilter, String localBoot) {
        List<File> fileList = new ArrayList<>();
        if(new File(localBoot).isDirectory()){
            for(File subPath : new File(localBoot).listFiles()){
                List<File> sub = praserToFileList(headerFilter,subPath.getAbsolutePath());
                fileList.addAll(sub);
            }
        }else{
            if(headerFilter.accept(new File(localBoot),new File(localBoot).getName())){
                fileList.add(new File(localBoot));
            }
        }
        return fileList;
    }

    public static List<TableDefinition> praserHeaderList(List<File> headerList) {
        List<TableDefinition> tableDefinitionList = new ArrayList<>();
        for(File file : headerList){
            tableDefinitionList.add(praserFileToTableDefinition(file));
        }
        return tableDefinitionList;
    }

    private static TableDefinition praserFileToTableDefinition(File file) {
        TableDefinition tableDefinition = new TableDefinition();

        String db = LocalToHiveParameter.db;
        String tableName = file.getParent().replace(LocalToHiveParameter.localBoot+File.separator,"").replace(File.separator,"_");
        List<ColumnDefinition> columnDefinitions = getColumnDefinitionList(file);
        String location = LocalToHiveParameter.hdfsBoot+"/"+file.getParent()
                .replace(LocalToHiveParameter.localBoot+File.separator,"")
                .replace(File.separator,"/");
        String absolutePath = file.getAbsolutePath();
        String absoluteParentPath = file.getParent();
        //赋值特殊的分割符号
        if(LocalToHiveParameter.splitor.containsKey(absoluteParentPath)){
            tableDefinition.setSplitor(LocalToHiveParameter.splitor.get(absoluteParentPath));
        }
        tableDefinition.setAbsolutePath(absolutePath);
        tableDefinition.setAbsoluteParentPath(absoluteParentPath);//父路径
        tableDefinition.setLocation(location);
        tableDefinition.setDb(db);
        tableDefinition.setTableName(tableName);
        tableDefinition.setColumnDefinitions(columnDefinitions);
        return tableDefinition;
    }

    private static List<ColumnDefinition> getColumnDefinitionList(File file) {
        List<ColumnDefinition> columnDefinitions = new ArrayList<>();
        String line = null;
        try {
            BufferedReader bufferedReader = new BufferedReader(new FileReader(file));
            while((line = bufferedReader.readLine())!= null){
                String[]s = line.split(",");
                columnDefinitions.add(new ColumnDefinition(s[0],s[1],s[2]));
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return columnDefinitions;
    }

    /**
     * 将TableDefinition解释成为可执行sql
     * */
    public static void explainTableDefinition(List<TableDefinition> tableDefinitionList) {
        for(TableDefinition tableDefinition : tableDefinitionList){
            tableDefinition.setDropSql(getDropSqlFromTableDefinition(tableDefinition));
            tableDefinition.setCreateSql(getCreateSqlFromTableDefinition(tableDefinition).replace("\uFEFF", ""));
        }
    }

    private static String getCreateSqlFromTableDefinition(TableDefinition tableDefinition) {
        StringBuffer sb = new StringBuffer();
        sb.append("CREATE EXTERNAL TABLE "+tableDefinition.getFullTable()+" (\n");
        List<ColumnDefinition> columnDefinitions = tableDefinition.getColumnDefinitions();
        for(int i = 0;i<columnDefinitions.size();i++){
            if(i == columnDefinitions.size()-1){
                sb.append(columnDefinitions.get(i)+"\n");
            }else{
                sb.append(columnDefinitions.get(i)+",\n");
            }
        }
        sb.append(")\n");
        sb.append("ROW FORMAT DELIMITED FIELDS TERMINATED BY '"+tableDefinition.getSplitor()+"' \n");
        sb.append("LINES TERMINATED BY '\\n'\n" );
        sb.append("LOCATION '"+tableDefinition.getLocation()+"'\n");
        sb.append("TBLPROPERTIES(\"skip.header.line.count\"=\"1\")\n");
        return sb.toString();
    }

    private static String getDropSqlFromTableDefinition(TableDefinition tableDefinition) {
        String dropSql = String.format("drop table if exists %s.%s",new String[]{tableDefinition.getDb(),tableDefinition.getTableName()});
        return dropSql;
    }
}
