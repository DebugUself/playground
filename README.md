## 更改说明

### 实现功能
在前端页面输入一个动作的信息，点击“添加”后，存入数据库，并在命令行显示所有的历史数据。

### 增加了前端和后端的数据通信功能
使用jquery实现了html和flask之间的数据传递，将用户在前端输入的数据传给后台处理。

addExerciseform.html修改如下：
1. 第6行增加如下代码，调用jquery模块。
	`<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
	`

2.  增加63到65行代码，在按下“添加”按钮时，会将movrc赋值给movdata，并通过post传递出去。
	 `document.getElementById("theButton").onclick = function() {
	`  `getMov()
	``  $.post( "/postmov", { movdata: movrec });
	``   };
	`
3. 为了实现上面的代码，需要给“添加”按钮增加一个id，在99行修改了如下代码。

	 `<input id = "theButton" type="submit" name=“addex” value="添加" ">
	`

FitLog.py代码修改如下：

1. 增加16到18行代码，用于接受前端传递的数据。

	` @app.route('/postmov', methods = 'POST')
	`  `def getpostmovdata():
	`` mdata = request.form'movdata'  
	`
### 数据库调用接口修改
此修改只影响函数调用，数据库结构没有做任何修改。
1. 为了方便日后多组动作同时传递，在每个动作之间使用逗号隔开，在addExerciseform.html修改如下，在末尾加了一个逗号：

	 `movrec = daterecord + " " + exercise + " " +
	`` time + " " + repetition + " " + set + " " + weight + " " + distance+","
	`
2. record_movement存储动作库的返回值增加了日期，方便record_fitdata直接调用，如FitLog.py的19到21行所示：

	 `fitdate,fitdata = recordmovement(mdata) 
	`` recordfitdata(fitdate,fitdata) #将健身日期和本次动作存入健身数据库
	`










