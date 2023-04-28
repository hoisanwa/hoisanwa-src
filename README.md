# 台山话字词典 / Hoisanwa Dictionary

本仓库收有 https://hoisanwa.github.io 嘅原始数据，以及相关嘅预处理代码。

This repo contains the source data (as an Obsidian Vault) and preprocessing scripts for https://hoisanwa.github.io.

## 自建离线版 / Build from source

浏览离线版有两种方法。其一，係用 [Obsidian.md](https://obsidian.md) 打开 `Hoisanwa/` 文件夹；其二，係将 `Hoisanwa/`嘅内容转格成网页，再用浏览器打开。托管到 https://hoisanwa.github.io 嘅网页版，正係用 [obsidianhtml](https://pypi.org/project/obsidianhtml/) 将本仓库的 `Hoisanwa/` 嘅内容转成 HTML。如需自建本地离线版，可用 `pip` 安装 `obsidianhtml`：

```
pip install obsidianhtml
```

然后将本仓库克隆到本地，最后用运行 `obsidianhtml`：

```bash
git clone https://github.com/hoisanwa/hoisanwa-src
obsidianhtml run -f Hoisanwa/Home.md -i config.yaml --clean
```

即可在本地离线浏览网页版。

## 参与本项目 / Join Us

如果想参与本项目，你可以：

1. Fork 本仓库，参照以有嘅条目编写你想加入嘅词条（`Hoisanwa/words/xx.md`）同录音（`Hoisanwa/audios/xx-口音-性别.m4a`），然后递交 pull-request；
2. 到 [Issue](https://github.com/hoisanwa/hoisanwa-src/issues)提要求，或到[Discussion](https://github.com/hoisanwa/hoisanwa-src/discussions) 发起讨论。


