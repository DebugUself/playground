# PY104 CH4 Database 探索记录

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
* 进阶任务 * 学有余力，可以使用 Flask 的扩展 Flask-SQLAlchemy 来替代 sqlite3 模块，和 Flask 更好地结合。

## 路线

* 查看以往代码,梳理工作原理与数据流
    * 迁移相关代码,完成基本工具的 DEMO
* 数据存储格式的讨论
    * 直接拉取单次 API 查询
    * 将整个文件拉取到本地 ,固定时间轮询更新,用户查询直接在本地

## 探索记录

- I 看看到python 的衍生文件与sublime 的布局结构文件,所以想设置 ignore 文件来清理仓库中的文件
    + A github help
        * => [Ignoring files - User Documentation](https://help.github.com/articles/ignoring-files/)
        * I  概念卡: Ignoring files
            - 功能: 告诉 git 哪些文件应对被忽视,不被 check in 到 github
            - 操作:
                + **local .gitignore**
                    * 应用于单个 git 仓库文件
                    * 进入git仓库根目录,` touch .gitignore`
                    * 添加相应规则
                * **global .gitignore**
                    * 应用于电脑上所有 git 仓库文件
                    * 根目录创建 `~/.gitignore_global`
                    * 添加相应规则
                    * 激活设置文件
                        * `git config --global core.excludesfile ~/.gitignore_global`
                - **.git/info/exclude**
                    + 用于那些不希望与他人分享的 `.gitignore` 规则
                        * 那些只希望本地生成,不希望其他用户生成的文件
                            - 比如编辑器生成的文件
                    + 进入git仓库根目录,使用文本编辑器打开 `.git/info/exclude`
                    + 添加相关文规则
            - 注意: 
                + 已经被 check in 的文件无法被 `.gitignore` 忽视
                + 必须取消追踪这些文件
                    * git rm --cached FILENAME

            - 资源:
                + 一般必要的设置
                    + [Some common .gitignore configurations](https://gist.github.com/octocat/9257657)
                - 各种操作系统,语言,环境的. ignore 模板
                    + [A collection of useful .gitignore templates
](https://github.com/github/gitignore)
    - A Google `github ignore`
        - => [github/gitignore: A collection of useful .gitignore templates](https://github.com/github/gitignore) 
            - 各种.ignore 的模板
                - python
                - jupyter-notebook
                - sublime
            - Q  pipenv 的 pipfile 和pipfile.lock 应该被隐藏吗?
                + 这是原始文件,用于生成项目依赖环境,应当不用隐藏
    + A 查看仓库文件是哪些需要隐藏的文件
        * __pycache__
        * .sublime-project
        * .sublime-worklplace
        * 


+ A 重温 pipenv 的使用方法
    * Ref
        * => [Basic Usage of Pipenv — pipenv 2018.05.18 documentation](https://docs.pipenv.org/basics/)
        * => [Advanced Usage of Pipenv — pipenv 2018.05.18 documentation](https://docs.pipenv.org/advanced/)
    - I 总体建议 与 版本控制
        + 大部分情况,保留 `Pipfile` 和 `Pipfile.lock` 在版本控制中
        + 如果使用多版本 python 为目标,则不要保留 `Pipfile.lock`
        + 在 `Pipfile` 的[requires]  部分设定指定 python 版本
        + `pipenv install` 完全适配 `pip inatall` 
            + => ([User Guide — pip 10.0.1 documentation](https://pip.pypa.io/en/stable/user_guide/#installing-packages))
    * I Pipenv 示例启动工作流
        - 克隆/创建项目仓库
            ```
            ...
            $ cd myproject
            ```
        - 如果目录中有 `pipfile` ,直接从其中下载依赖包
            - `$ pipenv install`
        * 或者添加依赖包到你的新项目
            - `$ pipenv install <package>`
                + 如果没有`pipfile`, 安装后会自动创建文件
                + 如果有` pipfile`, 安装后文件会自动更新
        * 激活 pipenv 的 Shell 环境
            ```
            $ pipenv shell
            $ python --version
            …
            ```
    * I Pipenv 示例更新工作流
        - 查看变更
            - ` $ pipenv update --outdated`
        * 一次更新所有包
            - ` $ pipenv update`
        * 一次更新单个包
            - ` $ pipenv update <pkg>`

* A 在 CH4 文件夹部署虚拟环境


##  TL

- 180525 NBR-hugh `4T` init