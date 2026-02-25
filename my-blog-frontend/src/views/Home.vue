<!-- eslint-disable vue/multi-word-component-names -->
<!--&lt;!&ndash;<template>&ndash;&gt;-->
<!--&lt;!&ndash;  <el-row :gutter="20">&ndash;&gt;-->
<!--&lt;!&ndash;    <el-col :span="18">&ndash;&gt;-->
<!--&lt;!&ndash;      <h2>最新/热门文章</h2>&ndash;&gt;-->
<!--&lt;!&ndash;      <el-card v-for="item in articles" :key="item.id" style="margin-bottom: 20px;">&ndash;&gt;-->
<!--&lt;!&ndash;        <h3>{{ item.title }}</h3>&ndash;&gt;-->
<!--&lt;!&ndash;        <p>发布时间: {{ item.date }} | 标签: <el-tag v-for="tag in item.tags" :key="tag">{{ tag }}</el-tag></p>&ndash;&gt;-->
<!--&lt;!&ndash;        <p>摘要: {{ item.summary }}</p>&ndash;&gt;-->
<!--&lt;!&ndash;      </el-card>&ndash;&gt;-->
<!--&lt;!&ndash;    </el-col>&ndash;&gt;-->
<!--&lt;!&ndash;    <el-col :span="6">&ndash;&gt;-->
<!--&lt;!&ndash;      <el-card>&ndash;&gt;-->
<!--&lt;!&ndash;        <h4>公告</h4>&ndash;&gt;-->
<!--&lt;!&ndash;        <p>今天又是被好运砸中的一天～</p>&ndash;&gt;-->
<!--&lt;!&ndash;      </el-card>&ndash;&gt;-->
<!--&lt;!&ndash;      <el-card style="margin-top: 20px;">&ndash;&gt;-->
<!--&lt;!&ndash;        <h4>Github地址</h4>&ndash;&gt;-->
<!--&lt;!&ndash;        <p>https://github.com/CHM00</p>&ndash;&gt;-->
<!--&lt;!&ndash;      </el-card>&ndash;&gt;-->
<!--&lt;!&ndash;    </el-col>&ndash;&gt;-->
<!--&lt;!&ndash;  </el-row>&ndash;&gt;-->
<!--&lt;!&ndash;</template>&ndash;&gt;-->

<!--&lt;!&ndash;<script setup>&ndash;&gt;-->
<!--&lt;!&ndash;// 临时假数据，后面连后端替换&ndash;&gt;-->
<!--&lt;!&ndash;const articles = [&ndash;&gt;-->
<!--&lt;!&ndash;  { id: 1, title: 'Qt 入门', date: '2025-01-01', tags: ['Qt', 'C++'], summary: 'Qt 基础知识介绍...' },&ndash;&gt;-->
<!--&lt;!&ndash;  // 加更多&ndash;&gt;-->
<!--&lt;!&ndash;]&ndash;&gt;-->
<!--&lt;!&ndash;</script>&ndash;&gt;-->








