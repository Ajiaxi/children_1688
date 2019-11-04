package com.piday.tool.data.transfer.clusterlocal.localToCluster;

import java.io.*;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

//解析表头信息
public class SchemaInitial {
    public static String defult_split = ",";
    public static String defult_type = "horizon";

    public static Map<String, String> getHeaderMap(String headerFile) {
        return getHeaderMap(headerFile,defult_split);
    }

    public static Map<String, String> getHeaderMap(String headerFile, String split) {
        return getHeaderMap(new File(headerFile),defult_split,defult_type);
    }

    public static Map<String, String> getHeaderMap(File headerFile, String split, String type) {
        Map<String, String> map = new LinkedHashMap<>();
        try {
            if (type.equals(defult_type)) {
                BufferedReader bufferedReader = new BufferedReader(new FileReader(headerFile));
                String line = "";
                while((line = bufferedReader.readLine())!=null){
                    String key = line.split(split)[0];
                    String value = line.split(split)[1];
                    map.put(key,value);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return map;
    }


    public static List<HeaderInfo> getHeaderInfoList(String headerFile) {
        List<HeaderInfo> headerInfos = new ArrayList<>();
        try {
                BufferedReader bufferedReader = new BufferedReader(new FileReader(headerFile));
                String line = "";
                while((line = bufferedReader.readLine())!=null) {
                    HeaderInfo headerInfo = new HeaderInfo();
                    headerInfo.setColumnName(line.split(",")[0]);
                    headerInfo.setFieldType(line.split(",")[1]);
                    headerInfo.setComments(line.split(",")[2]);
                    headerInfos.add(headerInfo);
                }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return headerInfos;
    }


}
