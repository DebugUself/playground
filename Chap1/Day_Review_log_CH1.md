# Py104_Review_Log_CH1

## 激发

- Xiami 同学的[记录](https://github.com/thxiami/Py101-004/blob/master/Chap1/note/Log_1w.md)很棒!
- 开始记录,从 w2d3 开始

## w1d2_170815

- 完成 Chap1_Task               `4h`
    -  任务摘要&功能分析& JpNB 操作调试 `1h30m`
    -  字符串字典转化                 `30m` 
    -  查询互动与字典操作              `20m` 
    -  主体函数与整体调试              `1h40m` 

## w1d3_170816

- 00 点评学友代码 [dragon86yq](https://github.com/dragon86yq/Py101-004/commit/47d84392aa040f22696612260f25108675d2e440) `30m`
- 01 观看 dama mvp** `25m`

- 03 修改数字游戏的机构  `15m`
    - 激发:看卡包的结对编程视屏,发现原来的程序可改进
    - Number_Game_v2.1:
        - range(10);
        - range(1,10)

## w1d4_170817

-  00 Jupter Notebook md 渲染问题 `30m` 
-  01 对 subl 进行配置  `2h`
-  02 csv 文档细探       `1h`
    - 现象: 阐释对每个变量的含义进行深究
    - 改进: 应该上来就试运行实例代码

## w1d5_170818 

- 00 结束 Jupter Notebook md 渲染问题 `1h` 
- 01 修正 bug:重复查询无历史记录 `25m`
- 02 探索真正有效能的代码 
    - csv demo代码测试 ` 40m`
    - 测试脚本运行时间  `45m`
- 03 同侪   `45m`
    - 浏览[xiami的成长记录](https://github.com/thxiami/Py101-004/blob/master/Chap1/note/Log_1w.md#11-根据scottmg教练建议采用csv模块)
        1. 运用 timeit 测试 脚本运行时间
        2. 受其[钻研精神](https://github.com/thxiami/Py101-004/blob/master/Chap1/note/Log_1w.md#2-复盘--改进-2)触动,受到激励了.
        3. 技巧

        > 看 Hugo1030 的ipynb文件，发现在cell头部写上%%time可以输出单元代码运行时间，在函数调用前加%timeit ，如%timeit file_read_binary_buffer_and_decode(0) ，能调用timeit模块，这太方便了

## w1d6_170819

- 00 效能代码
    - 确定笔记形式  `20m`
    - 写 csv.read 的示例笔记 `40m`
    - 研究 报错  `40m`
    - csv探索完毕 `43m`
    - 对比运行时间,程序性能的思考 `1h`
    - collection,了解场景,理解 demo `40m`
        - 撰写 colection 笔记, 搜索性能判定 `40m`
- 01 回复 Issue
    - [ch1 任务难点「返回该城市天气数据」的思考 · Issue #42 · AIHackers/Py101-004](https://github.com/AIHackers/Py101-004/issues/42#issuecomment-323530954)
    - [ch1 任务难点「如何更好实现用户指令查询功能」的思考 · Issue #64 · AIHackers/Py101-004](https://github.com/AIHackers/Py101-004/issues/64#issuecomment-323538602)

- 复盘 
    - collection 似乎没有优化读取的函数?
    - 网络状况不好,影响探索探索
        - if 下载阻塞,网页打不开(1m),then 暂时搁置,切换任务
    - 多任务并行会模糊重点,降低探索速度
        - 将所有要点写于readme.md,逐条进行, 42m 记录成果,确定下一目标产出.
        - 固化节奏感
    - 提交的 commit 有些混乱,应及时分项提交.
