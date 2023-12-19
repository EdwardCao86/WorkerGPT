module.exports = {
    devServer: {
        proxy: {
            '/api/': {
                target: 'https://127.0.0.1:5000', // 目标路径，别忘了加http和端口号
                changeOrigin: true, // 是否跨域
                pathRewrite: {
                    '^/api': '' // 重写路径
                    // '^/123': ''  // 比如/123/admin/being/classes/classInfo 会被替代成/admin/being/classes/classInfo
                }
            }
        }
    }
}