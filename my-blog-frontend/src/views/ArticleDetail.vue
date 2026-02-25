<!--<template>-->
<!--  <div class="article-detail-container">-->
<!--    <div class="back-action">-->
<!--      <el-button @click="router.back()" icon="ArrowLeft" link>返回列表</el-button>-->
<!--    </div>-->

<!--    <el-card class="article-content-card" shadow="never">-->
<!--      <template #header>-->
<!--        <div class="article-header">-->
<!--          <h1 class="title">{{ article.title }}</h1>-->
<!--          <div class="meta">-->
<!--            <span>📅 发布于: {{ article.date }}</span>-->
<!--            <el-divider direction="vertical" />-->
<!--            <span>🏷️ 标签:-->
<!--              <el-tag v-for="tag in article.tags" :key="tag" size="small" class="mx-1">-->
<!--                {{ tag }}-->
<!--              </el-tag>-->
<!--            </span>-->
<!--          </div>-->
<!--        </div>-->
<!--      </template>-->

<!--      <div class="markdown-body" v-html="renderedContent"></div>-->
<!--    </el-card>-->
<!--  </div>-->
<!--</template>-->

<!--<script setup>-->
<!--import { ref, onMounted, computed } from 'vue'-->
<!--import { useRoute, useRouter } from 'vue-router'-->
<!--import { marked } from 'marked'-->
<!--import hljs from 'highlight.js'-->
<!--import 'highlight.js/styles/github-dark.css' // 引入深色代码主题-->

<!--// 配置 marked 使用 highlight.js-->
<!--marked.setOptions({-->
<!--  highlight: function (code, lang) {-->
<!--    const language = hljs.getLanguage(lang) ? lang : 'plaintext';-->
<!--    return hljs.highlight(code, { language }).value;-->
<!--  },-->
<!--  langPrefix: 'hljs language-'-->
<!--})-->


<!--const route = useRoute()-->
<!--const router = useRouter()-->

<!--// 模拟文章数据（后期对接后端 API）-->
<!--const article = ref({-->
<!--  id: null,-->
<!--  title: '加载中...',-->
<!--  date: '',-->
<!--  tags: [],-->
<!--  content: '' // 存放 Markdown 原文-->
<!--})-->

<!--// 使用 computed 实时将 Markdown 转为 HTML-->
<!--const renderedContent = computed(() => {-->
<!--  return marked(article.value.content || '')-->
<!--})-->

<!--onMounted(() => {-->
<!--  const articleId = route.params.id-->
<!--  // 模拟请求后端-->
<!--  fetchArticleData(articleId)-->
<!--})-->

<!--// import { mockArticles } from '@/data/articles'-->
<!--//-->
<!--// const fetchArticleData = (id) => {-->
<!--//   // 模拟异步请求-->
<!--//   setTimeout(() => {-->
<!--//     article.value = mockArticles[id] || { title: '未找到文章' };-->
<!--//   }, 200);-->
<!--// }-->

<!--import axios from 'axios'-->

<!--const fetchArticleData = async (id) => {-->
<!--  try {-->
<!--    const res = await axios.get(`http://150.158.123.242:8000/api/articles/${id}`)-->
<!--    article.value = res.data-->
<!--  } catch (error) {-->
<!--    console.error("加载文章详情失败:", error)-->
<!--    article.value.title = "加载失败"-->
<!--    article.value.content = "未找到该文章或接口异常"-->
<!--  }-->
<!--}-->


