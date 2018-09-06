# Py104_Review_Log_CH2

## w2d0_170820

### 事项

- [ ] 根据 @thxiami 同学的方案亮点优化 
    - =>[Py101-004/Chap1/project at master · NBR-hugh/Py101-004](https://github.com/NBR-hugh/Py101-004/tree/master/Chap1/project#update)
    - 报错:try except
    - mainmap
    - 比 if else 更高效的分支形式
    - 思考:如何理解他人代码? & 如何让他人容易理解自己的代码?

### 敌友

- 现象:长时间盯着屏幕,眼睛和颈椎略酸
- 原因:间歇时间未做必要休憩活动,大脑进入死线重复式当机
- 措施:if 闹钟响第二声, then 出去绕房一圈 or 倒水喝水

### 复盘

- 理解他人的代码,由源文件重头顺一遍,比局部摸索更高效
- 注意休息,一松一紧,大紧小松,不郁结,注意求助临界点,保持高效投入的探索节奏.
- CH1 的探索还未完成,CH2任务完成后回来继续

## w2d1_170821

### 事项

- [ ] 开启 CH2 探索
    - [ ] 刷卡包,列功能 `20mm`
    - [ ] 理解 api,比较三个天气api `42m`
    - [ ] requests下载安装,快速启用 `42m`

## 敌友

- 现象: 学 requests 时会穷尽所有用法,效率降低
- 原因: 写笔记追求完备的内隐冲动,没有把解决问题,MVP 先行放在第一位
- 措施: 先写必要的用法,其他功能可以浏览一下标题有个映像,将不懂的名词列出, mvp 完成后回头研究

### 复盘

- 注意单位时间内的效率而不是用时的长短
- 注意演绎而不要穷尽
- 状态不好就先放下,保证基本投入的前提下,可以看书散步做别的,好好睡觉,来日再战.

## w2d2_170822

### 事项

- CH2 基本投入完成 mvp,明日完成程序说明以及笔记修缮后提交
    - 理解 import 机制,尝试使用相对导入失败 `42m`
    - 转换关键词,import 绝对导入成功 `20m` 
    - 改造:change ch1 to import  `42m`
    - 根据调试体验再次改造 `42m`
    - chaos: 改造错误,判断结构不可复用 `42m`
    - 对 requests 进行判断 `42m`
    - 主题调通,检查通读笔记 `42m`
    - 写了一首小诗 `20m`

### 敌友

- 现象:在分析判断结构时陷入思维混乱
- 分析:多个判断对象/层级导致决定纠结,没有特别理想的方案就此混乱
- 措施:及时记录及时分解,让思路显现化才能更容易暴露问题所在


### 复盘

- 只用英文关键词进行搜索
- 官方文档 和 Stack Overflow 是最高效的编程问题方案来源,多用多看,方向是对的,慢就不怕

## w2d3_170823

### 事项

- 提交 ch2 `20m`
-  撰写流程图说明,回复issue `1h40m`
    - =>[ch1 任务难点「如何更好实现用户指令查询功能」的思考 · Issue #64 · AIHackers/Py101-004](https://github.com/AIHackers/Py101-004/issues/64#issuecomment-323540706)
    -  [@ishanshan:readme 撰写分享](https://github.com/AIHackers/Py101-004/issues/47#issuecomment-323584531)
- 提交变量与全局变量的issue  `15m`  `车上`

### 敌友

- 没有时间只是借口,小心借口和自欺

### 复盘

- 只用英文关键词进行搜索
- 官方文档 和 Stack Overflow 是最高效的编程问题方案来源,多用多看,方向是对的,慢就不怕

## w2d4_170824

- 温度单位转换方案2 `20m`
- 指定地点指定日期 `20m`

## w2d5_170825

- 模块化 `20m`
- 指定天气查询:思路错误,重写 `42m`

## w2d6_170826

- improt 相对导入再探 `1h10m`
- 查询判断分支梳理, help 改造 `1h` `WARN`
- 改写 API_deal 模块 `42m`
- 日期查询整体完成 `42m`

### 复盘

- 改写程序比从头开写有慢又快
    - 慢在需要不停地调整结构,思考如何将功能最小改动的放进去
        - 那么时候时候适合重构?
        - 有哪些原则可以借鉴?
        - 如何提高重构的效率?
    - 快在功能原来就有了,只要模块复用性强,接口清晰明了,重构的速度就非常快
- 注意代码规范,`,`前无空格,后有空格
- 从始至终都还未使用类,其实是还不明白类的特性,有点,适用场合,必须坚持一个原则
    - 保证代码的正确性,能运行,进可能简洁
    - 因此没有必要的理由,还不甚清楚的知识暂时先放着,需要进一步探索.
- 写代码,读学友代码,看书,看源码要合理分配时间
    - 有时间限制与发布压力才有好的表现