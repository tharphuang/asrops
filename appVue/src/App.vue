<template>
  <el-container>
    <NavBar></NavBar>
    <AppMain></AppMain>
  </el-container>
</template>

<script>
    import {NavBar,AppMain} from "./components/layout/";
    export default {
        components: {AppMain, NavBar},
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .el-aside {
    color: #333;
  }
</style>
