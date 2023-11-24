btns = document.querySelectorAll('a')
len = btns.length - 1
currentlocation = location.href
for (let i = 0; i <= len; i++) {
    if (btns[i].href == currentlocation) {
        btns[i].className = 'active'
    }
}
$('.close-btn').on('click', function () {
    $('.navigation').css("display", "none")
    $(".close-btn").css("display", "none")
    $(".open-btn").css("display", "flex")
    $('.content').css("marginLeft , 0")
    $('.content').css("width , 100%")

})
$(".open-btn").on('click', function () {
    $('.navigation').css("display", "block")
    $(".close-btn").css("display", "flex")
    $(".open-btn").css("display", "none")
    $('.content').css("margin-left , 20%")
    $('.content').css("width , 75%")
})

window.addEventListener("load", () => {
    exp_url = "http://localhost:5000/api/bm/expenses/total"
    inc_url = "http://localhost:5000/api/bm/incomes/total"
    fetch(exp_url)
        .then((res) => res.json())
        .then((data) => {
            fetch(inc_url)
                .then((res) => res.json())
                .then((data_incomes) => {
                    income = Object.values(data_incomes[1])
                    expense = Object.values(data[1])
                    balance = income - expense
                    document.querySelector("#balance").innerHTML = `$${balance}`
                })
        })
})