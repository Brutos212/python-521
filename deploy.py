import paramiko
NOME_DA_CHAVE = './brutos.pem'
key = paramiko.RSAKey.from_private_key_file(NOME_DA_CHAVE)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    
    hostname='18.222.150.179',
    username='ubuntu',
    pkey=key
)

commands = [

    'sudo apt-get update -y',
    'sudo apt-get install -y python3-pip',

    'git clone https://github.com/Brutos212/python-521.git',

    'pip3 install -r python-521/requirements.txt',
    'sudo python3 python-521/app.py &',

]

for command in commands:
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode(), stderr.read().decode())
