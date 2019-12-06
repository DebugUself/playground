
# 报告标题

## 0. 摘要
通过复制写好的微信爬虫代码至 translator，使zotero 保存微信网页;
## 1. 背景
保存zotero 网页时总发生错误，错误报警为
`occur a erro `

查询官方文档，发现是 translator 的问题
[dev:translators [Zotero Documentation]](https://www.zotero.org/support/dev/translators)

查询论坛后，看到官方给出的解决方案是：the translator will update automatically, or you can update your translator now. Please let us know if you encounter any further errors.

因为这些因素，我才对 translator 有了了解的兴趣。继而联想到作业，何不通过代码了解一下？

但我不会编程，可别人既然写好了，直接拿来用也行。

参考黄忠和爱文的代码
- j[IA001/mp.js.md at d5325779d9fe6e6428884952a198041c56aa33f8 · asiachrispy/IA001](https://github.com/asiachrispy/IA001/blob/d5325779d9fe6e6428884952a198041c56aa33f8/ch0/mp.js.md)
- [dev:translators [Zotero Documentation]](https://www.zotero.org/support/dev/translators)
- [How to Write a Zotero Translator - Chapter 1](http://niche-canada.org/member-projects/zotero-guide/chapter1.html)


## 2. 分析过程
1. 分别把复制好的两份代码放到 zotero-translator

![](http://olvs25obh.bkt.clouddn.com/2018-05-06-150808.png)

2. 安装zotero - scaffold 插件


下载插件
![](http://olvs25obh.bkt.clouddn.com/2018-05-06-151111.png)

安装：工具-插件-齿轮-Install
![](http://olvs25obh.bkt.clouddn.com/2018-05-06-151004.png)
安装好后如下
![](http://olvs25obh.bkt.clouddn.com/2018-05-06-151222.png)
还出现在，双击
![](http://olvs25obh.bkt.clouddn.com/2018-05-06-151300.png)

打开界面：

![](http://olvs25obh.bkt.clouddn.com/2018-05-06-151342.png)

点击左上角：load:![](http://olvs25obh.bkt.clouddn.com/2018-05-06-151440.png)
得到

![](http://olvs25obh.bkt.clouddn.com/2018-05-06-151413.png)

有时候需要加几次才出来；选择你要加的文件

3. 到这一步的时候，其实发现接下来的调试就乱了。按照- [dev:translators [Zotero Documentation]](https://www.zotero.org/support/dev/translators)调试了几次没有成功；
4. 换了思路，用zotero已经写好的其他 js 文件调试，记下成功的截图，再反过来用成功的为依据，调试微信。
5. 最后成功
## 3. 结论+ 讨论
爱文的代码我没有成功；
黄忠的没有问题。
## 5. 经验
1. 倒退别人的成果也是学习；

这里有两个倒推：
一是推爱文和黄忠的代码；结合translator 官方文档读懂代码

二是，倒推 scaffolder 的成功案例，看成功的样子是什么的，再调试自己的。

2. 遇到问题，不要因为自己不懂就跳过去。官方文档，都写的明明白白，要学会看文档解决问题。

## changelog
- 180505


