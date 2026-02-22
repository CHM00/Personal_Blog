<!--&lt;!&ndash;<template>&ndash;&gt;-->
<!--&lt;!&ndash;  <div>&ndash;&gt;-->
<!--&lt;!&ndash;    &lt;!&ndash; 你的博客内容 &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;    <h1>欢迎来到我的个人博客</h1>&ndash;&gt;-->
<!--&lt;!&ndash;    <p>这里记录了我的技术心得...</p>&ndash;&gt;-->

<!--&lt;!&ndash;    &lt;!&ndash; 直接使用聊天组件 &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;    <AIChatAssistant />&ndash;&gt;-->
<!--&lt;!&ndash;  </div>&ndash;&gt;-->

<!--&lt;!&ndash;  <el-container style="height: 100vh;">&ndash;&gt;-->
<!--&lt;!&ndash;    <el-header>&ndash;&gt;-->
<!--&lt;!&ndash;      <el-menu&ndash;&gt;-->
<!--&lt;!&ndash;        :default-active="activeIndex"&ndash;&gt;-->
<!--&lt;!&ndash;        mode="horizontal"&ndash;&gt;-->
<!--&lt;!&ndash;        @select="handleSelect"&ndash;&gt;-->
<!--&lt;!&ndash;      >&ndash;&gt;-->
<!--&lt;!&ndash;        <el-menu-item index="/">首页</el-menu-item>&ndash;&gt;-->
<!--&lt;!&ndash;        <el-menu-item index="/qt">Qt 教程</el-menu-item>&ndash;&gt;-->
<!--&lt;!&ndash;        &lt;!&ndash;<el-menu-item index="/data-structure">数据结构</el-menu-item>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;        &lt;!&ndash; 后面加更多分类 &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;        <el-menu-item index="/admin">后台管理</el-menu-item>&ndash;&gt;-->
<!--&lt;!&ndash;      </el-menu>&ndash;&gt;-->
<!--&lt;!&ndash;    </el-header>&ndash;&gt;-->
<!--&lt;!&ndash;    <el-main>&ndash;&gt;-->
<!--&lt;!&ndash;      <router-view></router-view> &lt;!&ndash; 这里显示页面内容 &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;    </el-main>&ndash;&gt;-->
<!--&lt;!&ndash;    <el-footer>© 你的名字 | 知识分享 | 文章总数: xx | 字数: xx</el-footer>&ndash;&gt;-->
<!--&lt;!&ndash;  </el-container>&ndash;&gt;-->
<!--&lt;!&ndash;</template>&ndash;&gt;-->


<!--&lt;!&ndash;<script setup>&ndash;&gt;-->
<!--&lt;!&ndash;import { computed } from 'vue'&ndash;&gt;-->
<!--&lt;!&ndash;import { useRouter, useRoute } from 'vue-router'&ndash;&gt;-->
<!--&lt;!&ndash;import AIChatAssistant from '@/components/AIChatAssistant.vue'&ndash;&gt;-->

<!--&lt;!&ndash;const router = useRouter()&ndash;&gt;-->
<!--&lt;!&ndash;const route = useRoute()&ndash;&gt;-->

<!--&lt;!&ndash;const activeIndex = computed(() => route.path || '/')&ndash;&gt;-->

<!--&lt;!&ndash;const handleSelect = (key) => {&ndash;&gt;-->
<!--&lt;!&ndash;  router.push(key)&ndash;&gt;-->
<!--&lt;!&ndash;}&ndash;&gt;-->
<!--&lt;!&ndash;</script>&ndash;&gt;-->


<!--<template>-->
<!--  <el-container style="height: 100vh;">-->
<!--    &lt;!&ndash; 顶部导航 &ndash;&gt;-->
<!--    <el-header>-->
<!--      <el-menu-->
<!--        :default-active="activeIndex"-->
<!--        mode="horizontal"-->
<!--        @select="handleSelect"-->
<!--        background-color="#333"-->
<!--        text-color="#fff"-->
<!--        active-text-color="#ffd04b"-->
<!--      >-->
<!--        <el-menu-item index="/">首页</el-menu-item>-->
<!--        <el-menu-item index="/qt">Qt 教程</el-menu-item>-->
<!--        &lt;!&ndash; <el-menu-item index="/data-structure">数据结构</el-menu-item> &ndash;&gt;-->
<!--        <el-menu-item index="/admin">后台管理</el-menu-item>-->
<!--      </el-menu>-->
<!--    </el-header>-->

