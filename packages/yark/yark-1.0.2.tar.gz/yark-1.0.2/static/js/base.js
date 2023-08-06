// Adds an error which will automatically be deleted 
function addError(msg) {
    let error = document.createElement("div")
    error.setAttribute("id", "error")
    error.innerText = msg
    document.body.appendChild(error)
    deleteError()
}

// Starts timer and then automatically deletes element
function deleteError() {
    let err = document.getElementById("error")
    if (err) {
        setTimeout(
            function () {
                err.remove()
            }, 4000
        )
    }
}