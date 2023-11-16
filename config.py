# save as ~/.config/mpremote/config.py
commands = {
    "A": "connect id:e6614864d3323634",
    "fl": "fs ls",
    "littlefs_rp2": [
        "exec",
        "--no-follow",
        "import os, machine, rp2; os.umount('/'); bdev = rp2.Flash();\
                os.VfsLfs2.mkfs(bdev, progsize=256); \
                vfs = os.VfsLfs2(bdev, progsize=256); \
                os.mount(vfs, '/'); machine.reset()",
    ],
    "test": ["mount", ".", "exec", "import test"],
    "info": ["mount", ".", "run", "fs_info.py"],
    "blink": ["mount", ".", "exec",
              "from blink import Blink; Blink()"]
}
