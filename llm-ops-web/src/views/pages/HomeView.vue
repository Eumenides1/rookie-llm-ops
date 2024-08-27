<template>
    <p>这是主页</p>
    <p>当前登录的账号是:{{ accountStore.account.name }}</p>
    <a-button type="primary" @click="updateName"> 更新名字</a-button>
</template>

<script setup lang="ts">
import { useAccountStore } from '@/stores/account'
const accountStore = useAccountStore()
function updateName() {
    accountStore.update({ name: 'eumendies' })
}
</script>

<style scoped></style>
