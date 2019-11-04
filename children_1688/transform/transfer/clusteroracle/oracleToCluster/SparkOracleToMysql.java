package com.piday.tool.data.transfer.clusteroracle.oracleToCluster;

import com.piday.tool.common.old.classes.spark.SparkContextLoaderLocalConfig;
import com.piday.tool.data.common.JDBCConstant;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.SQLContext;
import org.apache.spark.sql.SaveMode;
import org.apache.spark.sql.jdbc.JdbcDialect;
import org.apache.spark.sql.jdbc.JdbcDialects;
import org.apache.spark.sql.jdbc.JdbcType;
import org.apache.spark.sql.types.DataType;
import org.apache.spark.sql.types.DataTypes;
import org.apache.spark.sql.types.MetadataBuilder;
import scala.Option;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

/**
 * <h1> spark oracle to mysql</h1>
 * Move com.piday.tool.data from oracle database to mysql database
 * 将数据从oracle数据库中迁移到mysql数据库中
 *
 * @version 0.0.1
 */
public class SparkOracleToMysql {
    //Oracle
    private final String ORACLE_URL = "jdbc:oracle:thin:@10.172.116.147:1521:ORCL";
    private final String ORACLE_USER_NAME = "HMISW_10";
    private final String ORACLE_PASSWORD = "H13584";
    //mysql
    private final String MYSQL_USER_NAME = "root";
    private final String MYSQL_PASSWORD = "pidayOffice";
    private final String MYSQL_DATABASE = "hospital";
    private final String MYSQL_DRIVER = "com.mysql.jdbc.Driver";
    private final String MYSQL_ADDRESS = "127.0.0.1";
    private final String MYSQL_PORT = "3306";
    //spark
    private final String SPARK_MASTER = "spark://192.168.1.103:7077";

    private List<String> tableNames = new ArrayList<>();

    /**
     * Get table names from oracle database
     * 从oracle数据库中获取所有表名
     */
    public void getTableNames() {
        String driver = "oracle.jdbc.OracleDriver";
        Connection con = null;
        PreparedStatement pstm = null;
        ResultSet rs = null;
        try {
            Class.forName(driver);
            con = DriverManager.getConnection(ORACLE_URL, ORACLE_USER_NAME, ORACLE_PASSWORD);
            String sql = "select TABLE_NAME as TABLE_NAME from tabs";
            pstm = con.prepareStatement(sql);
            rs = pstm.executeQuery();
            while (rs.next()) {
                String str = rs.getString("TABLE_NAME");
                tableNames.add(str);
            }
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        } finally {
            try {
                con.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }

    /**
     * 将数据从oracle数据库迁移到mysql数据库
     */
    public void oracleToMysql() {
        SparkContextLoaderLocalConfig loader = SparkContextLoaderLocalConfig.getInstance(SPARK_MASTER
                , "Oracle to Mysql");
        SQLContext sqlContext = loader.getSqlContext();
        // register all the functions that will be used
        this.fangyan();
        sqlContext.setConf("spark.sql.tungsten.enabled", "true");

        Properties oracleProps = new Properties();
        oracleProps.put("user", ORACLE_USER_NAME);
        oracleProps.put("password", ORACLE_PASSWORD);

        Properties prop = new Properties();
        prop.setProperty(JDBCConstant.DRIVER, MYSQL_DRIVER);
        String mysqlUrl = String.format(JDBCConstant.MYSQL_URL, new String[]{MYSQL_ADDRESS, MYSQL_PORT, MYSQL_DATABASE});
        prop.setProperty(JDBCConstant.USER, MYSQL_USER_NAME);
        prop.setProperty(JDBCConstant.PASSWORD, MYSQL_PASSWORD);

        for (String tableName : tableNames) {
            System.out.println("Begin with table " + tableName);
            Dataset rows = sqlContext.read().jdbc(ORACLE_URL, tableName, oracleProps);
            rows.write().mode(SaveMode.Overwrite).jdbc(mysqlUrl, ORACLE_USER_NAME + '_' + tableName, prop);
            System.out.println("Successfully created table " + tableName);
        }
    }

    /**
     * 方言：在读写oracle数据库时进行相应转化
     */
    private void fangyan() {
        JdbcDialect dialect = new JdbcDialect() {

            //判断是否为oracle库
            @Override
            public boolean canHandle(String url) {
                return url.startsWith("jdbc:oracle");
            }

            //用于读取Oracle数据库时数据类型的转换
            @Override
            public Option<DataType> getCatalystType(int sqlType, String typeName, int size, MetadataBuilder md) {
                if (sqlType == Types.DATE || typeName.equals("DATE")) {
                    return Option.apply(DataTypes.StringType);
                } else if (sqlType == Types.LONGVARCHAR || typeName.equals("LONG")) {
                    return Option.apply(DataTypes.StringType);
                }
                return Option.empty();
            }

            //用于写Oracle数据库时数据类型的转换
            @Override
            public Option<JdbcType> getJDBCType(DataType dt) {
                if (DataTypes.StringType.sameType(dt)) {
                    return Option.apply(
                            new JdbcType("VARCHAR(255)", Types.VARCHAR));
                } else if (DataTypes.BooleanType.sameType(dt)) {
                    return Option.apply(
                            new JdbcType("NUMBER(1)", Types.NUMERIC));
                } else if (DataTypes.IntegerType.sameType(dt)) {
                    return Option.apply(
                            new JdbcType("NUMBER(10)", Types.NUMERIC));
                } else if (DataTypes.LongType.sameType(dt)) {
                    return Option.apply(
                            new JdbcType("NUMBER(19)", Types.NUMERIC));
                } else if (DataTypes.DoubleType.sameType(dt)) {
                    return Option.apply(
                            new JdbcType("NUMBER(19,4)", Types.NUMERIC));
                } else if (DataTypes.FloatType.sameType(dt)) {
                    return Option.apply(
                            new JdbcType("NUMBER(19,4)", Types.NUMERIC));
                } else if (DataTypes.ShortType.sameType(dt)) {
                    return Option.apply(
                            new JdbcType("NUMBER(5)", Types.NUMERIC));
                } else if (DataTypes.ByteType.sameType(dt)) {
                    return Option.apply(
                            new JdbcType("NUMBER(3)", Types.NUMERIC));
                } else if (DataTypes.BinaryType.sameType(dt)) {
                    return Option.apply(
                            new JdbcType("BLOB", Types.BLOB));
                } else if (DataTypes.TimestampType.sameType(dt)) {
                    return Option.apply(
                            new JdbcType("VARCHAR(24)", Types.VARCHAR));
                } else if (DataTypes.DateType.sameType(dt)) {
                    return Option.apply(
                            new JdbcType("VARCHAR(24)", Types.VARCHAR));
                } else if (DataTypes.createDecimalType()
                        .sameType(dt)) { //unlimited
/*                    return DecimalType.Fixed(precision, scale)
                            =>Some(JdbcType("NUMBER(" + precision + "," + scale + ")",
                            java.sql.Types.NUMERIC))*/
                    return Option.apply(
                            new JdbcType("NUMBER(38,4)", Types.NUMERIC));
                }
                return Option.empty();
            }
        };
        //注册此方言
        JdbcDialects.registerDialect(dialect);
    }

    public static void main(String[] args) {
        SparkOracleToMysql sotm = new SparkOracleToMysql();
        sotm.fangyan();
        sotm.getTableNames();
        sotm.oracleToMysql();
    }
}