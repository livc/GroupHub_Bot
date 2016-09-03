# GroupHub - Telegram Bot

“GroupHub_Bot”是一个收录telegram中文圈群组的机器人。

![](http://ww3.sinaimg.cn/large/9cd77f2ejw1f7g6vi60xig20ae0gw1h2.gif)

Bot：[@GroupHub_bot](https://telegram.me/GroupHub_bot)

GroupHub交流群：[GroupHub_Chat](https://telegram.me/GroupHub_Chat)

广播站（新收录群组会在此广播）：[@GroupHub](https://telegram.me/GroupHub)

管理员：[@livc95](https://telegram.me/livc95)

## 群组收录、更新
所有已收录的群组存储在 [groups.json](https://github.com/livc/GroupHub_Bot/blob/master/groups.json) 中，采用**BASE64**进行简单混淆。

群组的收录更新有两种方法：

- 直接将群组名、邀请链接、讨论主题发给[@livc95](https://telegram.me/livc95)。
- 在 [groups.json](https://github.com/livc/GroupHub_Bot/blob/master/groups.json) 中对应分类直接添加群组信息，然后发起Pull request。

**※** 第二种方法提交需注意：

- 超级群组直接将群组信息编码为BASE64，然后添加到json对应分类后面即可，**内容中有下划线的前面需要加反斜线“\”解析**（这是因为GroupHub_bot 采用markdown格式传输信息，下划线会被telegram识别为斜体的标识符），如：

	wordpress站长交流群 @wordpress\\_china
	编码后为d29yZHByZXNz56uZ6ZW/5Lqk5rWB576kIEB3b3JkcHJlc3NcX2NoaW5h
	于是在对应分类后面添加
	"TEXT": "d29yZHByZXNz56uZ6ZW/5Lqk5rWB576kIEB3b3JkcHJlc3NcX2NoaW5h"

- 非超级群组（也就是没有@xxx 名字的群组）需要提交为markdown格式的BASE64编码，即 \[群组名\]\(邀请链接\)，链接中如有下划线不需要解析如：

	\[V2EX后花园\]\(https://telegram.me/joinchat/Bg3MFjv5FgYrWI0Wq_HDo8Q)
	编码后为
	W1YyRVjlkI7oirHlm61dKGh0dHBzOi8vdGVsZWdyYW0ubWUvam9pbmNoYXQvQmczTUZqdjVGZ1lyV0kwV3FfSERvOFEp
	于是在对应分类后面添加
	"TEXT": "W1YyRVjlkI7oirHlm61dKGh0dHBzOi8vdGVsZWdyYW0ubWUvam9pbmNoYXQvQmczTUZqdjVGZ1lyV0kwV3FfSERvOFEp"
                                        
                                     
## add.py 脚本使用方法
add.py 是一个在向本地 groups.json 文件中插入新群组的脚本，使用时需将 add.py 和 groups.json 放在同一目录。

	python add.py 分类名 群组1信息 群组2信息 ...

如 

	python add.py 软件 "wordpress站长交流群 @wordpress\_china" "[V2EX后花园](https://telegram.me/joinchat/Bg3MFjv5FgYrWI0Wq_HDo8Q)"


## Inline mode
Inline mode 让你可以在任意会话（group, channel or chats）中与bot交互。

GroupHub_bot 的 inline mode 是发送颜文字。

![](http://ww1.sinaimg.cn/large/9cd77f2ejw1f7g6pqlf2gg20ae0gw7bg.gif)

其中标签关键字索引可以在 [yan.json](https://github.com/guo-yu/o3o/blob/master/yan.json) 中找到。

## BUG提交、功能建议

请到 [Issues](https://github.com/livc/GroupHub_Bot/issues) 页面反馈。

----------
新功能持续开发中……
