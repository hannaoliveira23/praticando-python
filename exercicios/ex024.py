nomeCidade = input('Digite o nome da cidade: ').strip()

primeiroNome = nomeCidade.split()[0]
result = 'SANTO' in primeiroNome.upper()

print('O nome da cidade começa com "Santo"?', result) # nomeCidade[:5] == 'SANTO'