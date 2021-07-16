import platform, time
import md5

def save_current_machine_md5():
    info = platform.uname()
    info = info.processor + info.node + info.system
    hash_md5 = md5.create_md5(info)
    return hash_md5

def save_imitate_dif_machine_md5():
    info_d = time.time()
    hash_md5 = md5.create_md5(info_d)
    return hash_md5

def work():
    global tmp_md5
    info = platform.uname()
    info = info.processor + info.node + info.system
    hash_md5 = md5.create_md5(info)





