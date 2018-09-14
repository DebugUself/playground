## CH4 数据库开发

## 主题

* SQL 语言和 SQLite 数据库管理系统
    * CRUD 基础交互
        * Create,Read,Update and Delete
    * ORM 
        * Objection Relation Mapping

## 任务

* 基础任务
    * 基本功能
        * 输入城市名，获取该城市最新天气情况
        * 点击「帮助」，获取帮助信息
        * 点击「历史」，获取历史查询信息
    * 扩展功能
        * 使用 SQLite 存储天气数据
        * 用户可通过 Web 页面的用户更正按钮，更正天气数据到数据库
        * 如果在5分钟以内查询相同的数据, 不用通过 API 访问远程数据源（较难，选做）
        * 可记录多个用户不同的查询历史（较难，选做）
    * 部署在命令行界面
* 进阶任务 
    * 学有余力，可以使用 Flask 的扩展 Flask-SQLAlchemy 来替代 sqlite3 模块，和 Flask 更好地结合。

## 路线

* [ ] 查看以往代码,梳理工作原理与数据流
    * [ ] 迁移相关代码,完成基本工具的 DEMO
* [ ] 数据存储格式的讨论
    * [ ] 直接拉取单次 API 查询
    * [ ] 将整个文件拉取到本地 ,固定时间轮询更新,用户查询直接在本地

## 探索记录

