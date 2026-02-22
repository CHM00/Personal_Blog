// import { createRouter, createWebHistory } from 'vue-router';
// import Home from '../views/Home.vue';
// import QtTutorial from '../views/QtTutorial.vue';
// // import AdminDashboard from '../views/admin/Dashboard.vue';
//
// const routes = [
//   { path: '/', component: Home },
//   { path: '/qt', component: QtTutorial },  // 像图片的 Qt 页面
//   // { path: '/admin', component: AdminDashboard, meta: { requiresAuth: true } },  // 后台
// ];
//
// const router = createRouter({ history: createWebHistory(), routes });
// export default router;

// import AdminPublish from '../views/AdminPublish.vue'; // 引入发布页
// import { createRouter, createWebHistory } from 'vue-router';
// import Home from '../views/Home.vue';
// import QtTutorial from '../views/QtTutorial.vue';
// import AboutMe from '../views/AboutMe.vue';
//
// const routes = [
//   { path: '/', component: Home },
//   { path: '/qt', component: QtTutorial },
//   { path: '/about', component: AboutMe },
//   { path: '/admin', component: AdminPublish }, // <--- 新增后台发布路由
//   // 新增这一行：文章详情页路由。动态参数 :id 代表文章的编号
//   // 这里使用了路由懒加载（() => import(...)），有助于提升首页加载速度
//   {
//     path: '/article/:id',
//     component: () => import('../views/ArticleDetail.vue')
//   }
// ];
//
// const router = createRouter({ history: createWebHistory(), routes });
// export default router;


// import { createRouter, createWebHistory } from 'vue-router';
// import Home from '../views/Home.vue';
// import QtTutorial from '../views/QtTutorial.vue';
// // 建议新建一个简单的 About.vue
// const About = { template: '<div style="padding:20px">这是关于我的页面</div>' };
//
// const routes = [
//   { path: '/', name: 'Home', component: Home },
//   { path: '/qt', name: 'Qt', component: QtTutorial },
//   { path: '/about', name: 'About', component: About },
//   // 移除或暂时隐藏未实现的 admin
// ];
//
// const router = createRouter({
//   history: createWebHistory(),
//   routes
// });
//
// export default router;


// import { createRouter, createWebHistory } from 'vue-router';
// import Home from '../views/Home.vue';
// import QtTutorial from '../views/QtTutorial.vue';
// import AboutMe from '../views/AboutMe.vue';
// import AdminPublish from '../views/AdminPublish.vue'; // 1. 引入发布页
//
// const routes = [
//   { path: '/', component: Home },
//   { path: '/qt', component: QtTutorial },
//   { path: '/about', component: AboutMe },
//   { path: '/admin', component: AdminPublish }, // 2. 注册后台发布路由
//   {
//     path: '/article/:id',
//     component: () => import('../views/ArticleDetail.vue')
//   }
// ];
//
// const router = createRouter({ history: createWebHistory(), routes });
// export default router;


import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import QtTutorial from '../views/QtTutorial.vue';
import AboutMe from '../views/AboutMe.vue';
import AdminPublish from '../views/AdminPublish.vue';
import Login from '../views/Login.vue'; // 引入登录页

const routes = [
  { path: '/', component: Home },
  { path: '/qt', component: QtTutorial },
  { path: '/about', component: AboutMe },
  { path: '/login', component: Login }, // 注册登录路由
  {
    path: '/admin',
    component: AdminPublish,
    meta: { requiresAuth: true } // 给后台打上“需要鉴权”的标记
  },
  { path: '/article/:id', component: () => import('../views/ArticleDetail.vue') }
];

const router = createRouter({ history: createWebHistory(), routes });

// 路由全局前置守卫：每次跳转页面前都会执行
router.beforeEach((to, from, next) => {
  // 如果去的页面需要鉴权
  if (to.meta.requiresAuth) {
    const token = localStorage.getItem('admin_token');
    if (token) {
      next(); // 有 Token，放行
    } else {
      next('/login'); // 没 Token，强制跳转到登录页
    }
  } else {
    next(); // 不需要鉴权的页面（如首页），直接放行
  }
});

export default router;