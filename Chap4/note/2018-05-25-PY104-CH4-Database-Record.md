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
    + [ ] 完成数据库的增删查改
        + 能够存储单条信息
        + 能够存储批量信息
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
        -   如何写 python 中的类?
            +  基本的 demo ,
            +  变形
            +  延伸
                *  父类/基类
                *  多态与继承
        -  我自己的开发 mvp 节奏是什么? 能否以文字形式表述出来?

- I 发现自己从重复犯错误,汇总反思
    - - R => 推进 2018-09-06 18:29
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
    - 1 对小任务事项没有时间与效果判定,未完成便搁置,半途重新开启一项任务,导致多任务中郁结

##  TL


- 180908 `2h` NBR-hugh add 数据库&SQL 基本探索 & 程序基本结构思考
- 180906 `2h30m` NBR-hugh add 仓库文件结构探索 & import 机制探索
- 180906 `3h05m` NBR-hugh 迁移复用原代码
- 180602 `4T` NBR-hugh add gitignore
- 180525 `4T` NBR-hugh  init
