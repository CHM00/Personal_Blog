<!-- eslint-disable vue/multi-word-component-names -->
<!--<template>-->
<!--  <el-row :gutter="20">-->
<!--    <el-col :span="18">-->
<!--      <h2>最新/热门文章</h2>-->
<!--      <el-card v-for="item in articles" :key="item.id" style="margin-bottom: 20px;">-->
<!--        <h3>{{ item.title }}</h3>-->
<!--        <p>发布时间: {{ item.date }} | 标签: <el-tag v-for="tag in item.tags" :key="tag">{{ tag }}</el-tag></p>-->
<!--        <p>摘要: {{ item.summary }}</p>-->
<!--      </el-card>-->
<!--    </el-col>-->
<!--    <el-col :span="6">-->
<!--      <el-card>-->
<!--        <h4>公告</h4>-->
<!--        <p>今天又是被好运砸中的一天～</p>-->
<!--      </el-card>-->
<!--      <el-card style="margin-top: 20px;">-->
<!--        <h4>Github地址</h4>-->
<!--        <p>https://github.com/CHM00</p>-->
<!--      </el-card>-->
<!--    </el-col>-->
<!--  </el-row>-->
<!--</template>-->

<!--<script setup>-->
<!--// 临时假数据，后面连后端替换-->
<!--const articles = [-->
<!--  { id: 1, title: 'Qt 入门', date: '2025-01-01', tags: ['Qt', 'C++'], summary: 'Qt 基础知识介绍...' },-->
<!--  // 加更多-->
<!--]-->
<!--</script>-->








<!--<template>-->
<!--  <el-row :gutter="20">-->
<!--    <el-col :span="18">-->
<!--      <div class="section-title">✨ 最新文章</div>-->
<!--      <el-card-->
<!--        v-for="item in articles"-->
<!--        :key="item.id"-->
<!--        class="article-card"-->
<!--        shadow="hover"-->
<!--      >-->
<!--        <h3 class="article-title">{{ item.title }}</h3>-->
<!--        <div class="article-meta">-->
<!--          <span>📅 {{ item.date }}</span>-->
<!--          <span class="tags">-->
<!--            🏷️-->
<!--            <el-tag v-for="tag in item.tags" :key="tag" size="small" type="info" class="tag-item">-->
<!--              {{ tag }}-->
<!--            </el-tag>-->
<!--          </span>-->
<!--        </div>-->
<!--        <p class="article-summary">{{ item.summary }}</p>-->
<!--        <div class="article-action">-->
<!--          <el-button type="primary" link @click="goToArticle(item.id)" > 阅读全文 >></el-button>-->
<!--        </div>-->
<!--      </el-card>-->
<!--    </el-col>-->

<!--    <el-col :span="6">-->
<!--      <el-card shadow="hover" class="sidebar-card">-->
<!--        <template #header>-->
<!--          <div class="card-header">📢 网站公告</div>-->
<!--        </template>-->
<!--        <p class="notice-text">欢迎来到我的个人知识库！✨</p>-->
<!--      </el-card>-->

<!--      <el-card shadow="hover" class="sidebar-card" style="margin-top: 20px;">-->
<!--        <template #header>-->
<!--          <div class="card-header">🔗 个人链接</div>-->
<!--        </template>-->
<!--        <div class="link-group">-->
<!--          <div class="link-item">-->
<!--            <el-icon><Link /></el-icon>-->
<!--            <el-link href="https://blog.csdn.net/weixin_49891405?type=blog" target="_blank" type="primary">-->
<!--              小明的CSDN博客-->
<!--            </el-link>-->
<!--          </div>-->
<!--          <div class="link-item" style="margin-top: 10px;">-->
<!--            <el-icon><Collection /></el-icon>-->
<!--            <el-link href="https://github.com/CHM00" target="_blank" type="info">-->
<!--              Github：CHM00-->
<!--            </el-link>-->
<!--          </div>-->
<!--        </div>-->
<!--      </el-card>-->
<!--    </el-col>-->



