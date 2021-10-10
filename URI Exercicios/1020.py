idade = int(input()) 

ano = idade // 365
mes = (idade % 365) // 30
dias = (idade % 365) % 30

print(ano,"ano(s)")
print(mes,"mes(es)")
print(dias,"dia(s)")
