<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="login-container">
    <el-card class="login-card" shadow="hover">
      <h2>后台管理登录</h2>
      <el-form :model="form" label-width="60px">
        <el-form-item label="账号">
          <el-input v-model="form.username" placeholder="请输入管理员账号" />
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="form.password" type="password" placeholder="请输入密码" show-password @keyup.enter="handleLogin" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleLogin" :loading="loading" style="width: 100%;">登 录</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import axios from 'axios'

const router = useRouter()
const form = ref({ username: '', password: '' })
const loading = ref(false)

const handleLogin = async () => {
  if (!form.value.username || !form.value.password) {
    ElMessage.warning('账号和密码不能为空')
    return
  }
  loading.value = true
  try {
    // FastAPI 的 OAuth2 需要表单格式 (URLSearchParams) 而不是 JSON
    const params = new URLSearchParams()
    params.append('username', form.value.username)
    params.append('password', form.value.password)

    const res = await axios.post('http://150.158.123.242:8000/api/login', params)

    // 登录成功，将 Token 存入浏览器的 localStorage
    localStorage.setItem('admin_token', res.data.access_token)
    ElMessage.success('登录成功！')

    // 跳转到发布页
    router.push('/admin')
  } catch (error) {
    ElMessage.error('登录失败：账号或密码错误')
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.login-container { display: flex; justify-content: center; align-items: center; height: 60vh; }
.login-card { width: 400px; padding: 20px; border-radius: 12px; }
h2 { text-align: center; margin-bottom: 30px; color: #333; }
</style>