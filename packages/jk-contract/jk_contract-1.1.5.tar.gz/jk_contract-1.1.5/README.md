# jk_contract 提取合同章节、小节、首页、风险级别

## 暂时不支持广发

## 安装方法

命令行输入`pip install jk_contract`

创建新的.py文件，输入：

`-*- coding: GBK -*-`

`import jk_contract as jk`

## 函数
##### 单个合同文件
`contract = jk.Contract('[合同文件路径]')`

`print(contract.get_risk_level() # 输出风险等级)`

`print(contract.get_chapter('[章节(如：基金的投资)]' # 输出章节内容)`

`print(contract.get_section_of_chapter('[章节]', '[小节(如：投资限制、投资范围)]' #输出小节内容)`

##### 多个合同文件
`contracts = jk.Contracts('合同文件夹路径')`

提取内容可以是章节或者章节内小节：

`content = contracts.get_chapters('[章节]')`

`content = contracts.get_sections('[章节]', '[小节]') #若提取多于一个小节，[小节]需要为list（参照使用案例)`

将提取内容以基金产品名字作为index生成dataframe：

`df = contracts.get_df(content)`

最后将df导出成excel:

`contracts.to_excel(df, '[导出路径]+[导出excel文件名称].xlsx')`

举例：

`contracts.to_excel(df, '~/Desktop/output.xlsx')`

## 使用案例（提取投资限制和投资范围）

##### 方法1:创建新python文件
```
# -*- coding: GBK -*-

import jk_contract as jk

contracts = jk.Contracts('/Users/andy/Desktop/work/ubiquant/合同提取/所有合同')
contents = contracts.get_sections('基金的投资', ['投资限制', '投资范围'])
contracts.to_excel(contracts.get_df(contents), '~/Desktop/output.xlsx')
```

##### 方法2:命令行

打开命令行输入：

```
jk_contract [input路径(如：'/Users/andy/Desktop/work/ubiquant/合同提取/所有合同')] [output路径(如：/Users/andy/Desktop/work/ubiquant/合同提取/output.xlsx)] [章节(如：基金的投资)] [小节(如：投资范围 投资限制)(注：小节可以多于一个)]
```