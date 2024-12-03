# colorcharify

## 简介
`colorcharify.py.py` 是一个 Python 脚本，用于将图片转换为彩色字符组成的图像。

## 特性
- 将图片转换为彩色字符组成的图像；
- 支持自定义字体；
- 支持自定义使用的字符；

## 准备

1. 确保您的系统已安装 `Python 3.x`；

2. 确保您的系统已安装以下Python第三方库：
   - `pillow`；
   - `tqdm`；
   - `numpy`.

   使用命令：

   ```bash
   pip install pillow tqdm numpy
   ```

   若您在安装numpy时遇到错误，请尝试：

   ```bash
   apt install python-numpy
   ```

3. 克隆此仓库：
   ```bash
   git clone https://github.com/tile-WWDCCS-name/colorcharify
   cd colorcharify
   ```

## 使用方法
运行脚本时，需要指定输入图片路径和输出图片路径。可以使用以下命令行参数：

```bash
python colorcharify.py <image_path> <output_path> <characters> [options]
```

### 参数说明
- `image_path`: 输入图片的路径；
- `output_path`: 输出图片的路径；
- `characters`: 要使用的字符；
- `-s`, `--size`: 横向汉字个数，默认为 300；
- `-cs`, `--char_size`: 单个汉字的尺寸，默认为 12；
- `-fp`, `--font_path`: 字体路径，默认为脚本所在文件夹下的 `font.ttf`；

### 示例
```bash
python colorcharify.py input.jpg output.png 这是几个字符 -s 400 -cs 14
```

## 注意事项
- 确保输入的图片路径正确且图片格式受支持；
- 字体文件（如 `font.ttf`）需放在与脚本相同的目录下，或者提供正确的路径；
- 对于较大的 `--size` 或 `--char_size` 参数值，处理时间可能会较长；
- 若您需使用其他的自定义字体，请确保您的字体能够显示您需要的字符。
