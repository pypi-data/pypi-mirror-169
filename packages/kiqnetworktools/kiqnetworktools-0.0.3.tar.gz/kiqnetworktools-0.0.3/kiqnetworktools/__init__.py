import subprocess
import re
import textfsm
from netmiko import ConnectHandler
import telnetlib
import os
import nmap

def get_lines(strs,patt):
        fi = re.split(r'\s+',strs)
        fil = list(filter(lambda x: patt in x, fi))
        if len(fil) > 0: return fil[0]

def comando_ps(cmd,pat):
    ps = subprocess.run(['powershell',"-Command",cmd], capture_output=True)
    str_ps = ps.stdout.decode("utf-8")
    f = list(filter(lambda x: pat in x, str_ps.splitlines()))
    files = list(map(lambda x: get_lines(x,pat), f))
    return files
    
def elimina_bd(fold):   
    cmd = 'rm .\\'+fold+'\\ -r -force'
    try:
        ps = subprocess.run(['powershell',"-Command",cmd])
    except BaseException as e:
        print(e)

def datos_desde_output(file,tmpl):
    result = []
    try:
        with open(tmpl) as tmpl, open(file) as data:
            re_table = textfsm.TextFSM(tmpl)
            raw_text_data = data.read()
            result = re_table.ParseText(raw_text_data)
        tmpl.close(), data.close()
    except BaseException as e:
        print(e)
    
    return result

def db_host(host,user,pwd,comandos=[]):
    device = {
        'device_type': 'huawei',
        'host': '',
        'username': '',
        'password': ''
        #'session_log': 'netmiko_session.log'
    }
    protocol = ''
    device['host'] = host
    device['username'] = user
    device['password'] = pwd
    print('Obteniendo servicios de',host)
    print('*'*50)
    
    try: os.mkdir('info/')
    except: pass
    try:
        net_connect = ConnectHandler(**device)
        protocol = 'ssh'
        for comando in comandos:
            info = net_connect.send_command_timing(comando,strip_command=False,strip_prompt=False)
            #print(comando[-7:])
            st = open('info/'+host+'_'+comando[-7:]+'.txt','w')
            st.write(info)
            st.close()
        net_connect.disconnect()
    except BaseException as e:
        print(e)
        print("SSH FALLÓ, toca Telnet a",host)
    if protocol == 'ssh': pass
    else:
        try:
            with telnetlib.Telnet(host) as tn:
                tn.read_until(b"Username:")
                tn.write(device['username'].encode('ascii') + b"\n")
                if device['password']:
                    tn.read_until(b"assword: ",5)
                    tn.write(device['password'].encode('ascii') + b"\n")
                    n, match, previous_text = tn.expect([br'>',br'fail'],5)
                    if n in range(1,2): raise Exception('Equipo no sincronizado con Tacacs')
                readoutput = ''
                tn.write('screen-length 0 temporary'.encode('ascii')+ b"\n")
                n, match, previous_text = tn.expect([br'>',br'ontinue',br"More ----"],10)
                readoutput += previous_text.decode("utf-8")
                for comando in comandos:
                        tn.write(comando.encode('ascii')+ b"\n")
                        n, match, previous_text = tn.expect([br'>',br'ontinue',br"More ----"],10)
                        if n == 2: 
                            tn.write(b"q")
                            n, match, _ = tn.expect([br">"],10)
                        if n == 1:
                            tn.write("y".encode('ascii') + b"\n")
                            n, match, previous_text = tn.expect([br"More ----"],10)
                            tn.write(b"q\n")
                        readoutput += previous_text.decode('unicode_escape')
                        #print(comando[-7:])
                        st = open(f'info/'+host+'_'+comando[-7:]+'.txt','w')
                        st.write(readoutput)
                        st.close()
                        readoutput = ''
                tn.write(b"quit\n")
                protocol = 'telnet'
        except BaseException as e:
            print(e)
    print(f"terminado",host)

def obten_lista_ips(str_redes):
    print('Obteniendo ips de red',str_redes) 
    nm = nmap.PortScanner()
    try: 
        nm.scan(hosts=str_redes,arguments='-sn')
        return [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    except BaseException as e: print(e)