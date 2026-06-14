# pydogsay

> Like `cowsay`, but with a dog. 🐕

A lightweight Python CLI that prints your message in a speech (or thought) bubble next to ASCII dog art.

---

## English

### Features

- Multiple dog styles: `default`, `small`, `big`, `think`, `bone`
- Speech and thought bubbles
- Text wrapping with configurable width
- Optional tongue and tail-wag animation
- Reads from arguments or stdin — zero dependencies beyond Python 3

### Requirements

- Python 3.7+

### Installation

Clone the repo and run directly:

```bash
git clone https://github.com/pyughub/pydogsay.git
cd pydogsay
python pydogsay.py "Hello, world!"
```

Or make it executable (Unix):

```bash
chmod +x pydogsay.py
./pydogsay.py "Woof!"
```

### Usage

```bash
python pydogsay.py [OPTIONS] [MESSAGE ...]
```

If no message is given, pydogsay reads from **stdin**. An empty input defaults to `Woof!`.

### Options

| Flag | Description |
|------|-------------|
| `-t`, `--thought` | Use a thought bubble instead of speech |
| `-d`, `--dog STYLE` | Dog style: `default`, `small`, `big`, `think`, `bone` (default: `default`) |
| `-w`, `--width N` | Max text wrap width (default: 40) |
| `-l`, `--list` | List all dog styles and exit |
| `-T`, `--tongue` | Add a tongue to the default dog |
| `-W`, `--wag` | Show a wagging tail animation (3 frames) |
| `-h`, `--help` | Show help |

### Examples

```bash
# Basic usage
python pydogsay.py "Who's a good developer?"

# Thought bubble with a big dog
python pydogsay.py -t -d big "Hmm... treats?"

# Pipe from another command
echo "Deploy succeeded!" | python pydogsay.py

# Preview all dog styles
python pydogsay.py -l

# Wagging animation (Ctrl+C to stop)
python pydogsay.py -W "Happy deploy day!"
```

### Sample output

```
 ______________________
< Who's a good developer? >
 ----------------------
      / \__
     (    @\___
     /         O
    /   (_____/
   /_____/   U
```

### License

MIT — see [LICENSE](LICENSE).

---

## 中文

### 功能

- 多种狗狗 ASCII 造型：`default`、`small`、`big`、`think`、`bone`
- 支持对话气泡与思考气泡
- 可配置文字换行宽度
- 可选吐舌头与摇尾巴动画
- 支持命令行参数或标准输入，仅依赖 Python 3 标准库

### 环境要求

- Python 3.7+

### 安装

克隆仓库后直接运行：

```bash
git clone https://github.com/pyughub/pydogsay.git
cd pydogsay
python pydogsay.py "你好，世界！"
```

Unix 系统可添加可执行权限：

```bash
chmod +x pydogsay.py
./pydogsay.py "汪汪！"
```

### 用法

```bash
python pydogsay.py [选项] [消息 ...]
```

未提供消息时，从**标准输入**读取；若输入为空，默认显示 `Woof!`。

### 选项

| 参数 | 说明 |
|------|------|
| `-t`, `--thought` | 使用思考气泡（而非对话气泡） |
| `-d`, `--dog STYLE` | 狗狗造型：`default`、`small`、`big`、`think`、`bone`（默认：`default`） |
| `-w`, `--width N` | 文字最大换行宽度（默认：40） |
| `-l`, `--list` | 列出所有狗狗造型并退出 |
| `-T`, `--tongue` | 为默认狗狗加上舌头 |
| `-W`, `--wag` | 播放摇尾巴动画（3 帧循环） |
| `-h`, `--help` | 显示帮助信息 |

### 示例

```bash
# 基本用法
python pydogsay.py "谁是最棒的开发者？"

# 思考气泡 + 大狗
python pydogsay.py -t -d big "嗯……有零食吗？"

# 管道输入
echo "部署成功！" | python pydogsay.py

# 预览所有造型
python pydogsay.py -l

# 摇尾巴动画（Ctrl+C 停止）
python pydogsay.py -W "部署日快乐！"
```

### 输出示例

```
 ______________________
< 谁是最棒的开发者？ >
 ----------------------
      / \__
     (    @\___
     /         O
    /   (_____/
   /_____/   U
```

### 许可证

MIT — 详见 [LICENSE](LICENSE)。
