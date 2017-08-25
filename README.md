# 小密圈备份

为了避免再次发生`与其相信谣言，不如相信XXX`的悲剧

---

目前备份了 	20170824
1. `代码审计-2212251881`
2. `qz安全情报分析-1852214142`
3. `安全数据与机器学习-5421844144`

---

后面不再push备份的json
如有需要修改 xiaomiquan_bak.py 中的 config 备份自己想要的圈子

```
token
name
user_id
avatar_url
```

--- 

## Requirement

* `python 2.7`
* `pip install requests`

--- 

## Usage

### step 1 `网页端登录后获取cookies`
![step 1](https://ws2.sinaimg.cn/large/a15b4afegy1fiw5vsqcocj211g09cmye.jpg)

### step 2 `修改 xiaomiquan_bak.py`
![step 2](https://ws2.sinaimg.cn/large/a15b4afegy1fiw5xfydk9j20gj029749.jpg)

### step 3 `设置需要备份的圈子ID`
![step 3](https://ws2.sinaimg.cn/large/a15b4afegy1fiw5y83q35j20a0028a9w.jpg)

### step 4 `python xiaomiquan_bak.py`