<!--&lt;!&ndash;<template>&ndash;&gt;-->
<!--&lt;!&ndash;  <el-row :gutter="20">&ndash;&gt;-->
<!--&lt;!&ndash;    <el-col :span="18">&ndash;&gt;-->
<!--&lt;!&ndash;      <div class="section-title">✨ 最新文章</div>&ndash;&gt;-->
<!--&lt;!&ndash;      <el-card&ndash;&gt;-->
<!--&lt;!&ndash;        v-for="item in articles"&ndash;&gt;-->
<!--&lt;!&ndash;        :key="item.id"&ndash;&gt;-->
<!--&lt;!&ndash;        class="article-card"&ndash;&gt;-->
<!--&lt;!&ndash;        shadow="hover"&ndash;&gt;-->
<!--&lt;!&ndash;      >&ndash;&gt;-->
<!--&lt;!&ndash;        <h3 class="article-title">{{ item.title }}</h3>&ndash;&gt;-->
<!--&lt;!&ndash;        <div class="article-meta">&ndash;&gt;-->
<!--&lt;!&ndash;          <span>📅 {{ item.date }}</span>&ndash;&gt;-->
<!--&lt;!&ndash;          <span class="tags">&ndash;&gt;-->
<!--&lt;!&ndash;            🏷️&ndash;&gt;-->
<!--&lt;!&ndash;            <el-tag v-for="tag in item.tags" :key="tag" size="small" type="info" class="tag-item">&ndash;&gt;-->
<!--&lt;!&ndash;              {{ tag }}&ndash;&gt;-->
<!--&lt;!&ndash;            </el-tag>&ndash;&gt;-->
<!--&lt;!&ndash;          </span>&ndash;&gt;-->
<!--&lt;!&ndash;        </div>&ndash;&gt;-->
<!--&lt;!&ndash;        <p class="article-summary">{{ item.summary }}</p>&ndash;&gt;-->
<!--&lt;!&ndash;        <div class="article-action">&ndash;&gt;-->
<!--&lt;!&ndash;          <el-button type="primary" link @click="goToArticle(item.id)" > 阅读全文 >></el-button>&ndash;&gt;-->
<!--&lt;!&ndash;        </div>&ndash;&gt;-->
<!--&lt;!&ndash;      </el-card>&ndash;&gt;-->
<!--&lt;!&ndash;    </el-col>&ndash;&gt;-->

<!--&lt;!&ndash;    <el-col :span="6">&ndash;&gt;-->
<!--&lt;!&ndash;      <el-card shadow="hover" class="sidebar-card">&ndash;&gt;-->
<!--&lt;!&ndash;        <template #header>&ndash;&gt;-->
<!--&lt;!&ndash;          <div class="card-header">📢 网站公告</div>&ndash;&gt;-->
<!--&lt;!&ndash;        </template>&ndash;&gt;-->
<!--&lt;!&ndash;        <p class="notice-text">欢迎来到我的个人知识库！✨</p>&ndash;&gt;-->
<!--&lt;!&ndash;      </el-card>&ndash;&gt;-->

<!--&lt;!&ndash;      <el-card shadow="hover" class="sidebar-card" style="margin-top: 20px;">&ndash;&gt;-->
<!--&lt;!&ndash;        <template #header>&ndash;&gt;-->
<!--&lt;!&ndash;          <div class="card-header">🔗 个人链接</div>&ndash;&gt;-->
<!--&lt;!&ndash;        </template>&ndash;&gt;-->
<!--&lt;!&ndash;        <div class="link-group">&ndash;&gt;-->
<!--&lt;!&ndash;          <div class="link-item">&ndash;&gt;-->
<!--&lt;!&ndash;            <el-icon><Link /></el-icon>&ndash;&gt;-->
<!--&lt;!&ndash;            <el-link href="https://blog.csdn.net/weixin_49891405?type=blog" target="_blank" type="primary">&ndash;&gt;-->
<!--&lt;!&ndash;              小明的CSDN博客&ndash;&gt;-->
<!--&lt;!&ndash;            </el-link>&ndash;&gt;-->
<!--&lt;!&ndash;          </div>&ndash;&gt;-->
<!--&lt;!&ndash;          <div class="link-item" style="margin-top: 10px;">&ndash;&gt;-->
<!--&lt;!&ndash;            <el-icon><Collection /></el-icon>&ndash;&gt;-->
<!--&lt;!&ndash;            <el-link href="https://github.com/CHM00" target="_blank" type="info">&ndash;&gt;-->
<!--&lt;!&ndash;              Github：CHM00&ndash;&gt;-->
<!--&lt;!&ndash;            </el-link>&ndash;&gt;-->
<!--&lt;!&ndash;          </div>&ndash;&gt;-->
<!--&lt;!&ndash;        </div>&ndash;&gt;-->
<!--&lt;!&ndash;      </el-card>&ndash;&gt;-->
<!--&lt;!&ndash;    </el-col>&ndash;&gt;-->