<!--// const fetchArticleData = (id) => {-->
<!--//   // 模拟数据源-->
<!--//   const mockData = {-->
<!--//     '1': {-->
<!--//       title: '从 RNN 到 Transformer',-->
<!--//       date: '2026-02-20',-->
<!--//       tags: ['Transformer', 'LSTM'],-->
<!--//       content: `# 深度学习核心面试题专项突破：从 RNN 到 Transformer-->
<!--//-->
<!--// 本篇总结了深度学习面试中最高频的四个核心知识点：LSTM 机制、CNN 感受野与文本卷积、ResNet 残差原理以及 Transformer FFN 的作用。-->
<!--//-->
<!--// -&#45;&#45;-->
<!--//-->
<!--// ## 92. LSTM 的核心计算过程-->
<!--// LSTM 通过“门控机制”解决了标准 RNN 的梯度消失问题，实现了长距离记忆。-->
<!--//-->
<!--// ### 三个核心门控：-->
<!--// 1. **遗忘门 (Forget Gate)**：决定丢弃上一时刻细胞状态 $C_{t-1}$ 中的哪些冗余信息。-->
<!--// 2. **输入门 (Input Gate)**：决定当前输入 $x_t$ 中哪些新信息要存入细胞状态。-->
<!--// 3. **输出门 (Output Gate)**：基于更新后的细胞状态 $C_t$，决定输出什么作为隐藏状态 $h_t$。-->
<!--//-->
<!--// ### 两个关键状态：-->
<!--// * **细胞状态 (Cell State, $C_t$)**：贯穿整个序列的“主干道”，负责长距离记忆。-->
<!--// * **隐藏状态 (Hidden State, $h_t$)**：负责当前时刻的预测，并传递给下一时刻。-->
<!--//-->
<!--// -&#45;&#45;-->
<!--//-->
<!--// ## 93. CNN 感受野与文本卷积 (TextCNN)-->
<!--//-->
<!--// ### 什么是感受野 (Receptive Field)？-->
<!--// 感受野是指 Feature Map 上任何一个点映射回原始输入图上能够“看到”的区域大小。感受野越大，网络捕捉的全局特征和上下文信息就越强。-->
<!--//-->
<!--// ### CNN 用于文本卷积的原理-->
<!--// 在 Transformer 普及前，TextCNN 是文本分类的主流。-->
<!--// * **输入形式**：文本被表征为 $[Sequence\\_length, Embedding\\_Dim]$ 的矩阵。-->
<!--// * **卷积核操作 (1D)**：卷积核宽度固定等于词向量维度，仅在高度（时间步方向）滑动。-->
<!--// * **捕捉信息**：本质是提取**局部语义**。高度为 2 的卷积核捕捉 Bi-gram（双词组）特征，高度为 3 则捕捉 Tri-gram（三词组）特征。-->
<!--//-->
<!--// -&#45;&#45;-->
<!--//-->
<!--// ## 94. 残差网络 (ResNet) 的原理-->
<!--// 为了解决深层网络中的**梯度消失**和**退化问题**，ResNet 引入了“跳跃连接”。-->
<!--//-->
<!--// * **核心公式**：$y = F(x) + x$-->
<!--// * **原理**：网络学习的是残差映射 $F(x) = y - x$。如果这一层学不到东西，$F(x)$ 趋近于 0，网络退化为恒等映射，保证了性能不退化。-->
<!--// * **梯度传播**：在反向传播时，梯度可以通过恒等映射的“高速公路”直接传递到浅层，有效缓解了梯度消失。-->
<!--//-->
<!--// -&#45;&#45;-->
<!--//-->
<!--// ## 95. Transformer 前馈神经网络 (FFN) 的作用-->
<!--// FFN 是 Point-Wise 的，即对序列中每个 Token 独立操作：-->
<!--// $$FFN(x) = \\text{Activation}(xW_1 + b_1)W_2 + b_2$$-->
<!--//-->
<!--// ### 核心作用：-->
<!--// 1. **引入非线性**：Attention 本质是加权平均（线性操作），FFN 通过激活函数提供非线性拟合能力。-->
<!--// 2. **特征加工**：Attention 负责“汇聚”上下文，FFN 负责对汇聚后的信息进行“深度加工与整合”。`-->
<!--//     },-->
<!--//     '2': {-->
<!--//       title: '从零开始：基于 Vue3 + Element Plus 的个人技术博客搭建指南',-->
<!--//       date: '2026-02-18',-->
<!--//       tags: ['Vue3', '前端', '工程化'],-->
<!--//       content: `-->
<!--//     # 基于 Vue3 + Element Plus 的个人技术博客搭建指南-->
<!--//-->
<!--//     搭建一个属于自己的博客是技术成长的第一步。本文将详细记录如何利用 Vue3 全家桶和 Element Plus 构建一个高性能、响应式的技术博客系统。-->
<!--//-->
<!--//     -&#45;&#45;-->
<!--//-->
<!--//     ## 一、 技术栈选型-->
<!--//     * **框架**：Vue 3 (Composition API) - 享受极致的开发体验。-->
<!--//     * **构建工具**：Vite - 毫秒级的热更新。-->
<!--//     * **UI 组件库**：Element Plus - 简洁美观的桌面端组件。-->
<!--//     * **路由管理**：Vue Router - 实现单页面应用（SPA）的无缝切换。-->
<!--//     * **文本渲染**：Marked + Highlight.js - 让你的技术文章支持 Markdown 与代码高亮。-->
<!--//-->
<!--//     -&#45;&#45;-->
<!--//-->
<!--//     ## 二、 核心搭建步骤-->
<!--//-->
<!--//     ### 1. 项目初始化-->
<!--//     使用 Vite 快速创建项目模板：-->
<!--//     \`\`\`bash-->
<!--//     npm create vite@latest my-blog &#45;&#45; &#45;&#45;template vue-->
<!--//     cd my-blog-->
<!--//     npm install-->
<!--//     \`\`\`-->
<!--//-->
<!--//     ### 2. 集成 Element Plus-->
<!--//     安装 UI 库并配置自动按需导入（推荐方案，减少打包体积）：-->
<!--//     \`\`\`bash-->
<!--//     npm install element-plus @element-plus/icons-vue-->
<!--//     \`\`\`-->
<!--//-->
<!--//     ### 3. 构建响应式布局-->
<!--//     在 \`App.vue\` 中，我们采用经典的“上-中-下”结构。为了让内容在宽屏显示器上不被拉伸，我们给中间层设置一个 \`max-width: 1200px\`：-->
<!--//     \`\`\`css-->
<!--//     .main-container {-->
<!--//       max-width: 1200px;-->
<!--//       margin: 0 auto;-->
<!--//       padding: 20px;-->
<!--//     }-->
<!--//     \`\`\`-->
<!--//-->
<!--//     -&#45;&#45;-->
<!--//-->
<!--//     ## 三、 关键功能实现-->
<!--//-->
<!--//     ### 1. 动态路由切换-->
<!--//     通过 Vue Router 配置动态参数，实现点击列表进入详情：-->
<!--//     \`\`\`javascript-->
<!--//     {-->
<!--//       path: '/article/:id',-->
<!--//       component: () => import('./views/ArticleDetail.vue')-->
<!--//     }-->
<!--//     \`\`\`-->
<!--//-->
<!--//     ### 2. Markdown 渲染引擎-->
<!--//     为了让博客支持直接展示代码，我们需要配置 Marked 渲染器：-->
<!--//     \`\`\`javascript-->
<!--//     import { marked } from 'marked';-->
<!--//     import hljs from 'highlight.js';-->
<!--//-->
<!--//     marked.setOptions({-->
<!--//       highlight: (code, lang) => hljs.highlightAuto(code).value-->
<!--//     });-->
<!--//     \`\`\`-->
<!--//-->
<!--//     -&#45;&#45;-->
<!--//-->
<!--//     ## 四、 进阶优化建议-->
<!--//-->
<!--//     1.  **全局 AI 助手**：在 \`App.vue\` 中挂载一个悬浮窗口，集成大模型 API（如 DeepSeek 或 Qwen），打造智能面试助手。-->
<!--//     2.  **SEO 优化**：使用预渲染插件或切换到 Nuxt.js (SSR) 以提升搜索引擎排名。-->
<!--//     3.  **持久化存储**：后期建议接入 Node.js + MongoDB，实现文章的动态管理和后台发布。-->
<!--//-->
<!--//     -&#45;&#45;-->
<!--//-->
<!--//     ## 五、 结语-->
<!--//     一个博客不仅仅是代码的堆砌，更是思考的留痕。希望这个指南能帮你迈出技术输出的第一步！-->
<!--//-->
<!--//     > **项目源码参考**：[我的 Github](https://github.com/CHM00)-->
<!--//     `-->
<!--//     },-->
<!--//     '3': {-->
<!--//       title: '大模型微调 PEFT vs LLaMA-Factory：两种微调(SFT)模式深度对比与原理解析',-->
<!--//       date: '2026-02-22',-->
<!--//       tags: ['AI', 'LLM', '微调'],-->
<!--//       content: `-->
<!--// # 大模型微调 PEFT vs LLaMA-Factory：两种微调(SFT)模式深度对比与原理解析-->
<!--//-->
<!--// 在 LLM（大语言模型）微调的圈子里，开发者通常会接触到两种截然不同的流派：一种是**原生代码流**，即直接使用 HuggingFace Transformers 和 PEFT 库编写 Python 代码；另一种是**框架工具流**，以 LLaMA-Factory 为代表的集成化工具。-->
<!--//-->
<!--// -&#45;&#45;-->
<!--//-->
<!--// ## 一、 两种微调模式简介-->
<!--//-->
<!--// ### 1. PEFT-->
<!--// **核心逻辑**：开发者需要自己处理数据清洗、Tokenizer 编码、Label Masking（标签掩码）、模型加载、LoRA 配置挂载以及训练循环。-->
<!--//-->
<!--// ### 2. LLaMA-Factory-->
<!--// 这是目前工业界和学术界快速迭代的首选。通过**配置驱动**（YAML 或 命令行参数）来控制训练。-->
<!--//-->
<!--// -&#45;&#45;-->
<!--//-->
<!--// ## 二、 核心实现流程对比-->
<!--//-->
<!--// ### 1. 数据预处理-->
<!--// * **PEFT**：需要手动编写函数处理 Prompt 格式（如 \`<|im_start|>\`）和 Loss 掩码计算。-->
<!--// * **LLaMA-Factory**：指定 \`&#45;&#45;template qwen\` 即可，内置模板库自动处理拼接。-->
<!--//-->
<!--// ### 2. 模型加载与 LoRA 挂载-->
<!--// * **PEFT**：显式定义 \`LoraConfig\` 并调用 \`get_peft_model\`。-->
<!--// * **LLaMA-Factory**：参数化配置 \`&#45;&#45;lora_target all\` 自动识别所有线性层。-->
<!--//-->
<!--// -&#45;&#45;-->
<!--//-->
<!--// ## 三、 PEFT与LlamaFactory在Autodl的实现-->
<!--// ### LlamaFactory 强化学习 (DPO) 示例：-->
<!--// \`\`\`bash-->
<!--// llamafactory-cli train \\-->
<!--//     &#45;&#45;stage dpo \\-->
<!--//     &#45;&#45;model_name_or_path qwen/Qwen2.5-0.5B-Instruct \\-->
<!--//     &#45;&#45;finetuning_type lora \\-->
<!--//     &#45;&#45;template qwen \\-->
<!--//     &#45;&#45;dataset dpo_zh_demo \\-->
<!--//     &#45;&#45;lora_target all \\-->
<!--//     &#45;&#45;fp16 True-->
<!--// \`\`\`-->
<!--//-->
<!--// -&#45;&#45;-->
<!--//-->
<!--// ## 四、 结语-->
<!--// **LLaMA-Factory 本质上就是一套写得非常健壮的“原生代码”**。建议先用框架跑通流程，再深入 PEFT 源码进行魔改。-->
<!--//     `-->
<!--//     }-->
<!--//   }-->
<!--//   // 模拟网络延迟-->
<!--//   setTimeout(() => {-->
<!--//     if (mockData[id]) {-->
<!--//       article.value = { id, ...mockData[id] }-->
<!--//     } else {-->
<!--//       article.value.title = '文章不存在'-->
<!--//     }-->
<!--//   }, 300)-->
<!--// }-->
<!--</script>-->

