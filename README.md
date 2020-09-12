> 爬取中国地震网的所有数据

# 依赖

> 所需依赖

- Python 3 

- Scrapy 

- MongoDB

# 使用

> 使用方法

1. 设置 `MONGO_URI` 、 `MONGO_DATABASE` 和 `COLLECTION_NAME` 环境变量

2. 运行爬虫

   ```python
   scrapy crawl earthquake
   ```


# 数据字段

> 存储数据的结构

| 字段名称        | 说明         |
| :-------------- | ------------ |
| latitude        | 震点纬度     |
| longitude       | 震点经度     |
| location        | 震点位置     |
| strength        | 地震强度     |
| earthquake_time | 地震发生时间 |

