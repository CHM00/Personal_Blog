
import axios from 'axios'
import { ElMessage } from 'element-plus'
import router from '@/router'

const instance = axios.create({
  baseURL: 'http://150.158.123.242:8000', // 你的后端地址
  timeout: 10000
})

// 响应拦截器
instance.interceptors.response.use(
  (response) => {
    return response
  },
  (error) => {
    // 检查是否是 401 错误
    if (error.response && error.response.status === 401) {
      ElMessage.error('登录已过期或无权限，请重新登录')

      // 1. 清除本地过期的 Token
      localStorage.removeItem('admin_token')

      // 2. 强制跳转到登录页
      router.push('/login')
    } else {
      ElMessage.error(error.message || '网络请求失败')
    }
    return Promise.reject(error)
  }
)

export default instance