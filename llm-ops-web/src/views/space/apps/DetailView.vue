<template>
    <a-button @click="debug">发起请求</a-button>
</template>

<script setup lang="ts">
import { post } from '@/utils/request'
async function debug() {
    const response = await post('/app/9b4305e4-4b94-47da-8843-a495133b3d44/debug', {
        body: {
            query: '你好',
        },
    })
    console.log(response)
}
</script>

<style lang="scss" scoped></style>
