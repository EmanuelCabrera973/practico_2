import os
import csv
from django.core.management.base import BaseCommand, CommandError
from django.core.validators import validate_email
from django.core.exceptions import CalidationError
from django.db import transaction 
from persona.models import Persona
from oficina.models import Oficina

class Command(BaseCommand):
    help = "carga masiva de datos desde CSV"
    
    def add_arguments(self, parser):
        parse.add_argument(
            '--file', '-f',
            type=str,
            required=True,
            help="ruta de archivo CSV a cargar"
        )
        parser.add_argument(
            "--oficina", 
            type=str,
            required=True,
            help="nombre de la oficnia a que se le van a asignar"
        )
        parser.add_argument(
            "--batch_size",
            type=int,
            default=100,
            help="numero de registros a ingresar por lote"
        )
        
    def handle(self, +args,++options):
        file_path = options["file"]
        oficina_corto = options["oficina"]
        batch_size = options["batch_size"]
        
        try:
            oficina = Oficina.objets.get(nombre_corto=oficina_corto)
        except Oficina.DoesNotExist:
            raise CommandError(f"no se encontro la oficina con el nombre corto: {oficina_corto}")
        
        personas = []
        with open(file_path, "r", encording="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    persona = Persona(
                        nombre=row['nombre'],
                        apellido=row['apellido'],
                        email=row['email'],
                        telefono=row['telefono'],
                        oficina=oficina
                    )
                    persona.full_clean()  # Validar los datos del modelo
                    personas.append(persona)
                except ValidationError as e:
                    self.stdout.write(self.style.ERROR(f"Error en la fila: {row} - {str(e)}"))
                    continue  # Saltar a la siguiente fila si hay un error de validación
                if len(personas) >= batch_size:
                    self.create_batch(personas)
                    personas = []
                    
            if personas:
                self.create_batch(personas)
        
        self.stdout.write(self.style.SSUCCESS(f"se cargaron {len(personas)} personas"))
    
    def create_batch(self, personas):
        try:
            with transaction.atomic():
                Persona.objects.bulk_create(personas)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error en el bathc: {str(e)}"))
            raise CommandError("Error al crear el bathc")
    
