package com.piday.tool.data.transfer.clustermysql.ClusterToMsql;

import com.piday.tool.common.factory.spark.ISparkInstance;
import com.piday.tool.common.factory.spark.SparkFactory;
import com.piday.tool.data.common.interfaces.IConf;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.SaveMode;


public class Client {

    private IConf iConf;

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
        Dataset rows = iSparkInstance.getSqlContext().sql("select * from "+iConf.getClusterTable());
        rows.write().mode(SaveMode.Overwrite).jdbc(iConf.getDBUrl(), iConf.getDBTable(), iConf.getProperties());
    }
}