<!--<style scoped>-->
<!--.article-detail-container {-->
<!--  padding-bottom: 40px;-->
<!--}-->

<!--.back-action {-->
<!--  margin-bottom: 15px;-->
<!--}-->

<!--.article-content-card {-->
<!--  border-radius: 8px;-->
<!--  border: none;-->
<!--}-->

<!--.article-header {-->
<!--  text-align: center;-->
<!--  padding: 20px 0;-->
<!--}-->

<!--.article-header .title {-->
<!--  font-size: 28px;-->
<!--  color: #2c3e50;-->
<!--  margin-bottom: 15px;-->
<!--}-->

<!--.article-header .meta {-->
<!--  color: #909399;-->
<!--  font-size: 14px;-->
<!--}-->

<!--.mx-1 {-->
<!--  margin: 0 4px;-->
<!--}-->

<!--/* Markdown 样式修饰（可以按需引入 github-markdown-css） */-->
<!--.markdown-body {-->
<!--  line-height: 1.8;-->
<!--  font-size: 16px;-->
<!--  color: #333;-->
<!--}-->
<!--.markdown-body :deep(h2) {-->
<!--  border-bottom: 1px solid #eee;-->
<!--  padding-bottom: 10px;-->
<!--  margin-top: 30px;-->
<!--}-->
<!--.markdown-body :deep(pre) {-->
<!--  background: #f6f8fa;-->
<!--  padding: 16px;-->
<!--  border-radius: 6px;-->
<!--  overflow: auto;-->
<!--}-->
<!--</style>-->


