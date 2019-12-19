<template>
  <el-container style="height: 968px; border: 1px solid #eee">
    <el-aside width="200px" style="background-color: rgb(238, 241, 246);text-align: left">
      <el-menu
        :default-openeds="open_list"
        :router="true"
        class="el-menu-vertical-demo"
        background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
        <el-submenu index="1">
          <template slot="title"><i class="el-icon-document-checked"></i>代码仓库</template>
            <el-menu-item index="data" >检查上传</el-menu-item>
            <el-menu-item index="analysis">分析检测</el-menu-item>
            <el-menu-item index="1-3">问题反馈</el-menu-item>
        </el-submenu>
        <el-submenu index="2">
          <template slot="title"><i class="el-icon-coffee-cup"></i>质量分析</template>
            <el-menu-item index="2-1">选项2-1</el-menu-item>
        </el-submenu>
        <el-submenu index="3">
          <template slot="title"><i class="el-icon-setting"></i>功能设置</template>
            <el-menu-item index="3-1">选项3-1</el-menu-item>
        </el-submenu>
      </el-menu>
    </el-aside>

    <el-container>
      <el-header style="text-align: right">
        <el-button class="el-icon-user"  type="primary" style="margin-right: 15px;size: 20px">用户</el-button>
      </el-header>
      <el-main>
        <router-link to="/Data">DateTest</router-link>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
    data() {
        return {
            open_list: ['1', '2'],
        }
    },
    methods: {
        getData() {
            this.$http.get('api/code').then((res)=>{
                console.log("test")
            });
            console.log("lll")
        },
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .el-header {
    background-color: #409eff;
    color: #333;
    line-height: 60px;
  }

  .el-aside {
    color: #333;
  }
</style>
