<template>
  <div class="ai-chat-wrapper">
    <!-- 悬浮按钮 -->
    <button class="ai-toggle-btn" @click="toggleChat">
      面试
      助手
    </button>

    <!-- 聊天面板 -->
    <div v-if="isOpen" class="chat-panel">
      <div class="chat-header">
        <span>🤖 面试问答助手</span>
        <button class="close-btn" @click="toggleChat">×</button>
      </div>

      <div class="chat-messages" ref="messagesContainer">
        <div
          v-for="(msg, index) in messages"
          :key="index"
          class="message"
          :class="msg.type === 'user' ? 'user-msg' : 'ai-msg'"
        >
          {{ msg.text }}
          <span v-if="msg.loading" class="loading">...</span>
        </div>
      </div>

      <div class="chat-input-area">
        <input
          v-model="userInput"
          type="text"
          placeholder="输入你的问题..."
          @keyup.enter="sendMessage"
          ref="inputRef"
        />
        <button @click="sendMessage" :disabled="isSending">发送</button>
      </div>
    </div>
  </div>
</template>

<script setup>
// import { ref, nextTick, onMounted } from 'vue'
import { ref, nextTick } from 'vue'   // 删掉 onMounted
// 状态
const isOpen = ref(false)
const userInput = ref('')
const messages = ref([
  { type: 'ai', text: '你好！我是博主的 AI 助手。擅长C++、AI算法以及应用开发相关问题，你想了解什么？' }
])
const isSending = ref(false)
const messagesContainer = ref(null)
const inputRef = ref(null)

// 切换显示
const toggleChat = () => {
  isOpen.value = !isOpen.value
  if (isOpen.value) {
    nextTick(() => {
      inputRef.value?.focus()
    })
  }
}

// 发送消息
const sendMessage = async () => {
  const question = userInput.value.trim()
  if (!question || isSending.value) return

  // 添加用户消息
  messages.value.push({ type: 'user', text: question })
  userInput.value = ''

  // 添加 loading
  const loadingIndex = messages.value.push({ type: 'ai', text: '', loading: true }) - 1
  scrollToBottom()

  isSending.value = true

  try {
    const response = await fetch('http://150.158.123.242:8000/api/ask', {
      // 或 http://localhost:8000/api/ask   如果你在本地访问
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question })
    })
    // const response = await fetch('/api/ask', {
    //   method: 'POST',
    //   headers: { 'Content-Type': 'application/json' },
    //   body: JSON.stringify({ question })
    // })

    const data = await response.json()

    // 替换 loading 消息
    messages.value[loadingIndex] = {
      type: 'ai',
      text: data.status === 'success' ? data.answer : '抱歉，服务器开小差了：' + data.answer
    }
  } catch (err) {
    messages.value[loadingIndex] = {
      type: 'ai',
      text: '网络请求失败，请检查后端服务是否正常启动。'
    }
  } finally {
    isSending.value = false
    scrollToBottom()
  }
}

// 自动滚动到底部
const scrollToBottom = () => {
  nextTick(() => {
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
    }
  })
}
</script>

<style scoped>
/* 把你原 HTML 的所有样式复制过来，并加 scoped 避免污染全局 */
.ai-chat-wrapper {
  position: fixed;
  bottom: 30px;
  right: 30px;
  z-index: 1000;
}

.ai-toggle-btn {
  width: 60px;
  height: 60px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 50%;
  box-shadow: 0 4px 15px rgba(0,123,255,0.4);
  cursor: pointer;
  font-size: 16px;
  font-weight: bold;
  transition: transform 0.3s ease;
}

.ai-toggle-btn:hover {
  transform: scale(1.05);
}

.chat-panel {
  position: absolute;
  bottom: 80px;
  right: 0;
  width: 350px;
  height: 500px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 5px 25px rgba(0,0,0,0.15);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  border: 1px solid #e0e0e0;
}

/* 其余样式保持原样：.chat-header, .chat-messages, .message, .user-msg, .ai-msg, .loading, .chat-input-area, input, button 等 */
.chat-messages {
  flex: 1;
  padding: 15px;
  overflow-y: auto;
  background-color: #f9f9fa;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.message {
  max-width: 80%;
  padding: 10px 14px;
  border-radius: 8px;
  font-size: 14px;
  line-height: 1.5;
  word-wrap: break-word;
}

.user-msg {
  background-color: #007bff;
  color: white;
  align-self: flex-end;
  border-bottom-right-radius: 2px;
}

.ai-msg {
  background-color: white;
  color: #333;
  align-self: flex-start;
  border-bottom-left-radius: 2px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.loading {
  font-style: italic;
  color: #888;
  font-size: 12px;
}

.chat-input-area {
  display: flex;
  padding: 10px;
  background: white;
  border-top: 1px solid #eee;
}

.chat-input-area input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 20px;
  outline: none;
}

.chat-input-area input:focus {
  border-color: #007bff;
}

.chat-input-area button {
  background: none;
  border: none;
  color: #007bff;
  font-weight: bold;
  padding: 0 15px;
  cursor: pointer;
}

.chat-header {
  background-color: #007bff;
  color: white;
  padding: 15px;
  font-size: 16px;
  font-weight: bold;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.close-btn {
  background: none;
  border: none;
  color: white;
  font-size: 20px;
  cursor: pointer;
}
</style>