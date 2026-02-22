<template>
  <el-row :gutter="20">
    <el-col :span="16">
      <h1>Python教程</h1>
      <el-menu mode="vertical">
        <el-menu-item>1. Python入门</el-menu-item>
        <el-menu-item>2. Python高阶</el-menu-item>
        <!-- ... 像图片的 1-7 项 -->
      </el-menu>
      <!-- 点击加载内容，使用 marked 渲染 Markdown -->
      <div v-html="markedContent"></div>
    </el-col>
<!--    <el-col :span="8">-->
<!--      <el-card>方法论 | 知识点</el-card>-->
<!--      <el-card class="red">今天又是... 正能量卡片</el-card>-->
<!--&lt;!&ndash;      <el-button type="primary">公众号</el-button>&ndash;&gt;-->
<!--    </el-col>-->
  </el-row>
</template>

<script setup>
import { ref } from 'vue';
import { marked } from 'marked';
const markedContent = ref(marked('您的 Markdown 内容'));  // 从 API 加载
</script>
