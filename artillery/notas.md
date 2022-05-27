Escenario de calentamiento:
usuarios: 5
duracion: 30

NOTA: 5 usuarios por segundo se conectaran durante 30 segundos
latencia: tiempo de demora del serivicio a responder

valores_de_velocidad: {min, max, medina} deben de estar sobre los 100

p95 de percentil: se conectaron a la velocidad de 73
p99 de percentil: se conectaron a la velocidad de 76 

config:
  target: "http://127.0.0.1:5000"
  phases:
    - duration: 30
      arrivalRate: 5
      name: Warm up

scenarios:
  - flow:
    - get:
        url: "/api/v1/get"

    - think: 2
    - get:
        url: "/api/v1/get?id={{ userId }}"


artillery run -e develop test.yaml --output result.json
artillery report --output result.html result.json