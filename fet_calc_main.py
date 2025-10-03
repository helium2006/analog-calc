#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
模拟计算器主程序入口
此文件是模拟计算器项目的主入口点，负责启动FET计算器的GUI界面。
"""

import sys
import os

# 添加项目根目录到Python路径，确保可以正确导入fet_calc模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    """主函数，负责启动FET计算器的GUI界面"""
    try:
        # 导入GUI主窗口模块
        from fet_calc.gui.fet_calc_main_window import Win
        
        # 创建计算器主窗口实例
        # 使用Win类（继承自WinGUI）来获取完整功能
        app = Win()
        
        # 启动主事件循环
        app.mainloop()
        
    except ImportError as e:
        print(f"导入模块时出错: {e}")
        print("请确保所有依赖模块已正确安装。")
        sys.exit(1)
    except Exception as e:
        print(f"程序运行时出错: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # 当脚本被直接执行时，调用主函数
    main()
    