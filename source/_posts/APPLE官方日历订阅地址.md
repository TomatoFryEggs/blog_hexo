---
title: APPLE官方日历订阅地址
date: 2019-03-28 13:44:08
tags: iOS APPLE
---

> 因：为了在iOS上kindle使用Google和wiki，将手机地区改成了HK。

用了几天，便发现手机上的日历也被改成了HK地区的节假日。在网上查询了很多结果，发现大多数给订阅链接都是http、https开头，点击后iOS设备（iOS12.2）会将日历添加到私人日历中而不是新的日历订阅，研究发现，只要将http(s)改成webcal就生成单独订阅了。

仔细观察，发现APPLE官方提供的地址为国家（地区）日历规律为：

```
webcal://p10-calendars.icloud.com/holiday/<ISO 3166-1 Alpha 2 code>_<ISO 639-1 code>.ics
```



##### 附常用订阅LIST：

中国大陆法定节假日
[webcal://p22-calendars.icloud.com/published/2/RL1JwQQtKFudYOiicAG_adz9DdrozFeZzv5Uyrs4s3gyWobdzL1NZFH-ZHAsTfuAevtnzdqVdYmcRO_Y_dWtxeIdmzUA1TNkAt5RuotJmsg](webcal://p22-calendars.icloud.com/published/2/RL1JwQQtKFudYOiicAG_adz9DdrozFeZzv5Uyrs4s3gyWobdzL1NZFH-ZHAsTfuAevtnzdqVdYmcRO_Y_dWtxeIdmzUA1TNkAt5RuotJmsg)

中国内地节日
[webcal://p10-calendars.icloud.com/holiday/CN_zh.ics](webcal://p10-calendars.icloud.com/holiday/CN_zh.ics)

中国台湾节日
[webcal://p10-calendars.icloud.com/holiday/TW_zh.ics](webcal://p10-calendars.icloud.com/holiday/TW_zh.ics)

中国香港节日
[webcal://p10-calendars.icloud.com/holiday/HK_zh.ics](webcal://p10-calendars.icloud.com/holiday/HK_zh.ics)

美国
[webcal://p10-calendars.icloud.com/holiday/US_en.ics](webcal://p10-calendars.icloud.com/holiday/US_en.ics)

日本
[webcal://p10-calendars.icloud.com/holiday/JP_ja.ics](webcal://p10-calendars.icloud.com/holiday/JP_ja.ics)

澳大利亚
[webcal://p10-calendars.icloud.com/holiday/AU_en.ics](webcal://p10-calendars.icloud.com/holiday/AU_en.ics)

法国
[webcal://p10-calendars.icloud.com/holiday/FR_fr.ics](webcal://p10-calendars.icloud.com/holiday/FR_fr.ics)

德国
[webcal://p10-calendars.icloud.com/holiday/DE_de.ics](webcal://p10-calendars.icloud.com/holiday/DE_de.ics)

英国
[webcal://p10-calendars.icloud.com/holiday/GB_en.ics](webcal://p10-calendars.icloud.com/holiday/GB_en.ics)