<!--<template>-->
<!--  <div class="article-detail-container">-->
<!--    <div class="back-action">-->
<!--      <el-button @click="router.back()" link>🔙 返回列表</el-button>-->
<!--    </div>-->

<!--    <el-card class="article-content-card" shadow="never">-->
<!--      <template #header>-->
<!--        <div class="article-header">-->
<!--          <h1 class="title">{{ article.title }}</h1>-->
<!--          <div class="meta" v-if="article.date">-->
<!--            <span>📅 发布于: {{ article.date }}</span>-->
<!--            <el-divider direction="vertical" />-->
<!--            <span>🏷️ 标签:-->
<!--              <el-tag v-for="tag in article.tags" :key="tag" size="small" class="mx-1">-->
<!--                {{ tag }}-->
<!--              </el-tag>-->
<!--            </span>-->
<!--          </div>-->
<!--        </div>-->
<!--      </template>-->

<!--      <div class="markdown-body" v-html="renderedContent"></div>-->
<!--    </el-card>-->
<!--  </div>-->
<!--</template>-->

<!--<script setup>-->
<!--import { ref, onMounted, computed } from 'vue'-->
<!--import { useRoute, useRouter } from 'vue-router'-->
<!--// import { marked } from 'marked'-->
<!--// import hljs from 'highlight.js'-->
<!--// import 'highlight.js/styles/github-dark.css'-->
<!--import axios from 'axios'-->



