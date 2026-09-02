Caso de Uso: Transferencia Bancaria

ID: CU-03

Nombre: Realizar transferencia bancaria

Actor primario: Cliente autenticado

Actores secundarios: Sistema de notificaciones, Core bancario

Precondiciones:

- El cliente está autenticado en el sistema
- La cuenta origen tiene saldo disponible
- La cuenta origen se encuentra activa (no bloqueada)

Postcondiciones (éxito):

- El saldo de la cuenta origen disminuye en el monto
- El saldo de la cuenta destino aumenta en el monto
- Se registra la operación en el historial de ambas cuentas
- Se envía notificación al cliente

Flujo principal:

1. El cliente selecciona "Nueva transferencia"
2. El cliente ingresa el número de cuenta destino y el monto
3. El sistema valida los datos ingresados
4. El sistema muestra un resumen para confirmación
5. El cliente confirma la operación
6. El sistema procesa la transferencia
7. El sistema muestra el comprobante

Flujos alternativos:

2a. Monto ingresado no válido (cero, negativo o excede límite diario):

- 2a.1 El sistema muestra "Monto inválido, ingrese un valor correcto"
- 2a.2 El sistema permite al cliente reingresar el monto (vuelve al paso 2)

3a. Número de cuenta destino inexistente:

- 3a.1 El sistema informa "Cuenta destino no encontrada"
- 3a.2 El cliente puede corregir el dato (vuelve al paso 2) o cancelar

5a. El cliente cancela la confirmación:

- 5a.1 El sistema descarta la operación
- 5a.2 El caso de uso termina sin cambios

Excepciones:

3b. Saldo insuficiente:

- 3b.1 El sistema informa "Saldo insuficiente para realizar la operación"
- 3b.2 El caso de uso termina

6a. Fallo en el servicio de transferencia:

- 6a.1 El sistema revierte cualquier cambio parcial (rollback)
- 6a.2 El sistema informa "No fue posible completar la transferencia. Intente más tarde"
- 6a.3 El sistema registra el error internamente

6b. Fallo en el envío de notificación:

- 6b.1 La transferencia se completa y se registra correctamente
- 6b.2 El sistema informa "Transferencia exitosa, pero no se pudo enviar la notificación"
- 6b.3 El sistema reintenta el envío de notificación en segundo plano
