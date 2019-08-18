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