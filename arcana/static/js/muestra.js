const cartas = document.querySelectorAll('.carta-img')
const titulo = document.querySelector('.titulo')


const pantalla = document.querySelector('.pantalla')
const image = document.createElement('img')

cartas.forEach((element) => {
    element.addEventListener('click', ()=>{
        image.src  = element.src
        pantalla.src = image.src
    })
})