<!--import 'katex/dist/katex.min.css';-->
<!--import { marked } from 'marked';-->
<!--import markedKatex from 'marked-katex-extension';-->
<!--import hljs from 'highlight.js';-->
<!--import 'highlight.js/styles/github-dark.css';-->

<!--// 使用扩展-->
<!--marked.use(markedKatex({-->
<!--  throwOnError: false, // 即使公式写错也不要让整个页面崩溃-->
<!--  displayMode: false   // 默认非块级模式，它会自动根据 $ 或 $$ 识别-->
<!--}));-->

<!--marked.setOptions({-->
<!--  highlight: function (code, lang) {-->
<!--    const language = hljs.getLanguage(lang) ? lang : 'plaintext';-->
<!--    return hljs.highlight(code, { language }).value;-->
<!--  },-->
<!--  langPrefix: 'hljs language-'-->
<!--})-->

<!--const route = useRoute()-->
<!--const router = useRouter()-->

<!--const article = ref({-->
<!--  id: null,-->
<!--  title: '努力加载中...',-->
<!--  date: '',-->
<!--  tags: [],-->
<!--  content: ''-->
<!--})-->

<!--const renderedContent = computed(() => {-->
<!--  return marked(article.value.content || '')-->
<!--})-->

<!--onMounted(() => {-->
<!--  const articleId = route.params.id-->
<!--  fetchArticleData(articleId)-->
<!--})-->

