# Practica EIEC - DevOps - UNIR
## Jhimi Rosales

Este repositorio nos servirá para demostrar el uso de Git en la asignatura de EIEC y muchas cosas mas.

---

Los comandos del Makefile funcionarán en Linux y MacOS. En caso de usar Windows, necesitarás adaptarlos o ejecutarlos en una máquina virtual Linux.

## Ejecución

```sh
python3 main.py <filename> <dup> <order>
```

  filename: **ruta** al fichero que contiene la lista de palabras, una por línea

  dup: **yes|no**, yes para eliminar palabras duplicadas, no para mantener la lista

  order: **asc|desc**, opcional, asc para ordenar ascendentemente, desc para ordenar descendentemente (por defecto es asc)


---
Usando el fichero creado palabras.txt

Ejm:
```sh
python3 main.py palabras.txt no asc
python3 main.py palabras.txt yes asc
```

Cuando se pone un fichero que no existe por defecto mostrara una lista.

Ejm:
```sh
python3 main.py filex.txt no desc
```
