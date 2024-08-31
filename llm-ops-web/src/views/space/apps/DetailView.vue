<template>
    <!--最外层容器-->
    <div class="min-h-screen">
        <!--顶部导航栏-->
        <header class="flex items-center h-[74px] bg-gray-100 border-b border-gray-200 px-4">
            顶部导航
        </header>
        <!--主内容区域-->
        <div class="flex flex-row h-[calc(100vh-74px)]">
            <!--左侧编排区域-->
            <div class="w-2/3 bg-gray-50 h-full">
                <header
                    class="flex items-center h-16 border-b border-gray-200 px-7 text-xl text-gray-700"
                >
                    应用编排
                </header>
                <div class="flex flex-row h-[calc(100% - 64px)]">
                    <div class="flex-1 border-r border-gray-200 p-6">人设与回复逻辑</div>
                    <div class="flex-1 p-6">应用能力</div>
                </div>
            </div>
            <!--右侧编排区域-->
            <div class="flex flex-col w-1/3 bg-white h-full">
                <header
                    class="flex flex-shrink-0 items-center h-16 px-4 text-xl bg-white border-b border-gray-200 shadow-sm"
                >
                    调试与预览
                </header>
                <!--调试对话界面-->
                <div
                    class="h-full min-h-0 px-6 py-7 overflow-x-hidden overflow-y-scroll scrollbar-w-none"
                >
                    <!--消息-->
                    <div
                        class="flex flex-row gap-2 mb-6"
                        v-for="message in messages"
                        :key="message.content"
                    >
                        <!--头像-->
                        <a-avatar
                            v-if="message.role == 'human'"
                            :size="30"
                            class="flex-shrink-0"
                            :style="{ backgroundColor: '#3370ff' }"
                            >刘</a-avatar
                        >
                        <!--头像-->
                        <a-avatar
                            v-else
                            :size="30"
                            :style="{ backgroundColor: '#00d0b6' }"
                            class="flex-shrink-0"
                        >
                            <icon-apps />
                        </a-avatar>
                        <!--实际消息-->
                        <div class="flex flex-col gap-2">
                            <div class="font-semibold text-gray-700">
                                {{ message.role === 'human' ? 'jaguarliu' : 'LLM Ops' }}
                            </div>
                            <div
                                v-if="message.role === 'human'"
                                class="max-w-max bg-blue-700 text-white border border-blue-800 px-4 py-3 rounded-2xl leading-5"
                            >
                                {{ message.content }}
                            </div>
                            <div
                                v-else
                                class="max-w-max bg-gray-100 text-gray-900 border border-gray-200 px-4 py-3 rounded-2xl leading-5"
                            >
                                {{ message.content }}
                            </div>
                        </div>
                    </div>
                    <div
                        v-if="!messages.length"
                        class="mt-[200px] flex flex-col items-center justify-center gap-2"
                    >
                        <a-avatar :size="70" shape="square" :style="{ backgroundColor: '#00d0b6' }">
                            <icon-apps />
                        </a-avatar>
                        <div class="text-2xl font-semibold text-gray-900 mt-2">LLM Ops</div>
                    </div>
                    <!--AI加载状态-->
                    <div v-if="isLoading" class="flex flex-row gap-2 mb-6">
                        <!--头像-->
                        <a-avatar
                            :size="30"
                            class="flex-shrink-0"
                            :style="{ backgroundColor: '#00d0b6' }"
                        >
                            <icon-apps></icon-apps>
                        </a-avatar>
                        <div class="flex flex-col gap-2">
                            <div class="font-semibold text-gray-700">LLM OPS</div>
                            <div
                                class="max-w-max bg-gray-100 text-gray-900 border border-gray-200 px-4 py-3 rounded-2xl leading-5"
                            >
                                <icon-loading />
                            </div>
                        </div>
                    </div>
                </div>
                <!--调试对话输入框-->
                <div class="w-full flex-shrink-0 flex flex-col">
                    <div class="px-6 flex items-center gap-4">
                        <a-button
                            type="text"
                            shape="circle"
                            class="flex-shrink-0"
                            @click="clearMessages"
                        >
                            <template #icon>
                                <icon-empty :size="16" :style="{ color: '#374151' }" />
                            </template>
                        </a-button>
                        <!--输入框-->
                        <div
                            class="h-[50px] flex items-center gap-2 px-4 flex-1 border border-gray-200 rounded-full"
                        >
                            <input
                                type="text"
                                class="flex-1 outline-0"
                                v-model="query"
                                @keyup.enter="send"
                            />
                            <a-button type="text" shape="circle" class="flex-shrink-0">
                                <template #icon>
                                    <icon-plus-circle :size="16" :style="{ color: '#374151' }" />
                                </template>
                            </a-button>
                            <a-button
                                type="text"
                                shape="circle"
                                class="flex-shrink-0"
                                @click="send"
                            >
                                <template #icon>
                                    <icon-send :size="16" :style="{ color: '#1d4ed8' }" />
                                </template>
                            </a-button>
                        </div>
                    </div>
                    <!--底部提示文字-->
                    <div class="text-center text-gray-500 text-xs py-4">
                        内容由 AI 生成，无法确保真实准确，仅供参考。
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { debugApp } from '@/services/app'
import { Message } from '@arco-design/web-vue'
import { ref } from 'vue'
import { useRoute } from 'vue-router'
const route = useRoute()

// 定义交互所需的数据
const query = ref('')
const messages = ref([] as any[])
const isLoading = ref(false)

const clearMessages = () => {
    messages.value = []
}

const send = async () => {
    // 获取用户输入的数据，判断是否合法
    if (!query.value) {
        Message.error('内容不能为空')
        return
    }
    // 上一次请求还没有处理完成，不允许发起新的请求
    if (isLoading.value) {
        Message.warning('请求处理中。。。')
        return
    }

    try {
        const humanQuery = query.value
        messages.value.push({
            role: 'human',
            content: humanQuery,
        })
        query.value = ''
        isLoading.value = true
        const resp = await debugApp(route.params.app_id as string, humanQuery)
        console.log(typeof resp)

        messages.value.push({
            role: 'ai',
            content: resp.data.content,
        })
    } finally {
        isLoading.value = false
    }
}
</script>

<style lang="scss" scoped></style>
