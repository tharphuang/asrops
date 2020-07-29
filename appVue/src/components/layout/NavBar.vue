<template>
  <section class="nav-bar">
    <div>
      <el-menu
        :default-openeds="open_list"
        :router="true"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b">
        <el-submenu index="1">
          <template slot="title"><i class="el-icon-document-checked"></i><span>文件仓库</span></template>
          <el-menu-item index="codehub">上传识别</el-menu-item>
          <el-menu-item index="analysis">结果检测</el-menu-item>
          <el-menu-item index="1-3">结果分析</el-menu-item>
        </el-submenu>
        <el-submenu index="2">
          <template slot="title"><i class="el-icon-coffee-cup"></i>质量分析</template>
          <el-menu-item index="2-1">选项2-1</el-menu-item>
        </el-submenu>
        <el-submenu index="3">
          <template slot="title"><i class="el-icon-coin"></i>发布模型</template>
          <el-menu-item index="coderelease">模型版本</el-menu-item>
        </el-submenu>
        <el-submenu index="4">
          <template slot="title"><i class="el-icon-setting"></i>功能设置</template>
          <el-menu-item index="4-1">选项4-1</el-menu-item>
        </el-submenu>
      </el-menu>
    </div>
  </section>
</template>

<script>
    export default {
        name: "NavBar",
        data(){
          return{
               open_list: ['1'],
          }
        },
    }
</script>

<style scoped>
  .nav-bar{
    left: 0px;
    width: 175px;
    height: 100%;
    position: absolute;
    background-color: #545c64;
    text-align: left
  }

</style>