<!--    &lt;!&ndash; 主要内容区域 &ndash;&gt;-->
<!--    <el-main style="padding: 0;">-->
<!--      <router-view />-->
<!--    </el-main>-->

<!--    &lt;!&ndash; 底部 &ndash;&gt;-->
<!--    <el-footer style="text-align: center; line-height: 60px;">-->
<!--      © 你的名字 | 知识分享 | 文章总数: xx | 字数: xx-->
<!--    </el-footer>-->

<!--    &lt;!&ndash; 全局悬浮 AI 聊天助手（所有页面可见） &ndash;&gt;-->
<!--    <AIChatAssistant />-->
<!--  </el-container>-->
<!--</template>-->

<!--<script setup>-->
<!--import { computed } from 'vue'-->
<!--import { useRouter, useRoute } from 'vue-router'-->
<!--import AIChatAssistant from '@/components/AIChatAssistant.vue'-->

<!--const router = useRouter()-->
<!--const route = useRoute()-->

<!--const activeIndex = computed(() => route.path || '/')-->

<!--const handleSelect = (key) => {-->
<!--  router.push(key)-->
<!--}-->
<!--</script>-->

<!--<style scoped>-->
<!--/* 可选：让 el-main 不要有默认 padding，交给子页面自己控制 */-->
<!--.el-main {-->
<!--  padding: 0 !important;-->
<!--}-->
<!--</style>-->







<!--<template>-->
<!--  <el-container class="blog-layout">-->
<!--    <el-header class="blog-header">-->
<!--      <div class="header-content">-->
<!--        <div class="logo">✨ CHM的知识宇宙</div>-->

<!--        <el-menu-->
<!--          :default-active="activeIndex"-->
<!--          mode="horizontal"-->
<!--          @select="handleSelect"-->
<!--          background-color="transparent"-->
<!--          text-color="#e5e7eb"-->
<!--          active-text-color="#ffd04b"-->
<!--          class="nav-menu"-->
<!--          :ellipsis="false"-->
<!--        >-->
<!--          <el-menu-item index="/">首页</el-menu-item>-->
<!--          <el-menu-item index="/qt">教程</el-menu-item>-->
<!--          <el-menu-item index="/about">关于我</el-menu-item>-->
<!--          <el-menu-item index="/admin">后台发布</el-menu-item>-->
<!--        </el-menu>-->
<!--      </div>-->
<!--    </el-header>-->

<!--    <el-main class="blog-main">-->
<!--      <div class="main-container">-->
<!--        <router-view v-slot="{ Component }">-->
<!--          <transition name="fade" mode="out-in">-->
<!--            <component :is="Component" />-->
<!--          </transition>-->
<!--        </router-view>-->
<!--      </div>-->
<!--    </el-main>-->

<!--    <el-footer class="blog-footer">-->
<!--      <p>© 2026 CHM00 | 知识分享 | 持续学习，持续输出</p>-->
<!--    </el-footer>-->

<!--    <AIChatAssistant />-->
<!--  </el-container>-->
<!--</template>-->

<!--<script setup>-->
<!--import { computed } from 'vue'-->
<!--import { useRouter, useRoute } from 'vue-router'-->
<!--import AIChatAssistant from '@/components/AIChatAssistant.vue'-->

<!--const router = useRouter()-->
<!--const route = useRoute()-->

<!--// 动态绑定当前激活的菜单项-->
<!--const activeIndex = computed(() => route.path || '/')-->

<!--// 路由跳转机制-->
<!--const handleSelect = (key) => {-->
<!--  router.push(key)-->
<!--}-->
<!--</script>-->

<!--<style scoped>-->
<!--/* 整个布局背景设为非常浅的灰色，突出白色卡片 */-->
<!--.blog-layout {-->
<!--  min-height: 100vh;-->
<!--  background-color: #f4f5f7;-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--}-->

<!--/* 顶部导航样式优化 */-->
<!--.blog-header {-->
<!--  background-color: #24292f;-->
<!--  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);-->
<!--  padding: 0;-->
<!--  height: 60px;-->
<!--  position: sticky;-->
<!--  top: 0;-->
<!--  z-index: 100;-->
<!--}-->

