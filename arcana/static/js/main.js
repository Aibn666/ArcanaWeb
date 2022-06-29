let boton = document.querySelector('.exp-boton')

let btn_menu = document.querySelector('.btn_menu')
let arcana = document.querySelector('.img-arcana')
let portales = document.querySelectorAll('.portal')
let logo = document.querySelector('.logo')


if (boton) {
    boton.addEventListener('click', e=>{
        let codigo = document.querySelector('.codigo')
        const cod = '1234'
        if(codigo.value == cod) {
            location.href = 'http://localhost:8000/experiencia/experiencia'
        }
        else {
            alert('El Codigo ingresado es incorrecto.')
        }
    
    })
}
if(logo){
    logo.addEventListener('click', e => {
        location.href = 'https://arcanaweb.herokuapp.com/'
    })
}
if(btn_menu) {
    btn_menu.addEventListener('click', e => {
        let menu_items = document.querySelector('.menu_items')
        let contenedor = document.querySelector('.contenedor')
        let container = document.querySelector('.container')
        let contenido = document.querySelector('.contenido')
        let cont = document.querySelector('.cont')
        let title = document.querySelector('.title')
        menu_items.classList.toggle('show')
        if (contenedor) {
            contenedor.classList.toggle('down')
        }
        if (container) {
            container.classList.toggle('down')
        }
        if(cont) {
            cont.classList.toggle('down')
            title.classList.toggle('down')
        }
        if(contenido)
        contenido.classList.toggle('down')
        
    
    })
}


portales.forEach(portal => portal.addEventListener('click', e=>{
    const gate = portal.id
    if (gate == 'agua') {
        location.href = 'https://arcanaweb.herokuapp.com/experiencia/'
    }
    if (gate == 'fuego') {
        location.href = 'https://arcanaweb.herokuapp.com/comentarios/'
    }
    if (gate == 'tierra') {
        location.href = 'https://arcanaweb.herokuapp.com/rituales/'
    }
    if (gate == 'aire') {
        location.href = 'https://arcanaweb.herokuapp.com/astrologia/'
    }
}))

