window.addEventListener("scroll", function(){
    let header = document.querySelector('#nav')
    header.classList.toggle('scrolling',window.scrollY > 0)
})