<template>
  <div>
  <el-row>
      <el-upload
          :action='uploadApi'
          :multiple = false
          :on-remove="handleRemove"
          :on-change="handelChange"
          :on-success="getFileContent">
          <el-button size="small" type="success" style="margin-left: 20px">上传文件</el-button>
      </el-upload>
     <el-col :span="24" style="margin-top: 12px;background-color: white" >
       <el-steps :active="stepNumber" simple>
         <el-step title="上传文件" icon="el-icon-upload"></el-step>
         <el-step title="开始检测" icon="el-icon-mouse"></el-step>
         <el-step title="检测结果" icon="el-icon-s-claim"></el-step>
       </el-steps>
     </el-col>
  </el-row>
  <el-row :gutter="22" style="margin-top: 10px">
    <!--<el-row>
      <el-select v-model="language" placeholder="language" style="margin-left: 40px">
        <el-option
          v-for="item in languages"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
    </el-row>-->
    <el-row>
      <span style="margin-left: 40px">识别结果</span>
    </el-row>

    <el-col :span="11">
      <codemirror v-model="codeLeft"
                  :options="cmOption"
                  @cursorActivity="onCmCursorActivity"
                  @ready="onCmReady"
                  @focus="onCmFocus"
                  @blur="onCmBlur">
      </codemirror>
    </el-col>
    <el-col :span="11">
      <codemirror v-model="codeRight"
                  :options="cmOption"
                  @cursorActivity="onCmCursorActivity"
                  @ready="onCmReady"
                  @focus="onCmFocus"
                  @blur="onCmBlur">
      </codemirror>
    </el-col>
  </el-row>
    <el-button size="small" type="primary" style="margin-left: 20px;margin-top: 10px" @click="getFileList">文件列表</el-button>
    <el-transfer
      class="transferManage"
      style="vertical-align:middle;margin-left: 20%;margin-top: 20px"
      v-model="value"
      :data="fileList"
      :titles="['文件列表','等待检查']"
      >
    </el-transfer>
  </div>
</template>

<script>
 import {codemirror} from 'vue-codemirror'
 // language
  import 'codemirror/mode/vue/vue.js'
  // theme css
  import 'codemirror/theme/idea.css'
  // active-line.js
  import 'codemirror/addon/selection/active-line.js'
  // styleSelectedText
  import 'codemirror/addon/selection/mark-selection.js'
  import 'codemirror/addon/search/searchcursor.js'
  // highlightSelectionMatches
  import 'codemirror/addon/scroll/annotatescrollbar.js'
  import 'codemirror/addon/search/matchesonscrollbar.js'
  import 'codemirror/addon/search/searchcursor.js'
  import 'codemirror/addon/search/match-highlighter.js'
  // keyMap
  import 'codemirror/mode/clike/clike.js'
  import 'codemirror/addon/edit/matchbrackets.js'
  import 'codemirror/addon/comment/comment.js'
  import 'codemirror/addon/dialog/dialog.js'
  import 'codemirror/addon/dialog/dialog.css'
  import 'codemirror/addon/search/searchcursor.js'
  import 'codemirror/addon/search/search.js'
  import 'codemirror/keymap/sublime.js'
  // foldGutter
  import 'codemirror/addon/fold/foldgutter.css'
  import 'codemirror/addon/fold/brace-fold.js'
  import 'codemirror/addon/fold/comment-fold.js'
  import 'codemirror/addon/fold/foldcode.js'
  import 'codemirror/addon/fold/foldgutter.js'
  import 'codemirror/addon/fold/indent-fold.js'
  import 'codemirror/addon/fold/markdown-fold.js'
  import 'codemirror/addon/fold/xml-fold.js'


  export default {
      name: "document",
      components:{codemirror},
    data() {
      return {
          codeLeft: '',
          codeRight: '',
          fileList: [],
          stepNumber: 0,
          fileUploadName: '',
          value: [],
          uploadApi: this.$url+'/codehub/',
          cmOption: {
            tabSize: 4,
            foldGutter: true,
            styleActiveLine: true,
            lineNumbers: true,
            line: true,
            keyMap: "sublime",
            mode: 'text/x-vue',
            theme: 'idea',
            extraKeys: {
              'F11'(cm) {
                cm.setOption("fullScreen", !cm.getOption("fullScreen"))
              },
              'Esc'(cm) {
                if (cm.getOption("fullScreen")) cm.setOption("fullScreen", false)
              }
            }
          },
          language:'',
          languages:[{
            value: 1,
            label: 'Vue'
          },{
            value: 2,
            label: 'PHP'
          },{
            value: 3,
            label: 'Python'
          }],
      }
    },
    methods: {
      onCmCursorActivity(codemirror) {
          console.log('onCmCursorActivity', codemirror)
      },
      onCmReady(codemirror) {
          console.log('onCmReady', codemirror)
      },
      onCmFocus(codemirror) {
          console.log('onCmFocus', codemirror)
      },
      onCmBlur(codemirror) {
          console.log('onCmBlur', codemirror)
      },
      handelChange(file) {
        console.log(file.name);
        this.fileUploadName = file.name
      },
      getFileContent(){
          this.$http.get(this.$url+'/codehub/getFileContent/left.txt').then((res)=>{
              this.codeLeft = res.data;
          });
          this.$http.get(this.$url+'/codehub/getFileContent/right.txt').then((res)=>{
              this.codeRight = res.data;
          });
          this.stepNumber = 2;
      },
      getFileList(){
          this.fileList = [];
          this.$http.get(this.$url+'/codehub').then((res)=>{
              console.log(res)
              for (let item in res.data){
                  this.fileList.push({key:item,label:res.data[item]})
              }
              console.log(this.fileList)
            });
      },
      handleRemove(){
          this.code = '';
      }
    }
  }
</script>

<style xml:lang="scss">
  .el-transfer-panel{
    width: 400px;
  }
  .CodeMirror {
    height: 400px;
}
</style>
