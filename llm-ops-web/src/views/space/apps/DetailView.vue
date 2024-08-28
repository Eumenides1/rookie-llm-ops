<template>
    <a-button @click="debug">发起请求</a-button>
</template>

<script setup lang="ts">
import { post } from '@/utils/request'
async function debug() {
    const response = await post('/apps/completion', {
        body: {
            query: '你好',
        },
    })
    console.log(response)
}
</script>

<style lang="scss" scoped></style>