<!--&lt;!&ndash;&lt;!&ndash;    <el-col :span="6">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;      <el-card shadow="hover" class="sidebar-card">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;        <template #header>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;          <div class="card-header">📢 网站公告</div>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;        </template>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;        <p class="notice-text">今天又是被好运砸中的一天～ 🌟</p>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;        <p class="notice-text">欢迎来到我的个人知识库，这里主要分享 C++、Qt 及 AI 相关的技术踩坑日常。</p>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;      </el-card>&ndash;&gt;&ndash;&gt;-->

<!--&lt;!&ndash;&lt;!&ndash;      <el-card shadow="hover" class="sidebar-card">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;        <template #header>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;          <div class="card-header">🔗 个人链接</div>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;        </template>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;        <div class="link-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;          <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="github" width="20" />&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;          <a href="https://github.com/CHM00" target="_blank">Github: CHM00</a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;        </div>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;      </el-card>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;    </el-col>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;  </el-row>&ndash;&gt;-->
<!--&lt;!&ndash;</template>&ndash;&gt;-->

<!--&lt;!&ndash;<script setup>&ndash;&gt;-->
<!--&lt;!&ndash;import { useRouter } from 'vue-router'&ndash;&gt;-->

<!--&lt;!&ndash;// 2. 获取 router 实例&ndash;&gt;-->
<!--&lt;!&ndash;const router = useRouter()&ndash;&gt;-->

<!--&lt;!&ndash;const articles = ref([]) // 响应式空数组&ndash;&gt;-->

<!--&lt;!&ndash;// 页面加载时请求数据&ndash;&gt;-->
<!--&lt;!&ndash;onMounted(async () => {&ndash;&gt;-->
<!--&lt;!&ndash;  try {&ndash;&gt;-->
<!--&lt;!&ndash;    const res = await axios.get('http://150.158.123.242:8000/api/articles')&ndash;&gt;-->
<!--&lt;!&ndash;    articles.value = res.data&ndash;&gt;-->
<!--&lt;!&ndash;  } catch (error) {&ndash;&gt;-->
<!--&lt;!&ndash;    console.error("加载首页文章失败:", error)&ndash;&gt;-->
<!--&lt;!&ndash;  }&ndash;&gt;-->
<!--&lt;!&ndash;})&ndash;&gt;-->

<!--&lt;!&ndash;const goToArticle = (id) => {&ndash;&gt;-->
<!--&lt;!&ndash;  router.push(`/article/${id}`)&ndash;&gt;-->
<!--&lt;!&ndash;}&ndash;&gt;-->


<!--// const articles = [-->
<!--//   { id: 1, title: '从RNN到Transformer', date: '2026-02-20', tags: ['llm', '基础知识'], summary: '本文将带你理清关于大模型的基础知识' },-->
<!--//   { id: 2, title: '个人博客搭建指南', date: '2026-02-18', tags: ['个人博客', '前端界面'], summary: '记录了如何从零开始搭建一个带有全局 AI 悬浮窗的个人博客系统。' },-->
<!--//   {-->
<!--//     id: 3,-->
<!--//     title: '大模型微调 PEFT vs LLaMA-Factory：深度对比',-->
<!--//     date: '2026-02-22',-->
<!--//     tags: ['AI', 'LLM', '微调'],-->
<!--//     summary: '深度解析 PEFT 原生代码流与 LLaMA-Factory 框架流的区别、优劣及 AutoDL 实战指南。'-->
<!--//   }-->
<!--// ]-->
<!--//-->
<!--// // 3. 定义跳转函数，携带文章 ID 跳转到详情页-->
<!--// const goToArticle = (id) => {-->
<!--//   // 这里的反引号 ` 是为了拼接字符串，最终跳转路径类似 /article/1-->
<!--//   router.push(`/article/${id}`)-->
<!--// }-->

<!--&lt;!&ndash;</script>&ndash;&gt;-->

