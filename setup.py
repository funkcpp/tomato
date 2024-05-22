from cx_Freeze import setup, Executable

# 生成可执行文件的名称
exe_name = "your_executable_name.exe"

# 配置选项
options = {
    "build_exe": {
        "includes": ["PyQt5","sys","datetime","time"],  # 包含的第三方库
        "packages": [ "Ui_windows_list",
                     "Ui_add_text",
                    "frame_title",
                    "small_button",
                    "text_button"],  # 包含的本地模块
    }
}

# 设置
setup(
    name="Your Application Name",
    version="1.0",
    description="Description of your application",
    options=options,
    executables=[Executable("main_list.py")]  # 你的脚本文件
)



