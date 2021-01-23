import shlex
import socket
import subprocess
import time

app = Flask(__name__, static_folder='static')

def getinfo():
    if 'icanhazptr' in request.host:
        try:
            output = socket.gethostbyaddr(request.remote_addr)
            result = output[0]
        except:
            result = request.remote_addr
    
    elif 'icanhazepoch' in request.host:
        epoch_time = int(time.time())
        result = epoch_time

    else:
        result = request.remote_addr
    return Response("%s\n" % result, request.remote_addr)


if __name__ == "__main__":
    app.run()