<!--&lt;!&ndash;<style scoped>&ndash;&gt;-->
<!--&lt;!&ndash;.section-title {&ndash;&gt;-->
<!--&lt;!&ndash;  font-size: 22px;&ndash;&gt;-->
<!--&lt;!&ndash;  font-weight: bold;&ndash;&gt;-->
<!--&lt;!&ndash;  margin-bottom: 20px;&ndash;&gt;-->
<!--&lt;!&ndash;  color: #333;&ndash;&gt;-->
<!--&lt;!&ndash;}&ndash;&gt;-->

<!--&lt;!&ndash;.article-card {&ndash;&gt;-->
<!--&lt;!&ndash;  margin-bottom: 20px;&ndash;&gt;-->
<!--&lt;!&ndash;  border-radius: 8px;&ndash;&gt;-->
<!--&lt;!&ndash;  border: none;&ndash;&gt;-->
<!--&lt;!&ndash;}&ndash;&gt;-->

<!--&lt;!&ndash;.article-title {&ndash;&gt;-->
<!--&lt;!&ndash;  margin: 0 0 10px 0;&ndash;&gt;-->
<!--&lt;!&ndash;  font-size: 20px;&ndash;&gt;-->
<!--&lt;!&ndash;  color: #2c3e50;&ndash;&gt;-->
<!--&lt;!&ndash;  cursor: pointer;&ndash;&gt;-->
<!--&lt;!&ndash;  transition: color 0.3s;&ndash;&gt;-->
<!--&lt;!&ndash;}&ndash;&gt;-->

<!--&lt;!&ndash;.article-title:hover {&ndash;&gt;-->
<!--&lt;!&ndash;  color: #409eff;&ndash;&gt;-->
<!--&lt;!&ndash;}&ndash;&gt;-->

<!--&lt;!&ndash;.article-meta {&ndash;&gt;-->
<!--&lt;!&ndash;  font-size: 13px;&ndash;&gt;-->
<!--&lt;!&ndash;  color: #909399;&ndash;&gt;-->
<!--&lt;!&ndash;  margin-bottom: 15px;&ndash;&gt;-->
<!--&lt;!&ndash;  display: flex;&ndash;&gt;-->
<!--&lt;!&ndash;  align-items: center;&ndash;&gt;-->
<!--&lt;!&ndash;  gap: 15px;&ndash;&gt;-->
<!--&lt;!&ndash;}&ndash;&gt;-->

<!--&lt;!&ndash;.tag-item {&ndash;&gt;-->
<!--&lt;!&ndash;  margin-right: 5px;&ndash;&gt;-->
<!--&lt;!&ndash;}&ndash;&gt;-->

<!--&lt;!&ndash;.article-summary {&ndash;&gt;-->
<!--&lt;!&ndash;  color: #555;&ndash;&gt;-->
<!--&lt;!&ndash;  line-height: 1.6;&ndash;&gt;-->
<!--&lt;!&ndash;  margin-bottom: 15px;&ndash;&gt;-->
<!--&lt;!&ndash;}&ndash;&gt;-->

<!--&lt;!&ndash;.article-action {&ndash;&gt;-->
<!--&lt;!&ndash;  text-align: right;&ndash;&gt;-->
<!--&lt;!&ndash;}&ndash;&gt;-->

<!--&lt;!&ndash;.sidebar-card {&ndash;&gt;-->
<!--&lt;!&ndash;  margin-bottom: 20px;&ndash;&gt;-->
<!--&lt;!&ndash;  border-radius: 8px;&ndash;&gt;-->
<!--&lt;!&ndash;  border: none;&ndash;&gt;-->
<!--&lt;!&ndash;}&ndash;&gt;-->

<!--&lt;!&ndash;.card-header {&ndash;&gt;-->
<!--&lt;!&ndash;  font-weight: bold;&ndash;&gt;-->
<!--&lt;!&ndash;}&ndash;&gt;-->

<!--&lt;!&ndash;.notice-text {&ndash;&gt;-->
<!--&lt;!&ndash;  font-size: 14px;&ndash;&gt;-->
<!--&lt;!&ndash;  color: #606266;&ndash;&gt;-->
<!--&lt;!&ndash;  line-height: 1.6;&ndash;&gt;-->
<!--&lt;!&ndash;}&ndash;&gt;-->

