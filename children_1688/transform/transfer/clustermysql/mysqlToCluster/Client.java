package com.piday.tool.data.transfer.clustermysql.mysqlToCluster;

import com.piday.tool.common.factory.spark.ISparkInstance;
import com.piday.tool.common.factory.spark.SparkFactory;
import com.piday.tool.common.util.SparkUtils;
import com.piday.tool.data.transfer.clustermysql.IconfAdapter;
import com.piday.tool.data.common.interfaces.IConf;
import org.apache.spark.sql.Dataset;

/**
 * 1. 所有的mysql相关的由conf类驱动
 * 2. 主体类不需要进行修改
 *
 * */
public class Client {

    private IConf iConf;
    private ISparkInstance iSparkInstance;
    private SparkUtils sparkUtils;

    public Client(IConf iConf){
        this.iConf = iConf;
    }

    /**
     * 使用构造器内的conf组件进行操作
     *
     * */
    public void execute(){
        execute(this.iConf);
    }

    /**
     * 使用外部传入的conf进行操作
     * */
    public static void execute(IConf iConf){
        //获取spark组件  为单例，因此在同一个for内反复操作是一样的效果
        ISparkInstance iSparkInstance = SparkFactory.getSparkDefaultInstant(iConf.getMaster(),iConf.getApp(), iConf.getJars());
        //spark辅助类
        SparkUtils sparkUtils = new SparkUtils(iSparkInstance);
        //读取数据
        Dataset rows = iSparkInstance.getSqlContext().read().jdbc(iConf.getDBUrl(), iConf.getDBTable(), iConf.getProperties());
        //辅助类将数据写入
        sparkUtils.insertIntoDatabase(rows,iConf.getClusterTable());
    }

    public static void main(String[] args) {
        Client.execute(new IconfAdapter());
    }
}
