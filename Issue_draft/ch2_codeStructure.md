# 程序说明&字符流程图画法分享

## 激发

- [=>](https://github.com/AIHackers/Py101-004/issues/64#issuecomment-323540706) @thxiami 学友:询问程序说明中流程图的画法
- [=>](https://github.com/AIHackers/Py101-004/issues/47#issuecomment-323584531) @ishanshan 大总管: 期待分享一下写 README 的心得，和那个 structure 绘制的技巧。
- [=>](https://github.com/AIHackers/Py101-004/issues/70#issuecomment-324278297) @ Miss-3278: 程序使用说明地址： ……(一直都不知道这个该写啥，/(ㄒoㄒ)/~~)

- 所以,开个 issue 来谈谈,程序说明应该怎么写,抛砖引玉,欢迎交流指正. : D

## 思考

- 程序说明,也就是程序的 readme 文档,为什么存在?
    - 因为程序构成复杂,需要代码以外的文件来阐述
        - 用法
        - 结构
        - 功能
        - ... 
    - 即,以最快地速度
        - 让读者明了这是啥玩意

- 那么,如何真正地写清楚?
    - github 到处都是项目,到处都是 readme
    - 比如看看我们现在用的 requests
        - =>[requests/requests: Python HTTP Requests for Humans™ ✨🍰✨](https://github.com/requests/requests)
    - 相关文章说明:[Designing and Making the README file for your GitHub Repository - Darwin Biler](http://www.darwinbiler.com/designing-and-making-the-readme-file-for-your-github-repository/)
    - 乃至模板:[README.md template](https://gist.github.com/jxson/1784669)
    - 甚至不用看,自己觉得怎么能用的舒服怎么来,自觉都能有答案
- 故,参考之,提取了最基本的四点:
    - 环境:水土服否?
    - 简介:是个啥?
    - 功能:能干啥?
    - 用法:怎么干?
- 再,结合咱们课程的场景
    - 教练点评,学友点评,如何方便他们?
        - 更快更清晰 get 自己的思路
        - 更快明了程序解决过程中的关键点
        - 乃至,呈现来自他们灵感激发的改动.
    - 就有了
        - 思路步骤
        - 结构
        - 功能更新的列表
        - 探索笔记的链接
- 就成了这幅模样:[程序说明](https://github.com/NBR-hugh/Py101-004/tree/master/Chap1/project#structure)

## 心态

- 所以,答案其实就在眼前,只是许多同学毫无感知,为啥?
- 个人推测来自对自己行为的判定
    - 以做练习,交作业的学生心态来对待
- 而不是
    - 我是在开发一个真正可以发布,可以使用的产品.
- 故而从未将此当作问题来考虑
    - 只管自己写的爽
    - 那顾用户火葬场
- 学生心态要不得...

## 玩意

- 结构流程图出乎意料受欢迎 - -
- 但其实只是自己ch1思考时的一次小尝试,还不成熟
    - 怎么表达程序结构?
    - 一图胜千言
    - 想表达变量传递关系
    - 就尝试成这样
- ch1 版

```java
--------- +
{END}     ^                                                                                   +-> exit {end}
          ^                                                                                   |
(print)   ^                                                                                   |-> "user quiry history"   +->"help info"
          ^                                                                                   |                          |
(out)     ^              +->weather_dict ----------+  +->city_weather,history_list --------+  +                          |
          ^              |                         |  |                                    |  |                          |
[function]^  main()   +->file_deal()               |  weather_query()                      |  quit()                     help()
          ^   |       |  |                         |  |                                    |  |                          |
(in)      ^   |       |  +<-filename,weather_dict  |  +<-weather_dict,city,history_list    |  +<- history_list           +
          ^   |       |     ^        ^             |     ^            ^    ^               |  |   ^                      |
          ^   |       |     |        |             +-----+            |    |               +--|---+                      |
          ^   |       |     |        |                                |    |                  |                          |
(judge)   ^   |       |     |        |                              ?city  |              ?q or quit                ?h or help  ?wrong -> +
          ^   |       |     |        |                                ^    |                  ^                          ^          ^     |
          ^   |       |     |        |                                |    |                  |                          |          |     |
{BEGIN}   ^   +-----> + --> + -----> + -----------------------------> + -- + -----------------+------------------------> + -------- +     |
--------- +                                                           ^                       ^                          ^                |
          ^                                                           |                       |                          |                |
          |                                                           + ----- ------------- commond -------------------- +                |
          |                                                                                   |                                           |
          |                                                                                   +                                           |
Waiting...|                                                                                (input)< ------------------------------------- +
--------- +
```

- ch2 版

```java
--------- +
{END}     ^                                                               + ->exit()
          ^                                                               |
(print)   ^                + ->"help_info"  + ->"history" & "help_info"   |               + ->"c error"    + -> "city,weather,temp"            + -> 'NOT FOND'
          ^                |                |                             |               |                |                                   |
[out]     ^                |                |                             |               |                +-> weather_dict,history_list       +-------> + ---> +
          ^                |                |                             |               |                |                                   |         ^      |
[function]^                +-wq.help_info() +-wq.show_history()           +-wq.quit()     |                +-json_handle()                     |         |      |
          ^                |                |                             |               |                |                                   |         |      |
[in]      ^                |                history_list<----- + -------> +history_list   |                +response,weather_dict,history_list |         |      |
          ^                |                |                  |                          |                |                   ^         ^     |         |      |
(judge)   ^                ?h,help          ?history           |             ?quit        ?else            ?200                |         |     ?404      ?else  |
          ^                ^                ^                  |             ^            ^                ^                   |         |     ^         ^      |
          ^                |                |                  |             |            |                |                   |         |     |         |      |
          ^                + -------------- + ------------------------------ +----------- +                + --------------------------------- + ------- +      |
          ^                |                                   |                                           |                   |         |                      |
[pass]    ^             command     history_list-------------- +                                  response.status_code         |         |                      |
          ^                ^        ^                                                                      ^                   |         |                      |
          ^                +--------+                                                                      |                   |         |                      |
          ^                |                                                                               |                   |         |                      |
[function]^  +main()       +wq.command_work()                                                              +get_API_requests() |         |                      |
          ^  |             |                                                                               |                   |         |                      |
[in]      ^  |             +-command                                                                       +city,    weather_dict,history_list                  |
          ^  |                 ^                                                                           ^              ^        ^                            |
          ^  |                 |                                                                           |              |        |                            |
(judge)   ^  |             ?command:in command_tuple                                                       ?command:else  |        |                            |
          ^  |             ^                                                                               |              |        |                            |
          ^  |             |                                                                               |              |        |                            |
{BEGIN}   ^  + ----------> + ----------------------------------------------------------------------------- + ------------ + ------ +                            |
--------- +                                                                                                                                                     |
          |                ^command                                                                                                                             |
          |                |                                                                                                                                    |
waiting...|              (input) <----------------------------------------------------------------------------------------------------------------------------- +
--------- +
```

- 大致步骤如下:
    - 01  构造第一个[function]层,将所有函数名称按运行顺序依次排开,输入的变量对应地放下2行,输出的变量对应地放上2行
    - 02 然后把自己当作运行程序的光标,从 main() 开始逐行运行,顺关系,画的优先级如下
        - 判断结构
        - 函数执行
        - 变量传递
    - 03 一条一条分支顺下来,整体的顺序是
        - 从下到上
        - 从左往右,表头最好先画好
        - 先画横线与节点,再画竖线
    - 04 如果在某个函数中调用函数,则需要再来一层[function] 
        - 如ch2版中所示
    - 05 基本上就是把表头中对应的量固定在对应的行,根据长度进行左右调整
    - 06 注意 md格式,用\`\`\` \`\`\` 来包含才不会变化, java 的渲染比较合适
        \`\`\`java
        \`\`\` 

- 但**缺点**也很明显
    - 程序过于复杂就没办法了
    - 也还没想好`类`应该如何放置
    - 用时极其长
        - 第一幅图由于第一次摸索,1h 45min
        - 第二幅考虑嵌套函数的结构,1h 50min
        - 强迫症患者请慎重...
    - 纯手动烦人,成本太高了
    - 除非,能够自动化...
    - 嗯哼?!
- 因此,其实并不推荐具体方法
    - 理想用时应该是15~20m成一张图
    - 还有待完善/乃至抛弃...
    - 我也只是强迫症,开了头就想把它完成
- 更重要的是背后的想法
    - 任何系统都可以拆解成输入-处理-输出的单元
    - 函数是这一形式的典型
    - 单元内/间的请求与响应必然可以用箭头表示关系
    - 判断结构尽可能放在一处(个人喜好)
    - ...

- 所以,是否还有什么快速 get 程序结构关系的好方法/工具?你是怎么想的呢!
 
- 以上,抛砖完成. : D

## 源

- DAMA:

    >出入-处理-输出
    >在战斗中学习战斗

## Timelog

- 170824 NBR-gugh `1h 30 m`
