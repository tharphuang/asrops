<template>
<div>
  <el-card class="box-card">
    <div slot="header">
      <span>软件发布版本</span>
    </div>
    <el-table :data="tableData" style="width: 100%">
      <el-table-column
      prop="date"
      label="日期">
      </el-table-column>
      <el-table-column
      prop="name"
      label="姓名">
      </el-table-column>
    </el-table>
  </el-card>
</div>
</template>

<script>
    export default {
        name: "version",
        data() {
            return{
                tableData: [{
                    date: '2012',
                    name: '测试一'
                },{
                    date: '2013',
                    name: '测试二'
                }]
            }
        }
    }
</script>

<style scoped>
  .box-card{
    width: 100%;
    height: 720px;
  }
</style>
