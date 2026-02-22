// import { createApp } from 'vue'
// import App from './App.vue'
// import ElementPlus from 'element-plus'
// import 'element-plus/dist/index.css'  // 样式
//
// const app = createApp(App)
// app.use(ElementPlus)
// app.mount('#app')

import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'  // 样式
import router from './router/index.js'  // 调整路径为你的路由文件位置，通常是 src/router/index.js

const app = createApp(App)
app.use(ElementPlus)
app.use(router)  // 添加这一行！
app.mount('#app')