- I 看看到python 的衍生文件与sublime 的布局结构文件,所以想设置 ignore 文件来清理仓库中的文件
    + A github help
        * => [Ignoring files - User Documentation](https://help.github.com/articles/ignoring-files/)

## 0 Ignoring files 概念与实操

- O **概念卡: Ignoring files**
    + 功能: 
        + 告诉 git 哪些文件应该被忽视,不被 check in 到 github 远程仓库
    + 要点:
        * **local .gitignore**
            - 应用于单个 git 仓库文件
            - 进入git仓库根目录,`touch .gitignore`
            - 添加相应规则
        - **global .gitignore**
            - 应用于电脑上所有 git 仓库文件
            - 根目录创建 `~/.gitignore_global`
            - 添加相应规则
            - 激活设置文件
                - `git config --global core.excludesfile ~/.gitignore_global`
        + **.git/info/exclude** 
            * 用于那些不希望与他人分享的 `.gitignore` 规则
                - 那些只希望本地生成,不希望其他用户生成的文件
                    + 比如编辑器生成的文件 
                    + ...
            * 进入git仓库根目录,使用文本编辑器打开 `.git/info/exclude`
            * 添加相关规则
    + 注意: 
        * 已经被 check in 的文件无法被 `.gitignore` 忽视
        * 必须取消追踪这些文件
            - git rm --cached FILENAME
    + 资源:
        * 一般必要的设置
            * [Some common .gitignore configurations](https://gist.github.com/octocat/9257657)
        + 各种操作系统,语言,环境的. ignore 模板
            * [A collection of useful .gitignore templates](https://github.com/github/gitignore)

- A `.gitignore` 实操设置:
    + A 设置全局的 .gitignore 
        + Q .gitignore  应该写哪些内容?
            + I 查看 仓库模板
                * [zoom-quiet/scm: all kinds of SCM stuff](https://github.com/zoom-quiet/scm)
                * [du4proto/.gitignore](https://github.com/DebugUself/du4proto/blob/DU_tools/.gitignore)
                * [scm/.gitignore at master · zoom-quiet/scm](https://github.com/zoom-quiet/scm/blob/master/.gitignore)
                * [Some common .gitignore configurations](https://gist.github.com/octocat/9257657)
                * [gitignore/Python.gitignore at master · github/gitignore](https://github.com/github/gitignore/blob/master/Python.gitignore)
                * [gitignore/SublimeText.gitignore at master · github/gitignore](https://github.com/github/gitignore/blob/master/Global/SublimeText.gitignore)
        - O 选取 common + python + media + SublimeText 三个部分作为基础模板,以后根据实际具体需求进行删改
            + 分析项目涉及的依赖/工具/语言...等等构件
            + 查找相关 .gitignore 模板,参考对应构件的规则进行设置
            + 编辑过程中要关注真实存在的文件,看是否有遗漏,进一步完善
                * 指定文件后缀
                    * `*.suffix`
                * 指定文件名
                    * `filename/` 文件包含的内容
                    *  `/filename` 包含该文件的父级文件内容
    * A 设置 py104 仓库的文件
        * A 查看仓库文件是哪些需要隐藏的文件
            - `__pycache__`
            - `.sublime-project`
            - `.sublime-worklplace`
            - `.ipynb_checkpoints`
        - Q  pipenv 的 pipfile 和pipfile.lock 应该被隐藏吗?
            + 这是原始文件,用于生成项目依赖环境,应当不用隐藏
            + 官方给出的[答案](https://docs.pipenv.org/basics/#general-recommendations-version-control)
                * > Generally, keep both Pipfile and Pipfile.lock in version control.
                * > Do not keep Pipfile.lock in version control if multiple versions of Python are being targeted.
        * A 编辑 py104 仓库的`.gitignore`文件
            *  python 模板 + sublimeText 模板
        + A Check out `gitignore` 设置之前的的生成文件 
            - I `git rm --cached FILENAME`
                -  O `git rm -r --cached __pycache__/`
                -  O `git rm -r --cached *.sublime-workspace`
                -  O `git rm -r --cached *.sublime-project`
        +  A `git push`
            *  检查相关文件是否被删除
                -  O 当面仓库无删除文件
                -  O 历史仓库无当前文件

## 1 原代码迁移

+ A 重温 pipenv 的使用方法
    * Ref
        * => [Basic Usage of Pipenv — pipenv 2018.05.18 documentation](https://docs.pipenv.org/basics/)
        * => [Advanced Usage of Pipenv — pipenv 2018.05.18 documentation](https://docs.pipenv.org/advanced/)
    - I 总体建议 与 版本控制
        + 大部分情况,保留 `Pipfile` 和 `Pipfile.lock` 在版本控制中
        + 如果使用多版本 python 为目标,则不要保留 `Pipfile.lock`
        + 在 `Pipfile` 的 `[requires]` 部分设定指定 python 版本
        + `pipenv install` 完全适配 `pip inatall` 
            + => [User Guide — pip 10.0.1 documentation](https://pip.pypa.io/en/stable/user_guide/#installing-packages)
    * I Pipenv 示例启动工作流
        - 克隆/创建项目仓库, 进入项目根目录
            ```shell
            ...
            $ cd myproject
            ```
        - 如果目录中有 `pipfile` ,直接从其中下载依赖包
            - `$ pipenv install`
        * 或者添加依赖包到新项目
            - `$ pipenv install <package>`
                + 如果没有`pipfile`, 安装后会自动创建文件
                + 如果有 `pipfile` , 安装后文件会自动更新
        * 激活 pipenv 的 Shell 环境
            ```shell
            $ pipenv shell
            $ python --version
            …
            ```
    * I Pipenv 示例更新工作流
        - 查看变更
            - `$ pipenv update --outdated`
        * 一次更新所有包
            - `$ pipenv update`
        * 一次更新单个包
            - `$ pipenv update <pkg>`

* A 在 CH4 文件夹部署虚拟环境 2018-09-06 09:42
    - A 清理原来文件
    - A 迁移 CH3 内容,确定依赖于 python 版本 : requirement
        + X 没有 requirement.txt,
        + O 可以直接复制 pipfile 与 pipfile.lock 迁移开发环境
        + O 检查 python 版本,检查依赖
    ```bash
    ➜  project git:(master) ✗ ls
    Pipfile      Pipfile.lock README.md    test.py
    ➜  project git:(master) ✗ pipenv shell
    Spawning environment shell (/bin/zsh). Use 'exit' to leave.
    . /Users/NBR-hugh/.local/share/virtualenvs/project-efWUULjV/bin/activate
    ➜  project git:(master) ✗ . /Users/NBR-hugh/.local/share/virtualenvs/project-efWUULjV/bin/activate
    (project-efWUULjV) ➜  project git:(master) ✗ python --version
    Python 3.6.5
    (project-efWUULjV) ➜  project git:(master) ✗ pipenv graph
    Flask==0.12.2
      - click [required: >=2.0, installed: 6.7]
      - itsdangerous [required: >=0.21, installed: 0.24]
      - Jinja2 [required: >=2.4, installed: 2.10]
        - MarkupSafe [required: >=0.23, installed: 1.0]
      - Werkzeug [required: >=0.7, installed: 0.14.1]
    requests==2.18.4
      - certifi [required: >=2017.4.17, installed: 2018.1.18]
      - chardet [required: >=3.0.2,<3.1.0, installed: 3.0.4]
      - idna [required: <2.7,>=2.5, installed: 2.6]
      - urllib3 [required: <1.23,>=1.21.1, installed: 1.22]
    ```

- A 迁移具体代码,运行ch3 代码
    +  A 本地运行 flask 
    +  X 失败,报错

- E builtins.IndentationError
    ```
    builtins.IndentationError
    File "/Users/NBR-hugh/Documents/github.nibirong.com/Py101-004/Chap4/project/WeatherQueryWebAPP_Flask.py", line 42
        return render_template('Index.html', DisplayInfo=history_info)
                                                                     ^
    IndentationError: unindent does not match any outer indentation level
    ```
    - O  缩进错误,没有注意多缩进了一格,已解决

- E ModuleNotFoundError
    - ModuleNotFoundError: No module named 'API_deal'
    - O root 目录下不能放置 `__init__.py` 文件
    - O 绝对引用与相对引用混杂,导致代码运行失败
    - O 删除了 root 目录的 `__init__.py` ,统一使用 绝对引用,错误解除

- X Import 机制 理解不到位
    + [The Definitive Guide to Python import Statements | Chris Yeh](https://stanford.edu/~chrisyeh/2017/08/08/definitive-guide-python-imports.html)

- O **概念卡: python Import 机制**
    + REF
        * [The Definitive Guide to Python import Statements | Chris Yeh](https://stanford.edu/~chrisyeh/2017/08/08/definitive-guide-python-imports.html)
    + demo
        ```
        test/                      # root folder
            packA/                 # package packA
                subA/              # subpackage subA
                    __init__.py
                    sa1.py
                    sa2.py
                __init__.py
                a1.py
                a2.py
            packB/                 # package packB (implicit namespace package)
                b1.py
                b2.py
            math.py
            other.py
            start.py
        ```
    - 注意:  we do not place a `__init__.py` file in our root `test/` folder.
    - 基础概念

#### 反思

- R => 反思与推进 2018-09-06 14:02
    + 记录所有操作与思考,一悬空就容易走神与卡壳
    + 重整项目骨架,重整模块命名,重新厘清 python import 机制


- X 项目骨架不规范,重整骨架 2018-09-06 15:28 
    + REF
        * [learn-python3-the-hard-way-jul-4-2017.pdf](https://program.bruintech.org/wp-content/uploads/2018/01/learn-python3-the-hard-way-jul-4-2017.pdf) ex46
        * [pallets/flask-website: The Flask website, built with Flask!](https://github.com/pallets/flask-website)
        * [Structuring Your Project — The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/structure/)
        * [coding style - What is the best Python library module skeleton code? - Stack Overflow](https://stackoverflow.com/questions/2387272/what-is-the-best-python-library-module-skeleton-code)
        * O hardway 的测试模块时失效的,选择深入 Hitchhiker 的指南
    + O 创建项目骨架
        ```
        README.rst
        LICENSE
        setup.py
        requirements.txt
        sample/__init__.py
        sample/core.py
        sample/helpers.py
        docs/conf.py
        docs/index.rst
        tests/test_basic.py
        tests/test_advanced.py
        ```
    - X  有很多当然任务用不上的部分,不太看得懂
    - A  把仓库拉取下来,弄懂每个部分的功能作用

#### 反思

- R => 卡顿,反思与推动
    + 过多的信息会导致行动瘫痪,番茄钟内必须给出2次自己的判断
    + 过多问题混杂也是如此
        * 如何解决 原来 ch3 的 import moudle 错误,进而深入理解 import 机制.
        * 怎样的仓库架构是合理的? 是最佳的?
    + 一个个来,不要空想,自己的判断,打字的手不能停.


- O **金句卡**
    + > Dress for the job you want, not the job you have.
    + from: [Structuring Your Project — The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/structure/#license)

- O 本地运行 flask 成功 2018-09-06 18:27



#### 反思

- R => 推进 2018-09-06 18:29
    + 不要去追求体系,不停止地探索中训练自己的姿势与反应,一个个知识点弄清楚,逐个攻破,从而建立起自己的体系
    -  text 撰写 概念卡: python import 机制 1T
        +  [The Definitive Guide to Python import Statements | Chris Yeh](https://stanford.edu/~chrisyeh/2017/08/08/definitive-guide-python-imports.html)
    -  text 撰写 技巧卡: python 项目仓库的文件结构 1T
        +  [Structuring Your Project — The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/structure/#license)
    -  code 正式开发 数据库 完成一次 增删查改   
    -  text 使用 python 写测试代码
        +  [Testing Your Code — The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/tests/)
    -  text 代码规范规约
        +  [A "Best of the Best Practices" (BOBP) guide to developing in Python.](https://gist.github.com/sloria/7001839)

-  I 重新厘定目标 4T
    + 利用数据库存储数据
    + 基础概念,基础操作,功能代码段  

## 代码规范

- I 代码规范
    + 长注释
        * 摘要行
        * 用例(如果需要)
        * 变量
        * 返回的数据类型与数据含义

```
"""Train a model to classify Foos and Bars.

Usage::

    >>> import klassify
    >>> data = [("green", "foo"), ("orange", "bar")]
    >>> classifier = klassify.train(data)

:param train_data: A list of tuples of the form ``(color, label)``.
:rtype: A :class:`Classifier <Classifier>`
"""
```

 
## 建立数据库基本概念 2018-09-07 10:08

- I 什么是数据库?
    + > A database is a collection of information that is organized so that it can be easily accessed, managed and updated.
    + I 更易于操作,管理与更新的信息组织形式

- I 常见数据库排行
    + [DB-Engines Ranking - popularity ranking of database management systems](https://db-engines.com/en/ranking)

- I SQL(Structured Query Language)
    +  REF
        *  [SQL syntax - Wikipedia](https://en.wikipedia.org/wiki/SQL_syntax
    +  定义
        *  关系型数据库标准查询语言
    +  元素
        *  Clauses
            - > constituent components of statements and queries
            -  语句与查询的组成部分
        *  Expressions
            - > produce either scalar values, or tables consisting of columns and rows of data
            - 生成变量,或者生成含有多行多列数据的表
        *  Predicates
            -  > which specify conditions that can be evaluated to SQL three-valued logic (3VL) (true/false/unknown) or Boolean truth values and are used to limit the effects of statements and queries, or to change program flow.
            -  条件判定,限定条件: SQL 3VL 计算,布隆值
            -  限制语句与查询的条件,修或改程序流程
        *  Queries
            -  > retrieve the data based on specific criteria.
            -  根据某些条件寻找数据
        *  Statements
            -  >  may have a persistent effect on schemata and data, or may control transactions, program flow, connections, sessions, or diagnostics.
            -  持续作用于数据与数据组织
            -  数据库管理系统对数据库的单元操作,程序流,连接,会话,诊断
        *  Insignificant whitespace 
            -  无意义空白
            -  可以根据可读性任意调整
    +  实践练习
        *  [SQL Exercises, Practice, Solution - w3resource](https://www.w3resource.com/sql-exercises/)

+ I CRUD
    *  create, read, update and delete ，four basic functions of persistent storage
- I ORM
    +  Object Relation Mapping

- I SQL three-valued logic (3VL) (true/false/unknown)

- I 数据库的核心概念?
    + [Databases — The Hitchhiker's Guide to Python](https://docs.python-guide.org/scenarios/db/)

- I 通过 python 使用关系型数据库
    + [Using Relational Databases with Python](http://halfcooked.com/presentations/osdc2006/python_databases.html)
    + 

- I 层级
    + 数据库
        * 数据集合
            - [Database - Wikipedia](https://en.wikipedia.org/wiki/Database#Models)
    * 数据库管理系统
        - [Relational database management system - Wikipedia](https://en.wikipedia.org/wiki/Relational_database_management_system)
        - 关系型数据库
            + MySQL, PostgreSQL, Oracle、Microsoft SQL Server,SQLite
            + 免费: MySQL,PostgreSQL,SQLite
        - 非关系型数据库
            + MongoDB, Redis, CouchDB
    +  数据库交互语言
        *   SQL (使用与关系型)
    +  数据库交互方式                  
        * CRUD
        * ORM
    +  python 与数据库
        *   API 接口 : [PEP 249 -- Python Database API Specification v2.0 | Python.org](https://www.python.org/dev/peps/pep-0249/)
        *   基于接口的模块:
            - 与 SQLite 交互
                + [12.6. sqlite3 — DB-API 2.0 interface for SQLite databases — Python 3.7.0 documentation](https://docs.python.org/3/library/sqlite3.html)
            - ORM 的模块  [Databases — The Hitchhiker's Guide to Python](https://docs.python-guide.org/scenarios/db/)


- Q  什么时候用 class, 什么时候用 function?
    - REF
        - [class - Classes vs. Functions - Stack Overflow](https://stackoverflow.com/questions/18202818/classes-vs-functions)
    > Functions do specific things, classes are specific things.


## 开发思考

- A 业务
    + 获取 API 的返回文件,提取有效信息
    + 通过 sqlite3 与 SQL 配合 CRUD 数据
    +  API -> JOSN -> variables -> db -> opration/value -> web -> prompt / new value
        *  opration: CRUD
        *  value: city,{wheather:tmp,type...},time
            -  从今日此时期,之前的数据就基本对用户无用了
            -  日期 + 城市 定维 天气信息

- Q **程序核心操作,数据,以及对象?** 
    + 数据: 
        +  内容: city,{wheather:tmp,type...},time
        +  格式: dict,JSON,database,variable, file
        +  过程:
            + params -> dict -> url
            * url -> API -> JSON
            * JSON -> python[]提取 -> dict
            * variable -> SQL -> database
            * database <-> SQL / sqlite3 <->  variable on serve
            * variable on serve <-> flask/html(css/javascript)  <-> variable on browser
            * browser -> history -> text file
    + 对象与操作:
        * 彩云 API
            - 请求 url 所需参数
                + 不同 API 接口所需变量不同
                + dict
            - 发送 API request
                + 成功
                + 失败
            - 接收 API response
                + 成功
                + 失败
            - 处理 response 返回的 JOSN
                + 提取 JOSN 有效信息
                + 构造 天气信息 字典
        * Flask Web 框架
            - 接收 客户端功能请求:
                - 按钮:帮助,查询,历史,欢迎,更改
                - 输入:查询,更改
            - 返回 展示信息
        * SQLite database 数据库
            -  存储数据
            -  更新数据
            -  提取数据


- Q 数据应该一条条拉取,还是一次性全部拉取?
    +  O 应当一次性拉取,2个原因
        *  网络延迟的等待时间叠加,影响用户体验
        *  多个用户同时查询一条信息,操作过多

- Q 如何一次拉取所有城市天气信息到本地?
    + 


- A 重新实现 API 
    + A 使用类来实现 API 

- Q 如何写 python 类? 
    + 注意点
    + 最佳实践

- Q 如何可视化 db 文件
    + 用编辑器打开`*.db`文件是一串二进制数字?
    + [How to Open a Database File (.DB File) on PC or Mac - wikiHow](https://www.wikihow.tech/Open-a-Database-File-on-PC-or-Mac)
    + [DB Browser for SQLite](http://sqlitebrowser.org/)
        * 下载 
        - `$ brew cask install db-browser-for-sqlite`

## 2018-09-11 08:01 重新梳理混乱思绪

- I 开发路径图
    + [X] 重构 API 2018-09-10 
        * 抽离业务逻辑
        * 将数据与操作组合成类
    + [ ] 完成数据库的增删查改 2018-09-12
        + [x]能够存储单条信息
        + [ ]能够更新单条信息
        + [ ]能够存储批量信息
    - [ ] 将作品迁移如怼圈,以求获得及时反馈
        - [ ] 今日午饭后 1T
    + [ ] 卡片教程撰写
        -  text 撰写 概念卡: python import 机制 1T
            +  [The Definitive Guide to Python import Statements | Chris Yeh](https://stanford.edu/~chrisyeh/2017/08/08/definitive-guide-python-imports.html)
        -  text 撰写 技巧卡: python 项目仓库的文件结构 1T
            +  [Structuring Your Project — The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/structure/#license)
        -  text 使用 python 写测试代码
            +  [Testing Your Code — The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/tests/)
        -  text 代码规范规约
            +  [A "Best of the Best Practices" (BOBP) guide to developing in Python.](https://gist.github.com/sloria/7001839)
    *  [ ]基础疑问长考
        -   如何写好 python 中的类?
            +  基本的 demo 
            +  变形
            +  延伸
                *  父类/基类
                *  多态与继承
        -  我自己的开发 mvp 节奏是什么? 能否以文字形式表述出来?
            +  如何设计?
            +  如何规划开发计划?
            +  如何写设计文档?
            +  如何合理地 commit?
            +  如何处理读写 代码与文字的平衡?
            +  最小行为循环的基本单位是什么?

- I 发现自己重复犯错误,汇总反思
    - - R => 推进 2018-09-06 18:29
        + 不要去追求体系,他人体系镜花水月,在拆解过程中提问与回答,在不断问答中训练自己的姿势与反应,把一个个知识点表述清楚,逐个攻破,从而才能建立起自己体系,实现有效复用与快速调用.
        -  text 撰写 概念卡: python import 机制 1T
            +  [The Definitive Guide to Python import Statements | Chris Yeh](https://stanford.edu/~chrisyeh/2017/08/08/definitive-guide-python-imports.html)
        -  text 撰写 技巧卡: python 项目仓库的文件结构 1T
            +  [Structuring Your Project — The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/structure/#license)
        -  code 正式开发 数据库 完成一次 增删查改   
        -  text 使用 python 写测试代码
            +  [Testing Your Code — The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/tests/)
        -  text 代码规范规约
            +  [A "Best of the Best Practices" (BOBP) guide to developing in Python.](https://gist.github.com/sloria/7001839)
        -  logging  模块的调试使用
            +  [Stop Using "print" for Debugging: A 5 Minute Quickstart Guide to Python’s logging Module - The Invent with Python Blog](https://inventwithpython.com/blog/2012/04/06/stop-using-print-for-debugging-a-5-minute-quickstart-guide-to-pythons-logging-module/)
            +  [Logging HOWTO — Python 3.7.0 documentation](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)
            +  Report events that occur during normal operation of a program (e.g. for status monitoring or fault investigation)    logging.info() (or logging.debug() for very detailed output for diagnostic purposes)
    - - R => 卡顿,反思与推动
        + 过多的信息会导致行动瘫痪,番茄钟内必须给出2次自己的判断
        + 过多问题混杂也是如此
            * 如何解决 原来 ch3 的 import moudle 错误,进而深入理解 import 机制.
            * 怎样的仓库架构是合理的? 是最佳的?
        + 一个个来,不要空想,自己的判断,打字的手不能停.

    - R => 反思与推进 2018-09-06 14:02
        + 记录所有操作与思考,一悬空就容易走神与卡壳
        + 重整项目骨架,重整模块命名,重新厘清 python import 机制
* O  顽固错误
    - 0 没有记录,多方向多方案的持续空想,无法验证想法的正确性,盲目搜索信息
        + 每个番茄都是一次提醒:
            * 你在做什么? 你在完成什么? 
            * 你完成了什么? 你确定或者明白了什么?
            * 为了完成任务里还有 哪些需要明白的
    - 1 对小任务事项没有时间与效果判定,未完成便搁置,半途重新开启一项任务,导致多任务思路郁结,摸索紊乱
    - 2 贤者时间: 起床后,用餐后,睡觉前.

- I  想法
    - 如果用语言无法表述程序的组成,原理与功能实现,那么用代码也不能.
    - 写代码也需要腹稿,想得清楚,下笔才有神.
    - 每日的计划也需要腹稿,想得清晰清楚,行动才会有力.
    - 腹稿背后是知识树,但这太笼统了,更细一点就是 具体完备可复用知识点 + 层级组织形式
    - 代码是所有抽象关系的总和

- A 计划: 1h 完成数据库的增删查改 2018-09-11 08:38 失败
    + X 早饭,碎片,怼友激活 2018-09-11 10:15 才启动
    + X 1h 内完成失败,整体的设计没有想清楚,相关组件的功能与用法也不熟练,导致中断

- A  A 计划: 1h 完成数据库的增删查改 2018-09-11 10:16 [O 11:16] 
    + 增加一条天气信息
    + O 成功

- Q 变量传递不清晰
    +  直接 SQl 可以运行,但是通过变量传递就出现问题
    +   X 触发错误 -> sqlite3.OperationalError: near ".": syntax error

- E sqlite3.OperationalError: near ".": syntax error
```
  File "untitled.py", line 120, in singl_operation
    c.execute(sql_commands,info)
sqlite3.OperationalError: near ".": syntax error
```
    - X  INSERT INTO city_weather_now VALUES(?,?,?.?,?)
        + O `,` 不小心写作了`.` 

- Q sql 与 sqlite 3 分离遇到的问题
    - 增删查改 中的查需要调用 fetchone 的函数来传递返回值
    - 增删改 都是 to database
    - 而改 是 from database 
    - 需要做一个区分 
    - X 不必区分,重复的代码太多了,用一个if 做判断
        -  如果 SQL 语句中存在 SELECT 那么返回 SLECT 结果 即可

- X 尝试用 ? 代替 具体的 table 名时替换失败
    ```
           self.create_table = '''
                                CREATE TABLE IF NOT EXISTS city_weather_now (
                                                            date date,
                                                            city char,
                                                            type char,
                                                            temp char,
                                                            code tinyint)
                                '''
            def creat_weather_table(self):
                print(">>> 开始 创建 now whearher table 创建")
                sql_commands = self.create_table
                variable = ()
                print(variable)
                self.single_operation_to_db(sql_commands, variable)
                print(">>> 完成 当前天气信息 table 创建")


            def single_operation_to_db(self, sql_commands, variable):
                """Execute a single  opeantion to database(SQLite): add,delete,update
                sql_commands : a str,a single SQL statement(without ; )
                variable: a truple,table name/ clomuns name/ a insert raw..
                """
                print(">>>SQL 命令:", sql_commands)
                conn = sqlite3.connect('weather.db')
                c = conn.cursor()
                c.execute(sql_commands, variable)

                if 'SELECT' in sql_commands:
                    select_result = c.fetchall()
                    print(">>> 显示 SELECT 内容:", select_result)
                    return select_result
                else:
                    print(">>> 没有 SELECT 与 UPDATE 内容 ")

                conn.commit()
                conn.close()
                print('>>> 数据库单次操作成功!')
    ```
    - 当尝试使用变量 table_name 代替固定 的 table 名:city_weather_now 时失败,提示错误
    -  E `sqlite3.OperationalError: near "?": syntax error`
        +  X 暂时不知道原因,暂放,先完成主要功能

## 完成基本功能 2018-09-12 07:00

- R 一次改动不能太多,要有明确的任务目标与验证,保证程序每时每刻都在能够运行的状态 2018-09-12 06:40
    + A 希望存储 now weather 信息的 SQL 命令能够复用,调试修改变量名,但没有成功
    + A 希望完成 update 功能,但没有成功
    + A 希望修改调试姿势, 都是 print 调试感觉不舒服,应该有更好的调试方式
    - X 三个任务混杂,导致发生错误时不知定位在哪里

- Q 目前只能根据城市信息来 select 信息, 如何 根据多个限制条件?
    +  SQL: WHERE 后的 定位条件如何才能联合 ?

- Q 如果获取 update 的改动信息?
    +  X 尝试使用 cursor.fetchone() 没有任何返回信息
    +  I 或许可以 通过 commit 信息来调用? [w]

- A 显示 table 内所有内容
    + `def display_now_weather_table(self):`
    + `sql_commands ='SELECT * FROM city_weather_now'`
    + O 成功运行

- A 实现 database 的 UPDATE 功能
    + 根据城市信息 update 数据库中 相关的天气信息
    + A 尝试将重庆的信息变为暴雨
    + X city , type 的变量顺序相反
    + O 调整后就成功了

- A 实现 database 的 delete 功能
    + 根据城市信息 delete 相关天气信息
    +  A 尝试删除重庆信息

- A 尽快将项目迁移到怼圈分支,以寻求反馈

- I 似乎有点找到状态,意识的 MVP 集中
    + 混乱的意识和水流一样,没有固定的倾向就只能四处散落,没有力量
    + 意识的投入数量靠时间投入来衡量
    + 意识的投入质量只能通过预定任务的完成与代码是否成功来判定
    + 任务的规划与写函数类似:确定任务目标,确认返回结果,启动运行直到成功
        * 限定时间(1T)内未成功,重新描述问题,重新回顾探索路径,调整方向
        * 止损时间(2T)内未成功,已尝试2~3个方案,提问
            - 怼圈
            - Stack Overflow
    + 能做到这个前提是对自己情绪与思绪有平静的把握
        * 完备的规划
        * 明确的执行
        * 清晰的判定
        * 快速的反应
        * 无噪的内心

- Q 如何将项目迁移到怼圈
    + 建立孤子分支
    + 建立远程分支链接

- A 在 playground 中尝试链接
    + A 建立一个孤子分支
        * D 打断 查收 slack 信息
        * X ssh方式  git clone 失败,换成 HTTPS 方式成功
        * O 设置成功
        ```shell 
        ➜  du4proto.wiki git:(master) git clone https://github.com/DebugUself/playground.git
        Cloning into 'playground'...
        remote: Counting objects: 706, done.
        remote: Compressing objects: 100% (3/3), done.
        remote: Total 706 (delta 0), reused 0 (delta 0), pack-reused 703
        Receiving objects: 100% (706/706), 1.67 MiB | 162.00 KiB/s, done.
        Resolving deltas: 100% (234/234), done.
        Checking connectivity... done.

        ➜  du4proto.wiki git:(master) ✗ git checkout --orphan NBRpy104
        Switched to a new branch 'NBRpy104'

        ➜  du4proto.wiki git:(NBRpy104) ✗ git rm -rf .
        rm '180530DUmeetingSH.md'
        ...

        ➜  du4proto.wiki git:(NBRpy104) ✗ echo "#Title of Readme" > README.md
        ➜  du4proto.wiki git:(NBRpy104) ✗ git add README.md
        ➜  du4proto.wiki git:(NBRpy104) ✗ git commit -a -m "Initial Commit"
        [NBRpy104 (root-commit) 40c8b2c] Initial Commit
         1 file changed, 1 insertion(+)
         create mode 100644 README.md

        ➜  du4proto.wiki git:(NBRpy104) ✗ git push --set-upstream origin NBRpy104
        Counting objects: 3, done.
        Writing objects: 100% (3/3), 230 bytes | 0 bytes/s, done.
        Total 3 (delta 0), reused 0 (delta 0)
        To https://github.com/DebugUself/du4proto.wiki.git
         * [new branch]      NBRpy104 -> NBRpy104
        Branch NBRpy104 set up to track remote branch NBRpy104 from origin.
        ```

- X ⚠️  忘记注意地址... 建立了 wiki 仓库的分支... ⚠️
    +  A 删除远程 wiki 分支,并删除本地分支
        * [How do I delete a Git branch both locally and remotely? - Stack Overflow](https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-both-locally-and-remotely)
        *  删除远程分支 `git push --delete origin NBRpy104`
        *  删除本地分支 `git branch -D NBRpy104`
        ```shell
        ➜  du4proto.wiki git:(NBRpy104) ✗ git checkout master
        Switched to branch 'master'
        Your branch is up-to-date with 'origin/master'.
        ➜  du4proto.wiki git:(master) ✗ git branch -a
          NBRpy104
        * master
          remotes/origin/HEAD -> origin/master
          remotes/origin/NBRpy104
          remotes/origin/master
        ➜  du4proto.wiki git:(master) ✗ git push --delete origin NBRpy104
        To https://github.com/DebugUself/du4proto.wiki.git
         - [deleted]         NBRpy104

        ➜  du4proto.wiki git:(master) ✗ git branch -D NBRpy104
        Deleted branch NBRpy104 (was 40c8b2c).

        ➜  du4proto.wiki git:(master) ✗ git branch -a
        * master
          remotes/origin/HEAD -> origin/master
          remotes/origin/master
        ```
        - O 成功消除错误影响

- A 在 playground 测试: 将本地 py104 仓库关联到 playground 仓库的 NBRpy104 分支上 

    + A 将本地的py104仓库 master 分支 关联到 NBRpy104 远程分支上
        * [Git - Working with Remotes](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
    + X 直接关联失败
    + E  error: src refspec NBRpy1040 does not match any.
    ```
    ➜  Py101-004 git:(master) ✗ git remote add -t NBRpy104 -f play  https://github.com/DebugUself/playground.git
    Updating play
    warning: no common commits
    remote: Counting objects: 3, done.
    remote: Total 3 (delta 0), reused 1 (delta 0), pack-reused 2
    Unpacking objects: 100% (3/3), done.
    From https://github.com/DebugUself/playground
     * [new branch]      NBRpy104   -> play/NBRpy104
    ➜  Py101-004 git:(master) ✗ git push --set-upstream play  NBRpy1040
    error: src refspec NBRpy1040 does not match any.
    error: failed to push some refs to 'https://github.com/DebugUself/playground.git'
    ```
    + I 判断: 没有任何可以一致匹配的内容导致更新失败
        * O 时间线上的 commit 以及 仓库内容的冲突导致无法合并
        * A 选择
            * 00 将 Py104-004 的全部内容复制到分支目录下, 另启一个分支,丢失原本的 commit 历史记录
            * 01 由于是重构,直接将新的代码文件复制出来,另启一个分支,丢失原本的commit,丢失原本 Chap 4 之前的代码内容.
            * 02 创建软链接,将新代码的文件关联到 怼圈远程分支, 不过小步修改实现后需要 2 次 commit,原 py104 仓库的 commit 历史不会中断,新的分支丢失 commit 记录.
        * O 选择 方案 02 -> 失败
        * E 不知是否还有更好的关联方式,发怼圈 issue 求助

- Q 如何创建软链接? 
    + REF [How to Create and Use Symbolic Links (aka Symlinks) on a Mac](https://www.howtogeek.com/297721/how-to-create-and-use-symbolic-links-aka-symlinks-on-a-mac/)
        - `ln -s /path/to/original /path/to/link`

* A 尝试 方案2 失败
    - 当前路径: /Users/NBR-hugh/Documents/github.nibirong.com/Py101-004/Chap4/projects
    - 目标路径: /Users/NBR-hugh/Documents/github.nibirong.com/playground/ projects
    - X 不行,软链接知识建立一个关联,没有具体文件可以
    - A 看来得用硬链接
        + `man ln`
            * > By default, ln makes hard links.
        + X 报错
        + REF : [硬链接(hard link)和符号连接(symbolic link)的区别-每天进步一点点……-51CTO博客](http://blog.51cto.com/wzgl08/308987)
            * > 硬链接文件有两个限制
                1）、不允许给目录创建硬链接
                2）、只允许在同一文件系统中的文件之间才能创建链接
- X 方案 02 失败
    + ln 是无实体关联链接,无法同步具体内容
    + 如何实现不同文件系统中的具体内容的拷贝?
        * S  auto related copy file mac
        * [automator - Is there a way for OSX to auto-copy a file somewhere whenever it's updated? - Ask Different](https://apple.stackexchange.com/questions/182716/is-there-a-way-for-osx-to-auto-copy-a-file-somewhere-whenever-its-updated)
        * [How to Schedule an Automatic File Backup in a Mac: 11 Steps](https://www.wikihow.com/Schedule-an-Automatic-File-Backup-in-a-Mac)
        * [Auto copy for files from folder to folder upon instant writing | Unix Linux Forums | UNIX for Advanced & Expert Users](https://www.unix.com/unix-for-advanced-and-expert-users/61278-auto-copy-files-folder-folder-upon-instant-writing.html)
        * [Automatically copying files from one fold… - Apple Community](https://discussions.apple.com/thread/2246916)

- I 发布 怼圈 Issue 求助
    + -> [3d\[ASK\] 如何将开发了一半的项目迁入怼圈孤子分支? · Issue #470 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/470#issuecomment-420907166)

- I  [目标定义不清晰](https://github.com/DebugUself/du4proto/issues/470#issuecomment-420907166)
    + A 分析对应效果与行为
    + I 基本组成: 
        + [本地/远程] py104 仓库 master 分支 [仓库所有文件/部分代码文件]
        + [本地/远程] playground 仓库 NBRpy104 分支 
    + I 主要决策点
        * 内容: 迁移 整个 py104 仓库 master 分支内所有文件,还是只迁移 正在重构中的代码与记录
        * 内容: 迁移后  原本仓库的 commit 历史是否能够完整保留
        * 形式: 唯一实体原则, 希望一处改动,多处自动/半自动变动
        * 成本: 由于往后需要多次提交,所以需要尽可能少的操作,降低行动成本
        * 先形式,后内容,
    + I 原先的行动序列
        ```
        0 [local py104 master] => [remote py104 master]

        [local py104 master]:make the change ->  git add  ->  git commit -> git push -> [remote py104 master]:update the change
        ```

    + 逻辑分析
        * 一处实体改动,多处 本地/远程备份自动更新
        * 1 一处文件实体, 经过 X 操作, 自动/半自动完成 多仓库提交 失败
        ```
        1 [local py104 master]  => [remote playground NBRpy104] 
                                => [remote py104 master]

        具体命令:
        [local py104 master]:make the change -> git add  ->  git commit +
                                                                        |
        + <------------------------------------------------------------ +
        +-> git push => [remote py104 master]:update the change
        +-> git push --set-upstream play NBRpy104  => [remote playground  NBRpy104]:update the change
        ```
        * 2 一处文件实体, 经过 X 操作, 自动变成多个实体, 再对应不同的仓库, 自动/半自动完成 提交
            - 2.1 尝试软链接,对软链接定义不明而失败, ln 不产生实体
            - 2.2 搜索了一下,指向 mac 自带的工具 automator 
                - [欢迎使用 Automator - Apple 支持](https://support.apple.com/zh-cn/guide/automator/welcome/mac)
        ```
        2 [local py104 master] =>  [remote py104 master]
            | (auto copy way)
            + => [local playground NBRpy104] => [remote playground NBRpy104]

        具体命令:
        [local py104 master]:make the change -> git add  ->  git commit -> git push => [remote py104 master]:update the change
        |
        +(auto copy way) 
        |
        + => [local playground NBRpy104]: update the change -> git add  ->  git commit -> git push => [remote playground NBRpy104]:update the change
        ```

- 接下来的行动
    + 1 可能存在直接关联的方式,但由于我对 git 的理解实现,目前无法实现,
        * 对于 match 的判定其实存在疑虑:
            - 如果同时判定commmit 信息与具体内容,那么该方法基本不可能了
            - 但如果只是判定具体内容,那么将文件复制过去后,丢失之前的 commit, 但可以实现今后的 commit 的同步
    + 2 探索  automator 自动拷贝
    + 3 重复的 push/commit 的操作 看能否通过 shell 命令 或者 zsh 的 alias 功能 简化
    + 4 如果都不行,那就直接复制到孤子分支上了事,只是这样会造成 commit 历史的割裂

- I 求助反馈
    - REF 
        - [3d\[ASK\] 如何将开发了一半的项目迁入怼圈孤子分支? · Issue #470 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/470#issuecomment-420990946)
        - [du4proto/20170828\_two\_unrelated\_repo\_in\_one\_gitfolder.md at YHarticles · DebugUself/du4proto](https://github.com/DebugUself/du4proto/blob/YHarticles/20170828_two_unrelated_repo_in_one_gitfolder.md)

    + I 00 `--allow-unrelated-histories` 
        + git push [远程库名][本地分支名]:[远程分支名]
            ```
            λ git clone du4proto url
            λ cd du4proto
            λ git checkout -orphan yanhui
            (delect files)
            λ git remote add yhpy103 url
            λ git fetch yhpy103
            λ git merge yhpy103/master --allow-unrelated-histories
            (modify some files, eg. README.md)
            λ git add .
            λ git commit
            λ git push origin yanhui:yanhui
            ```
    + I 01  官方文档 => git 本身有另外的多仓库管理策略/工具/技巧
    + I 02  通用性自动化工具, python 实现的 Fabric 
    + I 03   `.git` 文件 (hooks)
    + I 04  1.* 比较容易上手,即尝试直接关联,而非自动复制实体

- A 尝试 leilayanhui  的方案
    -  X 只能推送同一分支:  py104:master -> playground:master
    -  X  fetch + merge,其实还是有两个实体了
    -  git push --set-upstream play  NBRpy1040 --allow-unrelated-histories


Q 命令行的文字编辑技巧

    - 如何实现光标的快速跳转?
        + [Mac下iTerm2光标按照单词快速移动设置 - CSDN博客](https://blog.csdn.net/skyyws/article/details/78480132)
        + [iTerm2 快捷键大全 - 陈斌彬的技术博客](https://cnbin.github.io/blog/2015/06/20/iterm2-kuai-jie-jian-da-quan/)
        + O 通过修改 映射,实现 alt + 左右方向键,实现光标 word 间跳转




##  TL


- 180908 `2h` NBR-hugh add 数据库&SQL 基本探索 & 程序基本结构思考
- 180906 `2h30m` NBR-hugh add 仓库文件结构探索 & import 机制探索
- 180906 `3h05m` NBR-hugh 迁移复用原代码
- 180602 `4T` NBR-hugh add gitignore
- 180525 `4T` NBR-hugh  init
