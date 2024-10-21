import flet as ft

def main(page):
    tasks = []
    modify_rows = {}  # Diccionario para almacenar las filas de modificación asociadas a cada tarea

    def add_clicked(e):
        task = ft.Checkbox(label=new_task.value, on_change=update_task)
        delete_button = ft.IconButton(icon=ft.icons.DELETE, on_click=lambda _: delete_task(task_row))
        modify_button = ft.IconButton(icon=ft.icons.EDIT, on_click=lambda _: modify_task(task))
        
        task_row = ft.Row([task, delete_button, modify_button])
        tasks.append(task_row)  # Ahora agregamos toda la fila a la lista de tasks
        page.add(task_row)

        new_task.value = ""
        new_task.focus()
        new_task.update()

    def update_task(e):
        task = e.control
        if task.value:
            task.label = f"{task.label} (completado)"
        else:
            task.label = task.label.replace(" (completado)", "")
        task.update()

    def delete_task(task_row):
        tasks.remove(task_row)  # Eliminamos la fila completa
        page.remove(task_row)
        page.update()

    def modify_task(task):
        new_label = ft.TextField(value=task.label, width=300)
        save_button = ft.ElevatedButton("Guardar", on_click=lambda _: save_task(task, new_label))
        
        modify_row = ft.Row([new_label, save_button])
        modify_rows[task] = modify_row  # Guardamos la fila de modificación para eliminarla más tarde

        page.add(modify_row)
        page.update()

    def save_task(task, new_label):
        task.label = new_label.value
        task.update()
        
        # Eliminamos la fila de modificación
        page.remove(modify_rows[task])
        del modify_rows[task]  # Eliminamos el registro del diccionario
        page.update()

    # Creación del logo
    logo = ft.Image(src="logo.png", width=400, height=200)
    
    # Mensaje de bienvenida
    welcome_message = ft.Text(
        value="¡Bienvenido a tu lista de tareas!", 
        size=20,
        weight=ft.FontWeight.BOLD
    )
    
    # Contenedor para el logo y el mensaje, con un ancho de 600px y alto de 400px
    welcome_container = ft.Container(
        content=ft.Column(
            [
                ft.Container(content=logo, alignment=ft.alignment.center),
                ft.Container(content=welcome_message, alignment=ft.alignment.center),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        ),
        width=600,
        height=400,
        alignment=ft.alignment.center,
    )

    new_task = ft.TextField(hint_text="Lista de compras", width=300)
    add_button = ft.ElevatedButton("Agregar", on_click=add_clicked)

    # Agregar el contenedor de bienvenida antes del formulario
    page.add(welcome_container)
    page.add(ft.Row([new_task, add_button]))

ft.app(main)
