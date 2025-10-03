# 模拟电路计算器

## 项目介绍
这是一个辅助计算场效应晶体管(FET)不同工作状态参数的图形界面程序。用户可以通过选择FET类型、输入参数，计算并查看各种工作模式下的晶体管特性和参数值。

## 功能特点
- 支持多种类型的场效应晶体管
  - JFET（结型场效应管）：N沟道和P沟道
  - MOSFET（金属-氧化物半导体场效应管）：
    - 增强型：N沟道和P沟道
    - 耗尽型：N沟道和P沟道
- 支持不同的工作模式
  - 基本使用模式
  - 直流自给偏置
  - 直流分压偏置
- 支持不同的放大电路结构
  - 共漏极放大电路
  - 共栅极放大电路
  - 共源极放大电路
- 可视化功能
  - 显示特性曲线
  - 显示图解法分析结果
- 参数统一标准
  - 电压：V（伏特）
  - 电流：mA（毫安）
  - 电阻：kΩ（千欧）
  - 跨导gm：mA/V（毫西门子）
  - 跨导参数Kn：mA/(V^2)

## 安装和使用

### 安装依赖
```bash
pip install -r requirements.txt
```

### 运行程序
```bash
python fet_calc_main.py
```

### 使用方法
1. 选择FET类型（N沟道JFET、P沟道JFET、增强型N沟道MOSFET等）
2. 选择直流工作模式（基本使用、直流自给偏置、直流分压偏置）
3. 选择放大电路结构（共漏极、共栅极、共源极）
4. 输入必要的参数（如I_DSS、U_GSoff、U_GSth等）
5. 点击相应的计算按钮获取结果
6. 使用特性曲线和图解法按钮可视化分析结果

## 项目结构
```
analog_calculator/
├── __init__.py
├── auto_init.py          # 自动为缺少__init__.py的文件夹创建空文件
├── diode_calc/           # 二极管计算模块（待实现）
├── fet_calc/             # FET计算器主要功能模块
│   ├── __init__.py
│   ├── fet_models/       # FET模型定义
│   │   ├── jfet/         # JFET模型
│   │   └── mosfet/       # MOSFET模型（包括增强型和耗尽型）
│   ├── gui/              # 图形用户界面
│   │   ├── component/    # GUI组件
│   │   └── gui_methord/  # GUI方法
│   └── utils/            # 工具函数
│       ├── data_process/ # 数据处理相关
│       ├── fet_using_situations/ # FET使用场景计算
│       └── tkinter_utils/ # Tkinter工具函数
├── fet_calc_main.py      # 主程序入口
          
```

## 参数说明
程序中所有计算都基于一个名为`params`的字典，包含以下主要参数：

### 输入参数
- `I_DSS`: 饱和漏极电流（mA）
- `fet_type`: FET类型（如'N_channel_jfet'）
- `ϕ_G`: 栅极电位（V）
- `ϕ_D`: 漏极电位（V）
- `ϕ_S`: 源极电位（V）
- `U_GSoff`: 截止栅源电压（V）
- `U_GSth`: 开启电压（V，用于增强型MOSFET）
- `λ`: 沟道调制参数
- `Kn`: 跨导参数（mA/(V^2)，用于MOSFET）
- `RS`: 源极电阻（kΩ）
- `RD`: 漏极电阻（kΩ）
- `RG`: 栅极电阻（kΩ）
- `RL`: 负载电阻（kΩ）
- `DC_use_situation`: 直流使用场景
- `amplifier_situation`: 放大电路类型

### 输出参数（计算结果）
- `U_GS`: 栅源电压（V）
- `U_DS`: 漏源电压（V）
- `U_GD`: 栅漏电压（V）
- `workspace`: 器件工作区域
- `ID`: 漏极电流（mA）
- `gm`: 跨导（mA/V）
- `An`: 放大倍数
- `I_D_basic_use`: 基本使用下的漏极电流（mA）
- `I_D_DC_self_bia`: 直流自给偏置下的漏极电流（mA）
- `I_D_DC_div_voltage_bia`: 直流分压偏置下的漏极电流（mA）

## 开发说明
如需扩展或修改此项目，请遵循以下原则：
1. 所有计算都应基于`params`字典进行
2. 新增的FET类型应放在`fet_models`目录下相应的子目录中
3. 新增的计算功能应放在`utils/fet_using_situations`目录下
4. GUI相关的修改应在`gui`目录下进行

## 注意事项
1. 请确保输入的参数符合实际物理器件的参数范围
2. 程序会根据输入的FET类型自动选择合适的计算模型
3. 如遇到缺少参数的提示，请检查是否已填写所有必要的参数
4. 电阻单位默认为kΩ，可根据需要切换为MΩ