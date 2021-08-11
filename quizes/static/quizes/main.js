const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtn=>modalBtn.addEventListener('click',()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz') 
    const num = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const score_to_pass = modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')


    modalBody.innerHTML = `
        <div class="h5 mb-3">Are you sure you want to start "${name}"?</div>
        <div class="text-muted">
            <ul>
                <li>Number of questions: <b>${num}</b></li>
                <li>Score to Pass: <b>${score_to_pass}%</b></li>
                <li>Difficulty: <b>${difficulty}</b></li>
                <li>Time: <b>${time}</b> minute</li>
            </ul>
        </div>
    `

    startBtn.addEventListener('click',()=>{
        window.location.href = url +pk
    })
}))