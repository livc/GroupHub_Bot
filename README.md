# GroupHub - Telegram Bot

“GroupHub_Bot”顾名思义，是一个收录telegram中文圈群组的机器人。

在tg群组娘项目不再维护后，GroupHub将担负起活跃tg中文圈的使命。

Bot：[@GroupHub_bot](https://telegram.me/GroupHub_bot)

GroupHub交流群：[GroupHub_Chat](https://telegram.me/GroupHub_Chat)

广播站（新收录群组会在此广播）：[@GroupHub](https://telegram.me/GroupHub)

管理员：[@livc95](https://telegram.me/livc95)

## 群组收录、更新
所有已收录的群组存储在 [groups.json](https://github.com/livc/GroupHub_Bot/blob/master/groups.json) 中，采用**BASE64**进行简单混淆（此举是因为有部分敏感内容的群组信息不宜直接暴露出来 - - ）。

群组的收录更新有两种方法：

- 直接将群组名、邀请链接、讨论主题发给[@livc95](https://telegram.me/livc95)。
- 在 [groups.json](https://github.com/livc/GroupHub_Bot/blob/master/groups.json) 中对应分类直接添加群组信息，然后发起Pull request。

**※** 第二种方法提交需注意：

- 超级群组直接将群组信息编码为BASE64，然后添加到json对应分类后面即可，如

> wordpress站长交流群 @wordpress_china
> 编码后为
> d29yZHByZXNz56uZ6ZW/5Lqk5rWB576kIEB3b3JkcHJlc3NfY2hpbmE=
> 于是添加
> "TEXT": "d29yZHByZXNz56uZ6ZW/5Lqk5rWB576kIEB3b3JkcHJlc3NfY2hpbmE="


- 非超级群组（也就是没有@xxx 链接的群组）需要提交为markdown格式的编码，即 \[群组名\]\(邀请链接\)，如
                                               
> [V2EX后花园](https://telegram.me/joinchat/Bg3MFjv5FgYrWI0WqHDo8Q)
> 编码后为
> W1YyRVjlkI7oirHlm61dKGh0dHBzOi8vdGVsZWdyYW0ubWUvam9pbmNoYXQvQmczTUZqdjVGZ1lyV0kwV3FIRG84USk=
> 于是添加
> "TEXT": "W1YyRVjlkI7oirHlm61dKGh0dHBzOi8vdGVsZWdyYW0ubWUvam9pbmNoYXQvQmczTUZqdjVGZ1lyV0kwV3FIRG84USk="
                                               
## BUG提交、功能建议

请到[Issues](https://github.com/livc/GroupHub_Bot/issues)页面反馈。

----------
新功能持续开发中……
