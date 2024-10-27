import pywhatkit

phone_number = 'Escrever o número de celular'
message = 'Opa, mandando mensagem pelo python'
hours = 20
minutes = 10

# Aqui, aumentamos o tempo de espera para 20 segundos
pywhatkit.sendwhatmsg_instantly(phone_number, message, hours, minutes)
print('Mensagem enviada')