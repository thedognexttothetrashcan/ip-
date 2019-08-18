# Flask


## 基本工程
- 一个文件就实现了Web项目
- 项目拆分
   - 创建App
   - 初始化App


### 第三方插件使用
- 安装 
    - pip install xxx
- 初始化
    - 每个依赖的初始化需要查看对应文档
- 使用


### Flask-Script
- 实现命令行参数支持


### Flask-Blueprint
- 解决路由加载的循环引用问题
- 安装
    - pip install flask-blueprint
- 初始化
    - 使用自己的名字 + 路由所在文件的名字进行创建
    - 注册到App上
- 使用
    - 和app注册路由的使用，基本完全一致


### shell
- 终端窗口
- 集成了Flask项目环境的一个终端


### SQLAlchemy
- python的orm
- flask-sqlalchemy 针对于Flask进行的专项封装
- 使用
    - 安装
        - pip install flask-sqlalchemy
    - 初始化
        - 使用app去创建SQLAlchemy对象
    - 定义模型，使用
    
    
### flask-migrate
- 安装
    - pip install flask-migrate
- 初始化
    - 是帮助app为数据库迁移
    - 初始化需要app和db
    
    
### 缓存
- flask-cache
- flask-caching
- 安装
    - pip install flask-caching
- 初始化
    - 绑定app
    - 设置缓存配置
- 使用
    - 推荐使用装饰器实现
    - 也可以自己原生实现


### Flask 内置对象
- request
- session
- config
- g


### 自定义状态吗
- 600 数据删除失败
    - 601 删除的数据不存在
    - 602 删除的数据存在级联数据
    
### 优秀的程序
- 高内聚
- 低耦合
- 高扩展性


### 知识点
- os.getenv
    - 从系统中获取环境变量
- or
    - A or B
    - 如果A不为空，就取A的值，如果A未空就拿B的值
- python文件加载
    - 只有被使用被导入的文件才会加载
    
    
#### API接口
- 接口地址
    - /api/movies/
- 请求方法
    - GET
    - POST
- 请求参数
    - GET
        - 可能不需要参数
            - 就是直接访问模式
        - 必须提供提供用户令牌才可能
            - 需要用户系统，用户权限系统
    - POST
        - 字段  m_name   类型   string    是否必须  是
        - 字段  m_duration  类型   int     是否必须   否
        
- 请求结果
    - GET
        - {
            status: 200,
            msg: ok,
            data:[
                {
                    m_name: '西虹市首富',
                    m_duration: 60
                },
                {
                    m_name: '一出好戏',
                    m_duration': 90
                }
            ]
        }
    - POST
        - {
            status: 200,
            msg: ok,
            data:{
                m_name: 'PythonCoding',
                m_duration: 15
            }
        }
        


- 接口地址
    - /api/movies/{id}/
- 请求方法
    - GET
    - POST
    - DELETE
- 请求参数
    - XXX
    - YYY
- 如果一个路径可能存在多种动作
    - 可以通过其它参数实现
        - QueryString
            - action
                - login
                - register
        - header
     
    
    
### Flask-RESTful
- 安装
    - pip install flaks-restful
- 初始化
    - 使用app 进行api对象的初始化
- 使用
    - 创建Resource，继承系统的Resource进行实现
        - 使用函数名来，请求方式
    - 在api 对象注册资源
    
- 定制输入
    - reqparse
- 定制输出
    - 使用fileds
    - 使用字典格式进行定制
    - fields.List 列表 JSONArray
    - fields.Nested 级联，嵌套   内部嵌套还是字典
    - 可使用  marshal 函数 进行定制
        - 数据
        - 格式
    - 也可以使用  marshal_with  （格式）
    
    
### 用户
- 是所有开发的核心
- 用户字段
    - 用户名
    - 密码
    - 邮箱
    - 手机号
    - 状态
        - 激活
    - 头像
    - 是否删除 （逻辑）
- 用户权限


### 算法
- 编码
    - base64
    - urlencode
    - 支持某些 原本不支持的字符编码问题
- 摘要算法
    - 哈希算法
    - 散列算法，杂凑算法，指纹算法
    - 单向不可逆，输出长度固定
    - md5， sha1 , sha256 ...
    - 验证
- 加密算法
    - 对称加密
        - 一把钥匙，密钥
        - DES， AES
        - 效率高
    - 非对称加密
        - 一堆钥匙，公钥，私钥
        - 公钥加密，只能私钥解密
        - 私钥加密，只能去解
        - RSA
        - 安全性最高
- md5 
    - 128位的二进制
    - 转成32位十六进制 
    - 32位 Unicode
    
### 数据安全
- generate_password_hash
    - 相同的输入每次输出不一样
- check_password_hash
    - 验证密码正确性
- 实现机制
    - 将数据进行了hash算法
    - 添加了时间或者随机数等干扰数据
- 验证的时候
    - 将数据还原
    - 清除干扰数据
    
### Property
- 将函数变成属性使用
- 属性在被操作的时候，我们可以去动态切入到属性的调用上
- 对属性赋值
    - 通过setter来切入流程
- del xxx 删除属性
    - 可以铜鼓deleter 切入流程
    - session就是这么做的
    - del session['key'']
    
    
### 权限设计
- 用户表
    - 权限表
    - 用户权限表
- 用户表中添加一个权限字段
    - 可以包含多个权限


### 实现代码复用
- 高可用
- 可用方案
    - 同学提供了第一个方案，封装成装饰器
    - 做一个基类Api，提供了验证方式
    - 使用钩子函数，AOP面向切面
    
### Flask-Session
- Session 服务端会话技术
- flask中session的数据安全需用使用  secret_key
- 安装
    - pip install flask-session
- 初始化
    - 指定SESSION_TYPE 
- 使用
    - 原有的使用方式


### Flask-Debugtoolbar
- 添加一种新型调试方式
- 仅在页面中使用
- 安装
    - pip install flask-debugtoolbar
- 初始化
    - 需要配置SECRET_KEY 
    - 使用app初始化 DebugToolbar对象
    
    
### Flask钩子函数
- before_request
    - 日志
    - 黑白名单
        - 优先级名单
    - 反爬
- after_request
- error_handler
- 如果在蓝图上
    - 比app的钩子函数多
    - 但是优先级没有app的钩子函数高
    - 蓝图监控通常是本蓝图中
    
- 一分钟最多访问三十次    

    
    