<!--const fetchArticleData = async (id) => {-->
<!--  try {-->
<!--    // 请求真实后端获取文章-->
<!--    const res = await axios.get(`http://150.158.123.242:8000/api/articles/${id}`)-->
<!--    if (res.data) {-->
<!--      article.value = res.data-->
<!--    }-->
<!--  } catch (error) {-->
<!--    console.error("加载文章失败:", error)-->
<!--    article.value.title = '文章加载失败'-->
<!--    article.value.content = '> 无法连接到后端，请检查 FastAPI 服务是否正常运行。'-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--<style scoped>-->
<!--/* 同样保留原有样式即可 */-->
<!--.article-detail-container { padding-bottom: 40px; }-->
<!--.back-action { margin-bottom: 15px; }-->
<!--.article-content-card { border-radius: 8px; border: none; }-->
<!--.article-header { text-align: center; padding: 20px 0; }-->
<!--.article-header .title { font-size: 28px; color: #2c3e50; margin-bottom: 15px; }-->
<!--.article-header .meta { color: #909399; font-size: 14px; }-->
<!--.mx-1 { margin: 0 4px; }-->
<!--.markdown-body { line-height: 1.8; font-size: 16px; color: #333; }-->
<!--.markdown-body :deep(h2) { border-bottom: 1px solid #eee; padding-bottom: 10px; margin-top: 30px; }-->
<!--.markdown-body :deep(pre) { background: #f6f8fa; padding: 16px; border-radius: 6px; overflow: auto; }-->
<!--</style>-->


<!--<template>-->
<!--  <el-row :gutter="20">-->
<!--    <el-col :span="18">-->
<!--      <el-card shadow="hover" class="article-detail-card">-->
<!--        <div v-if="loading" style="text-align: center; padding: 40px;">加载中...</div>-->

<!--        <div v-else-if="article">-->
<!--          <h1 class="detail-title">{{ article.title }}</h1>-->
<!--          <div class="detail-meta">-->
<!--            <span>📅 {{ article.date }}</span>-->
<!--            <span style="margin-left: 15px">-->
<!--               <el-tag v-for="tag in article.tags" :key="tag" size="small" style="margin-right:5px">{{ tag }}</el-tag>-->
<!--            </span>-->
<!--          </div>-->

<!--          <el-divider />-->

<!--          <v-md-preview :text="article.content"></v-md-preview>-->
<!--        </div>-->
<!--      </el-card>-->
<!--    </el-col>-->

<!--    <el-col :span="6">-->
<!--        </el-col>-->
<!--  </el-row>-->
<!--</template>-->

<!--<script setup>-->
<!--import { ref, onMounted } from 'vue'-->
<!--import { useRoute } from 'vue-router'-->
<!--import request from '@/utils/request'-->

<!--const route = useRoute()-->
<!--const article = ref(null)-->
<!--const loading = ref(false)-->

<!--onMounted(async () => {-->
<!--  loading.value = true-->
<!--  try {-->
<!--    const id = route.params.id-->
<!--    const res = await request.get(`/api/articles/${id}`)-->
<!--    article.value = res.data-->
<!--  } catch (error) {-->
<!--    console.error(error)-->
<!--  } finally {-->
<!--    loading.value = false-->
<!--  }-->
<!--})-->
<!--</script>-->

<!--<style scoped>-->
<!--.article-detail-card { min-height: 80vh; border-radius: 8px; border: none; }-->
<!--.detail-title { font-size: 28px; margin-bottom: 15px; color: #333; text-align: center;}-->
<!--.detail-meta { text-align: center; color: #999; margin-bottom: 20px; }-->
<!--</style>-->

<!--<template>-->
<!--  <el-row :gutter="20">-->
<!--    <el-col :span="18">-->
<!--      <el-card shadow="hover" class="article-detail-card">-->

<!--        <div class="header-container">-->
<!--          <el-page-header-->
<!--            @back="goBack"-->
<!--            content="文章详情"-->
<!--            title="返回列表"-->
<!--          >-->
<!--          </el-page-header>-->
<!--        </div>-->
<!--        <el-divider style="margin: 15px 0;" />-->

<!--        <div v-if="loading" style="text-align: center; padding: 40px; color: #999;">-->
<!--          <el-icon class="is-loading"><Loading /></el-icon> 加载中...-->
<!--        </div>-->

<!--        <div v-else-if="article">-->
<!--          <h1 class="detail-title">{{ article.title }}</h1>-->

<!--          <div class="detail-meta">-->
<!--            <span>📅 {{ article.date }}</span>-->
<!--            <span style="margin-left: 15px">-->
<!--               <el-tag-->
<!--                 v-for="tag in article.tags"-->
<!--                 :key="tag"-->
<!--                 size="small"-->
<!--                 type="info"-->
<!--                 effect="plain"-->
<!--                 style="margin-right:5px"-->
<!--               >-->
<!--                 {{ tag }}-->
<!--               </el-tag>-->
<!--            </span>-->
<!--          </div>-->

<!--          <div class="markdown-content">-->
<!--             <v-md-preview :text="article.content"></v-md-preview>-->
<!--          </div>-->
<!--        </div>-->

<!--        <el-empty v-else description="文章不存在或已删除"></el-empty>-->

<!--      </el-card>-->
<!--    </el-col>-->

<!--    <el-col :span="6">-->
<!--      <el-card shadow="hover" class="sidebar-card">-->
<!--        <template #header><div class="card-header">📢 导航</div></template>-->
<!--        <el-button type="primary" style="width: 100%" @click="goBack">返回首页</el-button>-->
<!--      </el-card>-->
<!--    </el-col>-->
<!--  </el-row>-->
<!--</template>-->

<!--<script setup>-->
<!--import { ref, onMounted } from 'vue'-->
<!--import { useRoute, useRouter } from 'vue-router'-->
<!--import request from '@/utils/request'-->
<!--import { Loading } from '@element-plus/icons-vue' // 引入加载图标-->

<!--const route = useRoute()-->
<!--const router = useRouter()-->
<!--const article = ref(null)-->
<!--const loading = ref(false)-->

<!--// [关键逻辑]：返回上一页-->
<!--const goBack = () => {-->
<!--  // router.back() 能保留列表页的滚动位置和状态-->
<!--  // 如果没有上一页历史（比如直接打开链接），则强制回首页-->
<!--  if (window.history.state.back) {-->
<!--    router.back()-->
<!--  } else {-->
<!--    router.push('/')-->
<!--  }-->
<!--}-->

<!--onMounted(async () => {-->
<!--  loading.value = true-->
<!--  try {-->
<!--    const id = route.params.id-->
<!--    const res = await request.get(`/api/articles/${id}`)-->
<!--    article.value = res.data-->
<!--  } catch (error) {-->
<!--    console.error("加载文章详情失败:", error)-->
<!--  } finally {-->
<!--    loading.value = false-->
<!--  }-->
<!--})-->
<!--</script>-->

<!--<style scoped>-->
<!--.article-detail-card {-->
<!--  min-height: 80vh;-->
<!--  border-radius: 8px;-->
<!--  border: none;-->
<!--}-->

<!--.header-container {-->
<!--  margin-bottom: 10px;-->
<!--}-->

<!--.detail-title {-->
<!--  font-size: 28px;-->
<!--  margin: 20px 0 15px 0;-->
<!--  color: #333;-->
<!--  text-align: center;-->
<!--  font-weight: 600;-->
<!--}-->

<!--.detail-meta {-->
<!--  text-align: center;-->
<!--  color: #999;-->
<!--  margin-bottom: 30px;-->
<!--  font-size: 14px;-->
<!--}-->

<!--/* 调整 Markdown 预览区域的样式，使其更美观 */-->
<!--.markdown-content :deep(.github-markdown-body) {-->
<!--  padding: 10px 20px;-->
<!--}-->
<!--</style>-->

<template>
  <div class="article-detail-container">
    <div class="back-action">
      <el-page-header @back="goBack" content="文章详情" title="返回列表" />
    </div>

    <el-card class="article-content-card" shadow="never">
      <template #header>
        <div class="article-header">
          <h1 class="title">{{ article.title }}</h1>
          <div class="meta" v-if="article.date">
            <span>📅 发布于: {{ article.date }}</span>
            <el-divider direction="vertical" />
            <span>🏷️ 标签:
              <el-tag v-for="tag in article.tags" :key="tag" size="small" class="mx-1">
                {{ tag }}
              </el-tag>
            </span>
          </div>
        </div>
      </template>

      <div class="markdown-body-wrapper">
         <v-md-preview :text="article.content"></v-md-preview>
      </div>

      <el-empty v-if="!article.content && !loading" description="暂无内容"></el-empty>
    </el-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import request from '@/utils/request' // 使用封装好的 request

const route = useRoute()
const router = useRouter()
const loading = ref(false)

const article = ref({
  id: null,
  title: '加载中...',
  date: '',
  tags: [],
  content: ''
})

// 返回上一页逻辑
const goBack = () => {
  if (window.history.state.back) {
    router.back()
  } else {
    router.push('/')
  }
}

onMounted(async () => {
  const articleId = route.params.id
  loading.value = true
  try {
    const res = await request.get(`/api/articles/${articleId}`)
    if (res.data) {
      article.value = res.data
    }
  } catch (error) {
    console.error("加载文章失败:", error)
    article.value.title = '加载失败'
    article.value.content = '> ❌ 无法获取文章内容，请检查网络或后端服务。'
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.article-detail-container {
  max-width: 1000px; /* 限制最大宽度，阅读体验更好 */
  margin: 0 auto;
  padding: 20px;
}

.back-action {
  margin-bottom: 20px;
}

.article-content-card {
  border-radius: 8px;
  border: none;
  min-height: 600px;
}

.article-header {
  text-align: center;
  padding: 10px 0 20px;
}

.title {
  font-size: 28px;
  color: #2c3e50;
  margin-bottom: 15px;
  font-weight: 600;
}

.meta {
  color: #909399;
  font-size: 14px;
}

.mx-1 {
  margin: 0 4px;
}

/* 调整 v-md-editor 的默认边距，使其与卡片更融合 */
.markdown-body-wrapper :deep(.github-markdown-body) {
  padding: 10px 20px;
}
</style>