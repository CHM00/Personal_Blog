<template>
  <div class="about-container">
    <el-row :gutter="20">
      <el-col :span="8">
        <el-card shadow="hover" class="profile-card">
          <el-avatar :size="100" :src="avatarUrl" />
<!--          <el-avatar :size="100" src="你的头像地址" />-->
          <h2>CHM</h2>
          <p>持续进化的开发者 / AI 爱好者</p>
          <el-divider />
          <div class="social-links">
            <el-link href="https://github.com/CHM00" target="_blank">Github</el-link>
          </div>
        </el-card>
      </el-col>

      <el-col :span="16">
        <el-card shadow="hover">
          <h3>🛠️ 技术栈</h3>
          <div class="skills">
            <span>C++ / Python</span> <el-progress :percentage="85" />
            <span>AI算法 / 应用</span> <el-progress :percentage="70" />
          </div>

          <el-divider />

          <h3>📜 个人经历</h3>
          <el-timeline>
            <el-timeline-item timestamp="2026-02" placement="top">
              开始搭建基于 Vue3 的 AI 个人博客系统
            </el-timeline-item>
            <el-timeline-item timestamp="2025-10" placement="top">
              深入研究 时空大模型
            </el-timeline-item>
          </el-timeline>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<style scoped>
.about-container { padding: 40px; max-width: 1200px; margin: 0 auto; }
.profile-card { text-align: center; }
.skills { margin-bottom: 20px; }
.skills span { font-size: 14px; color: #666; }
</style>


<script setup>
// 导入你的本地图片
import avatarUrl from '@/assets/logo.png'
</script>