# 项目：域名IP解析器

## 概述

本项目是一个Python脚本，旨在将域名解析为相应的IP地址，并将结果写入文本文件。它利用并发处理提高效率，并使用日志记录功能以便于调试和跟踪。

## 特性

- **并发域名解析**：使用`concurrent.futures.ThreadPoolExecutor`进行异步DNS查询。
- **日志记录**：使用Python的`logging`模块记录成功解析和错误信息。
- **输出到文件**：结果被写入`domain_ip_map.txt`文件，格式为制表符分隔值（TSV）。

## 先决条件

- Python 3.x
- `socket` 库（包含在Python标准库中）
- `concurrent.futures` 库（包含在Python标准库中）
- `logging` 库（包含在Python标准库中）

## 设置

1. **准备域名列表**：确保你有一个`domains.txt`文件，该文件与脚本位于同一目录下。此文件的每一行应包含一个域名。

2. **运行脚本**：使用Python执行脚本。它将创建或覆盖`domain_ip_map.txt`文件，填入解析的IP地址。

## 使用方法

通过在终端执行以下命令来运行脚本：

```bash
python path/to/your/script.py
```

确保`domains.txt`文件格式正确，并且位于预期的目录中。

## 代码解析

- **日志设置**：配置日志级别和格式。
- **`get_ip_address(domain)`**：尝试将域名解析为IP地址并记录结果。
- **`read_domains_from_file(filename)`**：从提供的文件中读取域名。
- **`main()`**：组织读取域名、解析IP并写入结果文件的过程。
- **并发执行**：使用线程池执行器同时解析多个域名。
- **错误处理**：捕获并记录域名解析过程中发生的异常。

## 输出

脚本生成一个名为`domain_ip_map.txt`的文件，其中每行包含一个IP地址和相应的域名，二者由制表符分隔。

## 示例 `domains.txt` 文件内容

```
github.githubassets.com
central.github.com
desktop.githubusercontent.com
assets-cdn.github.com
```

## 示例 `domain_ip_map.txt` 输出内容

```
185.199.109.154	github.githubassets.com
140.82.114.21	central.github.com
185.199.110.133	desktop.githubusercontent.com
185.199.108.153	assets-cdn.github.com
```

## 日志

日志以信息和错误级别生成。检查控制台或日志文件以获取解析过程的详细信息。

## 注意

- 确保脚本具有读取和写入目录中文件的必要权限。
- 每次运行脚本时都会覆盖`domain_ip_map.txt`文件。

## 许可

本项目是开源的，并可在[MIT许可](https://opensource.org/licenses/MIT)下获得。如有必要，请随意修改和分发。