<!--&lt;!&ndash;    <el-col :span="6">&ndash;&gt;-->
<!--&lt;!&ndash;      <el-card shadow="hover" class="sidebar-card">&ndash;&gt;-->
<!--&lt;!&ndash;        <template #header>&ndash;&gt;-->
<!--&lt;!&ndash;          <div class="card-header">📢 网站公告</div>&ndash;&gt;-->
<!--&lt;!&ndash;        </template>&ndash;&gt;-->
<!--&lt;!&ndash;        <p class="notice-text">今天又是被好运砸中的一天～ 🌟</p>&ndash;&gt;-->
<!--&lt;!&ndash;        <p class="notice-text">欢迎来到我的个人知识库，这里主要分享 C++、Qt 及 AI 相关的技术踩坑日常。</p>&ndash;&gt;-->
<!--&lt;!&ndash;      </el-card>&ndash;&gt;-->

<!--&lt;!&ndash;      <el-card shadow="hover" class="sidebar-card">&ndash;&gt;-->
<!--&lt;!&ndash;        <template #header>&ndash;&gt;-->
<!--&lt;!&ndash;          <div class="card-header">🔗 个人链接</div>&ndash;&gt;-->
<!--&lt;!&ndash;        </template>&ndash;&gt;-->
<!--&lt;!&ndash;        <div class="link-item">&ndash;&gt;-->
<!--&lt;!&ndash;          <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="github" width="20" />&ndash;&gt;-->
<!--&lt;!&ndash;          <a href="https://github.com/CHM00" target="_blank">Github: CHM00</a>&ndash;&gt;-->
<!--&lt;!&ndash;        </div>&ndash;&gt;-->
<!--&lt;!&ndash;      </el-card>&ndash;&gt;-->
<!--&lt;!&ndash;    </el-col>&ndash;&gt;-->
<!--  </el-row>-->
<!--</template>-->

<!--<script setup>-->
<!--import { useRouter } from 'vue-router'-->

<!--// 2. 获取 router 实例-->
<!--const router = useRouter()-->

<!--const articles = ref([]) // 响应式空数组-->

<!--// 页面加载时请求数据-->
<!--onMounted(async () => {-->
<!--  try {-->
<!--    const res = await axios.get('http://150.158.123.242:8000/api/articles')-->
<!--    articles.value = res.data-->
<!--  } catch (error) {-->
<!--    console.error("加载首页文章失败:", error)-->
<!--  }-->
<!--})-->

<!--const goToArticle = (id) => {-->
<!--  router.push(`/article/${id}`)-->
<!--}-->


// const articles = [
//   { id: 1, title: '从RNN到Transformer', date: '2026-02-20', tags: ['llm', '基础知识'], summary: '本文将带你理清关于大模型的基础知识' },
//   { id: 2, title: '个人博客搭建指南', date: '2026-02-18', tags: ['个人博客', '前端界面'], summary: '记录了如何从零开始搭建一个带有全局 AI 悬浮窗的个人博客系统。' },
//   {
//     id: 3,
//     title: '大模型微调 PEFT vs LLaMA-Factory：深度对比',
//     date: '2026-02-22',
//     tags: ['AI', 'LLM', '微调'],
//     summary: '深度解析 PEFT 原生代码流与 LLaMA-Factory 框架流的区别、优劣及 AutoDL 实战指南。'
//   }
// ]
//
// // 3. 定义跳转函数，携带文章 ID 跳转到详情页
// const goToArticle = (id) => {
//   // 这里的反引号 ` 是为了拼接字符串，最终跳转路径类似 /article/1
//   router.push(`/article/${id}`)
// }

<!--</script>-->

<!--<style scoped>-->
<!--.section-title {-->
<!--  font-size: 22px;-->
<!--  font-weight: bold;-->
<!--  margin-bottom: 20px;-->
<!--  color: #333;-->
<!--}-->

<!--.article-card {-->
<!--  margin-bottom: 20px;-->
<!--  border-radius: 8px;-->
<!--  border: none;-->
<!--}-->

<!--.article-title {-->
<!--  margin: 0 0 10px 0;-->
<!--  font-size: 20px;-->
<!--  color: #2c3e50;-->
<!--  cursor: pointer;-->
<!--  transition: color 0.3s;-->
<!--}-->

<!--.article-title:hover {-->
<!--  color: #409eff;-->
<!--}-->

<!--.article-meta {-->
<!--  font-size: 13px;-->
<!--  color: #909399;-->
<!--  margin-bottom: 15px;-->
<!--  display: flex;-->
<!--  align-items: center;-->
<!--  gap: 15px;-->
<!--}-->

