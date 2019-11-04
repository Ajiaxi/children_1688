package com.piday.tool.data.transfer.clustermysql;

import com.piday.tool.data.common.interfaces.*;

import java.util.Properties;

public class IconfAdapter implements IConf {

    protected String MYSQL_URL = "jdbc:mysql://192.168.1.103:3306/csm?useSSL=false&character_set_client=utf8&character_set_connection=utf8&serverTimezone=Asia/Shanghai";

    protected  String master = "spark://192.168.1.103:7077";
    protected  String app = "aa";

    protected  String user = "piday";
    protected  String password = "pidayOffice";
    //需要进行迁移的表
    protected  String dbTable = "logsticTest";
    protected  String clusterTable = "test.logsticTest";
    protected String[] jars = new String[] {"/home/zifang/workplace/idea_workplace/pidaytool/src/main/resources/mysql-connector-java-5.1.40.jar"};

    @Override
    public Properties getProperties(){
        Properties props = new Properties();
        props.put("user", getUser());
        props.put("password", getPassword());
        return props;
    }

    @Override
    public String getUser() {
        return user;
    }

    @Override
    public String getPassword() {
        return password;
    }

    @Override
    public String getDBUrl() {
        return MYSQL_URL;
    }

    @Override
    public String getApp() {
        return app;
    }

    @Override
    public String getMaster() {
        return master;
    }

    @Override
    public String getClusterTable() {
        return clusterTable;
    }

    @Override
    public String getDBTable() {
        return dbTable;
    }

    @Override
    public String[] getJars() {
        return jars;
    }
}
