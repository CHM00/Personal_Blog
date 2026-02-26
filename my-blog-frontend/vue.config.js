// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })

// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true,
//   devServer: {
//     historyApiFallback: true,
//     allowedHosts: [
//       'chen5.asia',       // 允许您的主域名
//       'www.chen5.asia',   // 允许 www 子域名
//       '.chen5.asia'       // 匹配所有二级域名
//     ],
//     // 如果仍然报错，可以取消下面这一行的注释（仅限调试使用）
//     // client: { overlay: false }
//   }
// })

const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    // 1. 解决 "Invalid Host header" 问题
    allowedHosts: [
      'chen5.asia',
      'www.chen5.asia',
      '.chen5.asia'
    ],
    // 2. 配置客户端连接参数，强制使用 wss 协议
    client: {
      webSocketURL: 'wss://chen5.asia/ws',
    },
    // 3. 修复报错：指定 WebSocket 服务器实现类型为 'ws'
    webSocketServer: 'ws',

    // 4. 确保开发服务器监听所有网卡
    host: '0.0.0.0',
    port: 8080
  }
})
