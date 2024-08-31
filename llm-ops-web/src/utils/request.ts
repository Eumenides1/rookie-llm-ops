import { apiPrefix, httpCode } from '@/config'
import { Message } from '@arco-design/web-vue'
// 超时时间控制
const TIME_OUT = 100000

// 基础配置
const baseFetchOptions = {
    method: 'GET',
    mode: 'cors',
    credentials: 'include',
    headers: new Headers({
        'Content-Type': 'application/json',
    }),
    redirect: 'follow',
}

type FetchOptionType = Omit<RequestInit, 'body'> & {
    params?: Record<string, any>
    body?: BodyInit | Record<string, any> | null
}

// 封装基础的 fetch
const baseFetch = <T>(url: string, fetchOptions: FetchOptionType): Promise<T> => {
    // 将配置信息合并
    const options: typeof baseFetchOptions & FetchOptionType = Object.assign(
        {},
        baseFetchOptions,
        fetchOptions,
    )
    // 组装 url
    let urlWithPrefix = `${apiPrefix}${url.startsWith('/') ? url : `/${url}`}`
    // 结构出对应的请求方法，params，body 参数
    const { method, params, body } = options
    // 如果请求是 GET 并且传递了 params
    if (method === 'GET' && params) {
        const paramsArray: string[] = []
        Object.keys(params).forEach((key) => {
            paramsArray.push(`${key}=${encodeURIComponent(params[key])}`)
        })
        if (urlWithPrefix.search(/\?/) === -1) {
            urlWithPrefix += `?${paramsArray.join('&')}`
        } else {
            urlWithPrefix += `&${paramsArray.join('&')}`
        }

        delete options.params
    }

    if (body) {
        options.body = JSON.stringify(body)
    }

    return Promise.race([
        new Promise((resolve, reject) => {
            setTimeout(() => {
                reject('接口已超时')
            }, TIME_OUT)
        }),
        // 发起一个正常请求
        new Promise((resolve, reject) => {
            globalThis
                .fetch(urlWithPrefix, options as RequestInit)
                .then(async (res) => {
                    const json = await res.json()
                    if (json.code === httpCode.success) {
                        resolve(json)
                    } else {
                        Message.error(json.message)
                        reject(new Error(json.message))
                    }
                })
                .catch((err) => {
                    Message.error(err.message)
                    reject(err)
                })
        }),
    ]) as Promise<T>
}

export const request = <T>(url: string, options = {}) => {
    return baseFetch<T>(url, options)
}

export const get = <T>(url: string, options = {}) => {
    return request<T>(url, Object.assign({}, options, { method: 'GET' }))
}

export const post = <T>(url: string, options = {}) => {
    return request<T>(url, Object.assign({}, options, { method: 'POST' }))
}
