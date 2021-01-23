import json
import shlex
import socket
import subprocess
import time

from flask import Flask, Response, request, send_from_directory

app = Flask(__name__, static_folder='static')
traceroute_bin = "/bin/tracerout-suid"

@app.route("/")
def icanhazafunction():
    mimetype = "text/plain"
    if 'icanhazptr' in request.host:
        try:
            output = socket.gethostbyaddr(request.remote_addr)
            result = output[0]
        except:
            result = request.remote_addr
    elif 'icanhazepoch' in request.host:
        epoch_time = int(time.time())
        result = epoch_time
    elif 'icanhaztrace' in request.host:
        valid_ip = False
        try:
            socket.inet_pton(socket.AF_INET, request.remote_addr)
            valid_ip = True
        except socket.error:
            pass
        if valid_ip:
            if 'icanhaztraceroute' in request.host:
                tracecmd = shlex.split("%s -q 1 -f 2 -w 1 %s" % (traceroute_bin, request.remote_addr))
            else:
                tracecmd = shlex.split("%s -q 1 -f 2 -w 1 -n %s" % (traceroute_bin, request.remote_addr))
            
            result = subprocess.Popen(
                    tracecmd,
                    stdout=subprocess.PIPE
                    ).communicate()[0].strip()
            result = result.decode('utf-8')
        else:
            result = request.remote_addr

    elif 'icanhazproxy' in request.host:
        proxy_headers = [
                'via',
                'forwarded',
                'client-ip',
                'useragent_via',
                'proxy_connection',
                'xproxy_connection',
                'http_pc_remote_addr',
                'http_client_ip',
                'http_x_appengine_country'
                ]
        found_headers = {}
        for header in proxy_headers:
            value = request.headers.get(header, None)
            if value:
                found_headers[header] = value.strip()

        if len(found_headers) > 0:
            mimetype = "application/json"
            result = json.dumps(found_headers)
        else:
            return Response(""), 204
    
    elif: 'icanhazheaders' in request.host:
        mimetype = "application/json"
        result = json.dumps(dict(request.headers))
    else:
        result = request.remote_addr
    return Response("%s\n" % result, mimetype=mimetype, headers={"X-Your-Ip": request.remote_addr})


@app.route('/crossdomain.xml')
@app.route('/humans.txt')
@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

if __name__ == "__main__":
    app.run()
