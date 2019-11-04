package com.piday.tool.data.transfer.clusterlocal.localToHive;

import java.util.List;

public class TableDefinition {

    public String getSplitor() {
        return splitor;
    }

    public void setSplitor(String splitor) {
        this.splitor = splitor;
    }

    private String splitor = "\\t";

    public String getTableName() {
        return tableName;
    }

    public void setTableName(String tableName) {
        this.tableName = tableName;
    }

    public String getDb() {
        return db;
    }

    public void setDb(String db) {
        this.db = db;
    }

    public List<ColumnDefinition> getColumnDefinitions() {
        return columnDefinitions;
    }

    public void setColumnDefinitions(List<ColumnDefinition> columnDefinitions) {
        this.columnDefinitions = columnDefinitions;
    }

    private String tableName;
    private String db;
    private List<ColumnDefinition> columnDefinitions;

    private String dropSql;
    private String createSql;
    private String location;
    private String absolutePath;
    private String absoluteParentPath;

    public String getAbsolutePath() {
        return absolutePath;
    }

    public void setAbsolutePath(String absolutePath) {
        this.absolutePath = absolutePath;
    }

    public String getAbsoluteParentPath() {
        return absoluteParentPath;
    }

    public void setAbsoluteParentPath(String absoluteParentPath) {
        this.absoluteParentPath = absoluteParentPath;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public String getDropSql() {
        return dropSql;
    }

    public void setDropSql(String dropSql) {
        this.dropSql = dropSql;
    }

    public String getCreateSql() {
        return createSql;
    }

    public void setCreateSql(String createSql) {
        this.createSql = createSql;
    }

    public String getFullTable(){
        return db+"."+tableName;
    }
}
