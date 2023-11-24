filterOptions = document.querySelector('#filter-options')
filterParent = document.querySelector(".filter-parent")
filterType = document.querySelector("#filter-type")
table = document.querySelector('#columntitles')

// render divisions
tableDataName = document.querySelector('#column-data-name')
tableDataCategory = document.querySelector('#column-data-category')
tableDataAmount = document.querySelector('#column-data-amount')
tableDataDate = document.querySelector('#column-data-date')
let type = null

//forms
dateForm = document.querySelector("#filterByDate")
amountForm = document.querySelector("#lessGreater")
categoryForm = document.querySelector("#categoryForm")
nameForm = document.querySelector("#nameForm")
forms = [dateForm, amountForm, categoryForm, nameForm]

//inputs
nameInput = document.querySelector("#nameInput")
categoryInput = document.querySelector("#category-select")
amountInput = document.querySelector("#amount-select")

//check for type
function initializeType() {

    if (filterType.value == "incomes") {
        type = "incomes"
    } else if (filterType.value == "expenses") {
        type = "expenses"
    } else {
        return
    }
    return type
}

//render items
const fetchApi = async (url, renderDiv) => {
    type = initializeType()
    renderDiv.innerHTML = ''
    await fetch(url)
        .then((res) => res.json())
        .then((data) => {
            fetchedData = data
            console.log(fetchedData);
            data.forEach(element => {
                renderDiv.innerHTML += `
                <tr>
                <td>${element.name}</td>
                <td>${type}</td>
                <td>${element.amount}</td>
                <td>
                <button class="edit-btn">Edit</button>
                <button class="delete-btn">Delete</button>
                </td>
                </tr>
                `
            });
        })

}

const fetchApi_short = async (url, renderDiv) => {
    type = initializeType()
    renderDiv.innerHTML = ''
    await fetch(url)
        .then((res) => res.json())
        .then((data) => {
            fetchedData = data
            fetchedData.forEach(element => {
                console.log(element);
                renderDiv.innerHTML += `
                <tr>
                <td>${element.name}</td>
                <td>${type}</td>
                <td>${element.amount}</td>
                <td>
                <button class="edit-btn">Edit</button>
                <button class="delete-btn">Delete</button>
                </td>
                </tr>
                `
            });
        })

}
dateForm.addEventListener("submit", (e) => {
    e.preventDefault()

    type = initializeType()
    if (type) {
        startDate = document.querySelector("#start-date")
        endDate = document.querySelector("#end-date")
        if (startDate.value == "" && endDate.value == "") {
            return
        } url = `http://localhost:5000/api/bm/${type}/date/${startDate.value}/${endDate.value}`
        fetchApi(url, tableDataDate)
    }
})


nameForm.addEventListener("submit", (e) => {
    e.preventDefault()
    //if item occor more than one time it is not returing array of that item
    type = initializeType()
    if (type) {
        if (nameInput.value == "") {
            return
        }
        url = `http://localhost:5000/api/bm/${type}/${nameInput.value.toLowerCase()}`
        console.log(url);
        fetchApi(url, tableDataName)
    }
})

amountForm.addEventListener("submit", (e) => {
    e.preventDefault()

    type = initializeType()
    if (type) {
        if (nameInput == "") {
            return
        }
        if (amountInput.value == "less") {
            amount = document.querySelector("#amount")
            url = `http://localhost:5000/api/bm/${type}/amt_lt/${amount.value}`
        } else if (amountInput.value == "greater") {
            url = `http://localhost:5000/api/bm/${type}/amt_gt/${amount.value}`

        } else {
            return
        }
        console.log(url);
        fetchApi(url, tableDataAmount)
    }
})

filterType.addEventListener("change", () => {
    categoryInput.innerHTML = ""
    names = []
    previous = null
    type = initializeType()
    if (type) {
        url = `http://localhost:5000/api/bm/${type}/categories`
        fetch(url)
            .then((res) => res.json())
            .then((data) => {
                data.map((item) => {
                    itemName = Object.keys(item);
                    itemCategory = item[Object.keys(item)].category_id

                    itemName.map((name) => {
                        if (!names.includes(name)) {
                            names.push(name)
                            categoryInput.innerHTML += `
                                <option value="${itemCategory}">${name}</option>
                            `
                        }
                    })

                })
            })
    }
})

categoryForm.addEventListener("submit", (e) => {
    e.preventDefault()
    categoryToSearch = categoryInput.value

    type = initializeType()
    if (type) {
        if (categoryToSearch == "") {
            return
        }
        url = `http://localhost:5000/api/bm/${type}/category/${categoryToSearch}`

        console.log(url);
        fetchApi(url, tableDataCategory)
    }
})

