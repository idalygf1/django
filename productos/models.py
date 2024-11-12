from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre=models.CharField(max_length=30) #CharField es igual a Varchar en BD
    descripcion=models.CharField(max_length=200)
    stock=models.IntegerField() #IntegerField es igual a tipo entero en BD
    precio=models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)


    def __str__(self): #para que retorne los valores 
        return self.nombre
    

class Pedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_cliente = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido de {self.nombre_cliente} - {self.producto.nombre}"