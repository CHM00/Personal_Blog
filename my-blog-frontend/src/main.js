// import { createApp } from 'vue'
// import App from './App.vue'
// import ElementPlus from 'element-plus'
// import 'element-plus/dist/index.css'  // 样式
//
// const app = createApp(App)
// app.use(ElementPlus)
// app.mount('#app')

// import { createApp } from 'vue'
// import App from './App.vue'
// import ElementPlus from 'element-plus'
// import 'element-plus/dist/index.css'  // 样式
// import router from './router/index.js'  // 调整路径为你的路由文件位置，通常是 src/router/index.js
//
// const app = createApp(App)
// app.use(ElementPlus)
// app.use(router)  // 添加这一行！
// app.mount('#app')

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// 引入 Element Plus (假设你之前已经引了)
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

// --- Markdown 预览组件配置 ---
import VMdPreview from '@kangc/v-md-editor/lib/preview';
import '@kangc/v-md-editor/lib/style/preview.css';
// 引入 github 主题
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';
// 引入 highlight.js 代码高亮
import hljs from 'highlight.js';

VMdPreview.use(githubTheme, {
  Hljs: hljs,
});

const app = createApp(App)

// 注册图标
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

app.use(router)
app.use(ElementPlus)
app.use(VMdPreview) // 挂载 Markdown 预览组件
app.mount('#app')


