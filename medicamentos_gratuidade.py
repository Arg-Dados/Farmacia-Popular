import paramiko
import pandas as pd

ssh_host = '15.235.110.107'
ssh_port = 2205
ssh_user = ''
ssh_password = ''

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh_client.connect(ssh_host, port=ssh_port, username=ssh_user, password=ssh_password)
    sftp_client = ssh_client.open_sftp()
    print('conectado')
except:
    print('Falha na conexão, credenciais possivelmente incorretas')
    exit()
    
remote_path = "/opt/dados/Lista de Medicamentos Gratuidade - EAN Novembro 2023.xlsx"

with sftp_client.open(remote_path) as file:
    df = pd.read_excel(file)
    print('DataFrame pronto')
    