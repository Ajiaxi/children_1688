package com.piday.tool.data.transfer.clusterlocal.localToHive;

public class ColumnDefinition {

    private String name ;
    private String type;
    private String description;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public ColumnDefinition(String name, String type, String description) {
        this.name = name;
        this.type = type;
        this.description = description;
    }

    @Override
    public String toString(){
        return name+" "+type+" comment "+"'"+description+"'";
    }
}
