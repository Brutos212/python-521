import paramiko

NOME_DA_CHAVE = './python-521.pem'
key = paramiko.RSAKey.from_private_key_file(NOME_DA_CHAVE)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(

    hostname='18.222.150.179',
    username='ubuntu',
    pkey=key
)