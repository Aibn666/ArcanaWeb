const grande = document.querySelector('.grande')
const carta = document.querySelectorAll('.carta')
const punto = document.querySelectorAll('.punto')
const muestra = document.querySelector('.vista-previa')
const cerrar = document.querySelector('.cerrar')
let estado = 0;
punto.forEach((cadaPunto, i) =>{
    punto[i].addEventListener('click',()=>{
        let posicion = i
        let operacion = posicion * (-14)

        grande.style.transform = `translateX(${ operacion }%)`

        punto.forEach((cadaPunto, i)=>{
            punto[i].classList.remove('activate')
        })
        punto[i].classList.add('activate')
        console.log(punto[i])

    })
})
muestra.addEventListener('click', () =>{
    if (muestra.classList == 'vista-previa') {
        muestra.classList.add('activate')
    } else muestra.classList.remove('activate')
})