<!--.header-content {-->
<!--  max-width: 1200px; /* 限制导航栏最大宽度 */-->
<!--  margin: 0 auto;-->
<!--  display: flex;-->
<!--  align-items: center;-->
<!--  justify-content: space-between;-->
<!--  padding: 0 20px;-->
<!--  height: 100%;-->
<!--}-->

<!--.logo {-->
<!--  color: #fff;-->
<!--  font-size: 20px;-->
<!--  font-weight: bold;-->
<!--}-->

<!--.nav-menu {-->
<!--  border-bottom: none !important;-->
<!--}-->

<!--/* 中间内容区域优化 */-->
<!--.blog-main {-->
<!--  padding: 20px 0;-->
<!--  flex: 1; /* 让 main 撑满剩余空间，把 footer 推到底部 */-->
<!--}-->

<!--.main-container {-->
<!--  max-width: 1200px; /* 居中限制最大宽度，这是博客必备的设计 */-->
<!--  margin: 0 auto;-->
<!--  padding: 0 20px;-->
<!--}-->

<!--/* 底部样式优化 */-->
<!--.blog-footer {-->
<!--  background-color: #fff;-->
<!--  text-align: center;-->
<!--  color: #666;-->
<!--  line-height: 60px;-->
<!--  border-top: 1px solid #eaeaef;-->
<!--  height: 60px;-->
<!--}-->

<!--/* 页面切换的渐变动画 */-->
<!--.fade-enter-active,-->
<!--.fade-leave-active {-->
<!--  transition: opacity 0.3s ease;-->
<!--}-->
<!--.fade-enter-from,-->
<!--.fade-leave-to {-->
<!--  opacity: 0;-->
<!--}-->
<!--</style>-->


<template>
  <el-container class="blog-layout">
    <el-header class="blog-header">
      <div class="header-content">
        <div class="logo">✨ CHM的知识宇宙</div>

        <el-menu
          :default-active="activeIndex"
          mode="horizontal"
          @select="handleSelect"
          background-color="transparent"
          text-color="#e5e7eb"
          active-text-color="#ffd04b"
          class="nav-menu"
          :ellipsis="false"
        >
          <el-menu-item index="/">首页</el-menu-item>
<!--          <el-menu-item index="/qt">教程</el-menu-item>-->
          <el-menu-item index="/admin">后台发布</el-menu-item>
          <el-menu-item index="/about">关于我</el-menu-item>
        </el-menu>
      </div>
    </el-header>

    <el-main class="blog-main">
      <div class="main-container">
        <router-view v-slot="{ Component }">
          <transition name="fade" mode="out-in">
            <component :is="Component" />
          </transition>
        </router-view>
      </div>
    </el-main>

    <el-footer class="blog-footer">
      <p>© 2026 CHM00 | 知识分享 | 持续学习，持续输出</p>
    </el-footer>

    <AIChatAssistant />
  </el-container>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import AIChatAssistant from '@/components/AIChatAssistant.vue'

const router = useRouter()
const route = useRoute()

const activeIndex = computed(() => route.path || '/')

const handleSelect = (key) => {
  router.push(key)
}
</script>

<style scoped>
/* 原有样式全部保留即可 */
.blog-layout { min-height: 100vh; background-color: #f4f5f7; display: flex; flex-direction: column; }
.blog-header { background-color: #24292f; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); padding: 0; height: 60px; position: sticky; top: 0; z-index: 100; }
.header-content { max-width: 1200px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; padding: 0 20px; height: 100%; }
.logo { color: #fff; font-size: 20px; font-weight: bold; }
.nav-menu { border-bottom: none !important; }
.blog-main { padding: 20px 0; flex: 1; }
.main-container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
.blog-footer { background-color: #fff; text-align: center; color: #666; line-height: 60px; border-top: 1px solid #eaeaef; height: 60px; }
.fade-enter-active, .fade-leave-active { transition: opacity 0.3s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
</style>