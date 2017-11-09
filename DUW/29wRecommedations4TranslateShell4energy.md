# 推荐 Recommedations
~ 嗯哼各种怼路上发现的嗯哼...

#### 管理你的精力，而不是你的时间   
- [管理你的精力，而不是你的时间](https://mp.weixin.qq.com/s/dgm9nq156L8PqTw-4aTB9w)
- 本文作者提出将精力分为4种：体力、关注的精力、情绪的精力、和精神的精力。
    + 关注的精力:单线工作，心流状态不容易累；多线工作容易累
    + 情绪的精力:做喜欢的事不觉得累；做枯燥的事容易累
    + 精神的精力:潜意识里认为这事有意义，不累；潜意识觉得这事无意义，容易累
- 作者认为，要有意识地为 **重要的、困难的** 事情，预留精力。

#### Translate Shell
- [soimort/translate-shell: Command-line translator using Google Translate, Bing Translator, Yandex.Translate, etc.](https://github.com/soimort/translate-shell)
- Translate Shell 的前身是Google Translate CLI。它是一款由Google Translate, Bing Translator, Yandex.Translate and Apertium等多家翻译巨头驱动的命令行翻译应用。您可以在终端这样使用它:
        
```
$ trans 'Saluton, Mondo!'
Saluton, Mondo!

Hello, World!

Translations of Saluton, Mondo!
[ Esperanto -> English ]
Saluton ,
    Hello,
Mondo !
    World!
```

- Translate Shell 也有人机交互界面:用户输入文本，Translate Shell将逐行翻译用户输入的这些文本，如下:

```
$ trans -shell -brief
> Rien ne réussit comme le succès.
Nothing succeeds like success.
> Was mich nicht umbringt, macht mich stärker.
What does not kill me makes me stronger.
> Юмор есть остроумие глубокого чувства.
Humor has a deep sense of wit.
> 學而不思則罔，思而不學則殆。
Learning without thought is labor lost, thought without learning is perilous.
> 幸福になるためには、人から愛されるのが一番の近道。
In order to be happy, the best way is to be loved by people.
```