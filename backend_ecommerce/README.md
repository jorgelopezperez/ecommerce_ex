# Diseño y implementación del back-end de un e-commerce

## Primera parte

Formas parte de nuestro súper equipo de desarollo y en el sprint actual te has asignado las siguientes Stories (tareas):

**Back-end: Añadir productos con dto. en cesta y poder aplicar códigos promocionales**

Como *propietario de una cadena de tiendas a nivel internacional* quiero poder introducir mis productos en la tienda y que los clientes puedan comprarlos con ciertos descuentos en función del país. También quiero poder crear códigos promocionales para poder hacer campañas de marketing aplicando un descuento de cierta cantidad de dinero si la compra supera un mínimo.

*Criterio de aceptación:*
* Se guardan los productos. Estos pueden:
    * Tener precios distintos según el país
    * Tener un porcentaje de descuento sobre el precio.
* Se pueden aplicar códigos promocionales.
    * Consisten en un descuento de una cantidad fija sobre el total de la cesta siempre que este total supere un mínimo.

- - -

## Segunda parte

Después de un tiempo con la tienda en marcha, como empresa hemos fijado el objetivo de aumentar el precio medio de las cestas. Es decir, que los clientes gasten más en cada compra.

Hemos analizado las cestas y hemos visto que la mayoría de compras incluyen solo una unidad de cada producto. Desde el departamento de marketing nos han recomendado implementar descuentos por cantidad para incentivar a los clientes a comprar más.

Nos han explicado que la mejor forma de aplicar los descuentos por cantidad es hacerlo por tramos. Por ejemplo, de 1 a 10 unidades no aplicamos descuento, de 11 a 20 unidades aplicamos un descuento, de 21 a 30 unidades aplicamos un descuento mayor, etc. También han comentado que como no todos los casos son iguales, nos interesará que unas veces el descuento sea de una cantidad fija, y otras veces que sea de un porcentaje sobre el precio del producto.

Los descuentos por cantidad son descuentos adicionales sobre el precio final del producto (es decir, el precio del producto con descuento si lo tiene). También hay que tener en cuenta que los descuentos de cada tramo no se acumulan y se aplican una sola vez.

Ejemplo: producto con precio 10€ con descuento de 2€ que nos da un precio de venta 8€. Descuentos por cantidad: más de 10 unidades aplicamos un 10% de descuento, significa que el precio de venta final si compramos más de 10 unidades será de 7,20€. Si compramos 20 o más unidades, el precio de venta final seguirá siendo de 7,20€ porque no hay ningún descuento definido para 20 o más unidades.

Desde el departamento técnico hemos dedicido que implementaremos esta nueva funcionalidad en este sprint. 

- - -

### *Aclaraciones*

* Por simplicidad, no se considerarán las divisas en las cantidades monetarias. Es decir, trabajaremos sin unidad guardando solo el número. 15€ son 15; 17$ será 17.
* El lenguaje a usar es Python 3.x. El estilo, las buenas prácticas, la organización del diseño y la pulcritud del código no dependen del lenguaje de programación que se use ;)

### *¿Qué se evaluará?*

Tus conocimientos y habilidades de diseño y programación.

### *¿Qué debes hacer?*

Diseñar e implementar una solución para representar el back-end de este e-commerce simplificado. Junto a este enunciado se proporcionan los ficheros de tests de la funcionalidad, uno para cada parte. Para probarlos ejecuta:

```python3 -m unittest tests_part_1```

```python3 -m unittest tests_part_2```

El objetivo es conseguir estos incrementos de funcionalidad, además de obviamente pasar los tests. Para ello no puedes modificar los ficheros de los tests, usar persistencia (ej. base de datos, etc.) ni ningún framework (ej. Django, etc.). Aparte de estas restricciones, el diseño y la implementación del código es totalmente libre.

Hazlo lo mejor que sepas y ¡lúcete!