<!--.tag-item {-->
<!--  margin-right: 5px;-->
<!--}-->

<!--.article-summary {-->
<!--  color: #555;-->
<!--  line-height: 1.6;-->
<!--  margin-bottom: 15px;-->
<!--}-->

<!--.article-action {-->
<!--  text-align: right;-->
<!--}-->

<!--.sidebar-card {-->
<!--  margin-bottom: 20px;-->
<!--  border-radius: 8px;-->
<!--  border: none;-->
<!--}-->

<!--.card-header {-->
<!--  font-weight: bold;-->
<!--}-->

<!--.notice-text {-->
<!--  font-size: 14px;-->
<!--  color: #606266;-->
<!--  line-height: 1.6;-->
<!--}-->

<!--.link-item {-->
<!--  display: flex;-->
<!--  align-items: center;-->
<!--  gap: 10px;-->
<!--}-->
<!--.link-item a {-->
<!--  color: #409eff;-->
<!--  text-decoration: none;-->
<!--}-->
<!--.link-item a:hover {-->
<!--  text-decoration: underline;-->
<!--}-->
<!--</style>-->















<template>
  <el-row :gutter="20">
    <el-col :span="18">
      <div class="section-title">✨ 最新文章</div>

      <div v-if="articles.length === 0" style="text-align:center; padding:40px; color:#999">
        努力加载中...
      </div>

      <el-card
        v-for="item in articles"
        :key="item.id"
        class="article-card"
        shadow="hover"
      >
        <h3 class="article-title">{{ item.title }}</h3>
        <div class="article-meta">
          <span>📅 {{ item.date }}</span>
          <span class="tags">
            🏷️
            <el-tag v-for="tag in item.tags" :key="tag" size="small" type="info" class="tag-item">
              {{ tag }}
            </el-tag>
          </span>
        </div>
        <p class="article-summary">{{ item.summary }}</p>
        <div class="article-action">
          <el-button type="primary" link @click="goToArticle(item.id)">阅读全文 >></el-button>
        </div>
      </el-card>
    </el-col>

    <el-col :span="6">
      <el-card shadow="hover" class="sidebar-card">
        <template #header><div class="card-header">📢 网站公告</div></template>
        <p class="notice-text">欢迎来到我的个人知识库！✨</p>
      </el-card>

      <el-card shadow="hover" class="sidebar-card" style="margin-top: 20px;">
        <template #header><div class="card-header">🔗 个人链接</div></template>
        <div class="link-group">
          <div class="link-item">
            <el-link href="https://blog.csdn.net/weixin_49891405?type=blog" target="_blank" type="primary">
              小明的CSDN博客
            </el-link>
          </div>
          <div class="link-item">
            <el-link href="https://github.com/CHM00" target="_blank" type="primary">
              Github：CHM00
            </el-link>
          </div>
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const articles = ref([]) // 变成了响应式数据

// 挂载时请求后端接口
onMounted(async () => {
  try {
    const res = await axios.get('http://150.158.123.242:8000/api/articles')
    articles.value = res.data
  } catch (error) {
    console.error('获取文章列表失败:', error)
  }
})

const goToArticle = (id) => {
  router.push(`/article/${id}`)
}
</script>

<style scoped>
/* 这里的样式不需要变，保留你原有的即可 */
.section-title { font-size: 22px; font-weight: bold; margin-bottom: 20px; color: #333; }
.article-card { margin-bottom: 20px; border-radius: 8px; border: none; }
.article-title { margin: 0 0 10px 0; font-size: 20px; color: #2c3e50; cursor: pointer; transition: color 0.3s; }
.article-title:hover { color: #409eff; }
.article-meta { font-size: 13px; color: #909399; margin-bottom: 15px; display: flex; align-items: center; gap: 15px; }
.tag-item { margin-right: 5px; }
.article-summary { color: #555; line-height: 1.6; margin-bottom: 15px; }
.article-action { text-align: right; }
.sidebar-card { margin-bottom: 20px; border-radius: 8px; border: none; }
.card-header { font-weight: bold; }
.notice-text { font-size: 14px; color: #606266; line-height: 1.6; }
.link-item { display: flex; align-items: center; gap: 10px; margin-top: 10px; }
</style>







