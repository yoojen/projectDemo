form_addbyone = document.querySelector('#onebyone')
// form_addmany = document.querySelector("#addmany")

expenseName = document.querySelector("#expense_name")
expenseAmount = document.querySelector("#expense_amount")
expenseCategory = document.querySelector("#expense_category_type")
expenseDescription = document.querySelector("#description")

// expenseNameMany = document.getElementsByName("expenseNameMany")
// expenseAmountMany = document.getElementsByName("expenseAmountMany")
// expenseCategoryMany = document.getElementsByName("expenseCategoryMany")
// expenseDescriptionMany = document.getElementsByName("expenseDescriptionMany")


form_addbyone.addEventListener("submit", function (e) {
    e.preventDefault()
    const formData = new FormData()
    formData.append("name", expenseName.value)
    formData.append("amount", expenseAmount.value)
    formData.append("category", parseInt(expenseCategory.value))
    formData.append("desc", expenseDescription.value)

    // insert data into planings table
    // fetch("")
    url = "http://localhost:5000/api/bm/plans/"
    data = {
        "name": expenseName.value,
        "amount": expenseAmount.value,
        "category": expenseCategory.value,
        "description": expenseDescription.value
    }
    fetch(url, {
        method: "POST",
        body: formData
    })

})

window.addEventListener("load", () => {
    url = "http://localhost:5000/api/bm/plans/"

    fetch(url)
        .then(response => response.json())
        .then(data => {
            data.map((item) => {
                document.querySelector("#planned-list").innerHTML += `
                <tr>
                    <td>
                        <p>${item.name}</p>
                    </td>
                    <td>$${item.amount}</td>
                    <td>
                        <p>${item.description}</p>
                    </td>
                    <td>
                        <button class="edit-btn">Edit</button>
                        <button class="delete-btn">Delete</button>
                    </td>
                </tr>
                `
            })
        })

})
/*
form_addmany.addEventListener("submit", function (e) {
    e.preventDefault()
    const formData = new FormData()
    if (expenseNameMany.length > 1) {
        for (let i = 0; i < expenseNameMany.length; i++) {
            console.log(expenseNameMany[i].value);

            let formInput = [
                { "name": expenseNameMany[i].value },
                { "amount": expenseAmountMany[i].value },
                { "category": expenseCategoryMany[i].value },
                { "description": expenseDescriptionMany[i].value }
            ]
            formInput.map((item) => {
                keys = Object.keys(item)
                values = Object.values(item)
                formData.append(keys, values)
            })
        }
    }

    // insert data into planings table
    // fetch("")
})
*/