<!--&lt;!&ndash;.link-item {&ndash;&gt;-->
<!--&lt;!&ndash;  display: flex;&ndash;&gt;-->
<!--&lt;!&ndash;  align-items: center;&ndash;&gt;-->
<!--&lt;!&ndash;  gap: 10px;&ndash;&gt;-->
<!--&lt;!&ndash;}&ndash;&gt;-->
<!--&lt;!&ndash;.link-item a {&ndash;&gt;-->
<!--&lt;!&ndash;  color: #409eff;&ndash;&gt;-->
<!--&lt;!&ndash;  text-decoration: none;&ndash;&gt;-->
<!--&lt;!&ndash;}&ndash;&gt;-->
<!--&lt;!&ndash;.link-item a:hover {&ndash;&gt;-->
<!--&lt;!&ndash;  text-decoration: underline;&ndash;&gt;-->
<!--&lt;!&ndash;}&ndash;&gt;-->
<!--&lt;!&ndash;</style>&ndash;&gt;-->















<!--<template>-->
<!--  <el-row :gutter="20">-->
<!--    <el-col :span="18">-->
<!--      <div class="section-title">✨ 最新文章</div>-->

<!--      <div v-if="articles.length === 0" style="text-align:center; padding:40px; color:#999">-->
<!--        努力加载中...-->
<!--      </div>-->

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
<!--          <el-button type="primary" link @click="goToArticle(item.id)">阅读全文 >></el-button>-->
<!--        </div>-->
<!--      </el-card>-->
<!--    </el-col>-->

<!--    <el-col :span="6">-->
<!--      <el-card shadow="hover" class="sidebar-card">-->
<!--        <template #header><div class="card-header">📢 网站公告</div></template>-->
<!--        <p class="notice-text">欢迎来到我的个人知识库！✨</p>-->
<!--      </el-card>-->

<!--      <el-card shadow="hover" class="sidebar-card" style="margin-top: 20px;">-->
<!--        <template #header><div class="card-header">🔗 个人链接</div></template>-->
<!--        <div class="link-group">-->
<!--          <div class="link-item">-->
<!--            <el-link href="https://blog.csdn.net/weixin_49891405?type=blog" target="_blank" type="primary">-->
<!--              小明的CSDN博客-->
<!--            </el-link>-->
<!--          </div>-->
<!--          <div class="link-item">-->
<!--            <el-link href="https://github.com/CHM00" target="_blank" type="primary">-->
<!--              Github：CHM00-->
<!--            </el-link>-->
<!--          </div>-->
<!--        </div>-->
<!--      </el-card>-->
<!--    </el-col>-->
<!--  </el-row>-->
<!--</template>-->

<!--<script setup>-->
<!--import { ref, onMounted } from 'vue'-->
<!--import { useRouter } from 'vue-router'-->
<!--// import axios from 'axios'-->
<!--import request from '@/utils/request'-->

<!--const router = useRouter()-->
<!--const articles = ref([]) // 变成了响应式数据-->

<!--// 挂载时请求后端接口-->
<!--// onMounted(async () => {-->
<!--//   try {-->
<!--//     const res = await axios.get('http://150.158.123.242:8000/api/articles')-->
<!--//     articles.value = res.data-->
<!--//   } catch (error) {-->
<!--//     console.error('获取文章列表失败:', error)-->
<!--//   }-->
<!--// })-->

<!--onMounted(async () => {-->
<!--  try {-->
<!--    const res = await request.get('/api/articles')-->
<!--    articles.value = res.data-->
<!--  } catch (error) {-->
<!--    console.error('获取文章列表失败:', error)-->
<!--  }-->
<!--})-->


<!--const goToArticle = (id) => {-->
<!--  router.push(`/article/${id}`)-->
<!--}-->
<!--</script>-->

