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

* 查看以往代码,梳理工作原理与数据流
    * 迁移相关代码,完成基本工具的 DEMO
* 数据存储格式的讨论
    * 直接拉取单次 API 查询
    * 将整个文件拉取到本地 ,固定时间轮询更新,用户查询直接在本地

## 探索记录

- I 看看到python 的衍生文件与sublime 的布局结构文件,所以想设置 ignore 文件来清理仓库中的文件
    + A github help
        * => [Ignoring files - User Documentation](https://help.github.com/articles/ignoring-files/)

- O **概念卡: Ignoring files**
    + 功能: 
        + 告诉 git 哪些文件应对被忽视,不被 check in 到 github
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
            * 

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

* A 在 CH4 文件夹部署虚拟环境


##  TL

- 180525 NBR-hugh `4T` init
