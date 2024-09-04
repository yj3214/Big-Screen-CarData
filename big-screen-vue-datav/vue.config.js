const path = require('path')
const resolve = dir => {
  return path.join(__dirname, dir)
}
module.exports = {
  publicPath: './',
  transpileDependencies: [],
  chainWebpack: config => {
    config.resolve.alias
      .set('_c', resolve('src/components')) // key,value自行定义，比如.set('@@', resolve('src/components'))
  },
  devServer: {  // 开发环境跨域情况的代理配置
    proxy: {
      // 【必要】访问自己搭建的后端服务器
      '/': {
        target: 'http://127.0.0.1:8000',
        changOrigin: true,
        ws: true,
        secure: false,
        pathRewrite: {
          '^/': '/'
        }
      },
    }
  }
}