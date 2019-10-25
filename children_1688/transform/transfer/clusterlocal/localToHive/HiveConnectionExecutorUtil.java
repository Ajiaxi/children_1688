package com.piday.tool.data.transfer.clusterlocal.localToHive;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.List;

public class HiveConnectionExecutorUtil {
    private static Connection connection;

    public static void loadTableDefinition(List<TableDefinition> tableDefinitionList) {
        for(TableDefinition tableDefinition : tableDefinitionList){
            executeSingle(tableDefinition);
        }
    }

    private static void executeSingle(TableDefinition tableDefinition) {
        Connection connection = getConnection();
        try {
            Statement statement = connection.createStatement();
            statement.execute(tableDefinition.getDropSql());
            statement.execute(tableDefinition.getCreateSql());
        } catch (SQLException e) {
            e.printStackTrace();
        }

    }

    private static Connection getConnection() {
        try {
            Class.forName("org.apache.hive.jdbc.HiveDriver");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
            System.exit(1);
        }

        if(connection == null){
            try {
                connection = DriverManager.getConnection("jdbc:hive2://192.168.1.103:10000/zhili", "hive", "***!");
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
        return connection;
    }
}