<!--<style scoped>-->
<!--/* 这里的样式不需要变，保留你原有的即可 */-->
<!--.section-title { font-size: 22px; font-weight: bold; margin-bottom: 20px; color: #333; }-->
<!--.article-card { margin-bottom: 20px; border-radius: 8px; border: none; }-->
<!--.article-title { margin: 0 0 10px 0; font-size: 20px; color: #2c3e50; cursor: pointer; transition: color 0.3s; }-->
<!--.article-title:hover { color: #409eff; }-->
<!--.article-meta { font-size: 13px; color: #909399; margin-bottom: 15px; display: flex; align-items: center; gap: 15px; }-->
<!--.tag-item { margin-right: 5px; }-->
<!--.article-summary { color: #555; line-height: 1.6; margin-bottom: 15px; }-->
<!--.article-action { text-align: right; }-->
<!--.sidebar-card { margin-bottom: 20px; border-radius: 8px; border: none; }-->
<!--.card-header { font-weight: bold; }-->
<!--.notice-text { font-size: 14px; color: #606266; line-height: 1.6; }-->
<!--.link-item { display: flex; align-items: center; gap: 10px; margin-top: 10px; }-->
<!--</style>-->




<template>
  <el-row :gutter="20">
    <el-col :span="18">
      <div class="section-title">✨ 最新文章</div>

      <el-alert
        v-if="isAdmin"
        title="管理员权限已激活"
        type="success"
        show-icon
        style="margin-bottom: 20px"
      />

      <div v-if="loading" style="text-align:center; padding:40px; color:#999">数据加载中...</div>

      <el-card v-for="item in articles" :key="item.id" class="article-card" shadow="hover">
        <div class="card-header-flex">
          <h3 class="article-title" @click="goToArticle(item.id)">{{ item.title }}</h3>

          <div v-if="isAdmin" class="admin-actions">
            <el-button
              type="danger"
              size="small"
              plain
              @click.stop="handleDelete(item.id)"
            >
              删除
            </el-button>
          </div>
        </div>

        <div class="article-meta">
          <span>📅 {{ item.date }}</span>
          <span class="tags">
            🏷️ <el-tag v-for="tag in item.tags" :key="tag" size="small" type="info" class="tag-item">{{ tag }}</el-tag>
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
        <div v-if="!isAdmin" style="margin-top: 15px">
          <el-button type="primary" size="small" @click="router.push('/login')">管理员登录</el-button>
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessageBox, ElMessage } from 'element-plus'
import request from '@/utils/request'

const router = useRouter()
const articles = ref([])
const loading = ref(false)

// 必须严格匹配你在 Login.vue 中存入的 'admin_token'
const isAdmin = computed(() => {
  return !!localStorage.getItem('admin_token')
})

const fetchArticles = async () => {
  loading.value = true
  try {
    const res = await request.get('/api/articles')
    articles.value = res.data
  } catch (error) {
    console.error('获取文章失败:', error)
  } finally {
    loading.value = false
  }
}

const handleDelete = (id) => {
  ElMessageBox.confirm('确定要删除这篇文章吗？AI知识库也将同步移除。', '警告', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'warning'
  }).then(async () => {
    try {
      // 这里的路径必须与后端 @app.delete("/api/articles/{article_id}") 一致
      await request.delete(`/api/articles/${id}`)
      ElMessage.success('删除成功')
      fetchArticles()
    } catch (error) {
      ElMessage.error('删除失败，请检查登录状态')
    }
  }).catch(() => {})
}

const goToArticle = (id) => {
  router.push(`/article/${id}`)
}

onMounted(() => {
  fetchArticles()
  console.log("当前 admin_token:", localStorage.getItem('admin_token'))
})
</script>

<style scoped>
.section-title { font-size: 22px; font-weight: bold; margin-bottom: 20px; color: #333; }
.article-card { margin-bottom: 20px; border-radius: 8px; border: none; }
.card-header-flex {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}
.article-title { margin: 0; font-size: 20px; color: #2c3e50; cursor: pointer; }
.article-title:hover { color: #409eff; }
.article-meta { font-size: 13px; color: #909399; margin-bottom: 15px; display: flex; gap: 15px; }
.article-action { text-align: right; }
.sidebar-card { border-radius: 8px; border: none; }
</style>