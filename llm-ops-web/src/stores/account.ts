import { defineStore } from 'pinia'
import { ref } from 'vue'

const initAccount = {
    name: 'jaguarliu',
    email: '18829526908@163.com',
    avatar: '',
}

export const useAccountStore = defineStore('account', () => {
    // 定义数据
    const account = ref({ ...initAccount })
    // 函数/动作
    function update(params: any) {
        Object.assign(account.value, params)
    }

    function clear() {
        account.value = { ...initAccount }
    }

    return { account, update, clear }
})
