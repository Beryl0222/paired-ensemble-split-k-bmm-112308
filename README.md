# 气象扰动的配对 Split-K 矩阵乘与守恒舍入

集合扰动投影的输入块、回执及单精度交接。 仓库记录均为本地合成资料，不依赖外部数据服务。

## 数据约定

a 是 [批,行,存储K]，b 是共享的 [存储K,输出列]。全体数最初解读为 IEEE-754 binary32。logical_k 后属于填充。数学扰动大小为原二进制输入值的实数点积，不在 K 段边界舍入。

terms_binary64 提供可精确加到总量的各分量乘积，rounded32 是按本设备局部加法口径的诊断值，不能从该值复原块的确切贡献。read_permitted 约定消费者何时能访问原资料；未获准的输入原值仅用于事后复核。回执版别以本次 A、B 和控制场版本为共同身份。

设备接受有限 binary32 的对值 (X+,X−)。配对要求 (X++X−)/2 在实数意义精确等于控制场。以 (X+−X−)/2 为设备真实扰动，选与数学扰动绝对偏差最小的合法对，代价并列时绝对扰动较小者优先。还需满足 max_abs_error 及幅值衰减不得超过 max_attenuation。0 的正负位型统一按 +0。

## 读取与核对

在 Python 3.11 环境执行 `python -m pip install -r requirements.txt` 安装数值依赖。
`python -m unittest discover -s tests -v` 读取 `data/exchange.json` 并核对资料结构与关键输入关系。
