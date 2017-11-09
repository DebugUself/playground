# 怼周刊发布手册 

参考 [DUW/README](https://github.com/DebugUself/du4proto/blob/DUW/README.md)

- 发行: 每周一期
    
    一般 周一 20:20 发布，分三个渠道发布：

    + [release](https://github.com/DebugUself/du4proto/releases)
    + [Debug Uself 自怼圈](https://groups.google.com/forum/#!forum/debuguself)
    + 再分享 pdf 到 [知识星球 - 连接一千位铁杆粉丝,知识变现,小团队共享](https://www.xiaomiquan.com/)

### 进展 Progress/提交 统计方法
- 进展 Progress/提交
  + 提交统计的是，本周push到master+push到其他分支的所有authors人数
  + 来到du4proto仓库界面 [Pulse · DebugUself/du4proto](https://github.com/DebugUself/du4proto/pulse)
  + 在overview栏目下面会有，**October 22, 2017 – October 29, 2017**
  + 例如，本周显示 **Excluding merges, 8 authors have pushed 10 commits to master and 48 commits to all branches. On master, 6 files have changed and there have been 183 additions and 48 deletions.** 说明，本周共有8位怼员push commits，其中前3名是，YanHui 12commits,Wangjunyu 9commits, leilayanhui 7commits 


### 进展 Progress/状态 统计方法
- 进展 Progress/状态:
  + 下载DU_tools 分支到本地，寻找chk4st.py 
  + pip安装模块` pip install rainbow_logging_handler`
  + pwd:DU_tools/st
  + 在上述目录下，终端运行 `python3 chk4st.py > **w.csv`
  + 获得含有html table的csv
  + 把csv复制粘贴到DU**_draft.md的`进展 Progress/状态`
  + 将DU_tools/st目录下，刚刚生成的中间文件，**w.csv删除

### 成果 Achievements 统计方法
- 根据[Pulse](https://github.com/DebugUself/du4proto/pulse)，可知本周所有提交commits的authors
- 逐一查看authors的分支
  + 比如，查看 **Wangjunyun** 的分支，观察其本周commits
  + 比较tricky的部分是，**Wangjunyun** 的分支命名为 **Leon.junyu** 
  + 查看 **Leon.junyu** 分支本周commit情况
- 注意:

### DUW发布自查表
- [ ] Release time:注意时间
- [ ] 定场诗
- [ ] 进度 Timelines:注意当周怼周会链接
- [ ] 进展 Progress
- [ ] 成果 Achievements
- [ ] 故事 Stories
- [ ] 推荐 Recommedations

### **w_draft.md -> **w.md 
- 完成DUW发布自查表所有内容后
- 将**w_draft.md 重命名为 **w.md
- git push到DUW分支上
  
### pdf文档生成方法
`注意:pdf由于选用插件不同，可能呈现不同风格，建议使用如下插件+风格`

- 浏览器
  + chrome

- 插件
  + [Markdown Preview Plus - Chrome Web Store](https://chrome.google.com/webstore/detail/markdown-preview-plus/febilkbfcbhebfnokafefeacimjdckgl?hl=en-US)

- 风格设置
  + Miscs
    * chrome extensions -> Markdown Preview Plus -> Options -> Enable HTML content Note(此选项必须点击)
  + Theme
    * Default CSS -> Github(建议风格)

- pdf生成
  + git下载duw分支
  + 用chrome打开当期duw的md文件->自动呈现为Github风格网页
  + print->save pdf
  
### pdf发布方法
- release
  + 来到[Releases](https://github.com/DebugUself/du4proto/releases)界面
  + 填写release信息
    + tag version 
      * v17.9.25(发布当日日期)
    + target branch
      * DUW
    + release title
      * DU**w
    + write
      * DU23w.pdf -> 运用浏览器手动生成
      * Source code (zip) -> release后自动生成
      * Source code (tar.gz) -> release后自动生成
    + This is a pre-release
      * 勾选此项

- 怼圈邮件列表
  + 来到gmail群组[Debug Uself 自怼圈](https://groups.google.com/forum/#!forum/debuguself)
  + 新建NEW TOPIC
    * 上传DU24w pdf

- 知识星球
  + 地址:[知识星球 - 连接一千位铁杆粉丝,知识变现,小团队共享](https://www.xiaomiquan.com/)
  + 文案:#ANN# #DUW# **w怼周刊来啦~ (其他可自由发挥)
  + 上传DU**w pdf

### 发布确认:slack吼
- 3渠道发布完成后，需在slack #general 频道 @channel宣告发布
  + `**w怼周刊来啦！[url link]`

### 反馈渠道
- 本issue[3d[TASK]怼周刊发布手册wiki反馈渠道](https://github.com/DebugUself/du4proto/issues/240)下回复，怼周刊发布手册步骤
- 或直接进入wiki[怼周刊发布手册 ](https://github.com/DebugUself/du4proto/wiki/DUW2pub)，进行增补

# changelog
- 171106 bear add slack吼
- 171030 bear add 进展 Progress/进展 py脚本命令行
- 171030 bear add 进展 Progress/提交 统计方法
- 171009 bear add DUW发布自查表
- 171002 bear add how2GetProgressTable
- 1709 bear init
