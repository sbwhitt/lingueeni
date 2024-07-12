def get_ip() -> str:
    import json
    import subprocess

    cmd = ["ip", "-json", "route"]

    res = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout.read()
    output = json.loads(res)

    ip = [o["gateway"] for o in output if o["dst"] == "default"][0]
    return ip

print(get_ip())
