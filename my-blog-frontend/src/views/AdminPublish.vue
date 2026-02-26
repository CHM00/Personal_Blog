<template>
  <div class="publish-container">
    <el-card shadow="never" class="publish-card">
      <h2>📝 发布新文章</h2>

      <el-form label-width="80px" :model="form">
        <el-form-item label="文章标题">
          <el-input v-model="form.title" placeholder="输入炫酷的标题..." />
        </el-form-item>

        <el-form-item label="标签">
          <el-input v-model="tagsInput" placeholder="输入标签，用逗号分隔，如：AI,Vue3,C++" />
        </el-form-item>

        <el-form-item label="文章摘要">
          <el-input v-model="form.summary" type="textarea" :rows="2" placeholder="一句话总结这篇文章..." />
        </el-form-item>

        <el-form-item label="正文内容">
          <el-input v-model="form.content" type="textarea" :rows="15" placeholder="支持 Markdown 语法..." style="font-family: monospace;" />
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="submitArticle" :loading="isSubmitting">发布文章</el-button>
          <el-button @click="resetForm">清空</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { ElMessage } from 'element-plus'
// import axios from 'axios'
import { useRouter } from 'vue-router'
import request from '@/utils/request' // 引入刚才封装的拦截器对象


const router = useRouter()
const tagsInput = ref('')
const isSubmitting = ref(false)

const form = ref({
  title: '',
  summary: '',
  content: ''
})

const submitArticle = async () => {
  if (!form.value.title || !form.value.content) {
    ElMessage.warning('标题和内容不能为空！')
    return
  }

  isSubmitting.value = true
  try {
    // 将逗号分隔的字符串转为数组
    const tagsArray = tagsInput.value.split(',').map(t => t.trim()).filter(t => t)

    const payload = {
      title: form.value.title,
      tags: tagsArray,
      summary: form.value.summary,
      content: form.value.content
    }

    // 替换成你的后端地址
    // await axios.post('http://150.158.123.242:8000/api/articles', payload)


    const token = localStorage.getItem('admin_token')
    // 使用 request 代替 axios
    await request.post('/articles', payload, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    ElMessage.success('发布成功！')
    router.push('/')
    } catch (error) {
      // 这里的 401 错误会被拦截器自动处理，组件内只需处理业务逻辑
      console.error('发布失败', error)
    }finally {
    isSubmitting.value = false
  }


  //   // 修改后的代码：提取 Token 并在 headers 里携带
  //   const token = localStorage.getItem('admin_token')
  //   await axios.post('http://150.158.123.242:8000/api/articles', payload, {
  //     headers: {
  //       Authorization: `Bearer ${token}`
  //     }
  //   })
  //   ElMessage.success('发布成功！AI助手已同步学习该文章。')
  //   router.push('/') // 发布成功后跳回首页
  // } catch (error) {
  //   ElMessage.error('发布失败，请检查后端服务。')
  //   console.error(error)
  // } finally {
  //   isSubmitting.value = false
  // }
}

const resetForm = () => {
  form.value = { title: '', summary: '', content: '' }
  tagsInput.value = ''
}
</script>

<style scoped>
.publish-container { max-width: 1000px; margin: 0 auto; padding: 20px; }
.publish-card { border-radius: 8px; }
h2 { text-align: center; margin-bottom: 30px; color: #333; }
</style>