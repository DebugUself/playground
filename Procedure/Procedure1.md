# Procedure1迁移到playground/zsy

----
## 第1版
### du4proto 
~ s08 登记梳理 + BASIC:yesterday时间 + today目标

### du4zsy
~ Nt 登记yesterday睡眠情况 + today睡眠目标
~ DUW 登记怼周刊发布手册 + 投稿
~ JOBWeekly 登记找工作

### blog.io 
~ PAPER 登记PaperLog 
~ Rd 登记日常读书Rd
~ RunWang 登记家庭旅行

## 第1版存在的问题
- 登记每日成果时,需要在du4zsy与blog.io 2个分别独立的分支搜索commit history
- 如果放在du4zsy分支上,所有文档都是私有库,无法共享给非怼员
- 如果放在blog.io分支上,分支commit又无法在slack上被其他怼员观察到

## 第1版改进的目标
- 所有文档放在1个分支上,只需查看1个分支的commit history
- 该分支可以共享给非怼员
- 该分支commit在slack #gh 频道可以被怼员观察到

## 第1版改进的方案
- 目标分支:DU orginazation/playground repository/zsy branch
- 测试该分支
    + 是否为private repo?
        * [x] 否
        * [x] 可分享文档给非怼员
    + 是否在slack #gh 频道可以被怼员观察到
        * [x] 可
- 文档迁移
    + RunWang 从blog.io迁移至playground/zsy
    + PAPER 从blog.io迁移至playground/zsy
    + Rd 从blog.io迁移至playground/zsy
    + Nt 从du4zsy迁移至playground/zsy
    + DUW 从du4zsy迁移至playground/zsy
    + JOBWeekly 从du4zsy迁移至playground/zsy

----
## 第2版
### du4proto 
~ s08 不变动

### 迁移至pl4zsy
注:本地目录为pl4zsy,远程仓库分支为playground/zsy

~ 从du4zsy迁移至playground/zsy
~ 从blog.io迁移至playground/zsy

- [x] Nt 
- [x] DUW 
- [x] JOBWeekly 
- [x] PAPER 
- [x] Rd 
- [x] RunWang 
- [x] Procedure 

# Changelog
17.11.09 bear init,1hr