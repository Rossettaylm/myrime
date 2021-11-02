import os
import shutil

currentDir = os.getcwd()
fcitx5Outdir = shutil.copytree(
    "fcitx5_in_.config", "home/rossetta/.config/fcitx5")
print("将fcitx5的配置文件复制到", fcitx5Outdir)

rimepath = "/home/rossetta/.local/share/fcitx5/rime"
rimeOutdir = shutil.copytree(currentDir, rimepath)
print("将rime的配置文件复制到", rimeOutdir)

os.rmdir(currentDir)
print("配置完成!")
