// 基础相应数据格式
export type BaseResponse<T> = {
    code: string
    message: string
    data: T
}

// 分页响应数据格式
export type BasePaginatorResponse<T> = BaseResponse<{
    list: Array<T>
    paginator: {
        total_page: number
        total_record: number
        current_page: number
        page_size: number
    }
}>
