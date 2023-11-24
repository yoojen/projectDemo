/**grabing html elements */
form = document.querySelector('#addtransform')
table = document.querySelector('#columntitles')
tableData = document.querySelector('#column-data')
filterOptions = document.querySelector('#filter-option')
type = null

/**handling change on input box */
filterOptions.addEventListener("change", () => {
    if (filterOptions.value === "incomes") {
        type = "incomes"
    } else {
        type = "expenses"
    }
    url = `http://localhost:5000/api/bm/${type}`
    fetchApi(url)
})

const fetchApi = async (url) => {
    // if (e.target.value == "") {
    //     less.innerHTML += "can't not work"
    //     return
    // } else {
    if (filterOptions.value === "Incomes") {
        type = "incomes"
    } else {
        type = "expenses"
    }
    tableData.innerHTML = ''
    await fetch(url)
        .then((res) => res.json())
        .then((data) => {
            fetchedData = Object.values(data)
            fetchedData.forEach(element => {
                tableData.innerHTML += `
                <tr>
                <td>${element.name}</td>
                <td>${element.amount}</td>
                
                </tr>
                `
            });
        })
    // }
}

form.addEventListener("submit", (e) => {
    e.preventDefault()

    const name = document.querySelector("#name").value
    const amount = document.querySelector("#amount").value
    const type = document.querySelector("#typeselect").value
    const category = document.querySelector("#category").value
    const desc = document.querySelector("#desc").value

    const formData = new FormData()
    formData.append("name", name)
    formData.append("amount", amount)
    formData.append("type", type)
    formData.append("category", parseInt(category))
    formData.append("desc", desc)
    console.log(formData)
    url = `http://localhost:5000/api/bm/${type}/`
    console.log(url);
    fetch(url, {
        method: "POST",
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
})