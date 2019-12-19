<template>
  <section class="app-main">
    <el-container>
      <el-header class="el-header" >
        <el-dropdown >
          <span style="color: white;font-size: 20px"><i class="el-icon-user"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>账号</el-dropdown-item>
            <el-dropdown-item>设置</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </el-header>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </section>
</template>

<script>
    export default {
        name: "AppMain"
    }
</script>

<style scoped>
  .app-main {
    left: 175px;
    width: calc(100% - 175px);
    height: 100%;
    position: absolute;
    background-color: #f9f9f9;
  }
  .el-header {
    background-color: #409eff;
    color: #333;
    line-height: 60px;
    text-align: right;
  }

</style>
