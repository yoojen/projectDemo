form_addbyone = document.querySelector('#onebyone')

/*inputs */
expenseName = document.querySelector("#expense_name")
expenseAmount = document.querySelector("#expense_amount")
expenseCategory = document.querySelector("#expense_category_type")
expenseDescription = document.querySelector("#description")

/*Inserting data in the db */
form_addbyone.addEventListener("submit", function (e) {
    e.preventDefault()
    const formData = new FormData()
    formData.append("name", expenseName.value)
    formData.append("amount", expenseAmount.value)
    formData.append("category", parseInt(expenseCategory.value))
    formData.append("desc", expenseDescription.value)

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

/** Fetch data on the load of the page */

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
